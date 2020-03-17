#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for the create_checks.py file
"""

import pytest
from nodeping_api import create_check

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
CUSTOMERID = parameters.CUSTOMERID
EMAIL = "me@example.com"
TARGET = "example.com"


def test_create_agent_check():
    """ Creates a basic agent check
    """

    label = "PYTEST_agent_check"

    result = create_check.agent_check(
        TOKEN, label=label, enabled=False, oldresultfail=True)

    assert "_id" in result.keys and result['label'] == label


def test_create_audio_check():
    """ Creates a basic audio check
    """

    label = "PYTEST_audio_check"
    target = "https://{0}".format(TARGET)

    result = create_check.audio_check(
        TOKEN, target, label=label, customerid=CUSTOMERID)

    assert "_id" in result.keys() and result['label'] == label


def test_create_dns_check():
    """ Creates a basic DNS check
    """

    label = "PYTEST_dns_check"

    result = create_check.dns_check(
        TOKEN, TARGET, label=label, customerid=CUSTOMERID)

    assert "_id" in result.keys() and result['label'] == label


def test_create_ftp_check():
    """ Creates a basic ftp check
    """

    label = "PYTEST_ftp_check"

    result = create_check.dns_check(
        TOKEN, TARGET, label=label, customerid=CUSTOMERID)

    assert "_id" in result.keys() and result['label'] == label


def test_create_httpcontent_check():
    """ Creates a basic httpcontent check

    This also tests adding a couple extra parameters like contentstring
    """

    label = "PYTEST_httpcontent_check"
    content_string = "Hello world"
    target = "https://{0}".format(TARGET)

    result = create_check.httpcontent_check(
        TOKEN, target, label=label, ipv6=True, contentstring=content_string, customerid=CUSTOMERID)

    errors = []

    if "_id" not in result.keys():
        errors.append("_id not found in response")
    if result['label'] != label:
        errors.append("label does not match")
    if result['parameters']['contentstring'] != content_string:
        errors.append("Content string not found in result")

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_create_push_check():
    """ Create a push check
    """

    label = "PYTEST_push_check"

    result = create_check.push_check(
        TOKEN, label=label, fields=parameters.FIELDS, customerid=CUSTOMERID)

    assert label in result['label'] and "_id" in result.keys()
