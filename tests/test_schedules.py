#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tests to manage schedules
"""

import pytest
from nodeping_api import schedules

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
CUSTOMERID = parameters.CUSTOMERID
SCHEDULE_NAME = "PYTEST_test_schedule"


def test_create_schedule():
    """
    """

    data = {'data': {'friday': {'disabled': True},
                     'monday': {'allday': True},
                     'saturday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
                     'sunday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
                     'thursday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
                     'tuesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
                     'wednesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'}}}

    result = schedules.create_schedule(
        TOKEN, data, SCHEDULE_NAME, customerid=CUSTOMERID)

    assert "error" not in result


def test_get_schedules():
    """
    """

    result = schedules.get_schedule(
        TOKEN, schedule=SCHEDULE_NAME, customerid=CUSTOMERID)

    assert "error" not in result


def test_update_schedules():
    """
    """

    data = {'data': {
        'tuesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
        'wednesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'}}}

    result = schedules.update_schedule(
        TOKEN, data, SCHEDULE_NAME, customerid=CUSTOMERID)

    assert "error" not in result


def test_delete_schedule():
    """
    """

    result = schedules.delete_schedule(
        TOKEN, SCHEDULE_NAME, customerid=CUSTOMERID)

    assert "error" not in result
