import json
import os

from credit_rating import calculate_credit_rating



try:
    all_mortgages = {}
    # i have files in mortgages folder load files one by one and add in mortgages list
    for file in os.listdir('mortgages'):
        if not file.endswith('.json'):
            continue
        with open(f'mortgages/{file}', 'r') as f:
            data = json.load(f)
            all_mortgages[file] = data['mortgages']

except FileNotFoundError:
    print("Error: 'mortgages.json' file not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'mortgages.json'.")
    exit(1)
except KeyError:
    print("Error: 'mortgages' key not found in JSON data.")
    exit(1)

try:
    # Calculate the credit rating
    for file, mortgages in all_mortgages.items():
        print(f"RMBS: {file}")
        print(f"Credit Rating: {calculate_credit_rating(mortgages)}")
        print()
except ValueError as e:
    print(f"Error: {e}")