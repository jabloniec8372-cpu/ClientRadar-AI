import csv
import os


def select_csv_file():
    csv_path = "core/companies.csv"

    if not os.path.exists(csv_path):
        print()
        print("❌ File not found:", csv_path)
        print()
        return None

    print()
    print("===================================")
    print("       IMPORTING CSV FILE")
    print("===================================")
    print()
    print("Loading:", csv_path)
    print()

    companies = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            companies.append(row)

    print(f"✅ Companies loaded: {len(companies)}")
    print()

    print("Company list:")
    print("----------------------------")

    for company in companies:
        print("-", company["company"])

    print()

    return companies