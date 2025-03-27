import unittest
from credit_rating import calculate_credit_rating, calculate_mortgage_risk_score

class TestCreditRating(unittest.TestCase):
    def test_low_risk_mortgage(self):
        """Test a single low-risk mortgage resulting in 'AAA' rating."""
        mortgages = [{
            "credit_score": 750,
            "loan_amount": 200000,
            "property_value": 250000,
            "annual_income": 60000,
            "debt_amount": 20000,
            "loan_type": "fixed",
            "property_type": "single_family"
        }]
        self.assertEqual(calculate_credit_rating(mortgages), "AAA")

    def test_mixed_mortgages(self):
        """Test a mix of mortgages resulting in 'AAA' rating."""
        mortgages = [
            {
                "credit_score": 750,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 60000,
                "debt_amount": 20000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 680,
                "loan_amount": 150000,
                "property_value": 175000,
                "annual_income": 45000,
                "debt_amount": 10000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "AAA")

    def test_high_risk_mortgage(self):
        """Test a high-risk mortgage resulting in 'C' rating."""
        mortgages = [{
            "credit_score": 600,
            "loan_amount": 300000,
            "property_value": 320000,
            "annual_income": 50000,
            "debt_amount": 30000,
            "loan_type": "adjustable",
            "property_type": "condo"
        }]
        self.assertEqual(calculate_credit_rating(mortgages), "C")

    def test_average_credit_adjustment(self):
        """Test adjustment based on average credit score affecting rating."""
        mortgages = [
            {
                "credit_score": 650,
                "loan_amount": 100000,
                "property_value": 200000,
                "annual_income": 100000,
                "debt_amount": 10000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 650,
                "loan_amount": 100000,
                "property_value": 200000,
                "annual_income": 100000,
                "debt_amount": 10000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 600,
                "loan_amount": 300000,
                "property_value": 320000,
                "annual_income": 50000,
                "debt_amount": 30000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "C")  # Total 6 > 5

    def test_missing_attribute(self):
        """Test that missing attributes raise ValueError."""
        mortgages = [{
            "credit_score": 750,
            "loan_amount": 200000,
            "property_value": 250000,
            "annual_income": 60000,
            "debt_amount": 20000,
            "loan_type": "fixed"
            # Missing 'property_type'
        }]
        with self.assertRaises(ValueError):
            calculate_credit_rating(mortgages)

    def test_empty_mortgages(self):
        """Test empty mortgage list returns 'C'."""
        mortgages = []
        self.assertEqual(calculate_credit_rating(mortgages), "C")

if __name__ == '__main__':
    unittest.main()