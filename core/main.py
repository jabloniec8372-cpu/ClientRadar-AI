from menu import show_menu
from csv_loader import select_csv_file
from company_analyzer import analyze_companies
from report_generator import generate_report


def main():
    print("===================================")
    print("      CLIENTRADAR AI v0.7")
    print("===================================")

    companies = []
    analyzed_companies = []

    while True:
        choice = show_menu()

        if choice == "1":
            companies = select_csv_file()
            analyzed_companies = []

            if companies:
                print("✅ Ready for AI analysis.")
                print(f"Loaded companies: {len(companies)}")
            else:
                print("❌ No companies loaded.")

            print()

        elif choice == "2":
            if not companies:
                print()
                print("⚠ Please import a CSV file first.")
                print()
                continue

            analyzed_companies = analyze_companies(companies)

        elif choice == "3":
            if not analyzed_companies:
                print()
                print("No analyzed companies yet. Please run option 2 first.")
                print()
                continue

            generate_report(analyzed_companies)

        elif choice == "4":
            print()
            print("👋 Goodbye!")
            break

        else:
            print()
            print("❌ Invalid option.")
            print()


if __name__ == "__main__":
    main()
