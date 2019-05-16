# Content of test_azlyrics.py

import pytest
import lyrics.azlyrics as az


class TestClass(object):
    @pytest.mark.parametrize(
        ("inp", "exp"),
        [
            (("Metallica", "One"), ("metallica", "one")),
            (("The Killers", "The Man"), ("killers", "theman")),
        ],
    )
    def test_clean_names(self, inp, exp):
        assert az.clean_names(inp[0], inp[1]) == exp

    @pytest.mark.parametrize(
        ("inp", "exp"),
        [
            (
                ("metallica", "one"),
                ("https://www.azlyrics.com/lyrics/metallica/one.html")
            ),
            (
                ("killers", "theman"),
                ("https://www.azlyrics.com/lyrics/killers/theman.html")
            ),
        ],
    )
    def test_create_url(self, inp, exp):
        assert az.create_url(inp[0], inp[1]) == exp
