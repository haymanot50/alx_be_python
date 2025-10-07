# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division safely with error handling."""
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        result = num / den
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handles non-numeric input
        return "Error: Please enter numeric values only."
