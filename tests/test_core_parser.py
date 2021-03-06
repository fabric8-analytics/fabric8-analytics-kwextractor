"""Tests for the CoreParser class."""

import pytest
from f8a_tagger.parsers.core_parser import CoreParser


def test_initial_state():
    """Check the initial state of CoreParser."""
    c = CoreParser()
    assert c is not None


def test_parse_method():
    """Check the method parse()."""
    c = CoreParser()
    parsed = c.parse("hello world", "txt")
    assert parsed == "hello world"

    parsed = c.parse("<html><body>hello world</body></html>", "html")
    assert parsed == "hello world"

    parsed = c.parse("<div>two</div> <div>divs</div>", "html")
    assert parsed == "two divs"

    # wrong content-type checking
    with pytest.raises(ValueError):
        c.parse("content", "unknown-content-type")

    # wrong content checking
    with pytest.raises(ValueError):
        c.parse("", "txt")


def test_parse_file_method_positive():
    """Check the method parse_file()."""
    c = CoreParser()

    parsed = c.parse_file("test_data/README.txt")
    assert parsed is not None

    parsed = c.parse_file("test_data/README.md")
    assert parsed is not None


def test_parse_file_method_negative():
    """Check the method parse_file()."""
    c = CoreParser()

    # Asciidoc parser is not implemented yet
    with pytest.raises(NotImplementedError):
        parsed = c.parse_file("test_data/README.asciidoc")
        print(parsed)

    with pytest.raises(ValueError):
        parsed = c.parse_file("test_data/keywords.yaml")
        print(parsed)


def test_parse_file_method_json_fallback():
    """Check the method parse_file()."""
    c = CoreParser()

    parsed = c.parse_file("test_data/README_markdown.json")
    assert parsed is not None

    parsed = c.parse_file("test_data/README_rst.json")
    assert parsed is not None


def test_parse_readme_json_method_positive():
    """Check the method parse_readme_json()."""
    c = CoreParser()

    parsed = c.parse_readme_json("test_data/README_markdown.json")
    assert parsed is not None

    parsed = c.parse_readme_json("test_data/README_rst.json")
    assert parsed is not None


def test_parse_readme_json_method_negative():
    """Check the method parse_readme_json() for wrong input."""
    c = CoreParser()

    with pytest.raises(TypeError):
        parsed = c.parse_readme_json(None)
        print(parsed)

    with pytest.raises(ValueError):
        parsed = c.parse_readme_json("test_data/README_empty.json")
        print(parsed)

    with pytest.raises(ValueError):
        parsed = c.parse_readme_json("test_data/README_null.json")
        print(parsed)

    with pytest.raises(ValueError):
        parsed = c.parse_readme_json("test_data/README_broken_no_content.json")
        print(parsed)

    with pytest.raises(ValueError):
        parsed = c.parse_readme_json("test_data/README_broken_no_type.json")
        print(parsed)


if __name__ == '__main__':
    test_initial_state()
    test_parse_method()
    test_parse_file_method_positive()
    test_parse_file_method_negative()
    test_parse_file_method_json_fallback()
    test_parse_readme_json_method_positive()
    test_parse_readme_json_method_negative()
