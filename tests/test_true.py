import pytest

from coreutils import true


def test_true():
    with pytest.raises(SystemExit) as e_info:
        true.main()

    assert e_info.value.code == 0
