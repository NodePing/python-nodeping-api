#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tests to disable checks
"""

import pytest
from nodeping_api import group_contacts

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
CUSTOMERID = parameters.CUSTOMERID
NAME = "PYTEST_group_name"
REPLACE_NAME = "PYTEST_replacement_name"


def test_get_all_groups():
    """
    """

    result = group_contacts.get_all(TOKEN, customerid=CUSTOMERID)

    assert "error" not in result.keys()


def test_create_group():
    """
    """

    result = group_contacts.create_group(TOKEN, NAME, customerid=CUSTOMERID)

    assert result['name'] == NAME


def test_update_group():
    """
    """

    contact_groups = group_contacts.get_all(TOKEN, customerid=CUSTOMERID)

    for i in contact_groups:
        if contact_groups[i]['name'] == NAME:
            result = group_contacts.update_group(
                TOKEN, i, name=REPLACE_NAME, customerid=CUSTOMERID)

            print(result)
            assert result['name'] == REPLACE_NAME


def test_delete_group():
    """
    """

    contact_groups = group_contacts.get_all(TOKEN, customerid=CUSTOMERID)

    for i in contact_groups:
        if contact_groups[i]['name'] == REPLACE_NAME:
            result = group_contacts.delete_group(
                TOKEN, i, customerid=CUSTOMERID)

            assert "error" not in result.keys()
