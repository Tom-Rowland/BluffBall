from bs4 import BeautifulSoup
from bs4.element import Tag
import datetime
import requests


def scrape_results() -> str:
    """
    Scrape football scores from the BBC Sport website for the previous day.

    This function retrieves yesterday's date, constructs a URL for the corresponding
    football scores webpage on BBC Sport, sends an HTTP request to fetch the webpage,
    parses the HTML content using BeautifulSoup, extracts the football scores from
    the main data div, and returns the cleaned text containing the scores.

    Returns:
    str: Text containing football scores extracted from the webpage.
    """
    yesterday = get_yesterday()
    url = f"https://www.bbc.co.uk/sport/football/scores-fixtures/{yesterday}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    scores_div = soup.find("div", id="main-data")
    urls = extract_match_urls(scores_div)
    scores_text = strip_html(scores_div)
    return scores_text


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


def strip_html(soup: Tag) -> str:
    """
    Strip HTML tags from a BeautifulSoup Tag object and return the cleaned text.

    Parameters:
    soup (Tag): A BeautifulSoup Tag object containing HTML content.

    Returns:
    str: Cleaned text extracted from the HTML content, with HTML tags and unnecessary whitespace removed.
    """
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    # Extract the text
    text = soup.get_text(separator=" ")

    # Remove leading/trailing whitespace and unnecessary line breaks
    cleaned_text = " ".join(text.split())

    return cleaned_text


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
