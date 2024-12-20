import os
import sys
from datetime import date

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024")

days = []
if len(sys.argv) == 1:
    days.append(date.today().day)

else:
    for num in sys.argv[1:]:
        days.append(num)


for day in days:
    boilerplate = f"""import os

os.chdir("C:\\\\Users\\\\seanc\\\\source\\\\repos\\\\Advent-of-Code\\\\2024\\\\Day {day}")

txt = open("input.txt", "r")
txt = txt.read()"""

    os.mkdir(f"Day {day}")

    one = open(f"Day {day}\\part1.py", "w")
    one.write(boilerplate)

    two = open(f"Day {day}\\part2.py", "w")
    two.write(boilerplate)
    open(f"Day {day}\\input.txt", "x")