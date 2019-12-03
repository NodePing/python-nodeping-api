#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tests to manage schedules
"""

import pytest
from nodeping_api import get_checks, update_checks

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
CUSTOMERID = parameters.CUSTOMERID


def test_update_check():
    """
    """

    check_types = parameters.CHECK_TYPES

    query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)
    my_checks = query.all_checks()

    for check in check_types:
        label = "PYTEST_{0}_check".format(check)
        fields = {"public": False, "interval": 15}

        for _, value in my_checks.items():
            if value['label'] == label:
                check_id = value['_id']
                result = update_checks.update(
                    TOKEN, check_id, check, fields, customerid=CUSTOMERID)

                assert "error" not in result
                break


def test_update_many_checks():
    """
    """

    checks_to_update = {}

    check_types = parameters.CHECK_TYPES

    query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)
    my_checks = query.all_checks()

    for check in check_types:
        label = "PYTEST_{0}_check".format(check)
        fields = {"public": False, "interval": 15}

        for _, value in my_checks.items():
            if value['label'] == label:
                checks_to_update.update({value['_id']: value['type']})
                # result = update_checks.update(
                #     TOKEN, check_id, check, fields, customerid=CUSTOMERID)

                # assert "error" not in result

    result = update_checks.update_many(
        TOKEN, checks_to_update, fields, customerid=CUSTOMERID)

    assert "error" not in result
