import rich
from PyInquirer import prompt

def showTitle():
    title = """
 █████╗ ██╗    ███████╗███████╗████████╗██╗   ██╗██████╗
██╔══██╗██║    ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
███████║██║    ███████╗█████╗     ██║   ██║   ██║██████╔╝
██╔══██║██║    ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝
██║  ██║██║    ███████║███████╗   ██║   ╚██████╔╝██║
╚═╝  ╚═╝╚═╝    ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝
    """

    rich.print(f'[green]{title}[/green]')

def showOptions(options: list[str], message: str = "Please choose an option:") -> int:
    questions = [
        {
            'type': 'list',
            'name': 'option',
            'message': message,
            'choices': options
        }
    ]

    answers = prompt(questions)
    selected_option = answers['option']

    return options.index(selected_option)


if __name__ == "__main__":
    showTitle()
    options = ["Start New Project", "Load Existing Project", "Exit"]
    choice = showOptions(options)
    rich.print(f"You selected option {choice + 1}: {options[choice]}")