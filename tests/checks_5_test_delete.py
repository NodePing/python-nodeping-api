#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test deleting NodePing checks

This test also acts as a clean up from test_create_checks
"""

import pytest
from nodeping_api import delete_checks, get_checks

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
CUSTOMERID = parameters.CUSTOMERID
EMAIL = "me@example.com"
TARGET = "example.com"


def test_delete_checks():
    """ Delete all checks made in the create check test
    """

    check_types = parameters.CHECK_TYPES

    query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)
    my_checks = query.all_checks()

    for check in check_types:
        label = "PYTEST_{0}_check".format(check)

        for key, value in my_checks.items():
            if value['label'] == label:
                result = delete_checks.remove(
                    TOKEN, key, customerid=CUSTOMERID)

                assert "error" not in result.keys()
