import argparse
import os
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def main(args):
    """
    Load and prepare MNIST dataset from CSV file
    """
    print("Starting MNIST data preparation...")
    
    # Create output directory
    output_dir = Path(args.output_data)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load MNIST dataset from CSV
    csv_path = Path(args.input_data) / 'mnist_full.csv'
    print(f"Loading MNIST dataset from {csv_path}...")
    
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found at {csv_path}")
    
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} samples from CSV")
    
    # Assume first column is label, rest are pixel values
    y = df.iloc[:, 0].values
    X = df.iloc[:, 1:].values
    
    print(f"Features shape: {X.shape}")
    print(f"Labels shape: {y.shape}")
    
    # Normalize pixel values to [0, 1]
    print("Normalizing data...")
    X = X.astype('float32') / 255.0
    
    # Reshape to image format (28, 28, 1)
    X = X.reshape(-1, 28, 28, 1)
    
    # Split into train and test sets (80/20 split)
    print("Splitting data into train and test sets...")
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Save preprocessed data
    print(f"Saving preprocessed data to {output_dir}...")
    np.save(output_dir / 'x_train.npy', x_train)
    np.save(output_dir / 'y_train.npy', y_train)
    np.save(output_dir / 'x_test.npy', x_test)
    np.save(output_dir / 'y_test.npy', y_test)
    
    print(f"Data preparation complete!")
    print(f"Training samples: {len(x_train)}")
    print(f"Test samples: {len(x_test)}")
    print(f"Image shape: {x_train.shape[1:]}")
    print(f"Number of classes: {len(np.unique(y_train))}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare MNIST dataset from CSV")
    parser.add_argument(
        "--input_data",
        type=str,
        required=True,
        help="Path to input data directory containing mnist_full.csv"
    )
    parser.add_argument(
        "--output_data",
        type=str,
        required=True,
        help="Path to output preprocessed data"
    )
    
    args = parser.parse_args()
    main(args)
