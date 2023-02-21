"""Searches for chords"""


import os
from typing import List
from haversine import haversine
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import reader_second


geolocator = Nominatim(user_agent="compicraft")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.00001)


def locator_second(films: List[tuple], start_point: tuple[str]) -> List[tuple]:
    """Finds chords for films"""
    films_lst = []
    checked_locs = []
    cont = 1
    point = 150 if len(films) > 150 else len(films)
    for film in films:
        for loc in film[1]:
            if loc in checked_locs:
                location = None
                break
            location = geolocator.geocode(loc, timeout=10)
            checked_locs.append(loc)
            if location is not None:
                break
        if location is None:
            continue
        chords = (location.latitude, location.longitude)
        dist = haversine(start_point, chords)
        films_lst.append((film[0], (chords, dist), location.address))
        if cont == point:
            break
        cont += 1
    films_lst.sort(key = lambda x: x[1][1])
    return films_lst


if __name__ == "__main__":
    os.chdir("D:/PythonProjects/course 1/semester 2/Lab1/task2/project_lab_1_task_2")
    all_films = reader_second.reader_second("locations.list", "2000")
    locs = locator_second(all_films, (39, -114))
    print(locs)
    print(len(locs))
