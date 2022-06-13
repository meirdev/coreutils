import time
from unittest.mock import call, patch

from click.testing import CliRunner

from coreutils import sleep


def test_main_negative_interval():
    runner = CliRunner()
    
    assert runner.invoke(sleep.main, ["-1"]).exit_code != 0


def test_main_not_a_number_interval():
    runner = CliRunner()

    assert runner.invoke(sleep.main, ["one"]).exit_code != 0


def test_main_not_exists_interval_suffix():
    runner = CliRunner()

    assert runner.invoke(sleep.main, ["1y"]).exit_code != 0


@patch("time.sleep")
def test_main_many_intervals_and_suffixes(sleep_mock):
    runner = CliRunner()

    runner.invoke(sleep.main, ["1s", "2m", "3h", "4d"])

    assert sleep_mock.mock_calls == [call(356521.0)]
