import json

try:
    with open("raw_data.txt", "r") as file:
        data = file.read()

    lines = data.split("\n")

    records = []

    for line in lines:
        line = line.strip()

        if line:
            parts = line.split(",")

            cleaned_parts = []

            for part in parts:
                cleaned_parts.append(part.strip())

            if len(cleaned_parts) == 4:
                company = cleaned_parts[1].title()
                industry = cleaned_parts[2].lower()
                city = cleaned_parts[3].title()

                record = {
                    "id": cleaned_parts[0],
                    "company": company,
                    "industry": industry,
                    "city": city
                }

                records.append(record)

    cities = set()
    industries = set()

    for record in records:
        cities.add(record["city"])
        industries.add(record["industry"])

    print("Total startups:", len(records))
    print("Unique cities:", len(cities))
    print("Unique industries:", len(industries))

    report = {
        "report_summary": {
            "total_startups": len(records),
            "unique_cities": len(cities),
            "unique_industries": len(industries)
        },
        "startups": records
    }

    with open("report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("Report generated successfully!")

except FileNotFoundError:
    print("Error: raw_data.txt file was not found.")

except Exception as error:
    print(f"Something went wrong: {error}")