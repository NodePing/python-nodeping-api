#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tests to disable checks
"""

import http.client
import pytest
from nodeping_api import notifications

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
CUSTOMERID = parameters.CUSTOMERID


def test_get_notifications():
    """
    """

    result = notifications.get_notifications(
        TOKEN, customerid=CUSTOMERID, limit=3)

    assert "error" not in result


def test_get_notification_id():
    """
    """

    single_notification = notifications.get_notifications(
        TOKEN, customerid=CUSTOMERID, limit=1)
    check_id = '-'.join(single_notification[0]['_id'].split('-')[0:2])

    result = notifications.get_notifications(
        TOKEN, customerid=CUSTOMERID, check_id=check_id, limit=2)

    assert "error" not in result
