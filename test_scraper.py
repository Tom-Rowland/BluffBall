from bs4 import BeautifulSoup
import scraper


def test_scrape_results():
    """
    Test that the scraper runs without errors.
    The output is expected to be a paragraph but there are no specific assertions we can make about the contents.
    """
    results = scraper.scrape_results()
    assert type(results) == str


def test_get_yesterday():
    """
    Test that we can retrieve yesterday's date in the right format.
    Pytest does not let us mock datetime.datetime.now() so we cannot check the value, only the format (YYYY-mm-dd)
    """
    yesterday = scraper.get_yesterday()
    assert len(yesterday) == 10

    for i, char in enumerate(yesterday):
        if i in (4, 7):
            assert char == "-"
        else:
            assert char in "0123456789"


def test_strip_html_basic_html():
    """
    Test that a simple HTML is stripped as expected
    """
    html_content = "<html><body><p>Hello, <b>world!</b></p></body></html>"
    expected_output = "Hello, world!"
    soup = BeautifulSoup(html_content, "html.parser")
    cleaned_text = scraper.strip_html(soup)
    assert cleaned_text == expected_output


def test_strip_html_script_and_style():
    """
    Test html stip with script and style
    """
    html_content = """
    <html>
    <head>
    <style>
    body {
        font-size: 16px;
    }
    </style>
    </head>
    <body>
    <p>Hello, <b>world!</b></p>
    <script>
    alert("Hello world!");
    </script>
    </body>
    </html>
    """
    expected_output = "Hello, world!"
    soup = BeautifulSoup(html_content, "html.parser")
    cleaned_text = scraper.strip_html(soup)
    assert cleaned_text == expected_output
