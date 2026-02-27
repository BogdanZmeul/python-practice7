import pandas as pd

def get_input_from_console() -> str:
    """
    Prompts the user to enter text via the console.
    Returns: str: The text entered by the user.
    """
    return input("Enter text: ")

def read_from_file(file_path: str) -> str:
    """
    Reads the content of a text file using Python's open() function.
    Input: file_path (str): The path to the source file.
    Returns: str: The content of the file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def read_from_file_pandas(file_path: str) -> str:
    """
    Reads a CSV file using the pandas library and returns it as a string.
    Input: file_path (str): The path to the CSV file.
    Returns: str: The string representation of the DataFrame.
    """
    df = pd.read_csv(file_path)
    return df.to_string()