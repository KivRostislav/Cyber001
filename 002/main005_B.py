from rich.console import Console
from rich.prompt import Prompt

from math import pi, fabs


def main():
    console = Console()
    absolute_error = float(Prompt.ask("Enter absolute error", console=console))

    i = 1
    result = 1.0
    denominator = 3
    while True:
        result = result + (1 / denominator if i % 2 == 0 else -1 / denominator)
        denominator += 2
        i += 1

        if fabs((4 * result) - pi) <= absolute_error:
            break
    console.print("Real value = {}, calculated value = {}, relative error = {}%, absolute error = {}, amount of elements = {}"
                  .format(pi, 4 * result, fabs((pi - (4 * result)) / pi) * 100, fabs(pi - (4 * result)), i))


if __name__ == "__main__":
    main()