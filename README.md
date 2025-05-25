**Chore Email Automation**
# INFO
- **Author**: Ke Xu
- **Date**: 5/22/2025

# 🚀 Python Environment Setup (Quick Guide)

## 1. ✅ Install Python
- Download Python: [https://python.org/downloads](https://python.org/downloads)
- During installation, make sure to check **"Add Python to PATH"**

---

## 2. 🐍 Create a Virtual Environment

```bash
# Navigate to your project folder
cd /path/to/your/project
```

# Create a virtual environment
python -m venv venv

## 3. 🌟 Activate the Virtual Environment

### On Windows:
```bash
# Activate the virtual environment
venv\Scripts\activate
```

### On Mac/Linux:
```bash
# Activate the virtual environment
source venv/bin/activate
```

---

## 4. 📦 Install Required Packages

### After activating the virtual environment:
```bash
# Install dependencies from requirements.txt
pip install -r requirements.txt
```


## 5. 🛠️ Setup `.env` File

Create a `.env` file in the root of your project directory and add the following variables:

```properties
# Your Gmail address
GMAIL_USER=your_email@gmail.com

# Your Gmail App Password (generate it from https://myaccount.google.com/apppasswords)(Requires two factor of your google account first)
GMAIL_APPPASSWORD=your_app_password

# Recipient email addresses (comma-separated for multiple recipients)
RECIPIENTS=recipient1@example.com,recipient2@example.com
```

Replace `your_email@gmail.com`, `your_app_password`, and `recipient1@example.com` with your actual Gmail credentials and recipient email addresses.

---
## 6. ▶️ Run the Python File

After setting up the `.env` file, replacing name and chores in `data.json` file if needed, and activating the virtual environment, run the Python script:

```bash
# Run the Python file
python main.py
```
