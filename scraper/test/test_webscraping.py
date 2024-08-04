from .. import webscraping
from bs4 import BeautifulSoup
import pytest


def test_scrape_match_reports():
    """
    Test that the scraper runs without errors.
    The output is expected to be a list of strings.
    """
    reports = webscraping.scrape_yesterday_match_reports()
    assert isinstance(reports, list)

    for report in reports:
        assert isinstance(report, str)


def test_get_yesterday():
    """
    Test that we can retrieve yesterday's date in the right format.
    Pytest does not let us mock datetime.datetime.now() so we cannot check the value, only the format (YYYY-mm-dd)
    """
    yesterday = webscraping.get_yesterday()
    assert len(yesterday) == 10

    for i, char in enumerate(yesterday):
        if i in (4, 7):
            assert char == "-"
        else:
            assert char in "0123456789"


@pytest.fixture
def main_data_div():
    with open("scraper/test/test_data/main-data div.txt", "r") as file:
        html: str = file.read()
    tag = BeautifulSoup(html, features="html.parser")
    return tag


def test_extract_match_urls(main_data_div):
    assert webscraping.extract_match_urls(main_data_div) == [
        "https://www.bbc.co.uk/sport/football/live/cp44lnvkp2pt",
        "https://www.bbc.co.uk/sport/football/live/c3gge1j73ldt",
        "https://www.bbc.co.uk/sport/football/live/c511d502dxvt",
        "https://www.bbc.co.uk/sport/football/live/cv22yndkddvt",
        "https://www.bbc.co.uk/sport/football/live/cn33mjvepg7t",
        "https://www.bbc.co.uk/sport/football/live/cpeekzd9xl0t",
        "https://www.bbc.co.uk/sport/football/live/c9994xv72y1t",
        "https://www.bbc.co.uk/sport/football/live/ce448z0182lt",
    ]


def test_pull_match_reports():
    urls = [
        "https://www.bbc.co.uk/sport/football/live/cnk4e0exnxdt",
        "https://www.bbc.co.uk/sport/football/live/cw0yv7vd0jlt",
        "https://www.bbc.co.uk/sport/football/live/cq5xn3n8xj8t",
        "https://www.bbc.co.uk/sport/football/live/ce78rgrn7xpt",
        "https://www.bbc.co.uk/sport/football/live/c3gv4gzzx64t",
        "https://www.bbc.co.uk/sport/football/live/c0ve3vzzw7yt",
        "https://www.bbc.co.uk/sport/football/live/cx72z733vg4t",
        "https://www.bbc.co.uk/sport/football/live/cd1r7166060t",
        "https://www.bbc.co.uk/sport/football/live/cw9yz9rr8jgt",
        "https://www.bbc.co.uk/sport/football/live/c98qr8nn7p4t",
        "https://www.bbc.co.uk/sport/football/live/cl4yk466l14t",
        "https://www.bbc.co.uk/sport/football/live/cx92z9xx851t",
        "https://www.bbc.co.uk/sport/football/live/cyj4zjrrd0zt",
        "https://www.bbc.co.uk/sport/football/live/c72702ddxzxt",
    ]

    reports = webscraping.pull_match_reports(urls)
    assert len(reports) == 6

    for report in reports:
        assert isinstance(report, str)
        assert len(report) > 100
