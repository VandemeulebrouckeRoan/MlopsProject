# MNIST MLOps Project - Complete Package
## Everything You Need to Get Started

**Created for:** Roan Vandemeulebroucke  
**Project:** MNIST Handwritten Digit Recognition with Full MLOps Pipeline  
**Date:** November 29, 2024

---

## 📦 What's Included

This package contains a complete, production-ready MLOps project:

### ✅ Source Code
- **Data Preparation Component** - Loads and preprocesses MNIST CSV
- **Training Component** - Trains CNN model with MLflow tracking
- **FastAPI Application** - REST API with interactive drawing interface
- **Docker Configuration** - Complete containerization setup
- **Kubernetes Manifests** - Deployment and service configurations
- **GitHub Actions Workflow** - Full CI/CD automation

### ✅ Documentation
- **README.md** - Comprehensive project documentation
- **QUICKSTART.md** - Step-by-step setup guide
- **REPORT_TEMPLATE.md** - Pre-filled report template for your assignment
- **Configuration files** - All Azure ML and infrastructure configs

### ✅ Key Features
1. **Interactive Web Interface** - Beautiful canvas for drawing digits
2. **Real-time Predictions** - Instant digit recognition
3. **Cloud Training** - Azure ML pipeline for model training
4. **Containerized Deployment** - Docker + Kubernetes ready
5. **CI/CD Automation** - GitHub Actions workflow included
6. **Production Ready** - Health checks, monitoring, auto-scaling

---

## 🚀 Quick Start (5 Steps)

### Step 1: Upload Your Data (5 min)
```bash
# You already have mnist_full.csv, upload it to Azure:
az storage blob upload \
  --account-name <your-storage> \
  --container-name mnist-data \
  --name mnist_full.csv \
  --file mnist_full.csv
```

### Step 2: Configure Azure (10 min)
1. Create Azure ML workspace
2. Update `.github/workflows/azure-ml-pipeline.yaml` with your details:
   - RESOURCE_GROUP
   - WORKSPACE_NAME
   - SUBSCRIPTION_ID

### Step 3: Set GitHub Secrets (5 min)
Add these to your GitHub repository settings:
- `AZURE_CREDENTIALS` (from service principal)
- `DOCKER_REGISTRY`
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

### Step 4: Push and Deploy (Auto)
```bash
git init
git add .
git commit -m "Initial MNIST MLOps project"
git remote add origin <your-repo-url>
git push -u origin main
```

GitHub Actions automatically:
- ✅ Creates Azure ML resources
- ✅ Trains the model
- ✅ Builds Docker image
- ✅ Deploys to Kubernetes (if configured)

### Step 5: Test Locally (While Waiting)
```bash
cd inference
pip install -r requirements.txt

# Need a model first - train locally or wait for Azure ML
uvicorn app:app --reload
# Visit http://localhost:8000 and draw!
```

---

## 🎨 What Makes This Special

### 1. Beautiful User Interface
- Professional gradient design
- Smooth drawing experience
- Mobile-friendly (touch support)
- Real-time feedback
- Probability distribution visualization

### 2. Enterprise-Grade Architecture
- Scalable Kubernetes deployment
- Health checks and monitoring
- Auto-scaling capabilities
- Zero-downtime deployments
- Production-ready logging

### 3. Complete MLOps Pipeline
- Automated training in Azure ML
- Version-controlled pipelines
- Experiment tracking with MLflow
- Model registration and versioning
- CI/CD with GitHub Actions

### 4. Professional Documentation
- Comprehensive README
- Quick start guide
- Pre-filled report template
- Code comments and examples
- Architecture diagrams

---

## 📊 Project Structure

```
mnist-mlops/
├── README.md                          # Main documentation
├── QUICKSTART.md                      # Setup guide
├── REPORT_TEMPLATE.md                 # Your report (just add screenshots!)
├── .gitignore                         # Git ignore rules
│
├── components/                        # Azure ML Components
│   ├── dataprep/
│   │   ├── code/dataprep.py          # CSV loading & preprocessing
│   │   └── dataprep.yaml             # Component definition
│   └── training/
│       ├── code/train.py             # CNN model training
│       └── training.yaml             # Component definition
│
├── environment/                       # Azure ML Environments
│   ├── compute.yaml                  # Compute cluster config
│   ├── conda-preprocessing.yaml      # Preprocessing dependencies
│   ├── conda-training.yaml           # Training dependencies
│   ├── preprocessing.yaml            # Azure ML env
│   └── training.yaml                 # Azure ML env
│
├── inference/                         # FastAPI Application
│   ├── app.py                        # Main API with drawing UI
│   ├── Dockerfile                    # Container definition
│   └── requirements.txt              # Python dependencies
│
├── kubernetes/                        # Kubernetes Configs
│   ├── deployment.yaml               # Deployment spec
│   └── service.yaml                  # Service (LoadBalancer)
│
├── pipelines/                         # Azure ML Pipelines
│   └── mnist-classification.yaml     # Training pipeline
│
└── .github/workflows/                 # CI/CD
    └── azure-ml-pipeline.yaml        # GitHub Actions workflow
```

---

## 📝 For Your Report

### Screenshots You Need to Take:

1. **Azure ML Workspace**
   - Workspace overview page
   - Compute cluster running

2. **Pipeline Execution**
   - Pipeline graph/diagram
   - Successful pipeline run
   - Training metrics (accuracy/loss curves)

3. **Model Registration**
   - Registered model in Azure ML
   - Model details page

4. **FastAPI Application**
   - Interactive web interface
   - Drawing a digit
   - Prediction results with probabilities
   - Swagger UI (/docs page)

5. **Docker & Kubernetes**
   - Docker build output
   - Container running
   - Kubernetes pods (`kubectl get pods`)
   - Kubernetes service (`kubectl get svc`)

6. **GitHub Actions**
   - Workflow overview
   - Successful workflow run
   - Workflow logs

7. **Testing**
   - Various digits being predicted
   - Confidence scores
   - Error cases (if any)

### Report is 90% Done!
The `REPORT_TEMPLATE.md` file is pre-filled with:
- ✅ Project description
- ✅ Dataset explanation
- ✅ Model architecture
- ✅ Azure ML setup instructions
- ✅ FastAPI implementation details
- ✅ Integration scenario
- ✅ Docker/Kubernetes configs
- ✅ CI/CD automation
- ✅ Results section

**You just need to:**
1. Add your screenshots where it says [INSERT SCREENSHOT: ...]
2. Update placeholder values (YOUR_RESOURCE_GROUP, etc.)
3. Add your actual metrics from training
4. Save as PDF or DOCX

---

## 🎯 Differences from Your Animal Classifier

Your existing animal classifier project focuses on image classification of animals (Cat/Dog/Panda). This MNIST project is similar but with these key differences:

| Feature | Animal Classifier | MNIST Digit Classifier |
|---------|------------------|------------------------|
| **Data Source** | Image files | CSV file (Kaggle) |
| **Input Size** | 64×64 RGB | 28×28 Grayscale |
| **Classes** | 3 (Cat, Dog, Panda) | 10 (0-9 digits) |
| **User Interface** | Upload image | **Draw on canvas** ⭐ |
| **Data Loading** | Image files | CSV preprocessing |
| **Special Feature** | - | **Interactive drawing** ⭐ |
| **Use Case** | Animal photos | Handwritten digits |

### The Drawing Interface is the Key Difference!
This project includes a beautiful, interactive canvas where users can:
- Draw digits with their mouse or finger
- Get instant predictions
- See probability distributions
- Much more engaging than just uploading files!

---

## 💡 What You Can Customize

### Easy Customizations:
1. **Model Architecture** - Add more layers in `components/training/code/train.py`
2. **Training Parameters** - Edit epochs, batch size in `pipelines/mnist-classification.yaml`
3. **UI Colors** - Change gradients in `inference/app.py` HTML section
4. **Kubernetes Replicas** - Scale up/down in `kubernetes/deployment.yaml`

### Advanced Customizations:
1. **Different Dataset** - Adapt for CIFAR-10, Fashion-MNIST, etc.
2. **Model Serving** - Add TensorFlow Serving instead of direct loading
3. **Database Integration** - Store predictions in Azure SQL or CosmosDB
4. **A/B Testing** - Deploy multiple model versions

---

## 🔍 Troubleshooting

### "Pipeline Failed in Azure ML"
- Check data path in `pipelines/mnist-classification.yaml`
- Verify `mnist_full.csv` is uploaded to blob storage
- Look at logs in Azure ML Studio

### "Model Not Found in Docker"
- Ensure model downloaded in GitHub Actions
- Check model path in `inference/Dockerfile`
- Verify model file exists: `./model/model.keras`

### "Canvas Drawing Not Working"
- Enable JavaScript in browser
- Try Chrome/Firefox (best compatibility)
- Check browser console for errors

### "Kubernetes Pod CrashLoopBackOff"
- Check pod logs: `kubectl logs <pod-name>`
- Verify Docker image exists and is accessible
- Check resource limits (may need more memory)

---

## 🎓 For Your Assignment Submission

### Checklist:
- [ ] Code works locally (tested FastAPI)
- [ ] Azure ML pipeline runs successfully
- [ ] Model trained and registered in Azure ML
- [ ] Docker image builds successfully
- [ ] Report filled out with screenshots
- [ ] All source code included in ZIP
- [ ] Azure resources cleaned up (to save costs!)

### What to Submit:
1. **ZIP file** containing all source code
2. **Report** (PDF or DOCX) with screenshots
3. **(Optional)** Short video demonstrating the drawing interface

### Report File:
Use `REPORT_TEMPLATE.md` as your starting point. You can:
- Edit it as Markdown and convert to PDF with pandoc
- Copy content to Word/Google Docs
- Fill in placeholders and add screenshots

---

## 🌟 Highlights for Your Presentation

If you need to present or demo this:

1. **Start with the Drawing Interface** - Most impressive!
   - Draw a digit live
   - Show real-time prediction
   - Highlight the beautiful UI

2. **Show Azure ML** - Enterprise MLOps
   - Pipeline automation
   - Experiment tracking
   - Model versioning

3. **Demonstrate Scalability** - Production ready
   - Kubernetes deployment
   - Auto-scaling
   - Health monitoring

4. **Walk Through CI/CD** - Modern DevOps
   - GitHub Actions automation
   - Automatic deployment
   - Version control

---

## 📚 Learning Resources

Want to understand more deeply?

- **Azure ML**: https://docs.microsoft.com/azure/machine-learning/
- **FastAPI**: https://fastapi.tiangolo.com/
- **Kubernetes**: https://kubernetes.io/docs/tutorials/
- **MLOps**: https://ml-ops.org/
- **CNN Tutorial**: https://www.tensorflow.org/tutorials/images/cnn

---

## 🎉 You're All Set!

This project includes everything you need for a top-grade MLOps assignment:

✅ Complete MLOps pipeline with Azure ML  
✅ Beautiful, interactive user interface  
✅ Production-ready deployment (Docker + Kubernetes)  
✅ Full CI/CD automation with GitHub Actions  
✅ Comprehensive documentation  
✅ Pre-filled report template  

**Total Setup Time:** ~30-45 minutes  
**Training Time:** ~15-20 minutes (automatic in Azure ML)  
**Report Time:** ~1-2 hours (mostly adding screenshots)

**Good luck with your assignment!** 🚀

---

## 💬 Need Help?

Common issues and solutions are in:
- `QUICKSTART.md` - Setup instructions
- `README.md` - Full documentation
- This file - Overview and tips

If stuck, check:
1. Azure ML logs in Azure ML Studio
2. GitHub Actions logs in repository
3. Pod logs: `kubectl logs <pod-name>`
4. API logs when running locally

---

**Remember:** Delete Azure resources when done to avoid charges!

```bash
# Delete resource group (removes everything)
az group delete --name <your-resource-group> --yes

# Or just delete the ML workspace
az ml workspace delete --name <workspace-name> --resource-group <rg>
```

---

**END OF SUMMARY**

*Built with ❤️ for your MLOps success!*
