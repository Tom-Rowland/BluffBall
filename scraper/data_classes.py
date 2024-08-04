from dataclasses import dataclass


@dataclass
class Match:
    home_team: str
    away_team: str
    competition: str
    home_score: int
    away_score: int
    report: str
