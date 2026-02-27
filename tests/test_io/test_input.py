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
