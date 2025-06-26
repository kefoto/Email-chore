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

    current_date = datetime.now().strftime("%B %d, %Y")
    msg["Subject"] = f"[AUTO] Barton Cleaning Chore - Week of {current_date}"

    link= "https://docs.google.com/document/d/1-g94_h1lE9z1vHkeMQp4jJfQI7Yo_tGtbuDt9z0zZVg/edit?tab=t.0"
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
    
    load_dotenv()
    # print("Raw RECIPIENTS:", os.getenv("RECIPIENTS"))
    
    EMAIL = os.getenv("GMAIL_USER")  # Your Gmail address
    APP_PASSWORD = str(os.getenv("GMAIL_APPPASSWORD"))  # Your Gmail App Password
    recipients = os.getenv("RECIPIENTS").split(",")

    print("Recipients:", recipients)

    
    # nateh353@gmail.com,morriskache@gmail.com,

    data = {}
    # Load data from a JSON file
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
    send_email(data, EMAIL, APP_PASSWORD, recipients)
    data_updated = shift_persons(data)
    with open("data.json", "w") as json_file:
        json.dump(data_updated, json_file, indent=4)


if __name__ == "__main__":
    # load_dotenv()
    # Schedule to run every wednesday at 6 AM
    main()
#     schedule.every().wednesday.at("06:00").do(main)
# # # Keep the script running
#     while True:
#         schedule.run_pending()
#         time.sleep(7200)
