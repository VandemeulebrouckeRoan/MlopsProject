import os
os.environ['TF_USE_LEGACY_KERAS'] = '1'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # Force CPU usage

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import base64

# Create FastAPI app
app = FastAPI(
    title="MNIST Digit Classifier API",
    description="MLOps deployment of handwritten digit recognition model",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = None

class DrawingData(BaseModel):
    image: str  # base64 encoded image

def load_model():
    """Load the model from the local filesystem"""
    global model
    
    if model is not None:
        return model
    
    # Model will be copied here during Docker build
    model_path = './model/model.keras'
    
    print(f"Loading model from {model_path}...")
    
    if not os.path.exists(model_path):
        print(f"ERROR: Model not found at {model_path}")
        raise FileNotFoundError(f"Model file not found at {model_path}")
    
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully!")
    
    return model

@app.on_event("startup")
async def startup_event():
    """Load model on startup"""
    print("Starting up - loading model...")
    try:
        load_model()
        print("Startup complete!")
    except Exception as e:
        print(f"WARNING: Failed to load model on startup: {e}")
        print("Model will be loaded on first prediction request")

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MNIST Digit Classifier</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                padding: 40px;
                max-width: 600px;
                width: 100%;
            }
            
            h1 {
                color: #333;
                text-align: center;
                margin-bottom: 10px;
                font-size: 2.5em;
            }
            
            .subtitle {
                text-align: center;
                color: #666;
                margin-bottom: 30px;
                font-size: 1.1em;
            }
            
            .canvas-container {
                background: #f8f9fa;
                border: 3px solid #667eea;
                border-radius: 15px;
                padding: 20px;
                margin-bottom: 20px;
                text-align: center;
            }
            
            canvas {
                border: 2px solid #ddd;
                border-radius: 10px;
                cursor: crosshair;
                background: white;
                touch-action: none;
            }
            
            .button-group {
                display: flex;
                gap: 10px;
                margin-top: 15px;
                flex-wrap: wrap;
            }
            
            button {
                flex: 1;
                padding: 15px 30px;
                font-size: 1.1em;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: all 0.3s ease;
                font-weight: 600;
                min-width: 140px;
            }
            
            .predict-btn {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            
            .predict-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }
            
            .clear-btn {
                background: #6c757d;
                color: white;
            }
            
            .clear-btn:hover {
                background: #5a6268;
                transform: translateY(-2px);
            }
            
            .result {
                margin-top: 30px;
                padding: 25px;
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                border-radius: 15px;
                display: none;
            }
            
            .result.show {
                display: block;
                animation: slideIn 0.3s ease;
            }
            
            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateY(-10px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .predicted-digit {
                font-size: 4em;
                font-weight: bold;
                text-align: center;
                color: #667eea;
                margin: 20px 0;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            }
            
            .confidence {
                text-align: center;
                font-size: 1.2em;
                color: #666;
                margin-bottom: 20px;
            }
            
            .probabilities {
                display: grid;
                grid-template-columns: repeat(5, 1fr);
                gap: 10px;
                margin-top: 20px;
            }
            
            .prob-item {
                background: white;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                border: 2px solid #e9ecef;
                transition: all 0.3s ease;
            }
            
            .prob-item:hover {
                border-color: #667eea;
                transform: scale(1.05);
            }
            
            .prob-digit {
                font-size: 1.5em;
                font-weight: bold;
                color: #333;
            }
            
            .prob-value {
                font-size: 0.9em;
                color: #666;
                margin-top: 5px;
            }
            
            .prob-bar {
                height: 6px;
                background: #e9ecef;
                border-radius: 3px;
                margin-top: 8px;
                overflow: hidden;
            }
            
            .prob-fill {
                height: 100%;
                background: linear-gradient(90deg, #667eea, #764ba2);
                border-radius: 3px;
                transition: width 0.5s ease;
            }
            
            .info-box {
                background: #e7f3ff;
                border-left: 4px solid #667eea;
                padding: 15px;
                margin-top: 20px;
                border-radius: 5px;
            }
            
            .info-box p {
                color: #004085;
                line-height: 1.6;
            }
            
            .loading {
                display: none;
                text-align: center;
                padding: 20px;
            }
            
            .loading.show {
                display: block;
            }
            
            .spinner {
                border: 4px solid #f3f3f3;
                border-top: 4px solid #667eea;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                animation: spin 1s linear infinite;
                margin: 0 auto;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✍️ Digit Classifier</h1>
            <p class="subtitle">Draw a digit (0-9) and let AI recognize it!</p>
            
            <div class="canvas-container">
                <canvas id="canvas" width="280" height="280"></canvas>
                <div class="button-group">
                    <button class="predict-btn" onclick="predict()">🔍 Predict</button>
                    <button class="clear-btn" onclick="clearCanvas()">🗑️ Clear</button>
                </div>
            </div>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p style="margin-top: 10px; color: #667eea;">Analyzing...</p>
            </div>
            
            <div class="result" id="result">
                <h2 style="text-align: center; color: #333; margin-bottom: 10px;">Prediction Result</h2>
                <div class="predicted-digit" id="predictedDigit">-</div>
                <div class="confidence" id="confidence">Confidence: -</div>
                
                <h3 style="color: #333; margin-top: 25px; margin-bottom: 15px;">All Probabilities</h3>
                <div class="probabilities" id="probabilities"></div>
            </div>
            
            <div class="info-box">
                <p><strong>💡 Tip:</strong> Draw clearly in the center of the canvas. The model works best with digits similar to those in the MNIST dataset.</p>
            </div>
        </div>
        
        <script>
            const canvas = document.getElementById('canvas');
            const ctx = canvas.getContext('2d');
            let isDrawing = false;
            let lastX = 0;
            let lastY = 0;
            
            // Set up canvas
            ctx.strokeStyle = 'black';
            ctx.lineWidth = 20;
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';
            
            // Mouse events
            canvas.addEventListener('mousedown', startDrawing);
            canvas.addEventListener('mousemove', draw);
            canvas.addEventListener('mouseup', stopDrawing);
            canvas.addEventListener('mouseout', stopDrawing);
            
            // Touch events
            canvas.addEventListener('touchstart', handleTouchStart);
            canvas.addEventListener('touchmove', handleTouchMove);
            canvas.addEventListener('touchend', stopDrawing);
            
            function startDrawing(e) {
                isDrawing = true;
                [lastX, lastY] = [e.offsetX, e.offsetY];
            }
            
            function draw(e) {
                if (!isDrawing) return;
                
                ctx.beginPath();
                ctx.moveTo(lastX, lastY);
                ctx.lineTo(e.offsetX, e.offsetY);
                ctx.stroke();
                [lastX, lastY] = [e.offsetX, e.offsetY];
            }
            
            function stopDrawing() {
                isDrawing = false;
            }
            
            function handleTouchStart(e) {
                e.preventDefault();
                const touch = e.touches[0];
                const rect = canvas.getBoundingClientRect();
                lastX = touch.clientX - rect.left;
                lastY = touch.clientY - rect.top;
                isDrawing = true;
            }
            
            function handleTouchMove(e) {
                if (!isDrawing) return;
                e.preventDefault();
                
                const touch = e.touches[0];
                const rect = canvas.getBoundingClientRect();
                const x = touch.clientX - rect.left;
                const y = touch.clientY - rect.top;
                
                ctx.beginPath();
                ctx.moveTo(lastX, lastY);
                ctx.lineTo(x, y);
                ctx.stroke();
                [lastX, lastY] = [x, y];
            }
            
            function clearCanvas() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                document.getElementById('result').classList.remove('show');
            }
            
            async function predict() {
                // Get canvas data
                const imageData = canvas.toDataURL('image/png');
                
                // Show loading
                document.getElementById('loading').classList.add('show');
                document.getElementById('result').classList.remove('show');
                
                try {
                    const response = await fetch('/predict-drawing', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ image: imageData })
                    });
                    
                    const data = await response.json();
                    
                    if (data.success) {
                        displayResult(data);
                    } else {
                        alert('Error: ' + data.error);
                    }
                } catch (error) {
                    alert('Error making prediction: ' + error);
                } finally {
                    document.getElementById('loading').classList.remove('show');
                }
            }
            
            function displayResult(data) {
                document.getElementById('predictedDigit').textContent = data.predicted_digit;
                document.getElementById('confidence').textContent = 
                    `Confidence: ${(data.confidence * 100).toFixed(1)}%`;
                
                const probsContainer = document.getElementById('probabilities');
                probsContainer.innerHTML = '';
                
                for (let i = 0; i < 10; i++) {
                    const prob = data.all_probabilities[i];
                    const probItem = document.createElement('div');
                    probItem.className = 'prob-item';
                    probItem.innerHTML = `
                        <div class="prob-digit">${i}</div>
                        <div class="prob-value">${(prob * 100).toFixed(1)}%</div>
                        <div class="prob-bar">
                            <div class="prob-fill" style="width: ${prob * 100}%"></div>
                        </div>
                    `;
                    probsContainer.appendChild(probItem);
                }
                
                document.getElementById('result').classList.add('show');
            }
        </script>
    </body>
    </html>
    """

@app.get("/health")
async def health():
    global model
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "classes": list(range(10))
    }

@app.post('/predict-drawing')
async def predict_drawing(data: DrawingData):
    """
    Predict digit from base64 encoded image from canvas
    """
    global model
    
    # Ensure model is loaded
    if model is None:
        try:
            load_model()
        except Exception as e:
            return {
                "success": False,
                "error": f"Model not loaded: {str(e)}"
            }
    
    try:
        # Decode base64 image
        image_data = data.image.split(',')[1]  # Remove data:image/png;base64,
        image_bytes = base64.b64decode(image_data)
        
        # Open image and convert to grayscale
        image = Image.open(io.BytesIO(image_bytes)).convert('L')
        
        # Resize to 28x28 (MNIST size)
        image = image.resize((28, 28), Image.Resampling.LANCZOS)
        
        # Convert to array and invert colors (MNIST has white digits on black background)
        image_array = np.array(image)
        image_array = 255 - image_array  # Invert
        
        # Normalize
        image_array = image_array.astype('float32') / 255.0
        
        # Reshape for model
        image_array = image_array.reshape(1, 28, 28, 1)
        
        # Make prediction
        predictions = model.predict(image_array, verbose=0)
        prediction_probabilities = predictions[0]
        predicted_digit = int(np.argmax(prediction_probabilities))
        
        return {
            "success": True,
            "predicted_digit": predicted_digit,
            "confidence": float(prediction_probabilities[predicted_digit]),
            "all_probabilities": [float(p) for p in prediction_probabilities]
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "error": str(e)
        }

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    """
    Upload an image file to classify the digit
    """
    global model
    
    # Ensure model is loaded
    if model is None:
        try:
            load_model()
        except Exception as e:
            return {
                "success": False,
                "error": f"Model not loaded: {str(e)}"
            }
    
    try:
        # Read image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert('L')
        
        # Resize to 28x28
        image = image.resize((28, 28), Image.Resampling.LANCZOS)
        
        # Convert to array and normalize
        image_array = np.array(image)
        image_array = 255 - image_array  # Invert if needed
        image_array = image_array.astype('float32') / 255.0
        image_array = image_array.reshape(1, 28, 28, 1)
        
        # Make prediction
        predictions = model.predict(image_array, verbose=0)
        prediction_probabilities = predictions[0]
        predicted_digit = int(np.argmax(prediction_probabilities))
        
        return {
            "success": True,
            "filename": file.filename,
            "predicted_digit": predicted_digit,
            "confidence": float(prediction_probabilities[predicted_digit]),
            "all_probabilities": {
                str(i): float(prob) 
                for i, prob in enumerate(prediction_probabilities)
            }
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "error": str(e)
        }

@app.get("/model-info")
async def model_info():
    return {
        "model_source": "Azure Machine Learning",
        "model_name": "mnist-digit-classifier",
        "model_type": "CNN (Convolutional Neural Network)",
        "classes": list(range(10)),
        "input_size": "28x28 grayscale images",
        "framework": "TensorFlow/Keras",
        "deployment": "MLOps Pipeline via GitHub Actions"
    }
