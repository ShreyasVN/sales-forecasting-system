```markdown
# AI-Driven Sales Analytics and Forecasting Dashboard

![Project Cover Image](images/Project%20Cover%20Image.png)

## 📖 Overview
This project provides an end-to-end automated solution for analyzing historical sales data and forecasting future trends. By leveraging machine learning and cloud-native architecture, it empowers sales teams and management to make data-driven decisions without manual reporting overhead.

---

## 🏗️ Architecture
The system is designed as a modular, automated pipeline moving from data ingestion to visualization.

![System Architecture Diagram](images/System%20Architecture%20Diagram.png)

**System Flow:**
1. **Ingestion:** Historical data is loaded from `data/raw/`.
2. **Processing:** Python scripts clean, aggregate, and engineer features (lag variables, rolling averages).
3. **Modeling:** A Random Forest regressor is trained to predict future sales.
4. **Visualization:** Forecast results are exported for Power BI dashboards.
5. **Automation:** GitHub Actions schedules daily execution to refresh predictions.

---

## 🚀 Key Features
- **Automated Data Pipeline:** Handles missing values, date formatting, and feature generation automatically.
- **Machine Learning Forecasting:** Uses Random Forest regression to predict daily sales volumes with accuracy metrics.
- **Interactive Dashboard:** Ready-to-use data output for Power BI visualization.
- **Cloud Ready:** Containerized with Docker and deployable on AWS EC2.
- **CI/CD Integration:** Fully automated workflows using GitHub Actions.

---

## 🛠 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python |
| **Data Processing** | Pandas, NumPy, Scikit-Learn |
| **Visualization** | Power BI |
| **Containerization** | Docker |
| **Cloud** | AWS EC2 |
| **Automation** | GitHub Actions |

---

## 📁 Project Structure

```text
sales-forecasting-system/
├── .github/
│   └── workflows/
│       └── automation.yml      # CI/CD Pipeline definition
├── data/
│   ├── raw/
│   │   └── store_sales.csv     # Input historical data
│   └── processed/
│       └── sales_predictions.csv # Output for Power BI
├── images/                     # Visual assets and diagrams
├── models/
│   └── sales_model.pkl         # Serialized ML model
├── src/
│   ├── config.py               # Configuration settings
│   ├── data_processing.py      # ETL and Feature Engineering
│   ├── train_model.py          # Training logic
│   └── main.py                 # Entry point
├── Dockerfile                  # Container definition
├── requirements.txt            # Python dependencies
└── README.md

```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.9+
* Docker (optional, for containerization)
* Power BI Desktop (for visualization)

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd sales-forecasting-system

```

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

```

### 3. Setup Data

Ensure the `store_sales.csv` file is placed in the `data/raw/` directory.
*(If not present, download it from [skforecast-datasets](https://www.google.com/search?q=https://raw.githubusercontent.com/skforecast/skforecast-datasets/main/data/store_sales.csv))*

### 4. Run the Pipeline

```bash
python src/main.py

```

### 5. Visualize in Power BI

1. Open Power BI Desktop.
2. Click **Get Data** -> **Text/CSV**.
3. Select `data/processed/sales_predictions.csv`.
4. Use the `date` field for the X-axis and `actual_sales` / `predicted_sales` for values.

---

## 🤖 Machine Learning Workflow

The model utilizes a Random Forest Regressor trained on time-series features:

* **Lag Features:** Sales from previous days (`lag_1`, `lag_2`).
* **Rolling Statistics:** 3-day moving average.
* **Temporal Features:** Day of week, month, weekend flag.

---

## 🔄 Automation & CI/CD

The project uses GitHub Actions to automate the forecasting pipeline. The workflow is triggered daily (Cron: `0 0 * * *`) to ensure the model is retrained with the latest data.

---

## 🌐 Deployment

The application is containerized using Docker for easy deployment to AWS EC2.

**Build Image:**

```bash
docker build -t sales-forecast-app .

```

**Run Container:**

```bash
docker run -v $(pwd)/data:/app/data sales-forecast-app

```

---

## 📊 Success Metrics

* **Forecast Accuracy:** Model consistently outperforms baseline naive forecasts.
* **Automation:** Zero-touch data refresh and model retraining.
* **Clarity:** Clear visualization of KPIs and trends in the dashboard.

---

## 📝 License

This project is for educational and internal business demonstration purposes.

