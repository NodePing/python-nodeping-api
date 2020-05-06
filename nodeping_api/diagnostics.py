#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Request diagnostic information from a probe or AGENT
"""

from . import _query_nodeping_api, _utils, config

API_URL = "{0}diagnostics".format(config.API_URL)


def get(
    token, checkid, location, tool, target=None, dnsserver=None, dnstype=None, count=10
):
    """ Get diagnostic information from a probe or agent

    :type token: string
    :param token: NodePing API token
    :type checkid: string
    :param checkid: ID for the check associated with this diagnostic request
    :type tool: string
    :param tool: The type of diagnostic you would like to run
    :type target: string
    :param target: optional URL, FQDN, IP you'd like diagnostics about.
    :type dnsserver: string
    :param dnsserver: FQDN or IP you'd like to query with the dig tool
    :type dnstype: string
    :param dnstype: DNS record query type used with the dig tool
    :type count: int
    :param count: For ping and mtr. Number of pings to send. Max of 100
    :return: Response from NodePing with diagnostics data
    :rtype: dict
    """

    queries = locals()
    del queries["token"]
    del queries["checkid"]
    queries = _utils.generate_querystring({k: v for k, v in queries.items() if v})

    url = "{0}/{1}{2}".format(API_URL, checkid, queries)
    url = _utils.create_url(token, url, customerid=None)

    return _query_nodeping_api.get(url)
