from unittest.mock import call, patch

from click.testing import CliRunner

from coreutils import yes


@patch("builtins.print")
def test_yes(print_mock):
    print_mock.side_effect = StopIteration()

    runner = CliRunner()

    try:
        runner.invoke(yes.main)
    except StopIteration:
        pass

    assert print_mock.mock_calls == [call("y")]
