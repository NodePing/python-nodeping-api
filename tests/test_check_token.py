#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from nodeping_api import check_token

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN


def test_token_info():
    """ Tests getting info and if the result isn't an error
    """

    result = check_token.info(TOKEN)

    assert "error" not in result.keys()


def test_token_valid():
    """ Tests the token validity to see if True is returned
    """

    result = check_token.is_valid(TOKEN)

    assert result is True


def test_token_info_fails():
    """ Supplies a bad token to get an error
    """

    result = check_token.info("not-a-real-token")

    assert "error" in result.keys()


def test_token_invalid():
    """ Supplies a bad token and expects False in return
    """

    result = check_token.is_valid("not-a-real-token")

    assert result is False
