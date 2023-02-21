"""Creates map with closest to point films"""


import argparse
import os
import sys
from reader_second import reader_second
from locator_second import locator_second
from mapper import mapper


parser = argparse.ArgumentParser()
parser.add_argument('year', type=str, help="year of films")
parser.add_argument('latitude', type=str, help="latitude of your point")
parser.add_argument('longtitude', type=str, help="longtitude of your point")
parser.add_argument("path_to_file", type = str, help="path to file with films")
args = parser.parse_args()


def check() -> None:
    """Checks for correct input"""
    if not os.path.isfile(args.path_to_file):
        sys.exit("File not found!")
    if not args.year.isnumeric():
        sys.exit("Wrong input!")


def main() -> None:
    """Main module"""
    check()
    try:
        chords = (float(args.latitude), float(args.longtitude))
    except ValueError:
        sys.exit("Wrong input!")
    print("Reading file with films...")
    films = reader_second(args.path_to_file, int(args.year))
    print(f"""Founded {len(films)} different films
Checking location of films...""")
    locs = locator_second(films, chords)
    print("Creating map...")
    mapper(locs, chords, int(args.year))
    print(f"Done! Map was saved to file '{os.getcwd()}\\film_map.html'")


if __name__ == "__main__":
    main()

