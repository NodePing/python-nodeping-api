#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Tests to disable checks
"""

import http.client
import pytest
from nodeping_api import information

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN


def test_get_probe_all():
    """
    """

    result = information.get_probe(TOKEN)

    # Compare result with pinghosts.txt
    conn = http.client.HTTPSConnection("nodeping.com")
    conn.request("GET", "/content/txt/pinghosts.txt")
    r1 = conn.getresponse()
    pinghosts = r1.read().decode('utf-8')
    pinghosts = pinghosts.split('\n')

    ip_addrs = []

    for i in pinghosts:
        ip_addrs.append(i.split(' ')[-1])

    for ip in ip_addrs:
        assert ip in str(result)


def test_get_probe_single():
    """
    """

    all_probes = information.get_probe(TOKEN)
    first_probe = next(iter(all_probes))
    single_probe = information.get_probe(TOKEN, probe=first_probe)

    assert single_probe == all_probes[first_probe]


def test_get_location_all():
    """
    """

    result = information.get_location(TOKEN)

    # There should be more than one region
    assert len(result.keys()) > 1


def test_get_location_single():
    """
    """

    all_locations = information.get_location(TOKEN)
    loc = next(iter(all_locations))
    single_loc = information.get_location(TOKEN, location=loc)

    assert single_loc == all_locations[loc]
