# result_downloader
Simply a python code to download result from hslc/hsslc.
Edit the website url on the code to your required site.
example: url = "https://results.indiaresults.com/mz/mbse/hslc-exam-result-2025/result.asp"
into url = "https://results.indiaresults.com/mz/mbse/hslc-exam-result-2024/result.asp" 
and so on.

Format for the name_roll_reg_list.txt is
Name,Roll,Reg
example: Alice,210120125,23191240122

Requirements:
1. Python Modules (install using pip):
   - requests
   - pdfkit
pip install requests pdfkit

2. wkhtmltopdf (required by pdfkit)
   - Download from: https://wkhtmltopdf.org/downloads.html
   - Install the version for your OS
   - Windows default path: C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe

3. Add wkhtmltopdf to System PATH (optional but recommended)#if not working this could be the reason
   OR
   Specify the full path in your Python script like this:
   pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
