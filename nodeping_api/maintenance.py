#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Manage scheduled or ad-hoc maintenance schedules.
Get, create, update, and delete maintenanec schedules for your account.

https://nodeping.com/docs-api-maintenance.html
"""

from . import _query_nodeping_api, _utils, config

API_URL = "{0}maintenance".format(config.API_URL)


def get_maintenance(token, customerid=None, maintenanceid=None):
    """ Get information about a maintenance schedule

    :param token: The NodePing token for the account
    :type token: str
    :param customerid: (optional) ID for the subaccount
    :type customerid: str
    :param maintenanceid: (optional) ID for the maintenance schedule.
    :return: Info about specified maintenanceid or all maintenance schedules
    :rtype: dict, list
    """

    if maintenanceid:
        url = "{0}/{1}".format(API_URL, maintenanceid)
    else:
        url = API_URL

    url = _utils.create_url(token, url, customerid)

    return _query_nodeping_api.get(url)


def create_maintenance(
        token,
        duration,
        checklist,
        name=None,
        enabled=True,
        cron=None,
        _id=None,
        customerid=None):
    """ Create an ad-hoc or scheduled maintenance schedule

    :param token: The NodePing token for the account
    :type token: str
    :param duration: the number of minutes to keep the checks disabled
    :type duration: int
    :param checklist: a list of check IDs to disable for this maintenance
    :type checklist: list
    :param name: A name you want to call this maintenance
    :type name: str
    :param enabled: whether you want the maintenance enabled or disabled
    :type enabled: bool
    :param cron: time to start scheduled maintenance (ignored for ad-hoc)
    :type cron: str
    :param _id: set to "ad-hoc" if you want to create an ad-hoc maintenance
    :type _id: str
    :param customerid: (optional) ID for the subaccount
    :type customerid: str

    Ad-hoc maintenance
    ------------------

    result = maintenance.create_maintenance(token, "test_maintenance", 20, [
                                            "201911191441YC6SJ-4S9OJ78G"],
                                            _id="ad-hoc")

    Scheduled maintenance
    ---------------------

    result = maintenance.create_maintenance(token, 20, [
                                            "201911191441YC6SJ-4S9OJ78G"],
                                            enabled=True, cron="1 12 * * *",
                                            name="scheduled")
    """

    check_variables = locals()

    if _id == "ad-hoc":
        url = "{0}/ad-hoc".format(API_URL)
    else:
        url = API_URL

    url = _utils.create_url(token, url, customerid)

    check_variables.pop('token')
    check_variables.pop('customerid')

    return _query_nodeping_api.post(url, check_variables)


def update_maintenance(
        token,
        _id,
        duration,
        checklist,
        name=None,
        enabled=True,
        cron=None,
        customerid=None):
    """ Update an existing maintenance schedule

    :param token: The NodePing token for the account
    :type token: str
    :param _id: The ID of your maintenance schedule. e.g. 9VKOB
    :type _id: str
    :param duration: the number of minutes to keep the checks disabled
    :type duration: int
    :param checklist: a list of check IDs to disable for this maintenance
    :type checklist: list
    :param name: A name you want to call this maintenance
    :type name: str
    :param enabled: whether you want the maintenance enabled or disabled
    :type enabled: bool
    :param cron: time to start scheduled maintenance
    :type cron: str
    :param customerid: (optional) ID for the subaccount
    :type customerid: str

    Update maintenance
    ------------------

    result = maintenance.create_update(token, "9VKOB", 20, [
                                            "201911191441YC6SJ-4S9OJ78G"],
                                            name="sample", cron="2 12 * * *")
    """

    check_variables = locals()

    url = "{0}/{1}".format(API_URL, _id)

    url = _utils.create_url(token, url, customerid)

    check_variables.pop('token')
    check_variables.pop('customerid')

    return _query_nodeping_api.put(url, check_variables)


def delete_maintenance(token, _id, customerid=None):
    """
    """

    url = "{0}/{1}".format(API_URL, _id)
    url = _utils.create_url(token, url, customerid)

    return _query_nodeping_api.delete(url)
