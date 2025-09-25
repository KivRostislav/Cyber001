import rich
from rich.console import Console
from rich.prompt import Prompt


def main():
    console = Console()
    num = float(Prompt.ask("Enter a number", console=console))

    fractional_part = num - (num // 1)
    rich.print("Fractional part = {0:.2f}".format(fractional_part))

if __name__ == '__main__':
    main()