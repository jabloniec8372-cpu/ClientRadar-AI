from website_checker import check_website


def calculate_score(company, website_status):
    score = 40

    if company["website"].startswith("https://"):
        score += 20

    if website_status["online"]:
        score += 25

    if website_status["title"] != "Unavailable":
        score += 5

    if company["country"] in ["USA", "Germany"]:
        score += 10

    return min(score, 100)


def get_recommendation(score):
    if score >= 90:
        return "High Priority"

    if score >= 75:
        return "Medium Priority"

    return "Low Priority"


def analyze_companies(companies):
    print()
    print("========== AI ANALYSIS ==========")
    print()

    analyzed_companies = []

    for company in companies:
        website_status = check_website(company["website"])
        score = calculate_score(company, website_status)
        recommendation = get_recommendation(score)

        result = {
            "company": company["company"],
            "website": company["website"],
            "country": company["country"],
            "website_online": website_status["online"],
            "website_status": website_status["status"],
            "website_title": website_status["title"],
            "score": score,
            "recommendation": recommendation,
        }

        analyzed_companies.append(result)

        print(f"Company: {company['company']}")
        print(f"Website: {company['website']}")
        print(f"Country: {company['country']}")
        print(f"Website Online: {website_status['online']}")
        print(f"HTTP Status: {website_status['status']}")
        print(f"Website Title: {website_status['title']}")
        print(f"AI Score: {score}/100")
        print(f"Recommendation: {recommendation}")
        print("---------------------------------------")

    print()
    print("✅ Analysis finished.")
    print()

    return analyzed_companies