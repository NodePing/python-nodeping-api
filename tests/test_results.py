#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tests to disable checks
"""

import pytest
from nodeping_api import get_checks, results

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
CUSTOMERID = parameters.CUSTOMERID


def test_get_results():
    """
    """

    query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)
    acc_checks = query.all_checks()
    check_id = next(iter(acc_checks))

    returned = results.get_results(
        TOKEN, check_id, limit=2, customerid=CUSTOMERID)

    assert "error" not in returned


def test_get_uptime():
    """
    """

    query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)
    acc_checks = query.all_checks()
    check_id = next(iter(acc_checks))

    returned = results.get_uptime(TOKEN, check_id, customerid=CUSTOMERID)

    assert "error" not in returned


def test_get_current():
    """
    """

    returned = results.get_current(TOKEN, customerid=CUSTOMERID)

    assert "error" not in returned
