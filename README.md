# bonusly
Bonusly HTTP Client with a bunch of features

## How to run
1. Go to https://bonus.ly/api and generate API token
2. Put it into .env file. This file is .gitignored so you will not commit your token accidentally
3. `Pipenv run python main.py --help` in order to display all available options
4. Example usage: `Pipenv run python main.py --to pawel@yourcompany.com --max 10 --round 5` (gives randomly 5 or 10 tokens).
