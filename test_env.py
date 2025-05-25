import os
from dotenv import load_dotenv

print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())

load_dotenv()

print("GMAIL_USER:", os.getenv("GMAIL_USER"))
print("GMAIL_APP_PASSWORD:", os.getenv("GMAIL_APPPASSWORD"))
print("RECIPIENTS:", os.getenv("RECIPIENTS"))
