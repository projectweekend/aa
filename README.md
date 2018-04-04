THIS IS A WORK IN PROGRESS!

`aa` is a webserver that runs Axis & Allies battle simulations (1000x) and returns the following stats:

* Attacker win percentage
* Defender win percentage
* Draw percentage

# Simulate a battle
The `Content-Type` for all requests and responses is `application/json`.
* Route: `/`
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


# Run webserver locally
```
$ pipenv run gunicorn --config=gconfig.py --reload app
```

# Run webserver in Docker locally
```
$ docker run -p 8000:8000 projectweekend/aa
```

# Run Tests
```
$ pytest --cov=. --cov-report=html
```
