from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
import hashlib
import time

BASE_URL = "https://www.rera.mp.gov.in/projectsrcg-loop.php"

def hash_rows(rows):
    text = "|".join([";".join(r) for r in rows])
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def fetch_page(request, params, retries=3):
    for attempt in range(retries):
        try:
            response = request.get(BASE_URL, params=params, timeout=60000)
            return response.text()
        except Exception as e:
            print(f"⚠️ Network error on page {params['pagenum']} (attempt {attempt+1}/{retries}): {e}")
            time.sleep(5)
    return None

def fetch_all_bhopal_projects():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(ignore_https_errors=True)
        request = context.request

        all_rows = []
        page_num = 1
        last_page_hash = None

        while True:
            params = {
                "show": "10",
                "pagenum": str(page_num),
                "search_txt": "",
                "search_dist": "444",   # Bhopal
                "search_tehs": "undefined",
                "project_type_id": ""
            }

            html = fetch_page(request, params)

            if html is None:
                print("❌ Failed after retries. Stopping.")
                break

            soup = BeautifulSoup(html, "html.parser")
            table = soup.find("table")

            if not table:
                print("No table found. Stopping.")
                break

            rows = []
            for row in table.find_all("tr")[1:]:
                cols = [c.get_text(strip=True) for c in row.find_all("td")]
                rows.append(cols)

            if not rows:
                print("No rows found. Stopping.")
                break

            # Detect repeated last page
            current_hash = hash_rows(rows)
            if current_hash == last_page_hash:
                print("Last page repeated. Stopping pagination.")
                break

            last_page_hash = current_hash
            all_rows.extend(rows)

            print(f"Fetched page {page_num} → {len(rows)} records")

            page_num += 1
            time.sleep(2)   # throttle requests

        browser.close()
        return all_rows


# Run
if __name__ == "__main__":
    data = fetch_all_bhopal_projects()
    print("TOTAL RECORDS:", len(data))

    # Save to CSV
    with open("mp_rera_bhopal_projects.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

    print("Saved: mp_rera_bhopal_projects.csv")
