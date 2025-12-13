# 🎯 MNIST Digit Recognition - MLOps Project

[![Azure ML Pipeline](https://github.com/VandemeulebrouckeRoan/MlopsProject/actions/workflows/azure-ml-pipeline.yaml/badge.svg)](https://github.com/VandemeulebrouckeRoan/MlopsProject/actions)

A complete end-to-end MLOps pipeline for handwritten digit classification using Azure Machine Learning, Docker, and Kubernetes. This project demonstrates production-grade machine learning deployment with automated CI/CD workflows.

## 🌟 Key Features

- **Interactive Web Interface** - Draw digits on an HTML5 canvas and receive instant predictions
- **Azure ML Pipeline** - Automated cloud-based model training with component-based architecture
- **Continuous Integration/Deployment** - GitHub Actions workflow for automated build and deployment
- **Containerization** - Docker-based application packaging for consistency across environments
- **Kubernetes Orchestration** - Production-ready deployment with load balancing and auto-healing
- **Azure Container Registry** - Private image registry for secure container storage
- **High Availability** - Multiple replica pods ensuring fault tolerance and scalability

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Actions Pipeline                   │
├─────────────────────────────────────────────────────────────┤
│  1. Train Model → Azure ML                                  │
│  2. Download Trained Model                                  │
│  3. Build Docker Image                                      │
│  4. Push to Azure Container Registry                        │
│  5. Deploy to Kubernetes                                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              Kubernetes Cluster (Docker Desktop)            │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐         ┌─────────────┐                   │
│  │  Pod 1      │         │  Pod 2      │                   │
│  │  FastAPI    │ ←────→  │  FastAPI    │                   │
│  └─────────────┘         └─────────────┘                   │
│         ↑                        ↑                          │
│         └────────────────────────┘                          │
│                    LoadBalancer                             │
│                  http://localhost                           │
└─────────────────────────────────────────────────────────────┘
```

## 📊 Technology Stack

### Cloud Infrastructure
- **Azure Machine Learning** - Managed service for model training, versioning, and deployment
- **Azure Container Registry (ACR)** - Private Docker registry (`rvazcr.azurecr.io`)
- **Kubernetes** - Container orchestration platform running on Docker Desktop
- **Docker** - Containerization technology for consistent application deployment

### Machine Learning
- **TensorFlow/Keras** - Deep learning framework for neural network implementation
- **MNIST Dataset** - 70,000 handwritten digit images for training and validation
- **Azure ML SDK** - Python SDK for pipeline orchestration and component management

### Application Stack
- **FastAPI** - Modern, high-performance Python web framework
- **Python 3.10** - Core programming language
- **HTML5 Canvas** - Interactive drawing interface for user input
- **Uvicorn** - ASGI server for serving the FastAPI application

### DevOps & CI/CD
- **GitHub Actions** - Workflow automation for CI/CD pipeline
- **Self-hosted Runner** - Dedicated build and deployment agent
- **YAML Pipelines** - Infrastructure and pipeline as code

## 📁 Project Structure

```
MlopsProject/
├── .github/
│   └── workflows/
│       └── azure-ml-pipeline.yaml      # Complete CI/CD pipeline definition
├── components/
│   ├── dataprep/                       # Data preprocessing component
│   │   ├── dataprep.yaml              # Component specification
│   │   └── code/dataprep.py           # Preprocessing logic
│   └── training/                       # Model training component
│       ├── training.yaml              # Component specification
│       └── code/train.py              # Training logic
├── environment/
│   ├── compute.yaml                    # Azure ML compute cluster config
│   ├── preprocessing.yaml              # Data prep environment dependencies
│   └── training.yaml                   # Training environment dependencies
├── inference/
│   ├── app.py                          # FastAPI web application
│   ├── Dockerfile                      # Container image definition
│   └── requirements.txt                # Application dependencies
├── kubernetes/
│   ├── deployment.yaml                 # Kubernetes deployment specification
│   └── service.yaml                    # Kubernetes service configuration
├── pipelines/
│   └── mnist-classification.yaml       # Azure ML pipeline definition
└── README.md
```

## 🔄 CI/CD Pipeline Workflow

### Stage 1: Model Training (Azure ML)
1. **Setup**: Installs Azure ML CLI and Python dependencies
2. **Infrastructure**: Creates or updates compute clusters and environments
3. **Components**: Registers data preprocessing and training components
4. **Execution**: Runs the training pipeline with configured hyperparameters
5. **Validation**: Waits for pipeline completion and validates results
6. **Artifact**: Downloads the trained `model.keras` file

### Stage 2: Build & Deploy
1. **Authentication**: Logs into Azure and ACR using service principal
2. **Image Build**: Creates Docker image with trained model embedded
3. **Registry Push**: Uploads image to ACR with version tags (latest + commit SHA)
4. **Deployment**: Applies Kubernetes manifests for deployment and service
5. **Verification**: Monitors rollout status and pod health
6. **Reporting**: Displays deployment information and access URLs

## 🎯 Machine Learning Pipeline

### Data Preparation Component
- Loads MNIST dataset from Azure ML data assets
- Normalizes pixel values (0-255 → 0-1)
- Splits data into training and validation sets
- Outputs preprocessed data to Azure ML datastore

### Training Component
- Accepts preprocessed data as input
- Builds convolutional neural network (CNN)
- Trains with configurable hyperparameters:
  - Epochs: 15
  - Batch size: 128
  - Learning rate: 0.001
- Saves trained model in Keras format
- Outputs model artifact for deployment

## 🚀 Deployment Architecture

### Kubernetes Configuration
- **Replicas**: 2 pods for high availability
- **Resource Limits**: 
  - Memory: 512Mi (request) / 1Gi (limit)
  - CPU: 250m (request) / 500m (limit)
- **Health Checks**:
  - Liveness probe on `/health` endpoint
  - Readiness probe for traffic routing
- **Service Type**: LoadBalancer exposing port 80

### Container Specifications
- Base image: `python:3.10-slim`
- Application port: 8000 (internal)
- Model path: `./model/model.keras`
- Environment: TensorFlow CPU-only mode

## 🔐 Security & Secrets

The project uses GitHub Secrets for secure credential management:
- `AZURE_CREDENTIALS` - Service principal for Azure authentication
- `AZURE_RESOURCE_GROUP` - Azure resource group name
- `AZURE_WORKSPACE` - Azure ML workspace name
- `AZURE_SUBSCRIPTION_ID` - Azure subscription identifier

## 📈 Monitoring & Observability

### Kubernetes Monitoring
```bash
# View pod status
kubectl get pods -l app=mnist-classifier

# Check application logs
kubectl logs -l app=mnist-classifier --tail=100

# Monitor service endpoints
kubectl get service mnist-classifier-service

# Describe pod details and events
kubectl describe pod -l app=mnist-classifier
```

### Application Endpoints
- **Main UI**: `http://localhost` - Interactive digit drawing interface
- **API Docs**: `http://localhost/docs` - OpenAPI/Swagger documentation
- **Health**: `http://localhost/health` - Service health check endpoint

## 🎓 Educational Value

This project demonstrates:
- **MLOps Best Practices** - Automated ML lifecycle management
- **Cloud-Native Development** - Containerization and orchestration
- **DevOps Principles** - CI/CD automation and infrastructure as code
- **Production Deployment** - High availability and fault tolerance
- **Azure Services** - Integration with enterprise cloud platform

## 📝 License

This project is created for educational purposes as part of an MLOps course at Howest.

## 👤 Author

**Roan Vandemeulebroucke**
- GitHub: [@VandemeulebrouckeRoan](https://github.com/VandemeulebrouckeRoan)
- Institution: Howest - Hogeschool West-Vlaanderen
- Program: MLOps 2025-2026

## 🙏 Acknowledgments

- Azure for Students program for cloud resources
- MNIST dataset creators and maintainers
- FastAPI and TensorFlow/Keras communities
- Howest faculty for project guidance