# Credit Rating Calculation for RMBS

## Overview
This project implements a credit rating calculation for Residential Mortgage-Backed Securities (RMBS) based on attributes of underlying mortgages. The solution computes individual risk scores, aggregates them, adjusts based on the average credit score, and assigns a rating ("AAA", "BBB", or "C").

## Project Structure
- `credit_rating.py`: Contains the business logic for calculating the credit rating.
- `test_credit_rating.py`: Unit tests using the `unittest` framework.
- `requirements.txt`: Lists required Python packages (none beyond standard library).
- `README.md`: This documentation file.
- **Run `run_credit_rating.py` to calculate the credit rating for a list of mortgages.**

## Requirements
- Python 3.x

## Installation
1. Clone or download the repository:


2. No additional dependencies are required as the solution uses only the Python standard library.

## Usage
Run the unit tests to verify the implementation:

``python -m unittest test_credit_rating.py``


To use the function in your code:
```python
from credit_rating import calculate_credit_rating

mortgages = [
    {
        "credit_score": 750,
        "loan_amount": 200000,
        "property_value": 250000,
        "annual_income": 60000,
        "debt_amount": 20000,
        "loan_type": "fixed",
        "property_type": "single_family"
    }
]
rating = calculate_credit_rating(mortgages)
print(rating)  # Outputs: "AAA"