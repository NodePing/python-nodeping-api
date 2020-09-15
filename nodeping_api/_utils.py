#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Helper functions to reduce code reuse and misc other uses
"""

try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote


def create_url(token, url, customerid):
    """ Creates the url for sending data to NodePing

    Formats the url based on whether or not the
    customerid is None

    :type token: string
    :param token: Your NodePing API token
    :type url: string
    :param url: full URL to API excluding the token and/or custid
    :type customerid: string
    :param customerid: Optional subaccount ID for your account
    :return: URL that will be used for HTTP request
    :rtype: string
    """

    if "?" in url:
        token_str = "&token="
    else:
        token_str = "?token="

    if customerid:
        url = "{0}{1}{2}&customerid={3}".format(url, token_str, token, customerid)
    else:
        url = "{0}{1}{2}".format(url, token_str, token)

    return url


def escape_url_string(string):
    """ Escape invalid strings that will be used for a url
    """

    return quote(string)


def generate_querystring(dictionary):
    """ Generates a querystring from a dictionary

    Removes all `None` values
    """

    dict_no_none = {k: v for k, v in dictionary.items() if v}

    querystring = "".join({"&{0}={1}".format(k, v) for k, v in dict_no_none.items()})

    return querystring.replace("&", "?", 1)
