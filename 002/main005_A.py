from rich.console import Console
from rich.prompt import Prompt

from math import pi, fabs


def main():
    console = Console()
    amount_of_elements = int(Prompt.ask("Enter number of elements", console=console))

    result = 1.0
    denominator = 3
    for i in range(amount_of_elements - 1):
        result = result + (1 / denominator if i % 2 == 1 else -1 / denominator)
        denominator += 2

    console.print("Real value = {}, calculated value = {}, relative error = {}%, absolute error = {}"
                  .format(pi, 4 * result, fabs((pi - (4 * result)) / pi) * 100, fabs(pi - (4 * result))))

if __name__ == "__main__":
    main()