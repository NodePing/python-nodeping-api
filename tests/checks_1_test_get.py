#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tests to disable checks
"""

import pytest
from nodeping_api import get_checks

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
CUSTOMERID = parameters.CUSTOMERID


def test_get_all_checks():
    """
    """

    query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)
    result = query.all_checks()

    assert "error" not in result.keys()


def test_get_passing_checks():
    """
    """

    query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)
    result = query.passing_checks()

    for i in result:
        assert result[i]['state'] == 1


def test_get_failing_checks():
    """
    """

    query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)
    result = query.failing_checks()

    for i in result:
        assert result[i]['state'] == 0


def test_get_by_id():
    """
    """

    # Need to get a check ID to test getting a single check
    query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)
    all_account_checks = query.all_checks()
    single = next(iter(all_account_checks))

    query = get_checks.GetChecks(TOKEN, checkid=single, customerid=CUSTOMERID)
    result = query.get_by_id()

    assert result['_id'] == single


def test_get_disabled_checks():
    """
    """

    query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)
    result = query.disabled_checks()

    for i in result:
        assert result[i]['type'] == 'disabled'
