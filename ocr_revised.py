from pdfminer.high_level import extract_text
import re
from datetime import datetime

def extract_features_from_pdf(pdf_path):
    text1 = extract_text(pdf_path, page_numbers=[0])
    text15 = extract_text(pdf_path, page_numbers=[14])
    text17 = extract_text(pdf_path, page_numbers=[16])

    # Dictionary to store the extracted information
    extracted_info = {}

    # Patterns for the first page
    patterns_page1 = {
        "Date Of Birth": r"DOB:?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{4})",
        "Credit Score": r"VANTAGESCORE 3.0\s*[\r\n]+\s*(\d{1,4})",
        "Months Employed": r"Total Time with Employer:\s*(\d+ \w+,\s*\d+ \w+)",
        "Number of Credit Lines": r"Revolving:\s*(\d+)",
        "Has Mortgage": r"Mortgage:\s*(\d+)"
    }

    # Pattern for the 16th page for 2021 Income
    income_pattern_2021 = r"2021\s*[$]([\d,]+\.\d{2})"
    income_match_2021 = re.search(income_pattern_2021, text15)
    if income_match_2021:
        extracted_info["Income 2021"] = income_match_2021.group(1)

    # Search for each pattern in the text of the first page and store the result in the dictionary
    for key, pattern in patterns_page1.items():
        match = re.search(pattern, text1)
        if match:
            extracted_info[key] = match.group(1)

    # Extract employment type
    employment_status_pattern = r"Employement Status:\s*(\w+)"
    employment_status_match = re.search(employment_status_pattern, text1)
    if employment_status_match:
        extracted_info["Employment Type"] = employment_status_match.group(1)

    # Extracting the Last Payment Amounts for ACTIVE tradelines
    active_payments = [float(match.group(1).replace("$", "")) for match in re.finditer(r"Total Debits: \s*[$]([\d,]+\.\d{2})", text17)]

    # Calculating the DTI
    annual_income = float(extracted_info["Income 2021"].replace(",", ""))
    monthly_income = annual_income / 12
    dti = sum(active_payments) / monthly_income
    extracted_info["DTI"] = round(dti, 4)

    # If "Months Employed" is found, convert it to months
    if "Months Employed" in extracted_info:
        months_employed_text = extracted_info["Months Employed"]
        years_match = re.search(r"(\d+)\s*years?", months_employed_text)
        months_match = re.search(r"(\d+)\s*months?", months_employed_text)

        total_months = 0
        if years_match:
            total_months += int(years_match.group(1)) * 12
        if months_match:
            total_months += int(months_match.group(1))

        extracted_info["Months Employed"] = total_months

    # If "Date of Birth" is found, compute the age
    if "Date Of Birth" in extracted_info:
        birth_date = datetime.strptime(extracted_info["Date Of Birth"], "%m/%d/%Y")
        current_year = datetime.now().year
        extracted_info["Age"] = current_year - birth_date.year - ((datetime.now().month, datetime.now().day) < (birth_date.month, birth_date.day))
        del extracted_info["Date Of Birth"]  # Remove the original date of birth

    # If "Has Mortgage" is found and it's greater than 0, then set "Has Mortgage" to "Yes"
    if "Has Mortgage" in extracted_info and int(extracted_info["Has Mortgage"]) > 0:
        extracted_info["Has Mortgage"] = "Yes"
    else:
        extracted_info["Has Mortgage"] = "No"

    return extracted_info