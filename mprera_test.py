import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.rera.mp.gov.in/view_project_details.php?id=VnUyenVEckNyM1VYUDRHbTgxMXgwdz09"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_text_after_label(soup, label):
    label_div = soup.find("div", string=lambda t: t and label in t)
    if not label_div:
        return None
    return label_div.find_next_sibling("div").get_text(strip=True)

def parse_project(url):
    print("Fetching project page...")
    r = requests.get(url, headers=HEADERS, timeout=120, verify=False)
    print("Status Code:", r.status_code)

    soup = BeautifulSoup(r.text, "html.parser")

    project = {}

    # ---------------- Project Info ----------------
    project["project_name"] = get_text_after_label(soup, "Project Name")
    project["registration_no"] = get_text_after_label(soup, "Registration Number")
    project["project_type"] = get_text_after_label(soup, "Project Type")
    project["application_status"] = get_text_after_label(soup, "Application Status")
    project["contact_email"] = get_text_after_label(soup, "Contact Email")
    project["land_ownership"] = get_text_after_label(soup, "Land Ownership")
    project["start_date"] = get_text_after_label(soup, "Proposed Start Date")
    project["end_date"] = get_text_after_label(soup, "Proposed End Date")
    project["extended_end_date"] = get_text_after_label(soup, "Extended End Date")

    # ---------------- Location ----------------
    project["state"] = get_text_after_label(soup, "State")
    project["district"] = get_text_after_label(soup, "District")
    project["tehsil"] = get_text_after_label(soup, "Tehsil")
    project["address"] = get_text_after_label(soup, "Project Address")

    # ---------------- Bank ----------------
    project["bank_account"] = get_text_after_label(soup, "Account Number")
    project["bank_name"] = get_text_after_label(soup, "Bank Name")
    project["ifsc"] = get_text_after_label(soup, "IFSC Code")

    # ---------------- Promoter ----------------
    project["promoter_name"] = get_text_after_label(soup, "Name :")
    project["promoter_type"] = get_text_after_label(soup, "Applicant Type")
    project["promoter_email"] = get_text_after_label(soup, "Email :")

    # ---------------- Documents ----------------
    documents = []
    doc_section = soup.find("h3", string=lambda t: t and "Project Documents" in t)
    if doc_section:
        table = doc_section.find_next("table")
        for row in table.select("tbody tr"):
            cols = row.select("td")
            if len(cols) >= 4:
                title = cols[1].get_text(strip=True)
                link = cols[3].find("a")
                file_url = link["href"] if link else None
                documents.append({
                    "title": title,
                    "file_url": file_url
                })

    project["documents"] = documents

    return project


if __name__ == "__main__":
    data = parse_project(URL)
    print("\n========== SCRAPED PROJECT DATA ==========\n")
    print(json.dumps(data, indent=2, ensure_ascii=False))
