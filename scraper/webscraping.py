from bs4 import BeautifulSoup
from bs4.element import Tag
import datetime
import requests


def scrape_yesterday_match_reports() -> list[str]:
    """
    Scrape football scores from the BBC Sport website for the previous day.

    This function retrieves yesterday's date, constructs a URL for the corresponding
    football scores webpage on BBC Sport, sends an HTTP request to fetch the webpage,
    parses the HTML content using BeautifulSoup, extracts the football scores from
    the main data div, and returns the cleaned text containing the scores.

    Returns:
    str: Text containing match reports extracted from the webpage.
    """
    yesterday = get_yesterday()
    url = f"https://www.bbc.co.uk/sport/football/scores-fixtures/{yesterday}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    scores_div = soup.find("div", id="main-data")
    urls = extract_match_urls(scores_div)
    reports = pull_match_reports(urls)

    return reports


def get_yesterday() -> str:
    """
    Get yesterday's date as a string in the format 'YYYY-MM-DD'.

    Returns:
    str: A string representing yesterday's date in 'YYYY-MM-DD' format.
    """
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y-%m-%d")

    return yesterday_str


def extract_match_urls(soup: Tag) -> list[str]:
    """
    Extracts and returns a list of match URLs from a BeautifulSoup Tag object containing HTML content.

    Parameters:
    soup (Tag): A BeautifulSoup Tag object containing HTML content.

    Returns:
    list[str]: A list of URLs for football live matches found within the provided HTML content.
    """
    urls = []
    # Find all anchor tags that have a 'href' containing '/sport/football/live/'
    live_football_links = soup.find_all(
        "a", href=lambda href: href and "/sport/football/live/" in href
    )

    # Extract the href attribute from each matching anchor tag
    for link in live_football_links:
        href = link.get("href")
        urls.append("https://www.bbc.co.uk" + href)

    return urls


def pull_match_reports(urls: list[str]) -> list[str]:
    """
    Extract match reports from a list of URLs.

    This function iterates through a provided list of URLs, checks each URL for a
    published match report, and uses a language model to extract relevant attributes
    for each match. It then returns a list of Match objects containing the extracted
    data.

    Parameters:
        urls (list[str]): A list of URLs to check for match reports.

    Returns:
        list[str]: A list of Match objects containing data extracted from the reports.
    """
    reports = []
    for url in urls:
        response = requests.get(f"{url}")
        soup = BeautifulSoup(response.text,features='html.parser')

        report_tag = soup.find("a", attrs={"href": "#Report"})

        # Check if the <a> tag exists
        if not report_tag:
            continue

        paragraphs = soup.find_all("p", class_=lambda x: x and "Paragraph" in x)
        report = ""
        for p in paragraphs:
            report += p.text + "\n"

        reports.append(report)
    return reports
