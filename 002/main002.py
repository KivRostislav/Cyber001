from rich.console import Console
from rich.prompt import Prompt
import rich


FACE_ELEMENTS = [
    "   /////  ",
    ' +""""""+ ',
    "(| 0  0 |)",
    " |   ^  | ",
    " |  '-' | ",
    " +------+ "
]
def main():
    console = Console()
    repeat = int(Prompt.ask("Enter repeat", console=console))

    for element in FACE_ELEMENTS:
        for _ in range(repeat):
            console.print(element, end=" ")
        console.print("\n")

if __name__ == "__main__":
    main()