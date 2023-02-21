"""Second version of list file reader"""


import os
from typing import List
from random import shuffle


def reader_second(path_to_file: str, wanted_year: int) -> List[tuple]:
    """Reads file with film info and returns 
    List with film name, year and location"""
    lst = []
    used_films = []
    with open(path_to_file, "r", encoding="utf-8") as file:
        for line in file:
            if "\t" in line:
                amount = line.count("\t")
                splitet = line.split("\t"*amount)
                if len(splitet) == 1:
                    splitet = line.split("\t"*(amount-1))
                if len(splitet) != 2:
                    splitet.pop(-1)
                if "\t" in splitet[1]:
                    splitet[1] = splitet[1][:splitet[1].index("\t")]
                info = separator(splitet)
                if info is not False:
                    if info[2] == str(wanted_year) and info[0] not in used_films:
                        used_films.append(info[0])
                        lst.append(info[:2])
    shuffle(lst)
    return lst


def separator(pure_info: List[str]) -> List[tuple]:
    """Seperates data correctly"""
    name_year = pure_info[0]
    locs = pure_info[1]
    if "{" in name_year:
        name_year = name_year[:name_year.index("{")]
    if "(" not in name_year:
        return False
    index = name_year.index("(")
    name = name_year[:index-1]
    year = name_year[index+1:index+5]
    if not year.isnumeric():
        return False
    loc_lst = locs.split(", ")
    loc_lst[-1] = loc_lst[-1].rstrip()
    i = 0
    while i < len(loc_lst):
        if "-" in loc_lst[i]:
            loc_lst[i] = loc_lst[i].split(" - ")[-1]
            break
        i += 1
    return (name, loc_lst, year)


if __name__ == "__main__":
    os.chdir("D:/PythonProjects/course 1/semester 2/Lab1/task2/")
    films = reader_second("locations.list", 2001)
    print(len(films))
