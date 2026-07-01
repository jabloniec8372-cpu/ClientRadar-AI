import csv
import os
from datetime import datetime


CSV_COLUMNS = [
    "company",
    "website",
    "country",
    "website_online",
    "website_status",
    "website_title",
    "score",
    "recommendation",
]


def create_report_paths():
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base_path = os.path.join("reports", f"clientradar_report_{timestamp}")

    return f"{base_path}.txt", f"{base_path}.csv"


def calculate_summary(analyzed_companies):
    scores = [company["score"] for company in analyzed_companies]
    best_company = max(analyzed_companies, key=lambda company: company["score"])
    worst_company = min(analyzed_companies, key=lambda company: company["score"])
    all_scores_equal = len(set(scores)) == 1

    return {
        "companies_analyzed": len(analyzed_companies),
        "websites_online": sum(
            1 for company in analyzed_companies if company["website_online"]
        ),
        "websites_offline": sum(
            1 for company in analyzed_companies if not company["website_online"]
        ),
        "average_score": sum(scores) / len(scores),
        "highest_score": max(scores),
        "lowest_score": min(scores),
        "best_company": best_company["company"],
        "worst_company": worst_company["company"],
        "all_scores_equal": all_scores_equal,
        "high_priority": sum(
            1 for company in analyzed_companies
            if company["recommendation"] == "High Priority"
        ),
        "medium_priority": sum(
            1 for company in analyzed_companies
            if company["recommendation"] == "Medium Priority"
        ),
        "low_priority": sum(
            1 for company in analyzed_companies
            if company["recommendation"] == "Low Priority"
        ),
    }


def build_statistics_text(summary):
    statistics_lines = [
        "",
        "========== REPORT STATISTICS ==========",
        "",
        f"Total companies analyzed: {summary['companies_analyzed']}",
        f"Average AI Score: {summary['average_score']:.1f}",
    ]

    if summary["all_scores_equal"]:
        statistics_lines.append(
            f"All companies have the same AI score: {summary['highest_score']}"
        )
    else:
        statistics_lines.append(
            f"Best company by score: {summary['best_company']} ({summary['highest_score']})"
        )
        statistics_lines.append(
            f"Worst company by score: {summary['worst_company']} ({summary['lowest_score']})"
        )

    statistics_lines.append("")

    return statistics_lines


def build_report_text(analyzed_companies, summary):
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

    report_lines.extend(build_statistics_text(summary))

    report_lines.extend([
        "",
        "Report generated.",
        "",
    ])

    return "\n".join(report_lines)


def save_text_report(report_text, txt_report_path):
    with open(txt_report_path, "w", encoding="utf-8") as file:
        file.write(report_text)


def save_csv_report(analyzed_companies, csv_report_path):
    with open(csv_report_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(analyzed_companies)


def print_summary(summary, txt_report_path, csv_report_path):
    print("=====================================")
    print("CLIENTRADAR SUMMARY")
    print("=====================================")
    print()
    print(f"Companies analyzed: {summary['companies_analyzed']}")
    print()
    print(f"Websites online: {summary['websites_online']}")
    print()
    print(f"Websites offline: {summary['websites_offline']}")
    print()
    print(f"Average AI Score: {summary['average_score']:.1f}")
    print()
    print(f"Highest score: {summary['highest_score']}")
    print()
    print(f"Lowest score: {summary['lowest_score']}")
    print()
    if summary["all_scores_equal"]:
        print(f"All companies have the same AI score: {summary['highest_score']}")
        print()
    else:
        print(f"Best company by score: {summary['best_company']}")
        print()
        print(f"Worst company by score: {summary['worst_company']}")
        print()

    print(f"High Priority: {summary['high_priority']}")
    print()
    print(f"Medium Priority: {summary['medium_priority']}")
    print()
    print(f"Low Priority: {summary['low_priority']}")
    print()
    print("TXT Report:")
    print(txt_report_path)
    print()
    print("CSV Report:")
    print(csv_report_path)
    print()
    print("=====================================")
    print()


def generate_report(analyzed_companies):
    txt_report_path, csv_report_path = create_report_paths()
    summary = calculate_summary(analyzed_companies)
    report_text = build_report_text(analyzed_companies, summary)

    save_text_report(report_text, txt_report_path)
    save_csv_report(analyzed_companies, csv_report_path)

    print(report_text)
    print(f"Saved to: {txt_report_path}")
    print(f"Saved to: {csv_report_path}")
    print()

    print_summary(summary, txt_report_path, csv_report_path)
