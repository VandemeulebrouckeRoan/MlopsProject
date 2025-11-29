import argparse
import os
from pathlib import Path
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import mlflow
import mlflow.tensorflow

def create_model(input_shape=(28, 28, 1), num_classes=10):
    """
    Create a CNN model for MNIST digit classification
    """
    model = keras.Sequential([
        layers.Input(shape=input_shape),
        
        # First convolutional block
        layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        
        # Second convolutional block
        layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        
        # Flatten and dense layers
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    return model

def main(args):
    """
    Train MNIST digit classification model
    """
    print("=" * 60)
    print("MNIST Digit Classifier Training")
    print("=" * 60)
    
    # Simple MLflow setup - just basic logging
    try:
        import mlflow
        mlflow.start_run()
    except Exception as e:
        print(f"MLflow not available, continuing without it: {e}")
    
    # Load preprocessed data
    data_path = Path(args.input_data)
    print(f"\nLoading data from {data_path}...")
    
    x_train = np.load(data_path / 'x_train.npy')
    y_train = np.load(data_path / 'y_train.npy')
    x_test = np.load(data_path / 'x_test.npy')
    y_test = np.load(data_path / 'y_test.npy')
    
    print(f"Training samples: {len(x_train)}")
    print(f"Test samples: {len(x_test)}")
    print(f"Image shape: {x_train.shape[1:]}")
    
    # Create model
    print("\nCreating model...")
    model = create_model()
    model.summary()
    
    # Compile model
    print("\nCompiling model...")
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=args.learning_rate),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Set up callbacks
    callbacks = [
        keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=5,
            restore_best_weights=True
        ),
        keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=3,
            min_lr=1e-7
        )
    ]
    
    # Train model
    print(f"\nTraining model for {args.epochs} epochs...")
    history = model.fit(
        x_train, y_train,
        batch_size=args.batch_size,
        epochs=args.epochs,
        validation_split=0.1,
        callbacks=callbacks,
        verbose=1
    )
    
    # Evaluate model
    print("\nEvaluating model on test set...")
    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
    
    print(f"\nFinal Results:")
    print(f"Test Loss: {test_loss:.4f}")
    print(f"Test Accuracy: {test_accuracy:.4f}")
    
    # Log final metrics if MLflow is available
    try:
        import mlflow
        mlflow.log_metric("test_loss", test_loss)
        mlflow.log_metric("test_accuracy", test_accuracy)
    except:
        pass
    
    # Save model
    output_dir = Path(args.model_output)
    output_dir.mkdir(parents=True, exist_ok=True)
    model_path = output_dir / 'model.keras'
    
    print(f"\nSaving model to {model_path}...")
    model.save(model_path)
    
    # End MLflow run if it was started
    try:
        import mlflow
        mlflow.end_run()
    except:
        pass
    
    print("\n" + "=" * 60)
    print("Training Complete!")
    print("=" * 60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train MNIST CNN model")
    
    parser.add_argument(
        "--input_data",
        type=str,
        required=True,
        help="Path to preprocessed data"
    )
    parser.add_argument(
        "--model_output",
        type=str,
        required=True,
        help="Path to save trained model"
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=15,
        help="Number of training epochs"
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=128,
        help="Batch size for training"
    )
    parser.add_argument(
        "--learning_rate",
        type=float,
        default=0.001,
        help="Learning rate"
    )
    
    args = parser.parse_args()
    main(args)
