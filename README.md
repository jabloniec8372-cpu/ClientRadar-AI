# 🚀 ClientRadar AI

**ClientRadar AI** is a beginner-friendly Python application for importing company leads from CSV, checking website availability, scoring companies, generating recommendations, and exporting reports.

The project is designed as a simple foundation for an AI-powered lead generation platform. It currently runs in the terminal and uses only Python's standard library.

---

## ✨ Features

| Feature | Status | Description |
|---|---:|---|
| CSV import | ✅ Working | Loads companies from `core/companies.csv`. |
| Website availability check | ✅ Working | Checks if company websites respond online. |
| HTTP status detection | ✅ Working | Captures response status such as `200`, `301`, or `403`. |
| Website title extraction | ✅ Working | Reads the page `<title>` when available. |
| Company scoring | ✅ Working | Calculates a simple lead score from website and country data. |
| Recommendations | ✅ Working | Labels companies as `High Priority`, `Medium Priority`, or `Low Priority`. |
| Terminal report | ✅ Working | Prints report output directly in the terminal. |
| TXT export | ✅ Working | Saves `clientradar_report.txt` in the project root. |
| CSV export | ✅ Working | Saves `clientradar_report.csv` in the project root. |

---

## 🔄 Workflow

```text
Start App
   |
   v
Import CSV
   |
   v
Analyze Companies
   |
   v
Check Website Availability
   |
   v
Calculate Score + Recommendation
   |
   v
Generate Report
   |
   +--> Print Report in Terminal
   |
   +--> Save TXT Report
   |
   +--> Save CSV Report
```

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| Python | Main programming language |
| `csv` | CSV import and export |
| `urllib` | Website requests |
| `http.client` | Fallback website status checks |
| `ssl` | HTTPS fallback handling |
| `re` | Website title extraction |

No external packages are required.

---

## 📦 Installation

Clone the project:

```bash
git clone https://github.com/YOUR_USERNAME/ClientRadar-AI.git
cd ClientRadar-AI
```

Or open the existing project folder in VS Code:

```powershell
cd C:\CCLIENT_RADAR_AI
```

Make sure Python is installed:

```bash
python --version
```

---

## ▶️ How To Run

From the project root, run:

```bash
python core\main.py
```

Then use the menu:

```text
1. Import CSV
2. Analyze Companies
3. Generate Report
4. Exit
```

Recommended flow:

```text
1 → import CSV
2 → analyze companies
3 → generate report
```

---

## 📄 Example CSV Input

The current CSV file is located at:

```text
core/companies.csv
```

Example format:

```csv
company,website,country
OpenAI,https://openai.com,USA
Microsoft,https://microsoft.com,USA
SAP,https://sap.com,Germany
BMW,https://bmw.com,Germany
```

---

## 📊 Example Output

Terminal report example:

```text
========== CLIENTRADAR REPORT ==========

Company: OpenAI
Website: https://openai.com
Country: USA
Website Online: True
HTTP Status: 200
Website Title: OpenAI | Research & Deployment
AI Score: 100/100
Recommendation: High Priority
---------------------------------------

Report generated.

Saved to: clientradar_report.txt
Saved to: clientradar_report.csv
```

Generated files:

| File | Description |
|---|---|
| `clientradar_report.txt` | Human-readable text report |
| `clientradar_report.csv` | Structured report data for spreadsheets or CRM workflows |

---

## 📁 Folder Structure

```text
ClientRadar AI/
|
+-- core/
|   +-- main.py
|   +-- menu.py
|   +-- csv_loader.py
|   +-- company_analyzer.py
|   +-- website_checker.py
|   +-- report_generator.py
|   +-- companies.csv
|
+-- clientradar_report.txt
+-- clientradar_report.csv
+-- README.md
```

### Main Files

| File | Purpose |
|---|---|
| `core/main.py` | Runs the application menu and workflow |
| `core/menu.py` | Displays the terminal menu |
| `core/csv_loader.py` | Loads companies from CSV |
| `core/company_analyzer.py` | Scores companies and creates recommendations |
| `core/website_checker.py` | Checks website availability, status, and title |
| `core/report_generator.py` | Prints and exports reports |

---

## 🧭 Project Roadmap

| Stage | Goal | Status |
|---|---|---:|
| Stage 1 | Terminal menu application | ✅ Done |
| Stage 2 | CSV import | ✅ Done |
| Stage 3 | Website availability checks | ✅ Done |
| Stage 4 | Lead scoring and recommendations | ✅ Done |
| Stage 5 | TXT and CSV report exports | ✅ Done |
| Stage 6 | Improve data validation | Planned |
| Stage 7 | Add richer lead scoring rules | Planned |
| Stage 8 | Prepare for AI-assisted recommendations | Planned |

---

## 🔮 Future Improvements

Potential next steps:

- Add better CSV validation and clearer error messages.
- Support custom CSV file paths.
- Add more scoring factors such as industry, company size, or website quality.
- Save reports into a dedicated `reports/` folder.
- Add automated tests for CSV loading, website checks, and report generation.
- Add a simple desktop or web interface.
- Connect future AI recommendation logic when the project is ready for external APIs.

---

## 💼 Freelance Use Case

ClientRadar AI is a practical lead analysis prototype for freelancers, agencies, and small businesses that want to qualify company leads faster.

It demonstrates:

- Clean Python project structure
- CSV-based business data processing
- Website availability analysis
- Simple lead scoring
- Report generation for client delivery

---

## 📌 Current Status

ClientRadar AI is currently a working terminal-based Python prototype. It imports leads, analyzes company websites, generates recommendations, and exports reports in both TXT and CSV formats.
