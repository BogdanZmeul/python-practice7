import pytest
from app.io.input import read_from_file, read_from_file_pandas


def test_read_from_file_success(tmp_path):
    """Successful reading of a standard text file."""
    p = tmp_path / "test.txt"
    content = "Bohdan,18\nStepan,25\nLiza,30"
    p.write_text(content, encoding="utf-8")
    assert read_from_file(str(p)) == content


def test_read_from_file_empty(tmp_path):
    """Reading from an empty text file."""
    p = tmp_path / "empty.txt"
    p.write_text("", encoding="utf-8")
    assert read_from_file(str(p)) == ""


def test_read_from_file_not_found():
    """Handling a non-existent file path."""
    with pytest.raises(FileNotFoundError):
        read_from_file("missing_file.txt")

def test_read_from_file_pandas_content(tmp_path):
    """Verifying Pandas correctly reads specific user data."""
    p = tmp_path / "data.csv"
    csv_content = "Bohdan,18\nStepan,25\nLiza,30"
    p.write_text(csv_content, encoding="utf-8")

    result = read_from_file_pandas(str(p))

    assert "Bohdan" in result
    assert "18" in result
    assert "Stepan" in result
    assert "25" in result
    assert "Liza" in result
    assert "30" in result


def test_read_from_file_pandas_format(tmp_path):
    """Ensuring the function returns a string type as expected."""
    p = tmp_path / "simple.csv"
    p.write_text("name,age\nUser,99", encoding="utf-8")

    assert isinstance(read_from_file_pandas(str(p)), str)


def test_read_from_file_pandas_missing():
    """Verifying Pandas raises FileNotFoundError for missing files."""
    with pytest.raises(FileNotFoundError):
        read_from_file_pandas("no_such_file.csv")