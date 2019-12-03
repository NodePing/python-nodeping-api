#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tests to disable checks
"""

import pytest
from nodeping_api import disable_check

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
CUSTOMERID = parameters.CUSTOMERID
TARGET = "example.com"


def test_disable_by_label():
    """ Testing disable checks by label
    """

    result = disable_check.disable_by_label(
        TOKEN, "PYTEST", disable=True, customerid=CUSTOMERID)

    assert "disabled" in result.keys() and "enabled" in result.keys()


def test_disable_by_target():
    """ Testing disable checks by target
    """

    result = disable_check.disable_by_target(
        TOKEN, "example.com", disable=False, customerid=CUSTOMERID)

    assert "disabled" in result.keys() and "enabled" in result.keys()


def test_disable_by_type():
    """ Testing disable checks by type
    """

    result = disable_check.disable_by_type(
        TOKEN, "PUSH", disable=False, customerid=CUSTOMERID)

    assert "disabled" in result.keys() and "enabled" in result.keys()


def test_disable_all():
    """ Testing disable all checks
    """

    result = disable_check.disable_all(
        TOKEN, disable=True, customerid=CUSTOMERID)

    assert "disabled" in result.keys() and "enabled" in result.keys()
