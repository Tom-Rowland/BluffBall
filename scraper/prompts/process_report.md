# Task

You will be provided with a BBC Sport report for a football match. You must determine the following from the match:
1. Home side
1. Away side
1. Home score
1. Away score
1. Competition
1. Discussion

The discussion is a short conversation two people might have about the game the next day in the same vein as the IT Crowd classic: "Did you see that ludicrous display last night?" "Yeah- what's Wenger thinking bringing Walcott on that early?" "You see, the thing about Arsenal is they always try and walk it in!" It should be  particularly "geezer"-like with an amount of moaning where applicable. Don't comment on what anyone has said in an interview if you are provided with one and certainly don't quote anyone's comments from an interview. If the match goes to penalties, the home/away scores you provide should be the score *before* the shootout.

# Output Format
You must output a JSON object structured like this one:
```json
{
    "home_side": "Arsenal",
    "away_side": "Luton Town",
    "home_score": 1,
    "away_score": 0,
    "competition": "English Premier League",
    "discussion": [
        {
            "person": 1,
            "content": "Did you see that ludicrous display last night?"
        },
        {
            "person": 2,
            "content": "Yeah- what's Wenger thinking bringing Walcott on that early?"
        },
        {
            "person": 1,
            "content": "You see, the thing about Arsenal is they always try and walk it in!"
        }
    ]
}
```