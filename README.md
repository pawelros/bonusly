# bonusly
Bonusly HTTP Client with a bunch of features

## Installation
`PIPENV_VENV_IN_PROJECT=true pipenv install` - this will put python virtual env inside of the project directory which will make easier to setup a cronjob later on

## How to run
1. Go to https://bonus.ly/api and generate API token
2. Put it into .env file. This file is .gitignored so you will not commit your token accidentally
3. `Pipenv run python main.py --help` in order to display all available options
4. Example usage: `Pipenv run python main.py --to pawel@yourcompany.com --max 10 --round 5` (gives randomly 5 or 10 tokens).

## Crontab
If you want to bonus your friends at regular basis:
1. pwd your project directory to get an absolute path to it
2. crontab -e
3. `00 14 * * 1-5 cd /Users/pawel/x/bonusly && .venv/bin/python3 main.py --to "friend@example.com" --max 10 --round 5 &> /Users/pawel/x/bonusly/bonusly.log`
