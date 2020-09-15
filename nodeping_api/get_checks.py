#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Get checks that were created on your NodePing account.

Allows you go get all checks, get passing, failing, by its ID,
disabled checks, and last results for a check.
"""

from . import _query_nodeping_api, _utils, config

API_URL = "{0}checks".format(config.API_URL)


class GetChecks:
    def __init__(self, token, checkid=None, customerid=None, current=None, uptime=False):
        """
        :type token: string
        :param token: NodePing API token
        :type checkid: string/list
        :param checkid: ID or list of IDs for check to retrieve data for
        :type customerid: string
        :param customerid: subaccount ID
        """

        self.token = token
        self.checkid = checkid
        self.customerid = customerid
        self.current = current
        self.uptime = uptime
        self.args = {
            "token": token,
            "id": checkid,
            "customerid": customerid,
            "current": current,
            "uptime": uptime
        }

    def all_checks(self):
        """ Gets all checks that exist for the account

        Makes a request to NodePing with the supplied API key.
        Returns all check information in a dictionary format.

        Must provide the account's API token and optionally the
        customerid to output subaccount checks
        """

        url = _utils.create_url(self.token, API_URL, self.customerid)

        if self.uptime:
            return self._get_check_uptime(url)

        return _query_nodeping_api.get(url)

    def get_many_checks(self):
        """ Get many checks for the account or subaccount

        Provide a list of check IDs to be fetched.
        """

        if not isinstance(self.checkid, list):
            return {"error": "A List must be provided"}

        checks = ",".join(self.checkid)
        args = self.args
        args["id"] = checks

        url = "{0}{1}".format(API_URL, _utils.generate_querystring(args))

        return _query_nodeping_api.get(url)

    def passing_checks(self):
        """ Gets all checks that are passing for the account

        Makes a request to NodePing with the supplied API key.
        Collects all checks for the account and removes all checks
        with a state of 0 which means the check is failing.
        """

        passing_checks = {}

        url = _utils.create_url(self.token, API_URL, self.customerid)

        if self.uptime:
            url = "{0}&uptime=true".format(url)

        all_checks_dictionary = _query_nodeping_api.get(url)

        for check_id, contents in all_checks_dictionary.items():
            try:
                state = contents["state"]
            except KeyError:
                state = 0

            if state == 1:
                passing_checks.update({check_id: contents})

        return passing_checks

    def failing_checks(self):
        """ Gets all checks for the account that are failing

        Makes a request to NodePing with the supplied API key.
        Queries NodePing for current failing checks.

        *NOTE* this will also include disabled checks
        """

        failing_checks = {}

        url = _utils.create_url(self.token, API_URL, self.customerid)

        if self.uptime:
            url = "{0}&uptime=true".format(url)

        all_checks_dictionary = _query_nodeping_api.get(url)

        for check_id, contents in all_checks_dictionary.items():
            try:
                state = contents["state"]
            except KeyError:
                state = 2

            if state == 0:
                failing_checks.update({check_id: contents})

        return failing_checks

    def get_by_id(self):
        """ Collects the check based on its ID

        Expects a valid check ID and API token. Collects all
        checks from NodePing and looks for the check with the
        specified ID. Returns the contents for that check
        """

        url = "{0}/{1}".format(API_URL, self.checkid)
        url = _utils.create_url(self.token, url, self.customerid)

        if self.uptime:
            return self._get_check_uptime(url)

        return _query_nodeping_api.get(url)

    def disabled_checks(self):
        """ Gets all checks for the account that are disabled

        Makes a request to NodePing with the supplied API key.
        Queries NodePing for current events for the check.
        """

        url = _utils.create_url(self.token, API_URL, self.customerid)

        if self.uptime:
            url = "{0}&uptime=true".format(url)

        events_checks = _query_nodeping_api.get(url)

        return {k: v for k, v in events_checks.items() if v["enable"] == "inactive"}

    def last_result(self):
        """ Get the last result for the specified check
        """

        url = "{0}/{1}?lastresult=true".format(API_URL, self.checkid)
        url = _utils.create_url(self.token, url, self.customerid)

        if self.uptime:
            return self._get_check_uptime(url)

        return _query_nodeping_api.get(url)

    def _get_check_uptime(self, url):
        """ Get check information along with its uptime

        Expects a valid check ID and API token. Collects all
        the info about the check and uptime for each day.
        """

        return _query_nodeping_api.get("%s&uptime=true" % url)
