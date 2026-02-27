def write_to_console(text: str) -> None:
    """
    Prints the provided text to the console.
    Input: text (str): The text to be displayed.
    """
    print(text)

def write_to_file(text: str, file_path: str) -> None:
    """
    Writes text to a file using Python's built-in open() function.
    Input: text (str): Text to save, file_path (str): Destination path.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)