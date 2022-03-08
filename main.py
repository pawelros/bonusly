import argparse
from dotenv import dotenv_values
import json
import random
import sys
import urllib3

from reasons import Reasons


def main(to, amount, reason, hashtag, api_token):

    body = {}

    body["receiver_email"] = to
    body["amount"] = amount
    body["hashtag"] = hashtag
    body["reason"] = reason

    j = json.dumps(body)

    print(j)

    # Creating a PoolManager instance for sending requests.
    http = urllib3.PoolManager()
    resp = http.request(
        "POST",
        "https://bonus.ly/api/v1/bonuses",
        body=j,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_token}"}
    )

    print(resp.data)


def random_hashtag():
    tags = [
        "#clients-not-customers",
        "#individual-effort-collective-success",
        "#pragmatic-pioneering",
        "#transparency-builds-trust-tbt",
    ]

    index = random.randrange(0, len(tags))

    return tags[index]


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Give bonusly points to your colleagues"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--amount",
        default=None,
        type=int,
        help="The number of points you want to give away",
    )
    group.add_argument(
        "--max",
        default="20",
        type=int,
        help="The number of maximum points you want to give away using random number generator.",
    )
    parser.add_argument(
        "--round",
        default=None,
        type=int,
        choices=[5, 10],
        help="If specified, randomly generated amount will be rounded to the given precision. i.e n=23; --round 5 will be rounded to 25, --round 10 to 20.",
    )
    parser.add_argument(
        "--to",
        default=None,
        required=True,
        help='[ a comma separated list of receiver emails i.e. "jp@example.com,monica@example.com"',
    )
    parser.add_argument(
        "--hashtag",
        default=None,
        choices=[
            "clients-not-customers",
            "individual-effort-collective-success",
            "pragmatic-pioneering",
            "transparency-builds-trust-tbt",
        ],
        help="Hashtag to use",
    )
    parser.add_argument(
        "--reason",
        default="random",
        help="Specific reason or random one",
    )

    args = parser.parse_args()

    random_step = args.round or 1
    amount = args.amount or random.randrange(random_step, args.max, random_step)
    hashtag = args.hashtag or random_hashtag()
    
    reason = args.reason
    if reason == "random":
        reason = Reasons.random()

    if hashtag[0] != "#":
        hashtag = "#" + hashtag

    if "@" not in args.to:
        print("--to must be an email")
        sys.exit(1)

    config = dotenv_values(".env")
    api_token = config["BONUSLY_API_TOKEN"]

    print("## THE THINGS I DO FOR TEAM:")
    main(args.to, amount, reason, hashtag, api_token)
