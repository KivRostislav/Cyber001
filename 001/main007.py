from rich.prompt import Prompt
import rich

from math import fabs


def main():
    a = int(Prompt.ask("Enter a number: "))
    b = int(Prompt.ask("Enter another number: "))

    max_num = (a + b + fabs(a - b)) / 2
    rich.print(max_num)

if __name__ == "__main__":
    main()