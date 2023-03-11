"""
functioons for project
"""
import pandas as pd
import random
import csv
import string
import time
from validate_email import validate_email


def generate_emails(valid_ratio=0.9, num_emails=1000, output_file="emails.csv"):
    """
    Generates and saves a list of random email addresses to a CSV file.

    Parameters:
    - valid_ratio (float): The proportion of valid email addresses to generate. Must be between 0 and 1.
    - num_emails (int): The total number of email addresses to generate.
    - output_file (str): The path of the CSV file to save the email addresses to.

    Returns:
    - None: The function saves the email addresses to a CSV file and does not return a value.
    """

    # Record the start time of the function for performance measurement
    start_time = time.time()

    # Initialize lists to hold valid and invalid email addresses
    valid_emails = []
    invalid_emails = []

    # Determine the number of valid and invalid email addresses to generate based on the valid_ratio parameter
    num_valid_emails = int(num_emails * valid_ratio)
    num_invalid_emails = num_emails - num_valid_emails

    # Generate valid emails
    for i in range(num_valid_emails):
        username = "".join(random.choices(string.ascii_lowercase, k=8))
        domain = "".join(random.choices(string.ascii_lowercase, k=8))
        tld = random.choice(["com", "org", "net"])
        email = f"{username}@{domain}.{tld}"
        valid_emails.append(email)

    # Generate invalid emails
    for i in range(num_invalid_emails):
        email = "".join(random.choices(string.ascii_lowercase, k=16))
        invalid_emails.append(email)

    # Combine valid and invalid emails and shuffle the list
    all_emails = valid_emails + invalid_emails
    random.shuffle(all_emails)

    # Save emails to CSV file
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["emails"])
        for email in all_emails:
            writer.writerow([email])

    # Record the end time of the function for performance measurement
    end_time = time.time()

    # Calculate the duration of the function and print a message to the console
    duration = end_time - start_time
    print(f"Generated and saved {num_emails} emails in {duration:.2f} seconds")


def get_valid_invalid_emails_from_csv(file_path):
    """
    This function reads the specified CSV, XLSX or XLS file into a pandas DataFrame, extracts the email addresses from
    the 'emails' column and checks each email address against the regular expression to separate valid and invalid email
    addresses. It returns two lists containing valid and invalid email addresses respectively.

    Args:
    - file_path (str): The file path of the input file containing email addresses in the 'emails' column.

    Returns:
    - valid_emails (list): A list of valid email addresses extracted from the 'emails' column.
    - invalid_emails (list): A list of invalid email addresses extracted from the 'emails' column.
    """

    # Read the file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Extract the email addresses from the 'emails' column
    emails = df["emails"].tolist()

    # Initialize lists to hold valid and invalid email addresses
    valid_emails = []
    invalid_emails = []

    # Check each email address against the regular expression
    for email in emails:
        if validate_email(email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)

    # Return the lists of valid and invalid email addresses
    return valid_emails, invalid_emails


def get_valid_and_invalid_emails_from_excel(file_path):
    """
    Extracts valid and invalid email addresses from an Excel file containing an 'emails' column.

    Args:
    - file_path: str, the path to the Excel file to be loaded

    Returns:
    - valid_emails: list, a list of valid email addresses extracted from the 'emails' column
    - invalid_emails: list, a list of invalid email addresses extracted from the 'emails' column

    Raises:
    - ValueError: if the 'emails' column is not present in the Excel file

    Dependencies:
    - pandas (imported as pd)
    - validate_email function from validate_email module

    Example usage:
    valid_emails, invalid_emails = get_valid_and_invalid_emails_from_excel("emails.xlsx")
    """

    # Load the file into a pandas DataFrame
    df = pd.read_excel(file_path, engine="openpyxl", na_filter=False)

    # Check if 'emails' column is present in the DataFrame
    if "emails" not in df.columns:
        raise ValueError("Excel file does not contain an 'emails' column")

    # Extract the email addresses from the 'emails' column
    emails = df["emails"].tolist()

    # Check each email address against the pattern and separate valid and invalid emails
    valid_emails = []
    invalid_emails = []
    for email in emails:
        if validate_email(email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)

    return valid_emails, invalid_emails
