# ESG Analytics Platform 🌍

A Django-based ESG (Environmental, Social, and Governance) Analytics Platform developed for the Breathe ESG Internship Assignment.

This platform helps companies:

- Upload emission datasets
- Process ESG records
- Review and approve emissions
- Detect suspicious data
- Generate ESG analytics
- Export ESG PDF reports
- Maintain audit logs
- Benchmark ESG performance

---

# 🚀 Features Implemented

## 1. ESG Data Ingestion

Supports uploading:

- SAP datasets
- Utility datasets
- Travel datasets

### Endpoints

```http
POST /api/upload/sap/
POST /api/upload/utility/
POST /api/upload/travel/
```

### Technologies Used

- Django REST Framework
- CSV Processing
- JSON Parsing

---

# 2. Emission Calculation Engine

Automatically calculates:

- CO2 emissions
- Scope 1 emissions
- Scope 2 emissions
- Scope 3 emissions

### Formula Used

```python
co2e = quantity * emission_factor
```

---

# 3. Review Workflow System

Analysts can:

- Approve records
- Reject records

### Endpoint

```http
POST /api/emissions/review/<record_id>/
```

### Example Request

```json
{
    "action": "approve"
}
```

---

# 4. Audit Logging System

Tracks:

- Who reviewed records
- Action performed
- Timestamp
- Metadata

### Endpoint

```http
GET /api/audits/logs/
```

### Audit Information Stored

- company
- emission_record
- actor
- action
- metadata
- timestamp

---

# 5. ESG Dashboard Analytics

Provides complete ESG metrics.

### Endpoint

```http
GET /api/emissions/dashboard/
```

### Metrics Included

- Total emissions
- Scope-wise emissions
- Approved records
- Pending records
- Rejected records
- Suspicious records

---

# 6. Top Emission Sources

Shows highest emission-producing categories.

### Endpoint

```http
GET /api/emissions/top-sources/
```

### Example Output

```json
[
  {
    "category": "Diesel",
    "total_co2e": 2948.0
  }
]
```

---

# 7. ESG Analytics Engine

Advanced ESG statistics.

### Endpoint

```http
GET /api/emissions/analytics/
```

### Analytics Included

- Total records
- Average emissions
- Highest emission source
- Total emissions

---

# 8. ESG Summary Report

Professional ESG summary generation.

### Endpoint

```http
GET /api/emissions/summary-report/
```

### Includes

- Company details
- Total emissions
- Scope breakdown
- Approved records
- Suspicious records

---

# 9. ESG Health Score

Calculates ESG quality score.

### Endpoint

```http
GET /api/emissions/health-score/
```

### Logic

Score depends on:

- Suspicious records
- Approved records
- Data quality

---

# 10. Company Benchmarking

Benchmarks ESG performance.

### Endpoint

```http
GET /api/emissions/benchmark/
```

### Benchmark Factors

- Total emissions
- Approved records
- Suspicious records

---

# 11. PDF ESG Report Export

Generates downloadable ESG PDF report.

### Endpoint

```http
GET /api/emissions/pdf-report/
```

### Technologies Used

- ReportLab
- Django HttpResponse

### PDF Includes

- Company details
- Emission summary
- ESG statistics
- Suspicious records

---

# 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Django | Backend framework |
| Django REST Framework | API development |
| SQLite | Database |
| ReportLab | PDF generation |
| Postman | API testing |
| GitHub | Version control |
| Render | Deployment |

---

# 📂 Project Structure

```text
backend/
│
├── audits/
├── companies/
├── emissions/
├── ingestion/
├── config/
│
├── manage.py
├── requirements.txt
├── Procfile
└── README.md
```

---

# ⚙️ Setup Instructions

## 1. Clone Repository

```bash
git clone <your-github-repo-url>
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Create Superuser

```bash
python manage.py createsuperuser
```

---

## 6. Run Server

```bash
python manage.py runserver
```

---

# 🌐 Deployment

Deployed using:

- Render.com

### Deployment Steps

1. Push code to GitHub
2. Connect repository to Render
3. Add build/start commands
4. Deploy Django app

---

# 🔗 Important API Endpoints

| Feature | Endpoint |
|---|---|
| Dashboard | `/api/emissions/dashboard/` |
| Analytics | `/api/emissions/analytics/` |
| Summary Report | `/api/emissions/summary-report/` |
| Health Score | `/api/emissions/health-score/` |
| Benchmark | `/api/emissions/benchmark/` |
| PDF Report | `/api/emissions/pdf-report/` |
| Audit Logs | `/api/audits/logs/` |

---

# 🧪 Testing

Tested using:

- Browser
- Postman
- Django Admin Panel

---

# 🔐 Admin Access

### Django Admin

```text
/admin/
```

### Features

- View emission records
- View audit logs
- Manage companies
- Review ESG data

---

# 📊 Sample ESG Metrics

```json
{
    "total_emissions": 9765.17,
    "scope_1_emissions": 6566.0,
    "scope_2_emissions": 2788.0,
    "scope_3_emissions": 411.17
}
```

---

# 📌 Key Learnings

During this project:

- Built REST APIs using Django REST Framework
- Implemented ESG workflows
- Generated PDF reports
- Performed analytics using Django ORM
- Implemented audit logging
- Learned deployment using Render

---

# 👨‍💻 Developed By

Narayana Mamidipaka

For Breathe ESG Internship Assignment
