#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Manage notification profiles for NodePing Account.

https://nodeping.com/docs-api-notificationprofiles.html
"""

from . import _query_nodeping_api, _utils, config

API_URL = "{0}notificationprofiles".format(config.API_URL)


def get(token,
        customerid=None,
        id=None):
    """Get one or all notification profiles for an account or subaccount.

    :param token: The NodePing token for your account
    :type token: str
    :param customerid: (optional) ID for the subaccount
    :type customerid: str
    :param id: (optional) - id of the notification profile you want to get.
    """
    if id:
        url = "{0}?id={1}".format(API_URL, id)
    else:
        url = API_URL

    url = _utils.create_url(token, url, customerid)

    return _query_nodeping_api.get(url)


def create(token,
           name,
           notifications,
           customerid=None):
    """Create a new notification profile.

    :param token: The NodePing token for your account
    :type token: str
    :param name: label for the notification profile
    :type name: str
    :param notifications: list containing the contact or group id, delay, and scheduling for notifications
    :type notifications: list
    :param customerid: (optional) ID for the subaccount
    :type customerid: str

    notifications param example:

    [
        {"contactkey1":
            {"delay":0,
                "schedule":"schedule1"
            }
        },
        {"contactkey2":
            {"delay":5,
                "schedule":"schedule2"
            }
        }
    ]
    """
    url = _utils.create_url(token, API_URL, customerid)
    data = {"notifications": notifications, "name": name}

    return _query_nodeping_api.post(url, data)


def update(token,
           name,
           id,
           notifications,
           customerid=None):
    """Update information for a contact profile.

    :param token: The NodePing token for your account
    :type token: str
    :param name: label for the notification profile
    :type name: str
    :param id: notification profile id you want to modify
    :type id: str
    :param notifications: list containing the contact or group id, delay, and scheduling for notifications
    :type notifications: list
    :param customerid: (optional) ID for the subaccount
    :type customerid: str

    notifications param example:

    [
        {"contactkey1":
            {"delay":0,
                "schedule":"schedule1"
            }
        },
        {"contactkey2":
            {"delay":5,
                "schedule":"schedule2"
            }
        }
    ]
    """
    url = _utils.create_url(token, API_URL, customerid)
    data = {"notifications": notifications, "name": name, "id": id}

    return _query_nodeping_api.put(url, data)


def delete(token,
           id,
           customerid=None):
    """Get one or all notification profiles for an account or subaccount.

    :param token: The NodePing token for your account
    :type token: str
    :param customerid: (optional) ID for the subaccount
    :type customerid: str
    :param id: (optional) - id of the notification profile you want to get.
    """
    url = "{0}/{1}".format(API_URL, id)

    url = _utils.create_url(token, url, customerid)

    return _query_nodeping_api.delete(url)
