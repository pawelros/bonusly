import argparse
import sys

def main():
    pass

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Give bonusly points to your colleagues'
    )
    parser.add_argument(
        '--amount',
        default='1',
        help='The number of points you want to give away',
    )
    parser.add_argument(
        '--amount-random-min',
        default='1',
        help='The number of minimum points you want to give away using random number generator. Must be used with --amount-random-max',
    )
    parser.add_argument(
        '--amount-random-max',
        default='1',
        help='The number of maximum points you want to give away using random number generator.  Must be used with --amount-random-min',
    )
    parser.add_argument(
        '--round',
        default=None,
        help='Allowed values [5|10]. If specified, randomly generated amount will be rounded. --amount-random-min must be >= --round value.',
    )
    parser.add_argument(
        '--to',
        default=None,
        help='[ a comma separated list of receiver emails i.e. "jp@example.com,monica@example.com"',
    )
    parser.add_argument(
        '--hashtag',
        default='random',
        help='Hashtag [ random | #clients-not-customers | #individual-effort-collective-success | #pragmatic-pioneering | #transparency-builds-trust-tbt ] ',
    )
    parser.add_argument(
        '--reason',
        default='random',
        help='Specific reason or random one',
    )

    args = parser.parse_args()

    print("## YOLO!")
    main()

