import csv
import requests as req
from bs4 import BeautifulSoup as bs

url = "https://realpython.github.io/fake-jobs/"

res = req.get(url)

if res.status_code == 200:
    soup = bs(res.text, "html.parser")
    jobs = soup.find_all("div", class_="card")

    with open("jobs.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "Job Link"])

        for job in jobs:

            title_tag = job.find("h2", class_="title")
            company_tag = job.find("h3", class_="company")
            location_tag = job.find("p", class_="location")
            link_tag = job.find("a")

            title = title_tag.text.strip() if title_tag else "N/A"
            comp = company_tag.text.strip() if company_tag else "N/A"
            location = location_tag.text.strip() if location_tag else "N/A"
            link = link_tag["href"] if link_tag and link_tag.get("href") else "N/A"

            writer.writerow([title, comp, location, link])

    print(len(jobs), "jobs scraped succesfully\nCreated the csv file!")

else: print("Couldn't fetch the site!")