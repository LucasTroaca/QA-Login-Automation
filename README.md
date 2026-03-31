## QA Login Automation
![Tests](https://github.com/LucasTroaca/QA-Login-Automation/actions/workflows/tests.yml/badge.svg)

Automated login using Python with Playwright + Pytest andPage Object Model

## About
This project is an automated test suite for login functionality using:

- pytest
- Page Object Model (POM)
- Data Driven Testing

It validates different login scenarios such as:
- Sucessful login
- Invalid credentials
- Without credentials

## Technologies

- Python
- Pytest
- Pytest fixture
- Playwright
- Git & Github

## Instalation
Clone repository: 
```bash
git clone https://github.com/LucasTroaca/QA-Login-Automation
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Install Playwright Browsers:
```bash
playwright install
```

## Running Tests
```bash
pytest -v
```

## CI
Tests are executed automatically using GitHub Actions on push or pull requests


## Screenshots
Screenshots are saved in:
screenshots/

## Author
Lucas Gabriel Troaca
