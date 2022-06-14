import time
from unittest.mock import call, patch

from click.testing import CliRunner

from coreutils import sleep


def test_main_negative_interval():
    runner = CliRunner()
    
    result = runner.invoke(sleep.main, ["-1"])

    assert result.exit_code != 0
    assert 'invalid time interval "-1"' in result.output


def test_main_not_a_number_interval():
    runner = CliRunner()

    result = runner.invoke(sleep.main, ["one"])

    assert result.exit_code != 0
    assert 'invalid time interval "one"' in result.output


def test_main_not_exists_interval_suffix():
    runner = CliRunner()

    result = runner.invoke(sleep.main, ["1y"])

    assert result.exit_code != 0
    assert 'invalid time interval "1y"' in result.output


@patch("time.sleep")
def test_main_many_intervals_and_suffixes(sleep_mock):
    runner = CliRunner()

    runner.invoke(sleep.main, ["1s", "2m", "3h", "4d"])

    assert sleep_mock.mock_calls == [call(356521.0)]
