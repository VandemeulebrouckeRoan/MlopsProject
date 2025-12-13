# 🎯 MNIST Digit Recognition - MLOps Project

[![Azure ML Pipeline](https://github.com/VandemeulebrouckeRoan/MlopsProject/actions/workflows/azure-ml-pipeline.yaml/badge.svg)](https://github.com/VandemeulebrouckeRoan/MlopsProject/actions)

A complete end-to-end MLOps pipeline for handwritten digit classification using Azure Machine Learning, Docker, and Kubernetes.

## 🌟 Features

- ✅ **Interactive Web Interface** - Draw digits and get real-time predictions
- ✅ **Azure ML Pipeline** - Automated model training in the cloud
- ✅ **CI/CD Automation** - GitHub Actions for complete deployment pipeline
- ✅ **Docker Containerization** - Consistent deployment across environments
- ✅ **Kubernetes Orchestration** - Production-ready deployment with high availability
- ✅ **Azure Container Registry** - Private image registry integration
- ✅ **Load Balancing** - 2 replica pods for fault tolerance

## 🏗️ Architecture

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

## 🚀 Quick Start

### Prerequisites

- Azure Account (Azure for Students)
- Docker Desktop with Kubernetes enabled
- GitHub account
- Self-hosted GitHub runner

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/VandemeulebrouckeRoan/MlopsProject.git
   cd MlopsProject
   ```

2. **Enable Kubernetes in Docker Desktop**
   - Open Docker Desktop → Settings → Kubernetes → Enable Kubernetes

3. **Create ACR secret for Kubernetes**
   ```bash
   kubectl create secret docker-registry acr-secret \
     --docker-server=rvazcr.azurecr.io \
     --docker-username=RvAzCr \
     --docker-password=$(az acr credential show --name RvAzCr --query "passwords[0].value" -o tsv)
   ```

4. **Access the application**
   ```
   http://localhost
   ```

### Automated Deployment

Every push to `main` triggers:
1. Azure ML model training
2. Docker image build with trained model
3. Push to Azure Container Registry
4. Deployment to local Kubernetes cluster

## 📊 Technologies Used

### Cloud & Infrastructure
- **Azure Machine Learning** - Model training and management
- **Azure Container Registry** - Private Docker registry
- **Kubernetes** - Container orchestration
- **Docker** - Containerization

### Machine Learning
- **TensorFlow/Keras** - Deep learning framework
- **MNIST Dataset** - Handwritten digit dataset
- **Azure ML SDK** - Pipeline orchestration

### Application
- **FastAPI** - High-performance web framework
- **Python 3.10** - Programming language
- **HTML5 Canvas** - Interactive drawing interface

### DevOps
- **GitHub Actions** - CI/CD automation
- **Self-hosted Runner** - Build and deployment agent

## 📁 Project Structure

```
MlopsProject/
├── .github/
│   └── workflows/
│       └── azure-ml-pipeline.yaml      # CI/CD pipeline
├── components/
│   ├── dataprep/                       # Data preprocessing component
│   └── training/                       # Model training component
├── environment/
│   ├── compute.yaml                    # Azure ML compute config
│   ├── preprocessing.yaml              # Data prep environment
│   └── training.yaml                   # Training environment
├── inference/
│   ├── app.py                          # FastAPI application
│   ├── Dockerfile                      # Container image definition
│   └── requirements.txt                # Python dependencies
├── kubernetes/
│   ├── deployment.yaml                 # K8s deployment config
│   └── service.yaml                    # K8s service config
├── pipelines/
│   └── mnist-classification.yaml       # Azure ML pipeline
└── README.md
```

## 🎯 Usage

### Training a New Model

Push changes to trigger automatic training:
```bash
git add .
git commit -m "Update training configuration"
git push origin main
```

### Accessing the Application

Once deployed, open your browser:
- **Main Interface**: http://localhost
- **API Documentation**: http://localhost/docs
- **Health Check**: http://localhost/health

### Monitoring Deployments

View pod status:
```bash
kubectl get pods -l app=mnist-classifier
```

View logs:
```bash
kubectl logs -l app=mnist-classifier --tail=100
```

View service info:
```bash
kubectl get service mnist-classifier-service
```

## 🔧 Configuration

### Azure Resources
- **Resource Group**: `mlops`
- **ML Workspace**: `mlprojectws`
- **Container Registry**: `rvazcr.azurecr.io`
- **Subscription**: Azure for Students

### Kubernetes
- **Replicas**: 2 pods
- **Resources**: 512Mi-1Gi memory, 250m-500m CPU
- **Service Type**: LoadBalancer
- **Port**: 80 → 8000

## 📈 CI/CD Pipeline

The automated pipeline includes:

1. **Setup & Training**
   - Install Azure ML CLI
   - Create/update compute resources
   - Create/update environments
   - Register components
   - Execute training pipeline
   - Wait for completion

2. **Build & Deploy**
   - Download trained model
   - Build Docker image
   - Push to Azure Container Registry
   - Deploy to Kubernetes
   - Verify deployment health

## 🛠️ Troubleshooting

### Pipeline Fails
- Check GitHub Actions logs
- Verify Azure credentials are set
- Ensure service principal has ACR permissions

### Can't Access Application
```bash
kubectl get service mnist-classifier-service
kubectl get pods -l app=mnist-classifier
kubectl logs -l app=mnist-classifier
```

### Pods Not Starting
```bash
kubectl describe pod -l app=mnist-classifier
```

## 📝 License

This project is created for educational purposes as part of an MLOps course at Howest.

## 👤 Author

**Roan Vandemeulebroucke**
- GitHub: [@VandemeulebrouckeRoan](https://github.com/VandemeulebrouckeRoan)
- School: Howest - Hogeschool West-Vlaanderen

## 🙏 Acknowledgments

- Azure for Students program
- MNIST dataset creators
- FastAPI framework
- TensorFlow/Keras community