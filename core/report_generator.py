import csv


def generate_report(analyzed_companies):
    csv_columns = [
        "company",
        "website",
        "country",
        "website_online",
        "website_status",
        "website_title",
        "score",
        "recommendation",
    ]

    report_lines = [
        "",
        "========== CLIENTRADAR REPORT ==========",
        "",
    ]

    for company in analyzed_companies:
        report_lines.append(f"Company: {company['company']}")
        report_lines.append(f"Website: {company['website']}")
        report_lines.append(f"Country: {company['country']}")
        report_lines.append(f"Website Online: {company['website_online']}")
        report_lines.append(f"HTTP Status: {company['website_status']}")
        report_lines.append(f"Website Title: {company['website_title']}")
        report_lines.append(f"AI Score: {company['score']}/100")
        report_lines.append(f"Recommendation: {company['recommendation']}")
        report_lines.append("---------------------------------------")

    report_lines.extend([
        "",
        "Report generated.",
        "",
    ])

    report_text = "\n".join(report_lines)

    with open("clientradar_report.txt", "w", encoding="utf-8") as file:
        file.write(report_text)

    with open("clientradar_report.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(analyzed_companies)

    print(report_text)
    print("Saved to: clientradar_report.txt")
    print("Saved to: clientradar_report.csv")
    print()
