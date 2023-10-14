import pytesseract
import re
from pdf2image import convert_from_path

def extract_features_from_pdf(pdf_path):
    """
    Extracts specified features from a PDF file using OCR.

    Args:
    - pdf_path (str): The path to the input PDF file.

    Returns:
    - dict: A dictionary containing the extracted features.
    """

    image1 = convert_from_path(pdf_path, first_page=1, last_page=1)[0]
    image15 = convert_from_path(pdf_path, first_page=15, last_page=15)[0]

    # Process the images using OCR to extract text
    text1 = pytesseract.image_to_string(image1)
    text15 = pytesseract.image_to_string(image15)

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

    # Search for each pattern in the text of the first page and store the result in the dictionary
    for key, pattern in patterns_page1.items():
        match = re.search(pattern, text1)
        if match:
            extracted_info[key] = match.group(1)

    # Pattern for the 15th page for Income
    income_pattern = r"2021\s*[\r\n]+\s*Total\s*[\r\n]+\s*Base Salary\s*[\r\n]+\s*Overtime\s*[\r\n]+\s*Commission\s*[\r\n]+\s*Bonus\s*[\r\n]+\s*Other\s*[\r\n]+\s*([$]\d+[,]*\d*\.\d{2})"
    income_match = re.search(income_pattern, text15)
    if income_match:
        extracted_info["Income 2021"] = income_match.group(1)

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
        from datetime import datetime
        birth_date = datetime.strptime(extracted_info["Date Of Birth"], "%m/%d/%Y")
        current_year = datetime.now().year
        extracted_info["Age"] = current_year - birth_date.year - ((datetime.now().month, datetime.now().day) < (birth_date.month, birth_date.day))
        del extracted_info["Date Of Birth"]  # Remove the original date of birth

    # If "Has Mortgage" is found and it's greater than 0, then set "Has Mortgage" to "Yes"
    if "Has Mortgage" in extracted_info and int(extracted_info["Has Mortgage"]) > 0:
        extracted_info["Has Mortgage"] = "Yes"
    else:
        extracted_info["Has Mortgage"] = "No"

    # Set employment type
    extracted_info["Employment Type"] = "Full Time"  # Setting as Full Time by default if the person is an employee

    return extracted_info