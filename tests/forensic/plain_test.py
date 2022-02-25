#!/usr/bin/python3
from autoctf.forensic.plain import auto_check_flag_in_file_with_grep,auto_check_flag_in_file_with_strings


def test_grep():
    assert auto_check_flag_in_file_with_grep("8b04fe3a04c641931247c4a912a39213.png"), b"flag{get_grepped}"

def test_strings():
    assert auto_check_flag_in_file_with_strings("8b04fe3a04c641931247c4a912a39213.png"), b"flag{get_grepped}"




if __name__ == "__main__":
    test_grep()
    print("Everything passed")
