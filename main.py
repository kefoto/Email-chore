import smtplib
import schedule
import os
import sys
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
import json

load_dotenv()

# Gmail credentials
  # Comma-separated list of recipients



def shift_persons(data):
    result = {}
    persons = data.get("people", [])
    last_person = persons.pop()  # Remove the last person
    persons.insert(0, last_person)  # Add them to the beginning of the list
    
    result["people"] = persons
    result["chores"] = data.get("chores", [])
    
    return result
    
# Compose the email
def send_email(data, EMAIL, APP_PASSWORD, recipients):
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = ", ".join(recipients)  # Displayed list in the email header
    from datetime import datetime

    current_date = datetime.strptime("5/22/2024", "%m/%d/%Y").strftime("%B %d, %Y")
    msg["Subject"] = f"[AUTO] Barton Cleaning Chore - Week of {current_date}"

    link= "https://www.icloud.com/notes/0c50Q7W6o4OxD4agg0b77mc8g#Cleaning"
    body_content = ""
    for i, chore in enumerate(data.get("chores", [])):
        person = data.get("people", [])[i % len(data.get("people", []))]
        body_content += f"{person}: {chore}\n"
    body = f'''Hi All Fellas from Barton,\n\nCleaning due this Sunday with your weekly Automatic Chore update:\n\n{body_content}'''

    body += f"\n\nWeekly Cleaning duty List:\n{link}\n{current_date}\nBest,\nKe Xu"
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, APP_PASSWORD)
            server.sendmail(EMAIL, recipients, msg.as_string())  # Actual recipient list
            print("Email sent successfully to multiple recipients!")
            
            server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")


def main():
    
    EMAIL = os.getenv("GMAIL_USER")  # Your Gmail address
    APP_PASSWORD = str(os.getenv("GMAIL_APPPASSWORD"))  # Your Gmail App Password
    recipients = os.getenv("RECIPIENTS").split(",")

    # print("Recipients:", recipients)
    # print("Email:", EMAIL)
    # print("App Password:", APP_PASSWORD)

    data = {}
    # Load data from a JSON file
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
    send_email(data, EMAIL, APP_PASSWORD, recipients)
    data_updated = shift_persons(data)
    with open("data.json", "w") as json_file:
        json.dump(data_updated, json_file, indent=4)


if __name__ == "__main__":
    # Schedule to run every Tuesday at 6 AM
    schedule.every().tuesday.at("06:00").do(send_email)
# # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(7200)
