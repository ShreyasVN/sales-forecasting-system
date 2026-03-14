# MLOps Pipeline: Automated Sales Analytics & Forecasting

![Project Cover Image](images/project-cover.png)

## 📖 System Overview

This project implements an automated **MLOps-style data pipeline** for sales forecasting.  
It demonstrates the complete lifecycle of a machine learning workflow, from raw data processing to containerized model execution and business intelligence integration.

The system processes sales datasets, performs ETL operations, trains a machine learning model, and generates forecast outputs that can be consumed by analytics dashboards.

---

# 🏗 Architecture Overview

The pipeline transforms raw sales data into predictive insights through a structured workflow.

### Pipeline Workflow

```
Raw Sales Dataset
        ↓
Data Cleaning & ETL (Pandas)
        ↓
Feature Engineering
(Lag Features, Rolling Averages)
        ↓
Model Training
(Random Forest Regressor)
        ↓
Forecast Generation
        ↓
Export Prediction Dataset
        ↓
Business Intelligence Dashboard
(Power BI)
```

This workflow supports automated data analysis and predictive insights for business decision making.

---

# ⚙️ Pipeline Automation

The system is designed to support **automated execution using CI/CD workflows and containerized environments**.

### GitHub Actions

Automated workflows ensure:

- pipeline execution validation
- dependency stability
- automated build verification

Scheduled retraining can be configured using cron-based workflows.

Example schedule:

```
0 0 * * *
```

This allows automated daily pipeline execution.

---

# 🛠 Technology Stack

| Domain | Technology | Implementation |
|------|-------------|----------------|
| Cloud Deployment | AWS EC2 | Container runtime environment |
| Containerization | Docker | Reproducible pipeline execution |
| CI/CD Automation | GitHub Actions | Pipeline validation and scheduling |
| Data Engineering | Python, Pandas, NumPy | ETL processing and feature engineering |
| Machine Learning | Scikit-learn | Random Forest Regression model |
| Visualization | Power BI | Business KPI dashboards |

---

# 🚀 Deployment Runbook

## 1. Containerized Execution (Recommended)

Build the container image:

```bash
docker build -t sales-forecast-mlops .

Run the pipeline container:

docker run -v $(pwd)/data:/app/data sales-forecast-mlops

This executes the full ETL and ML forecasting workflow in a containerized environment.


---

2. Local Development Setup

Clone the repository:

git clone <repo-url>
cd sales-forecast-mlops

Create virtual environment:

python -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the pipeline manually:

python src/main.py


---

📊 Output Artifacts

The pipeline generates a structured dataset for downstream analytics:

data/processed/sales_predictions.csv

This dataset contains:

predicted sales values

forecasted time-series metrics

processed business indicators


The output can be directly imported into Power BI dashboards.


---

🔄 Continuous Integration

GitHub Actions workflows validate:

pipeline execution

container build stability

dependency compatibility


This ensures reliable automated pipeline runs.


---

📂 Repository Structure

sales-forecast-mlops/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── etl_pipeline.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── main.py
│
├── docker/
│   └── Dockerfile
│
├── .github/workflows/
│   └── automation.yml
│
└── requirements.txt


---

📈 Key Learning Outcomes

Through this project I gained practical experience with:

building automated data engineering pipelines

implementing containerized ML workflows

integrating machine learning with business analytics dashboards

designing reproducible execution environments using Docker

validating pipelines using CI/CD automation



---

🔮 Future Improvements

Planned enhancements include:

cloud-native deployment using AWS managed services

integrating S3 for data storage

implementing model monitoring and drift detection

adding automated retraining triggers



---

👨‍💻 Author

Shreyas Neelaraddi Cloud / DevOps & MLOps Engineer

GitHub: https://github.com/ShreyasVN