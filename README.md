# 🌍 ESG Analytics Platform

A complete **full-stack ESG (Environmental, Social, and Governance) Analytics Platform** developed for the **Breathe ESG Internship Assignment**.

This project provides:

✅ ESG emissions tracking
✅ Interactive analytics dashboard
✅ REST API backend
✅ PDF report generation
✅ Cloud deployment using Render
✅ Frontend visualization using Streamlit

---

# 🚀 Live Deployment Links

## 🌐 Frontend Dashboard

https://breathe-esg-frontend-yhxm.onrender.com/

## ⚙️ Backend API

https://breathe-esg-assignment-thoq.onrender.com/

## 💻 GitHub Repository

https://github.com/sainarayana1/breathe-esg-assignment

---

# 📌 Project Overview

The ESG Analytics Platform is designed to help organizations monitor and analyze sustainability metrics related to carbon emissions.

The platform provides:

* Emission analytics
* CO₂ tracking
* ESG dashboards
* PDF reporting
* REST API endpoints
* Frontend visualization

---

# 🛠️ Tech Stack

## Backend

* Python
* Django
* Django REST Framework
* SQLite
* ReportLab

## Frontend

* Streamlit
* Pandas
* Requests

## Deployment

* Render Cloud Platform
* GitHub

---

# 📂 Project Structure

```bash
breathe-esg-assignment/
│
├── audits/
├── companies/
├── config/
├── emissions/
├── ingestion/
├── sample_data/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# ✨ Features

## ✅ ESG Dashboard

Interactive frontend dashboard for ESG insights.

## ✅ Emission Analytics

Breakdown of:

* Electricity emissions
* Travel emissions
* Fuel emissions

## ✅ Top Emission Sources

Tracks major contributors to carbon emissions.

## ✅ REST API Backend

Modular Django REST APIs for ESG operations.

## ✅ PDF Report Generation

Downloadable ESG sustainability reports.

## ✅ Cloud Deployment

Fully deployed backend and frontend on Render.

---

# 🌐 Backend API Endpoints

## Root API

```bash
GET /
```

Response:

```json
{
  "status": "success",
  "project": "Breathe ESG Internship Assignment"
}
```

---

## 📊 Dashboard Analytics

```bash
GET /api/emissions/dashboard/
```

Live API:
https://breathe-esg-assignment-thoq.onrender.com/api/emissions/dashboard/

---

## 📈 Emissions Analytics

```bash
GET /api/emissions/analytics/
```

Live API:
https://breathe-esg-assignment-thoq.onrender.com/api/emissions/analytics/

---

## 🏭 Top Emission Sources

```bash
GET /api/emissions/top-sources/
```

Live API:
https://breathe-esg-assignment-thoq.onrender.com/api/emissions/top-sources/

---

## 📝 ESG Summary Report

```bash
GET /api/emissions/summary-report/
```

Live API:
https://breathe-esg-assignment-thoq.onrender.com/api/emissions/summary-report/

---

## 📄 PDF Report Generation

```bash
GET /api/emissions/pdf-report/
```

Live API:
https://breathe-esg-assignment-thoq.onrender.com/api/emissions/pdf-report/

---

## 🏢 Companies API

```bash
GET /api/companies/
```

Live API:
https://breathe-esg-assignment-thoq.onrender.com/api/companies/

---

## 🔍 Audits API

```bash
GET /api/audits/
```

Live API:
https://breathe-esg-assignment-thoq.onrender.com/api/audits/

---

## 📥 Data Ingestion API

```bash
GET /api/ingestion/
```

Live API:
https://breathe-esg-assignment-thoq.onrender.com/api/ingestion/

---

# 🧪 Running the Project Locally

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sainarayana1/breathe-esg-assignment.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd breathe-esg-assignment
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Run Migrations

```bash
python manage.py migrate
```

---

## 7️⃣ Start Django Server

```bash
python manage.py runserver
```

Backend runs at:

```bash
http://127.0.0.1:8000/
```

---

# 🌐 Frontend Setup

## Install Frontend Dependencies

```bash
pip install streamlit pandas requests
```

---

## Run Frontend

```bash
streamlit run app.py
```

Frontend runs at:

```bash
http://localhost:8501/
```

---

# 📊 Dashboard Preview

The frontend dashboard displays:

✅ Total emissions
✅ Emission analytics
✅ Top emission sources
✅ ESG PDF report download
✅ API integration status

---

# 🚀 Deployment Details

## Backend Deployment

* Platform: Render
* Framework: Django REST Framework

## Frontend Deployment

* Platform: Render
* Framework: Streamlit

---

# 🔮 Future Improvements

* User Authentication
* PostgreSQL Integration
* Real-time ESG Monitoring
* AI-based Sustainability Predictions
* Interactive Charts
* CSV Upload System
* ESG Health Score System

---

# 👨‍💻 Author

## Narayana Mamidipaka

GitHub:
https://github.com/sainarayana1

---

# 📄 License

This project was developed for educational and internship evaluation purposes.
