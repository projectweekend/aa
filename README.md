![build badge](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZTFKb3JzWkxmWS94QVJVV0RlQW5VaVg4WGNqdWlUcUw2TzhhSllNcHJhUFF4bFFqalhSS0tHRHZ6VXJTRVJVSmZCeDlNYlVwUVczRVFpK1FSdy9QY1owPSIsIml2UGFyYW1ldGVyU3BlYyI6ImhyOHpsNVJXNW9NOHNNQTEiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

THIS IS A WORK IN PROGRESS!

`aa` is a web server of utilities for use with the Axis & Allies board game.

The `Content-Type` for all requests and responses is `application/json`.

# API Routes
* [Get unit info](#get-unit-info)
* [Simulate a battle](#simulate-a-battle)

## Get unit info
* Path: `/unit-info`
* Method: `GET`
* Response Body:
```json
{
    "land": [
        {
            "name": "infantry",
            "attack": 1,
            "defense": 2,
            "cost": 3,
            "movement": 1,
            "bonus": "Attacks at 2 when supported by Artillery"
        },
        {
            "name": "artillery",
            "attack": 2,
            "defense": 2,
            "cost": 4,
            "movement": 2,
            "bonus": "Supports Infantry and Mechanized Infantry"
        },
        {
            "name": "mechanized_infantry",
            "attack": 1,
            "defense": 2,
            "cost": 4,
            "movement": 2,
            "bonus": "Attacks at 2 when supported by Artillery"
        },
        {
            "name": "tank",
            "attack": 3,
            "defense": 3,
            "cost": 6,
            "movement": 2,
            "bonus": "Supports Tactical Bomber"
        }
    ],
    "air": [
        {
            "name": "fighter",
            "attack": 3,
            "defense": 4,
            "cost": 10,
            "movement": 4,
            "bonus": "Supports Tactical Bomber"
        },
        {
            "name": "tactical_bomber",
            "attack": 3,
            "defense": 3,
            "cost": 11,
            "movement": 4,
            "bonus": "Attacks at 4 when supported by Fighter or Tank"
        },
        {
            "name": "strategic_bomber",
            "attack": 4,
            "defense": 1,
            "cost": 12,
            "movement": 6,
            "bonus": ""
        }
    ],
    "sea": [
        {
            "name": "transport",
            "attack": 0,
            "defense": 0,
            "cost": 7,
            "movement": 2,
            "bonus": ""
        },
        {
            "name": "submarine",
            "attack": 2,
            "defense": 1,
            "cost": 6,
            "movement": 2,
            "bonus": ""
        },
        {
            "name": "destroyer",
            "attack": 2,
            "defense": 2,
            "cost": 8,
            "movement": 2,
            "bonus": ""
        },
        {
            "name": "cruiser",
            "attack": 3,
            "defense": 3,
            "cost": 12,
            "movement": 2,
            "bonus": ""
        },
        {
            "name": "aircraft_carrier",
            "attack": 0,
            "defense": 2,
            "cost": 16,
            "movement": 2,
            "bonus": ""
        },
        {
            "name": "battleship",
            "attack": 4,
            "defense": 4,
            "cost": 20,
            "movement": 2,
            "bonus": ""
        }
    ]
}
```

## Simulate a battle
* Path: `/`
* Method: `POST`
* Request Body:
```json
{
  "attacker": {
    "infantry": 5,
    "tank": 5
  },
  "defender": {
    "infantry": 10
  }
}
```
* Response Body:
```json
{
    "attacker": 66.8,
    "defender": 31.2,
    "draw": 2
}
```
