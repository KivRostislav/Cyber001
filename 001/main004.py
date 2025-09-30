import rich
from rich.console import Console
from rich.prompt import Prompt
from math import sqrt

def main():
    a = float(Prompt.ask("Enter a"))
    b = float(Prompt.ask("Enter b"))
    c = float(Prompt.ask("Enter c"))

    D = b**2 - 4*a*c
    if D < 0:
        rich.print("There are no roots")
        return;
    x1 = (-b + sqrt(D)) / (2*a)
    x2 = (-b - sqrt(D)) / (2*a)
    rich.print("x1 = {0:.2f} x2 = {1:.2f}".format(x1, x2))

if __name__ == "__main__":
    main()