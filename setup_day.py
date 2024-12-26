import os
import sys
import requests
import pathlib
from datetime import date

days = []
if len(sys.argv) == 1:
    days.append(date.today().day)
else:
    for num in sys.argv[1:]:
        days.append(num)

basePath = pathlib.Path(__file__).parent.resolve()
year = 2024
os.chdir(f"{basePath}\\{year}")

for day in days:
    boilerplate = f"""import os

os.chdir(f"{basePath}\\\\{year}\\\\Day {day}")

txt = open("input.txt", "r")
txt = txt.read()"""

    os.mkdir(f"Day {day}")

    one = open(f"Day {day}\\part1.py", "w")
    one.write(boilerplate)

    two = open(f"Day {day}\\part2.py", "w")
    two.write(boilerplate)

    input_file = open(f"Day {day}\\input.txt", "w")
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookie = open("..\\session.cookie").read().strip()
    response = requests.get(url, {}, cookies={"session": cookie})
    if not response.ok:
        raise RuntimeError(
            f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
        )
    input_file.write(response.text[:-1])