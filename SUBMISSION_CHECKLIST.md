# Assignment Submission Checklist
## MNIST MLOps Project - Roan Vandemeulebroucke

Use this checklist to ensure you've completed everything for your assignment.

---

## 📋 Pre-Submission Checklist

### ✅ Project Setup (Before Starting)

- [ ] Azure subscription is active
- [ ] Azure ML workspace created
- [ ] `mnist_full.csv` dataset ready
- [ ] GitHub repository created
- [ ] Docker Hub or Azure Container Registry account ready

### ✅ Data Preparation

- [ ] Downloaded MNIST dataset from Kaggle
- [ ] Merged into `mnist_full.csv` (if needed)
- [ ] Uploaded to Azure Blob Storage
- [ ] Verified file path in pipeline configuration
- [ ] Updated `pipelines/mnist-classification.yaml` with correct data path

### ✅ Azure ML Setup

- [ ] Created Azure ML workspace
- [ ] Updated `.github/workflows/azure-ml-pipeline.yaml` with:
  - [ ] RESOURCE_GROUP
  - [ ] WORKSPACE_NAME
  - [ ] SUBSCRIPTION_ID
- [ ] Created service principal for GitHub Actions
- [ ] Tested Azure CLI authentication locally (optional)

### ✅ GitHub Configuration

- [ ] Repository created and code pushed
- [ ] GitHub Secrets added:
  - [ ] AZURE_CREDENTIALS
  - [ ] DOCKER_REGISTRY
  - [ ] DOCKER_USERNAME
  - [ ] DOCKER_PASSWORD
- [ ] Branch protection rules (optional)
- [ ] README.md updated with your details

### ✅ Pipeline Execution

- [ ] GitHub Actions workflow triggered
- [ ] Compute cluster created successfully
- [ ] Environments registered in Azure ML
- [ ] Components registered in Azure ML
- [ ] Pipeline submitted and running
- [ ] Training completed successfully
- [ ] Model registered in Azure ML
- [ ] Docker image built and pushed
- [ ] No errors in workflow logs

### ✅ Local Testing (Recommended)

- [ ] Cloned repository locally
- [ ] Installed Python dependencies
- [ ] Trained model locally (or downloaded from Azure ML)
- [ ] Tested FastAPI application locally
- [ ] Drew digits and verified predictions work
- [ ] Tested API endpoints with curl/Postman
- [ ] Reviewed Swagger UI at http://localhost:8000/docs

### ✅ Docker Deployment

- [ ] Docker image builds without errors
- [ ] Container runs successfully
- [ ] API accessible at http://localhost:8000
- [ ] Drawing interface works in container
- [ ] Health check endpoint responds
- [ ] Model predictions are accurate

### ✅ Kubernetes Deployment (Optional but Recommended)

- [ ] Kubernetes cluster available (AKS, Minikube, etc.)
- [ ] Updated `kubernetes/deployment.yaml` with your Docker registry
- [ ] Deployment created successfully
- [ ] Service created (LoadBalancer)
- [ ] Pods are running (kubectl get pods)
- [ ] External IP assigned (kubectl get svc)
- [ ] Application accessible via external IP
- [ ] Tested auto-scaling (optional)

---

## 📸 Screenshots for Report

### Required Screenshots:

#### 1. Azure ML Workspace (2-3 screenshots)
- [ ] Workspace overview page showing name and resources
- [ ] Compute cluster page showing configuration
- [ ] Environments page showing registered environments

#### 2. Pipeline Execution (3-4 screenshots)
- [ ] Pipeline graph/flow diagram
- [ ] Pipeline run overview (showing success)
- [ ] Training job metrics page
- [ ] Training accuracy/loss curves (line charts)

#### 3. Model Registration (1-2 screenshots)
- [ ] Registered models page
- [ ] Model details showing version, framework, etc.

#### 4. FastAPI Application (4-5 screenshots)
- [ ] Home page with drawing canvas
- [ ] Canvas with a drawn digit
- [ ] Prediction results showing digit and confidence
- [ ] Probability distribution for all classes
- [ ] Swagger UI documentation page (/docs)

#### 5. Docker (2-3 screenshots)
- [ ] Docker build command output (showing success)
- [ ] Docker images list showing your image
- [ ] Container running (docker ps output)

#### 6. Kubernetes (2-3 screenshots)
- [ ] Kubernetes pods (kubectl get pods)
- [ ] Kubernetes service (kubectl get svc)
- [ ] Kubernetes dashboard (optional)

#### 7. GitHub Actions (2-3 screenshots)
- [ ] Workflow overview showing all jobs
- [ ] Successful workflow run (green checkmarks)
- [ ] One of the job logs (e.g., training job)

#### 8. Testing/Results (2-3 screenshots)
- [ ] Different digits being recognized
- [ ] High confidence predictions
- [ ] Example of all 10 digits (0-9) predicted

### Optional Screenshots:
- [ ] Azure ML experiment tracking page
- [ ] MLflow metrics comparison
- [ ] Kubernetes auto-scaling in action
- [ ] API performance metrics
- [ ] Cost analysis from Azure

---

## 📝 Report Checklist

Using `REPORT_TEMPLATE.md`:

### Section 1: Project Overview
- [ ] Updated with your name and date
- [ ] Project description filled in
- [ ] Dataset section complete
- [ ] Model architecture explained

### Section 2: Cloud AI Services
- [ ] Azure ML workspace details added
- [ ] Screenshots inserted
- [ ] Compute configuration explained
- [ ] Environment setup documented

### Section 3: FastAPI Implementation
- [ ] API architecture explained
- [ ] Interactive web interface described
- [ ] Screenshots of web UI added
- [ ] API endpoints documented

### Section 4: Software Integration
- [ ] Business scenario described (DigitTech or your own)
- [ ] Integration flow explained
- [ ] Benefits listed
- [ ] Technical integration details provided

### Section 5: Docker Deployment
- [ ] Dockerfile explained
- [ ] Build process documented
- [ ] Screenshots added
- [ ] Registry information included

### Section 6: Kubernetes Deployment
- [ ] Deployment configuration explained
- [ ] Service configuration documented
- [ ] Screenshots of running deployment
- [ ] Auto-scaling discussed (if implemented)

### Section 7: Automation/CI/CD
- [ ] GitHub Actions workflow explained
- [ ] Workflow stages documented
- [ ] Screenshots of successful runs
- [ ] Version control strategy described

### Section 8: Results
- [ ] Model performance metrics added
- [ ] Test results included
- [ ] API performance documented
- [ ] Real-world testing examples

### Section 9: Conclusion
- [ ] Key achievements summarized
- [ ] Skills demonstrated listed
- [ ] Future improvements suggested

### Final Review
- [ ] All [INSERT SCREENSHOT] placeholders replaced
- [ ] All YOUR_X placeholders updated with actual values
- [ ] Grammar and spelling checked
- [ ] Formatted consistently
- [ ] Exported to PDF or DOCX

---

## 📦 Final Submission Package

### What to Include:

#### 1. Source Code (ZIP file)
- [ ] All Python files (.py)
- [ ] All YAML configuration files
- [ ] Dockerfile and requirements.txt
- [ ] README.md
- [ ] .gitignore
- [ ] GitHub Actions workflow
- [ ] No unnecessary files (remove .pyc, __pycache__, etc.)

#### 2. Report (PDF or DOCX)
- [ ] All sections complete
- [ ] All screenshots included and labeled
- [ ] Professional formatting
- [ ] Page numbers
- [ ] Table of contents (optional)

#### 3. Optional: Video Demonstration
- [ ] Show drawing interface
- [ ] Demonstrate predictions
- [ ] Walk through Azure ML
- [ ] Show Kubernetes deployment
- [ ] Length: 3-5 minutes

### File Naming:
```
Submission/
├── RoanVandemeulebroucke_MLOps_SourceCode.zip
├── RoanVandemeulebroucke_MLOps_Report.pdf
└── RoanVandemeulebroucke_MLOps_Demo.mp4 (optional)
```

---

## ⚠️ Common Mistakes to Avoid

### Before Submission:

- [ ] ❌ Don't include virtual environments in ZIP
- [ ] ❌ Don't include model files (too large)
- [ ] ❌ Don't include .git directory
- [ ] ❌ Don't leave placeholder values in code
- [ ] ❌ Don't submit without testing locally first

### Report:

- [ ] ❌ Don't use low-quality screenshots
- [ ] ❌ Don't forget to label screenshots
- [ ] ❌ Don't copy-paste without understanding
- [ ] ❌ Don't claim features you didn't implement
- [ ] ❌ Don't forget page numbers

### Code:

- [ ] ❌ Don't hardcode credentials
- [ ] ❌ Don't commit sensitive information
- [ ] ❌ Don't leave debug print statements everywhere
- [ ] ❌ Don't include unused code
- [ ] ❌ Don't forget comments for complex parts

---

## 🧹 Cleanup (After Submission)

To avoid Azure charges:

### Delete Resources:

```bash
# Delete resource group (removes everything)
az group delete --name <your-resource-group> --yes --no-wait

# Or delete specific resources:
az ml workspace delete --name <workspace-name> --resource-group <rg>
az ml compute delete --name mnist-cluster
```

- [ ] Deleted Azure ML workspace
- [ ] Deleted compute cluster
- [ ] Deleted storage account (if created separately)
- [ ] Deleted container registry (if created separately)
- [ ] Verified no remaining resources in Azure portal
- [ ] Checked billing to ensure no ongoing charges

### Local Cleanup:

- [ ] Removed large model files from local machine
- [ ] Removed preprocessed data files
- [ ] Kept only source code for future reference

---

## 📊 Grading Criteria (Estimated)

Based on your assignment description:

| Criteria | Points | Your Status |
|----------|--------|-------------|
| Project explanation and data | 15% | ⬜ |
| Cloud AI services (Azure ML) | 25% | ⬜ |
| FastAPI implementation | 20% | ⬜ |
| Docker deployment | 15% | ⬜ |
| Kubernetes deployment | 10% | ⬜ |
| Automation (GitHub Actions) | 10% | ⬜ |
| Report quality | 5% | ⬜ |

### Bonus Points Opportunities:
- [ ] Video demonstration
- [ ] Advanced Kubernetes features (auto-scaling, etc.)
- [ ] Database integration
- [ ] Exceptional UI design
- [ ] Comprehensive testing
- [ ] Extra automation

---

## 📅 Timeline Suggestion

### Day 1 (3-4 hours):
- [ ] Set up Azure resources
- [ ] Upload data to blob storage
- [ ] Configure GitHub secrets
- [ ] Push code and trigger first pipeline run

### Day 2 (2-3 hours):
- [ ] Verify pipeline completed
- [ ] Test locally
- [ ] Build and test Docker image
- [ ] Deploy to Kubernetes (if planned)

### Day 3 (3-4 hours):
- [ ] Take all screenshots
- [ ] Fill in report template
- [ ] Review and polish report
- [ ] Test everything one more time

### Day 4 (1-2 hours):
- [ ] Final review of code
- [ ] Create submission ZIP
- [ ] Export report to PDF
- [ ] Submit 2 days before exam!

---

## ✅ Final Check Before Submission

### Test Everything One More Time:

```bash
# 1. Test locally
cd inference
pip install -r requirements.txt
uvicorn app:app --reload
# Visit http://localhost:8000 and draw digits

# 2. Test Docker
docker build -t mnist-test .
docker run -p 8000:8000 mnist-test
# Visit http://localhost:8000 and test

# 3. Verify Kubernetes (if deployed)
kubectl get pods
kubectl get svc
# Visit external IP and test

# 4. Review report
# Open REPORT_TEMPLATE.md
# Check all screenshots are clear
# Verify all placeholders filled

# 5. Create ZIP
zip -r submission.zip mnist-mlops/ \
  -x "*/node_modules/*" "*/.git/*" "*.pyc" "*/__pycache__/*"
```

### Submission Verification:

- [ ] ZIP file size reasonable (<50 MB)
- [ ] ZIP contains all necessary files
- [ ] Report is complete and professional
- [ ] Screenshots are clear and labeled
- [ ] Code runs without errors
- [ ] No sensitive information included

---

## 🎉 You're Ready to Submit!

Once all boxes are checked:

1. ✅ Submit ZIP file with source code
2. ✅ Submit report (PDF/DOCX)
3. ✅ (Optional) Submit video demonstration
4. ✅ Keep backup of everything
5. ✅ Clean up Azure resources

**Congratulations on completing your MLOps project!** 🚀

---

## 📞 Emergency Troubleshooting

If something goes wrong last minute:

### Pipeline Failed:
- Check logs in Azure ML Studio
- Verify data path is correct
- Ensure compute has sufficient resources

### Docker Won't Build:
- Check model file exists
- Verify requirements.txt is complete
- Try building with --no-cache flag

### Kubernetes Issues:
- Verify image is in registry
- Check resource limits
- Look at pod logs: `kubectl logs <pod-name>`

### Can't Access Application:
- Check firewall rules
- Verify port forwarding
- Test with curl first

---

## 💡 Last-Minute Tips

1. **Screenshot Quality**: Use full screen, clear resolution
2. **Report Length**: Quality > Quantity (aim for 15-25 pages)
3. **Code Comments**: Add comments where needed
4. **Testing**: Test on a clean environment if possible
5. **Backup**: Keep multiple copies of your work

---

**Good luck with your submission!** 🍀

*Remember: This project demonstrates real-world MLOps skills that companies value!*
