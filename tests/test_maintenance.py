#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from nodeping_api import maintenance, create_check, delete_checks

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
CUSTOMERID = parameters.CUSTOMERID
NAME = "PYTEST_CREATED_MAINTENANCE"
CHECK_NAME = "PYTEST_maintenance_check"


def test_create_ad_hoc():
    """
    """

    duration = 1
    checklist = []
    name = "PYTEST_AD_HOC"

    # Check needs to be created to add check to maintenance
    test_check = create_check.dns_check(
        TOKEN, "www.google.com", enabled=False, label=CHECK_NAME, customerid=CUSTOMERID)

    if "error" in test_check.keys():
        errors = True
        assert errors, "Could not create check for test"

    checklist.append(test_check['_id'])

    result = maintenance.create_maintenance(
        TOKEN, duration, checklist, name=name, _id="ad-hoc", customerid=CUSTOMERID)

    assert "error" not in result.keys()


def test_create_maintenance():
    """
    """

    duration = 5
    cron = "1 12 * * *"
    checklist = []

    # maintenance = maintenance.get_maintenance(TOKEN, customerid=CUSTOMERID)
    result = maintenance.create_maintenance(
        TOKEN, duration, checklist, name=NAME, enabled=False, cron=cron)

    assert "error" not in result.keys()


def test_get_all():
    """
    """

    result = maintenance.get_maintenance(TOKEN, customerid=CUSTOMERID)

    assert "error" not in result.keys()


def test_update_maintenance():
    """
    """

    maintenances = maintenance.get_maintenance(TOKEN, customerid=CUSTOMERID)
    duration = 20

    for key in maintenances['schedules'].keys():
        name = maintenances['schedules'][key]['name']

        if name == NAME:
            checklist = maintenances['schedules'][key]['checklist']
            result = maintenance.update_maintenance(
                TOKEN, key, duration, checklist)

            assert result[key]['duration'] == duration


def test_delete_maintenance():
    """
    """

    maintenances = maintenance.get_maintenance(TOKEN, customerid=CUSTOMERID)

    for key in maintenances['schedules'].keys():
        name = maintenances['schedules'][key]['name']

        if name == NAME:
            result = maintenance.delete_maintenance(
                TOKEN, key, customerid=CUSTOMERID)

            assert "error" not in result
