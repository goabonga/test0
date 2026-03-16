# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Chris <goabonga@pm.me>

from shomer import __version__

__expected_version__: str = "0.1.0"


def test_version() -> None:
    assert __version__ == __expected_version__
