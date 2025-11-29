# MNIST Digit Classifier - MLOps Project

An end-to-end MLOps implementation for handwritten digit recognition using the MNIST dataset, deployed with Azure Machine Learning, FastAPI, Docker, and Kubernetes.

## 🎯 Project Overview

This project demonstrates a complete MLOps pipeline that:
- Loads and preprocesses MNIST dataset from CSV
- Trains a CNN model using Azure Machine Learning
- Deploys the model as a REST API with FastAPI
- Includes an interactive web interface for drawing digits
- Containerizes the application with Docker
- Orchestrates deployment with Kubernetes
- Automates the entire workflow with GitHub Actions

## 📊 Dataset

The project uses the MNIST handwritten digit dataset from Kaggle:
- **Source**: https://www.kaggle.com/datasets/hojjatk/mnist-dataset
- **File**: `mnist_full.csv` (merged train and test sets)
- **Samples**: 70,000 images (28x28 grayscale)
- **Classes**: 10 digits (0-9)

## 🏗️ Architecture

```
┌─────────────────┐
│  Data Storage   │  mnist_full.csv on Azure Blob Storage
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Data Prep      │  Load CSV, normalize, split data
│  Component      │
└────────┬────────┘
         │
         v
┌─────────────────┐
│   Training      │  Train CNN model with TensorFlow
│   Component     │
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Model Output   │  Saved model.keras file
└────────┬────────┘
         │
         v
┌─────────────────┐
│  FastAPI        │  REST API + Web UI
│  Application    │
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Docker         │  Containerized application
│  Container      │
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Kubernetes     │  Scalable deployment
│  Cluster        │
└─────────────────┘
```

## 🚀 Getting Started

### Prerequisites

- Azure subscription
- Azure Machine Learning workspace
- Docker Desktop
- Kubernetes cluster (AKS, Minikube, or similar)
- Python 3.10+

### 1. Prepare Your Data

1. Download the MNIST dataset from Kaggle
2. Merge train and test CSV files into `mnist_full.csv`
3. Upload to Azure Blob Storage:
   ```bash
   az storage blob upload \
     --account-name <storage-account> \
     --container-name mnist-data \
     --name mnist_full.csv \
     --file mnist_full.csv
   ```

### 2. Configure Azure ML

1. Update the following files with your Azure details:
   - `.github/workflows/azure-ml-pipeline.yaml`
   - Update resource group, workspace name, subscription ID

2. Create Azure service principal:
   ```bash
   az ad sp create-for-rbac \
     --name "mnist-mlops" \
     --role contributor \
     --scopes /subscriptions/<subscription-id>/resourceGroups/<resource-group> \
     --sdk-auth
   ```

3. Add GitHub Secrets:
   - `AZURE_CREDENTIALS`: Output from service principal creation
   - `DOCKER_REGISTRY`: Your Docker registry URL
   - `DOCKER_USERNAME`: Docker registry username
   - `DOCKER_PASSWORD`: Docker registry password

### 3. Run the Pipeline

Push your code to GitHub to trigger the workflow:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

The GitHub Actions workflow will:
1. Create Azure ML compute and environments
2. Register pipeline components
3. Run the training pipeline
4. Download the trained model
5. Build and push Docker image
6. (Optional) Deploy to Kubernetes

## 🖥️ Local Development

### Train Locally

```bash
# Install dependencies
pip install pandas numpy tensorflow scikit-learn

# Prepare data
python components/dataprep/code/dataprep.py \
  --input_data ./data \
  --output_data ./preprocessed

# Train model
python components/training/code/train.py \
  --input_data ./preprocessed \
  --model_output ./model \
  --epochs 15
```

### Run API Locally

```bash
cd inference

# Install dependencies
pip install -r requirements.txt

# Ensure model exists at ./model/model.keras
# Run API
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000` to see the interactive drawing interface!

## 🐳 Docker Deployment

### Build and Run Container

```bash
cd inference

# Build image
docker build -t mnist-classifier .

# Run container
docker run -p 8000:8000 mnist-classifier
```

## ☸️ Kubernetes Deployment

### Deploy to Cluster

```bash
# Update deployment with your Docker registry
sed -i 's/YOUR_DOCKER_REGISTRY/your-registry.azurecr.io/' kubernetes/deployment.yaml

# Apply configurations
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml

# Get service URL
kubectl get service mnist-classifier-service
```

### Scale Deployment

```bash
kubectl scale deployment mnist-classifier --replicas=5
```

## 📡 API Endpoints

### Web Interface
- `GET /` - Interactive digit drawing interface

### Health Check
- `GET /health` - Returns health status and model info

### Predictions
- `POST /predict-drawing` - Predict from base64 canvas drawing
  ```json
  {
    "image": "data:image/png;base64,..."
  }
  ```

- `POST /predict` - Predict from uploaded image file
  ```bash
  curl -X POST "http://localhost:8000/predict" \
    -H "accept: application/json" \
    -H "Content-Type: multipart/form-data" \
    -F "file=@digit.png"
  ```

### Model Info
- `GET /model-info` - Returns model metadata

### API Documentation
- `GET /docs` - Swagger UI documentation
- `GET /redoc` - ReDoc documentation

## 🧪 Model Performance

The CNN model achieves:
- **Test Accuracy**: ~99%
- **Input**: 28x28 grayscale images
- **Output**: Probability distribution over 10 classes (0-9)

### Model Architecture

```
Conv2D(32, 3x3) → MaxPool(2x2) →
Conv2D(64, 3x3) → MaxPool(2x2) →
Flatten → Dropout(0.5) →
Dense(128) → Dropout(0.3) →
Dense(10, softmax)
```

## 📁 Project Structure

```
mnist-mlops/
├── .github/
│   └── workflows/
│       └── azure-ml-pipeline.yaml    # CI/CD workflow
├── components/
│   ├── dataprep/
│   │   ├── code/
│   │   │   └── dataprep.py          # Data preprocessing
│   │   └── dataprep.yaml             # Component definition
│   └── training/
│       ├── code/
│       │   └── train.py              # Model training
│       └── training.yaml             # Component definition
├── environment/
│   ├── compute.yaml                  # Compute configuration
│   ├── conda-preprocessing.yaml      # Preprocessing env
│   ├── conda-training.yaml           # Training env
│   ├── preprocessing.yaml            # Azure ML env
│   └── training.yaml                 # Azure ML env
├── inference/
│   ├── app.py                        # FastAPI application
│   ├── Dockerfile                    # Container definition
│   └── requirements.txt              # Python dependencies
├── kubernetes/
│   ├── deployment.yaml               # K8s deployment
│   └── service.yaml                  # K8s service
└── pipelines/
    └── mnist-classification.yaml     # Azure ML pipeline
```

## 🔄 CI/CD Pipeline

The GitHub Actions workflow automates:

1. **Setup**
   - Install Azure ML CLI
   - Authenticate with Azure

2. **Infrastructure**
   - Create/update compute cluster
   - Register environments
   - Register components

3. **Training**
   - Submit pipeline job
   - Monitor execution
   - Download trained model

4. **Deployment**
   - Build Docker image
   - Push to registry
   - Deploy to Kubernetes

## 🎨 Web Interface Features

- **Interactive Canvas**: Draw digits with mouse or touch
- **Real-time Prediction**: Instant classification results
- **Probability Distribution**: Visual display of all class probabilities
- **Responsive Design**: Works on desktop and mobile
- **Beautiful UI**: Modern gradient design with smooth animations

## 🔧 Configuration

### Training Hyperparameters

Edit in `pipelines/mnist-classification.yaml`:
```yaml
epochs: 15
batch_size: 128
learning_rate: 0.001
```

### Kubernetes Resources

Edit in `kubernetes/deployment.yaml`:
```yaml
resources:
  requests:
    memory: "512Mi"
    cpu: "250m"
  limits:
    memory: "1Gi"
    cpu: "500m"
```

## 🤝 Business Integration Example

### Fictional Company: DigitTech Solutions

**Scenario**: DigitTech provides document digitization services for banks and financial institutions.

**Integration**:
- Mobile app for bank tellers to scan handwritten check amounts
- Uploaded images sent to `/predict` endpoint
- Real-time validation of digit recognition
- Flagging low-confidence predictions for manual review
- Integration with existing banking software via REST API
- Scalable Kubernetes deployment handles peak transaction times

**Benefits**:
- 95% reduction in manual data entry
- Real-time processing of check deposits
- Improved accuracy over manual entry
- Audit trail with confidence scores

## 📝 Report Checklist

- [x] Project explanation and dataset description
- [x] Cloud AI services screenshots (see Azure ML workspace)
- [x] FastAPI implementation and integration explanation
- [x] Kubernetes deployment configuration
- [x] GitHub Actions automation
- [x] Source code included
- [x] README documentation

## 🐛 Troubleshooting

### Model not found error
- Ensure model is copied to `inference/model/model.keras` before building Docker image
- Check Azure ML pipeline completed successfully

### Canvas drawing not working
- Ensure JavaScript is enabled
- Try clearing browser cache
- Check browser console for errors

### Kubernetes pod not starting
- Check pod logs: `kubectl logs <pod-name>`
- Verify Docker image exists in registry
- Check resource limits

## 📚 Resources

- [Azure Machine Learning Docs](https://docs.microsoft.com/en-us/azure/machine-learning/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [MNIST Dataset Paper](http://yann.lecun.com/exdb/mnist/)

## 📄 License

This project is for educational purposes as part of an MLOps course assignment.

## ✍️ Author

**Roan Vandemeulebroucke**
MLOps Project - November 2024

---

*Built with ❤️ using Azure ML, TensorFlow, FastAPI, Docker, and Kubernetes*
