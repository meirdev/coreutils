from click.testing import CliRunner

from coreutils import echo


def test_main():
    runner = CliRunner()

    result = runner.invoke(echo.main, ["hello\\nworld"])

    assert result.output == "hello\nworld\n"


def test_main_hex_chars():
    runner = CliRunner()

    result = runner.invoke(echo.main, [r"\x48\x45\x4c\x4c\x4f"])

    assert result.output == "HELLO\n"


def test_main_oct_chars():
    runner = CliRunner()

    result = runner.invoke(echo.main, ["\\0110\\0105\\0114\\0114\\0117"])

    assert result.output == "HELLO\n"


def test_main_special_chars():
    runner = CliRunner()

    result = runner.invoke(echo.main, ["\\a\\b\\f\\n\\r\\v\\\\"])

    assert result.output == "\a\b\f\n\r\v\\\n"


def test_main_without_new_line():
    runner = CliRunner()

    result = runner.invoke(echo.main, ["-n", "hello\\nworld"])

    assert result.output == "hello\nworld"


def test_main_disable_escape():
    runner = CliRunner()

    result = runner.invoke(echo.main, ["-E", "hello\\nworld"])

    assert result.output == "hello\\nworld\n"
