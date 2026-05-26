# Appium Python Mobile Automation Framework

End-to-End Mobile Automation Framework developed using Appium with Python, Pytest, and Page Object Model (POM) architecture.

This project automates major user workflows of a Mobile E-Commerce Application including User Login, Product Browsing, Add To Cart, Checkout, and End-to-End Purchase Flow.

---

# Application Under Test

Mobile E-Commerce Application

---

# Tech Stack

- Python
- Appium
- Pytest
- Selenium WebDriver
- Page Object Model (POM)
- Android Studio
- Appium Inspector
- HTML Reports (pytest-html)
- WebDriver Manager
- Git & GitHub

---

# Framework Features

- Page Object Model Design Pattern
- Reusable Base Utilities
- Explicit Waits
- Pytest Fixtures
- HTML Reporting
- Screenshot Capture on Failures
- Modular Framework Structure
- Android Mobile Automation

---

# Project Structure

```bash
Appium_Framework/
│
├── Ecommerce_Framework/
│
├── pages/
│   ├── cart_page.py
│   ├── home_page.py
│   ├── products_page.py
│   ├── webview_page.py
│
├── tests/
│   ├── test_e2e_hybrid.py
│
├── utilities/
│   ├── base_page.py
│
├── screenshots/
├── reports/
│
├── conftest.py
└── pytest.ini
```

---

# Key Automation Scenarios

- Mobile User Login Validation
- Product Browsing & Selection
- Add Products To Cart
- Checkout & Order Placement
- End-to-End Purchase Flow
- Screenshot Capture on Failure
- HTML Report Generation

---

# Reporting

HTML reports are generated automatically after execution.

```bash
reports/report.html
```

Screenshots are automatically captured on test failures.

```bash
screenshots/
```

---

# Installation

```bash
pip install appium-python-client
pip install selenium
pip install pytest
pip install pytest-html
pip install webdriver-manager
```

OR

```bash
pip install -r requirements.txt
```

---

# Run Tests

## Run All Tests

```bash
pytest
```

## Run Specific Test File

```bash
pytest tests/test_login.py
```

## Run With HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

# Appium Server

Start Appium Server before execution.

```bash
appium
```

---

# Android Device Setup

- Connect Android Device or Start Emulator

Verify device connection:

```bash
adb devices
```

---

# Clone Repository

```bash
git clone https://github.com/prasiddh99/Appium_Python_Project.git
```

---

# Future Improvements

- Jenkins CI/CD Integration
- Parallel Mobile Execution
- Allure Reporting
- Hybrid App Automation
- API + Mobile Automation Integration
- Data Driven Testing
- Automate Test Cases

---

# Author

Prasiddh Dharmnathi

GitHub:
https://github.com/prasiddh99
