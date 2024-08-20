from scraper import llm_processing
from test.test_data import match_reports_list


def test_openai_completion():
    prompt = (
        "Your job is to write a 3 sentence story about the topic provided by the user."
    )
    input = "Theo Walcott"

    output = llm_processing.openai_completion(prompt, input)
    assert type(output) == str
    assert len(output) > 0


def test_generate_bluffball_matches():
    reports = match_reports_list.reports
    assert len(reports) == 4

    matches = llm_processing.generate_bluffball_matches(reports)
    assert len(matches) == 4

    match = matches[0]
    assert match.home_side == "Ajax"
    assert match.away_side == "Panathinaikos"
    assert match.home_score == 0
    assert match.away_score == 1
    assert "Europa League" in match.competition

    match = matches[1]
    assert match.home_side == "Brann"
    assert match.away_side in ("St. Mirren", "St Mirren")
    assert match.home_score == 3
    assert match.away_score == 1
    assert "Conference League" in match.competition

    match = matches[2]
    assert match.home_side in ("Tromsø", "Tromso")
    assert match.away_side == "Kilmarnock"
    assert match.home_score == 0
    assert match.away_score == 1
    assert "Conference League" in match.competition

    match = matches[3]
    assert match.home_side == "Larne"
    assert match.away_side == "Ballkani"
    assert match.home_score == 0
    assert match.away_score == 1
    assert "Conference League" in match.competition
