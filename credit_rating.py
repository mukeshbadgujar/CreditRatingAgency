def calculate_mortgage_risk_score(mortgage):
    """
    Calculate the risk score for a single mortgage based on its attributes.

    Args:
        mortgage (dict): Dictionary containing mortgage attributes.

    Returns:
        int: Risk score for the mortgage.

    Raises:
        ValueError: If any required attribute is missing.
    """
    required_keys = [
        'credit_score', 'loan_amount', 'property_value', 'annual_income',
        'debt_amount', 'loan_type', 'property_type'
    ]
    for key in required_keys:
        if key not in mortgage:
            raise ValueError(f"Missing required key: {key}")

    risk_score = 0

    # 1. Calculate Loan-to-Value (LTV) Ratio
    ltv = mortgage['loan_amount'] / mortgage['property_value']
    if ltv > 0.9:
        risk_score += 2
    elif ltv > 0.8:
        risk_score += 1

    # 2. Calculate Debt-to-Income (DTI) Ratio
    dti = mortgage['debt_amount'] / mortgage['annual_income']
    if dti > 0.5:
        risk_score += 2
    elif dti > 0.4:
        risk_score += 1

    # 3. Assess Credit Score
    credit_score = mortgage['credit_score']
    if credit_score >= 700:
        risk_score -= 1
    elif credit_score < 650:
        risk_score += 1

    # 4. Assess Loan Type
    if mortgage['loan_type'] == 'fixed':
        risk_score -= 1
    elif mortgage['loan_type'] == 'adjustable':
        risk_score += 1

    # 5. Assess Property Type
    if mortgage['property_type'] == 'condo':
        risk_score += 1

    return risk_score


def calculate_credit_rating(mortgages):
    """
    Calculate the credit rating for an RMBS based on a list of mortgages.

    Args:
        mortgages (list): List of dictionaries, each representing a mortgage.

    Returns:
        str: Credit rating ("AAA", "BBB", or "C").

    Raises:
        ValueError: If any mortgage is missing required attributes.
    """
    if not mortgages:  # Handle empty list case
        return "C"

    total_risk_score = 0
    total_credit_score = 0
    num_mortgages = len(mortgages)

    # Calculate individual risk scores and sum credit scores
    for mortgage in mortgages:
        risk_score = calculate_mortgage_risk_score(mortgage)
        total_risk_score += risk_score
        total_credit_score += mortgage['credit_score']

    # 6. Adjust total risk score based on average credit score
    average_credit_score = total_credit_score / num_mortgages
    if average_credit_score >= 700:
        total_risk_score -= 1
    elif average_credit_score < 650:
        total_risk_score += 1

    # Assign credit rating based on total risk score
    if total_risk_score <= 2:
        return "AAA"
    elif total_risk_score <= 5:
        return "BBB"
    else:
        return "C"