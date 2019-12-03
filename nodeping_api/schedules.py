#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Get, create, update, and delete schedules for notifications.
"""

from . import _query_nodeping_api, _utils, config

API_URL = "{0}schedules".format(config.API_URL)


def get_schedule(token, schedule=None, customerid=None):
    """ Get existing schedules in NodePing account

    Returns all the data in a dictionary format from the
    original JSON that is gathered from NodePing about
    the account's notification schedules.

    :param token: The NodePing API token for the account
    :type token: str
    :param schedule: The name of the notification schedule
    :type schedule: str
    :param customerid: (optional) ID for subaccount
    :type customerid: str
    :return: Response from NodePing
    :rtype: dict
    """

    if schedule:
        url = "{0}/{1}".format(API_URL, schedule)
        url = _utils.create_url(token, url, customerid)
    else:
        url = _utils.create_url(token, API_URL, customerid)

    return _query_nodeping_api.get(url)


def create_schedule(token, data, schedule_name, customerid=None):
    """ Create a new notification schedule for the specified NodePing account

    Sends data of a custom alert schedule to NodePing to be created
    for the specified user account. Returns the results from NodePing
    in a dictionary format.

    :param: token: The NodePing APi token for the account
    :type token: str
    :param data: The schedules for each day to receive notifications
    :type dict
    :param customerid: (optional) ID for subaccount
    :type customerid: str
    :return: Schedule ID and if the operation was completed or not
    :rtype: dict

    Example::

    {'data': {'friday': {'disabled': True},
              'monday': {'allday': True},
              'saturday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'sunday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'thursday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'tuesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'wednesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'}}}

    Days accept certain variables certain key/value pairs such as:
    time1: str - start of timespan (24-hour time)
    time2: str - end of timespan (24-hour time)
    exclude: True/False - inverts the time span so it is all day 
    except for the time between time1 and time2
    disabled: True/False - disables notifications for this day.
    allday: True/False - enables notifications for the entire day.
    """

    url = "{0}/{1}".format(API_URL, schedule_name)
    url = _utils.create_url(token, url, customerid)

    return _query_nodeping_api.post(url, data)


def update_schedule(token, data, schedule_name, customerid=None):
    """ Update a notification schedule for the specified NodePing account

    Sends data of a custom alert schedule to NodePing to modify a schedule
    for the specified user account. Returns the results from NodePing
    in a dictionary format.

    :param: token: The NodePing API token for the account
    :type token: str
    :param data: The schedules for each day to receive notifications
    :type dict
    :param customerid: (optional) ID for subaccount
    :type customerid: str
    :return: Schedule ID and if the operation was completed or not
    :rtype: dict

    Example::

    {'data': {'friday': {'disabled': True},
              'monday': {'allday': True},
              'saturday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'sunday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'thursday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'tuesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'wednesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'}}}

    Days accept certain variables certain key/value pairs such as:
    time1: str - start of timespan (24-hour time)
    time2: str - end of timespan (24-hour time)
    exclude: True/False - inverts the time span so it is all day 
    except for the time between time1 and time2
    disabled: True/False - disables notifications for this day.
    allday: True/False - enables notifications for the entire day.
    """

    url = "{0}/{1}".format(API_URL, schedule_name)
    url = _utils.create_url(token, url, customerid)

    return _query_nodeping_api.put(url, data)


def delete_schedule(token, schedule, customerid=None):
    """ Get existing schedules in NodePing account

    Returns all the data in a dictionary format from the
    original JSON that is gathered from NodePing about
    the account's notification schedules.

    :param token: The NodePing API token for the account
    :type token: str
    :param schedule: The name of the notification schedule
    :type schedule: str
    :return: Response from NodePing
    :rtype: dict
    """

    url = "{0}/{1}".format(API_URL, schedule)
    url = _utils.create_url(token, url, customerid)

    return _query_nodeping_api.delete(url)
