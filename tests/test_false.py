import pytest

from coreutils import false


def test_true():
    with pytest.raises(SystemExit) as e_info:
        false.main()

    assert e_info.value.code == 1
