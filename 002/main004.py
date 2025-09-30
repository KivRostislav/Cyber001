from random import random
from math import sqrt, pi

from rich.console import Console
from rich.prompt import Prompt

def main():
    console = Console()
    amount_of_points = int(Prompt.ask("Enter the amount of points", console=console))
    center_of_circle = (1, 1)

    amount_of_points_in_circle = 0

    for _ in range(amount_of_points):
        point_coordinate = (random() * 2, random() * 2)
        vector_len = sqrt(((center_of_circle[0] - point_coordinate[0])**2 + (center_of_circle[1] - point_coordinate[1])**2))
        in_circle = True if vector_len <= 1 else False
        if in_circle: amount_of_points_in_circle += 1

    console.print("Real value = {}, calculated value = {}".format(pi, 4 * (amount_of_points_in_circle / amount_of_points)))

if __name__ == "__main__":
    main()