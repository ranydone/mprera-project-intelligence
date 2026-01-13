MPRERA Project Intelligence Scraper

Automated Extraction of Real Estate Regulatory Data (Madhya Pradesh RERA)

📌 Project Overview

This project is an end-to-end Python-based web data extraction and analytics pipeline that programmatically collects real estate project information from the Madhya Pradesh Real Estate Regulatory Authority (MPRERA) portal.

The system scrapes structured project data at city level (e.g., Bhopal) and drills down into project-wise legal, financial, and compliance details, enabling downstream use cases such as property intelligence, due diligence, fraud detection, and automated valuation models (AVM).

🎯 Objectives

Automate collection of RERA-registered real estate projects

Extract project metadata, promoter details, bank/escrow info, inventory, and compliance

Enable city-wise analytics (e.g., all projects in Bhopal)

Provide structured datasets for:

Property due diligence

Ownership verification

Risk and fraud analysis

AVM (Automated Valuation Models)

🔧 Key Features
✅ 1. City-Wise Project Discovery

Filters projects by district/city (e.g., Bhopal)

Automatically identifies and collects project detail page URLs

Designed to scale across all districts in Madhya Pradesh

✅ 2. Deep Project Data Extraction

From each project detail page, the system extracts:

Project Info: Name, Registration No., Type, Status

Location: District, Tehsil, Address

Timeline: Start Date, End Date, Extension Date

Promoter: Name, Type, Email

Financials: Bank name, Escrow Account, IFSC

Inventory: Unit types, total units, sold, remaining

Compliance: Quarterly CA/Engineer certificates

Legal Documents: Title deed, land records, layouts (PDF links)

✅ 3. Production-Grade Networking

Handles SSL certificate issues common in government websites

Implements timeouts, retries, and polite request delays

Designed for stable execution on local systems

✅ 4. Structured Output

Data returned in JSON / Python dictionaries

Easily extendable to:

CSV / Excel export

SQL databases

Property analytics platforms

🧠 Use Cases

🏘 Property Intelligence Platforms – RERA data aggregation for buyers, banks, and developers

⚠️ Fraud & Risk Detection – Identify stalled, non-compliant, or risky projects

📊 AVM (Automated Valuation Models) – Project supply, inventory, and location analytics

🏦 NPA / Collateral Analysis – Legal and compliance validation for mortgage portfolios

📑 Due Diligence Automation – Faster title, approval, and documentation checks

🗂 Project Structure
mprera-project-scraper/
│
├── mprera_test.py              # Single project scraper (proof of concept)
├── mprera_bhopal_list.py      # Fetches all projects in Bhopal
├── mprera_bhopal_details.py   # Extracts detailed data for each Bhopal project
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

⚙️ Tech Stack

Language: Python 3.x

Libraries:

requests – HTTP networking

beautifulsoup4 – HTML parsing

Environment: Local execution (VS Code / Command Prompt)

Data Format: JSON / Structured Dictionaries

▶ How to Run
1️⃣ Install Dependencies
python -m pip install -r requirements.txt

2️⃣ Test with a Single Project
python mprera_test.py


✔ Validates connectivity, SSL handling, and parsing logic.

3️⃣ Fetch All Projects in Bhopal
python mprera_bhopal_list.py


✔ Lists all RERA-registered projects filtered by district = Bhopal.

4️⃣ Extract Detailed Project Data
python mprera_bhopal_details.py


✔ Scrapes structured legal, financial, and compliance information for each project.

🔐 Compliance & Ethics

Scrapes publicly available regulatory information only

No login bypass, CAPTCHA breaking, or restricted data access

Designed with rate limiting to avoid server overload

Intended strictly for research, analytics, and compliance automation

🚀 Future Enhancements

📥 Export to Excel / CSV / PostgreSQL

📄 Automated PDF Download & Text Extraction (Title Deeds, Khasra, Encumbrance)

🔍 Anomaly Detection Engine for fraud/stalled projects

🧠 Machine Learning Integration for:

Project risk scoring

Automated Valuation Models (AVM)

🌐 Multi-State RERA Support (MH RERA, UP RERA, etc.)

🏆 Skills Demonstrated

Web scraping of complex government portals

Data extraction from semi-structured HTML

Handling SSL and networking constraints

Data normalization and structuring

Real estate analytics and regulatory intelligence

📄 License

This project is intended for educational and research purposes using publicly accessible data.

🔗 Author

Ranjit Mishra
Real Estate Analytics | PropTech | Data Engineering
