import requests
import pdfkit

# Set path to wkhtmltopdf.exe
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"  # adjust this path if needed
)

# Input file with name,roll,reg
input_file = "name_roll_reg_list.txt"

# Result site and headers
url = "https://results.indiaresults.com/mz/mbse/hslc-exam-result-2025/result.asp"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": url
}

# PDF options — disable all external content
options = {
    'no-images': None,
    'disable-javascript': None,
    'disable-external-links': None,
    'enable-local-file-access': None
}

# Start session
session = requests.Session()

# Read and process entries
with open(input_file, "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if not line or line.count(",") < 2:
        continue  # Skip invalid lines

    name, roll_no, reg_no = [x.strip() for x in line.split(",", 2)]

    payload = {
        "rollno": roll_no,
        "regno": reg_no
    }

    response = session.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        html_content = response.text

        pdf_filename = f"{name}.pdf"
        try:
            pdfkit.from_string(html_content, pdf_filename, configuration=config, options=options)
            print(f"[✓] Saved PDF for {name} (offline-safe)")
        except Exception as e:
            print(f"[!] Skipped PDF for {name} due to error.")
    else:
        print(f"[✗] Failed to fetch result for {name}. Status Code: {response.status_code}")
