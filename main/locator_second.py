"""Searches for chords"""


from typing import List
from haversine import haversine
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="compicraft")


def locator_second(films: List[tuple], start_point: tuple[str]) -> List[tuple]:
    """Finds chords for films
    >>> locator_second([('"1001 Things You Should Know"', ['Glasgow', 'Scotland', 'UK'])],\
(49.83826, 24.02324))
    [('"1001 Things You Should Know"', ((55.8606182, -4.2497933), 1996.4736575513823), \
'Glasgow, Glasgow City, Alba / Scotland, G2 1DY, United Kingdom')]
    >>> locator_second([('"100 Bullets D\\'Argento"', ['Rome', 'Lazio', 'Italy'])], \
(49.83826, 24.02324))
    [('"100 Bullets D\\'Argento"', ((41.8933203, 12.4829321), 1253.859790905856), \
'Roma, Roma Capitale, Lazio, Italia')]"""
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
    import doctest
    print(doctest.testmod())
