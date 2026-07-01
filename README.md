# 🚀 ClientRadar AI

**Version:** v0.7

**ClientRadar AI** is a Python lead analysis tool that imports companies from CSV, checks website availability, scores leads, generates recommendations, and exports professional reports.

The project is designed as a clean, beginner-friendly foundation for an AI-powered lead generation platform. It currently runs in the terminal and uses only Python's standard library.

---

## ✨ Features

| Feature | Status | Description |
|---|---:|---|
| CSV import | ✅ Working | Loads companies from `core/companies.csv`. |
| Website availability check | ✅ Working | Checks whether company websites respond online. |
| HTTP status detection | ✅ Working | Captures response status such as `200`, `301`, or `403`. |
| Website title extraction | ✅ Working | Reads the page `<title>` when available. |
| Company scoring | ✅ Working | Calculates a simple lead score from website and country data. |
| Recommendations | ✅ Working | Labels companies as `High Priority`, `Medium Priority`, or `Low Priority`. |
| Terminal report | ✅ Working | Prints report output directly in the terminal. |
| Timestamped TXT export | ✅ Working | Saves text reports inside `reports/`. |
| Timestamped CSV export | ✅ Working | Saves structured CSV reports inside `reports/`. |
| Summary statistics | ✅ Working | Displays totals, online/offline counts, score stats, and priority counts. |

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
   +--> Create reports/ Folder
   |
   +--> Save Timestamped TXT Report
   |
   +--> Save Timestamped CSV Report
   |
   +--> Display Summary Statistics
```

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| Python | Main programming language |
| `csv` | CSV import and export |
| `datetime` | Timestamped report file names |
| `os` | Folder creation and file paths |
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

Saved to: reports/clientradar_report_2026-07-01_14-35-20.txt
Saved to: reports/clientradar_report_2026-07-01_14-35-20.csv
```

Summary example:

```text
=====================================
CLIENTRADAR SUMMARY
=====================================

Companies analyzed: 4

Websites online: 4

Websites offline: 0

Average AI Score: 100.0

Highest score: 100

Lowest score: 100

High Priority: 4

Medium Priority: 0

Low Priority: 0

TXT Report:
reports/clientradar_report_2026-07-01_14-35-20.txt

CSV Report:
reports/clientradar_report_2026-07-01_14-35-20.csv

=====================================
```

---

## 🗂 Reports Folder

ClientRadar AI v0.7 automatically creates a `reports/` folder when option `3` is selected.

Generated report files use the current local date and time:

```text
reports/clientradar_report_YYYY-MM-DD_HH-MM-SS.txt
reports/clientradar_report_YYYY-MM-DD_HH-MM-SS.csv
```

This keeps historical reports instead of overwriting the previous output.

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
+-- reports/
|   +-- clientradar_report_YYYY-MM-DD_HH-MM-SS.txt
|   +-- clientradar_report_YYYY-MM-DD_HH-MM-SS.csv
|
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
| `core/report_generator.py` | Prints reports, saves exports, and displays summary statistics |

---

## 🧭 Project Roadmap

| Stage | Goal | Status |
|---|---|---:|
| v0.6 | CSV import, website checks, scoring, TXT and CSV exports | ✅ Done |
| v0.7 | Reports folder, timestamped exports, summary statistics | ✅ Done |
| v0.8 | Better validation and automated tests | Planned |
| v0.9 | Richer scoring rules and cleaner report templates | Planned |
| v1.0 | Stable lead analysis workflow for client demos | Planned |

---

## 🔮 Future Improvements

Potential next steps:

- Add better CSV validation and clearer error messages.
- Support custom CSV file paths.
- Add automated tests for CSV loading, website checks, and report generation.
- Add more scoring factors such as industry, company size, or website quality.
- Save report metadata for easier tracking.
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
- Timestamped report generation
- Client-ready TXT and CSV exports

---

## 📌 Current Status

ClientRadar AI v0.7 is a working terminal-based Python prototype. It imports leads, analyzes company websites, generates recommendations, exports timestamped reports, and displays summary statistics.
