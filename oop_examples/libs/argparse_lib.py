import argparse
import os
import sys
# docs: https://docs.python.org/3/library/argparse.html?highlight=argparse

# print(sys.argv)
def demo_argparse():

    parser = argparse.ArgumentParser(
        prog='My argparse demo',
        description='Show argparse (parser actions)',
        epilog='End help'
    )
    parser.version = '0.1.0'

    parser.add_argument(
        'path',  # обязательный аргумент
        metavar='path',
        type=str,
        help='the path to be listed'
    )

    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',  # флаг сохранения true
        help='verbose show more info'
    )

    parser.add_argument(
        '-V',
        '--version',
        action='version'
    )

    parser.add_argument(
        '--no-run',
        action='store_true'  # если передан, то true
    )

    parser.add_argument(
        '-n',
        '--name',
        action='store'
    )

    parser.add_argument(
        '-k',
        action='store_const',
        const=42
    )

    parser.add_argument(
        '-i',
        '--info',
        action='help',
        help='alternative call help'
    )

    parser.add_argument(
        '-c',  # -cccc
        '--count',
        action='count',
        help='simple count'
    )

    parser.add_argument(
        '-a',
        '--append-val',
        action='append',  # -a 'some' -a 'thing' and etc.
        help='append values'
    )

    args = parser.parse_args()
    return args


args = demo_argparse()
print(args)
if args.verbose:
    print('Gonna list this dir:', args.path)
if not os.path.isdir(args.path):
    if args.verbose:
        print('No such directory!')
    sys.exit(1)
print('List of', args.path, ':', os.listdir(args.path))
if args.no_run:
    print('no run selected! leaving')
    sys.exit()
