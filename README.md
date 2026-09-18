# 🐍 Python Job Scraper

A beginner-friendly web scraping project built with Python that collects job listings from the [Fake Python Jobs](https://realpython.github.io/fake-jobs/) website.

The scraper extracts useful information from each job posting and stores the collected data in a CSV file for easy viewing and further analysis.

---

## 📌 About the Project

This project demonstrates the basic workflow of **web scraping using Python**.

The program visits the Fake Python Jobs website, reads its HTML structure, identifies individual job listings, extracts the required information, and saves the results into a `jobs.csv` file.

### Data Extracted

For each job posting, the scraper collects:

* **Job Title**
* **Company Name**
* **Location**
* **Job Detail Page URL**

The project also includes basic handling for missing fields so that the scraper can continue working even if some information is unavailable.

---

## 🛠️ Technologies Used

| Technology               | Purpose                                  |
| ------------------------ | ---------------------------------------- |
| **Python**               | Main programming language                |
| **Requests**             | Fetches the webpage HTML                 |
| **Beautiful Soup (bs4)** | Parses HTML and extracts job information |
| **CSV Module**           | Stores the scraped data in a CSV file    |

---

## 📂 Project Structure

```text
Python-Job-Scraper/
│
├── scraper.py
├── jobs.csv
└── README.md
```

### `scraper.py`

Contains the Python code responsible for:

* Sending a request to the website
* Parsing the HTML
* Finding job listings
* Extracting job information
* Saving the results to CSV

### `jobs.csv`

Contains the scraped job listings in a structured format.

---

## ⚙️ How It Works

The scraper follows these basic steps:

```text
Fake Python Jobs Website
          ↓
    Send HTTP Request
          ↓
       Get HTML
          ↓
   BeautifulSoup Parser
          ↓
     Find Job Cards
          ↓
 ┌────────┼─────────┐
 ↓        ↓         ↓
Title   Company   Location
          ↓
       Job URL
          ↓
       CSV File
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone github.com/Partha-zzz/python-job-scrapper
```

### 2. Open the project folder

```bash
cd Python-Job-Scraper
```

### 3. Install the required libraries

```bash
pip install requests beautifulsoup4
```

The `csv` module does not need to be installed because it is included with Python.

### 4. Run the scraper

```bash
python scraper.py
```

After successful execution, the scraped data will be saved in:

```text
jobs.csv
```

---

## 📊 Output

The generated CSV file contains the following columns:

```text
Job Title
Company
Location
Job URL
```

Example:

```text
Job Title,Company,Location,Job URL
Python Developer,Example Company,New York,https://...
Web Developer,Example Company,Boston,https://...
```

---

## 🎓 What I Learned

Through this project, I learned the fundamentals of **web scraping with Python**, including:

* How websites are structured using **HTML**
* How to inspect and identify HTML elements
* How to send HTTP requests using the **Requests** library
* How to parse HTML using **BeautifulSoup**
* How to use `find()` and `find_all()` to locate elements
* How to extract text and attributes such as `href`
* How to clean extracted data using `.strip()`
* How to handle missing HTML elements
* How to loop through multiple job listings
* How to organize scraped information into structured data
* How to write data into a **CSV file**
* Understanding the basic workflow of a real-world web scraper

This project also provides a foundation for more advanced scraping concepts such as **pagination, filtering, data cleaning, and scraping dynamic websites**.

---

## 🌐 Source Website

This project uses the **Fake Python Jobs** website created for educational purposes:

https://realpython.github.io/fake-jobs/

It is specifically designed for learning and practicing web scraping.

---

## 🔮 Future Improvements

Some possible improvements for this project include:

* Add keyword-based job filtering
* Add pagination support
* Sort jobs by location or company
* Add command-line search options
* Scrape additional job information
* Export data to JSON or Excel
* Add logging and better error handling
* Build a simple web interface for searching the scraped jobs

---

## 📄 License

This project is created for **educational and learning purposes**.
