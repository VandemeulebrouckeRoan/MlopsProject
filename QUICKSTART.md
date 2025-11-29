# Quick Start Guide

## 🚀 Getting Your MNIST MLOps Project Running

### Step 1: Prepare Your Data (5 minutes)

1. Download MNIST from Kaggle: https://www.kaggle.com/datasets/hojjatk/mnist-dataset
2. You should have `mnist_full.csv` ready
3. Upload to Azure Blob Storage:
   ```bash
   az storage blob upload \
     --account-name <your-storage> \
     --container-name mnist-data \
     --name mnist_full.csv \
     --file mnist_full.csv
   ```

### Step 2: Set Up Azure ML (10 minutes)

1. Create Azure ML Workspace:
   ```bash
   az ml workspace create \
     --name mnist-workspace \
     --resource-group your-rg \
     --location westeurope
   ```

2. Update configuration in `.github/workflows/azure-ml-pipeline.yaml`:
   - RESOURCE_GROUP
   - WORKSPACE_NAME  
   - SUBSCRIPTION_ID

### Step 3: Configure GitHub Secrets (5 minutes)

Add these secrets to your GitHub repository:

1. **AZURE_CREDENTIALS**
   ```bash
   az ad sp create-for-rbac \
     --name "mnist-mlops" \
     --role contributor \
     --scopes /subscriptions/<id>/resourceGroups/<rg> \
     --sdk-auth
   ```
   Copy the JSON output to this secret.

2. **DOCKER_REGISTRY**: e.g., `yourname.azurecr.io`
3. **DOCKER_USERNAME**: Your registry username
4. **DOCKER_PASSWORD**: Your registry password

### Step 4: Run the Pipeline (Auto)

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

GitHub Actions will automatically:
- Create compute and environments
- Train the model
- Build Docker image
- (Optionally) Deploy to Kubernetes

### Step 5: Test Locally (While Waiting)

```bash
# Install dependencies
cd inference
pip install -r requirements.txt

# You'll need a trained model first
# For testing, you can train locally:
cd ../components/training/code
python train.py --input_data /path/to/preprocessed --model_output ../../../inference/model --epochs 5

# Run the API
cd ../../../inference
uvicorn app:app --reload
```

Visit http://localhost:8000 and draw a digit!

### Step 6: Deploy to Kubernetes (Optional)

```bash
# Update your Docker registry in deployment.yaml
sed -i 's/YOUR_DOCKER_REGISTRY/yourregistry.azurecr.io/' kubernetes/deployment.yaml

# Deploy
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml

# Get URL
kubectl get svc mnist-classifier-service
```

## 🎯 Checkpoint: What You Should Have

After setup:
- ✅ Azure ML workspace created
- ✅ Data uploaded to blob storage
- ✅ GitHub secrets configured
- ✅ Code pushed to GitHub

After pipeline runs:
- ✅ Model trained in Azure ML
- ✅ Docker image in registry
- ✅ API accessible locally or in Kubernetes

## 🐛 Common Issues

### "Pipeline failed"
- Check Azure ML workspace logs
- Verify data path in `pipelines/mnist-classification.yaml`
- Ensure compute cluster is created

### "Model not found"
- Make sure pipeline completed successfully
- Check model was downloaded in GitHub Actions
- Verify model path in `inference/app.py`

### "Can't connect to Kubernetes"
- Check kubectl is configured: `kubectl cluster-info`
- Verify image pull secrets if using private registry
- Check pod logs: `kubectl logs <pod-name>`

## 📸 Screenshots for Report

Take screenshots of:
1. Azure ML workspace showing pipeline run
2. Training job metrics and graphs
3. Registered model in Azure ML
4. GitHub Actions workflow success
5. FastAPI /docs page
6. Drawing interface with prediction
7. Kubernetes dashboard (if deployed)

## 💡 Quick Test

Test the API with curl:
```bash
curl -X POST "http://localhost:8000/predict-drawing" \
  -H "Content-Type: application/json" \
  -d '{"image": "data:image/png;base64,..."}'
```

Or just visit http://localhost:8000 and use the drawing interface!

---

Need help? Check the full README.md or the troubleshooting section.
