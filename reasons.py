import random
class Reasons:
    @staticmethod
    def random():
        reasons = [
            'Great presentation about CI/CD today!',
            'For being always ready to investigate infrastructure mysteries',
            'Your careful code reviews are always very useful for the team!',
            'For all your work on stack manager.',
            'Nice work on the pulumi code changes! Looking forward to seeing this leveraged in our environment.',
            'thx for all your support!!',
            'nothing could have been possible without you!',
            'everyday is a new day with all your amazing work!',
            'thx again for all the time you pass on helping us!!',
            'Good presentation today!',
            'Friday\'s round table was absolutely great!',
            'For the great brainstorming session',
            'For harsh words that somethimes had to be told.',
            'for the thoughtful discussions within the team',
            'Smashing!',
            'thx for being an incredible team member !!!',
            'For daily handling of Cyclope with great sense of good humour',
            'for being a pulumi guru!',
            'Awesome work on bender',
            'best engineer I know',
            'Rapid turnaround on a high impact issue',
            'for being one man army and fixing all the things!',
            'for helping me in solving cache problem in github workflow.',
            'Thank you for helping with the release',
            'Thank you for helping to identify this nasty bug!'
        ]

        return random.choice(reasons)
