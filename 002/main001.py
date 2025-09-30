from rich.console import Console
from rich.prompt import Prompt
import rich


GRADING_SCALE = {(100, 90): "відмінно", (90, 50): "задовільно", (50, 0): "незадовільно" }
def main():
    console = Console()
    grade = int(Prompt.ask("Enter grade", console=console))

    result = ""
    for key, value in GRADING_SCALE.items():
        if key[1] < grade <= key[0]:
            result = value
    console.print("Ви набрали: {} балів, ваша оцінка: {}".format(grade, result))

if __name__ == "__main__":
    main()