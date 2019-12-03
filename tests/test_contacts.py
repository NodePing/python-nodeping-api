#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from nodeping_api import contacts

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
NAME = "PYTEST_CREATED_SUBACCOUNT"


def test_get_all():
    """
    """

    result = contacts.get_all(TOKEN)

    assert "error" not in result.keys()


def test_get_by_type():
    """
    """

    contact_method = None

    result = contacts.get_by_type(TOKEN, "email")

    if not result:
        # Try setting the contact type to SMS if the account does
        # not have email contact types
        result = contacts.get_by_type(TOKEN, "sms")

        if not result:
            pytest.fail("Test expects a contact with sms or email")
        else:
            contact_method = "sms"
    else:
        contact_method = "email"

    passing = True

    for i in result.keys():
        for j in result[i]['addresses'].keys():
            if contact_method not in result[i]['addresses'][j]['type']:
                pytest.fail()

    assert passing is True


def test_get_one():
    """
    """

    all_addresses = contacts.get_all(TOKEN)
    contact_id = next(iter(all_addresses.keys()))

    result = contacts.get_one(TOKEN, contact_id)

    assert "error" not in result.keys()


def test_create_contact():
    """
    """

    newaddresses = [
        {
            'action': 'post',
            'address': 'https://webhook.example.com',
            'data': {
                'event': '{event}',
                'id': '{_id}',
                'label': '{label}',
                'target': '{target}'
            },
            'headers': {'Content-Type': 'application/json'},
            'type': 'webhook'
        },
        {
            'address': 'me@example.com',
            'type': 'email'
        }
    ]

    result = contacts.create_contact(
        TOKEN, name=NAME, newaddresses=newaddresses)

    assert "error" not in result.keys()


def test_update_contact_addresses():
    """
    """

    all_addresses = contacts.get_all(TOKEN)

    for i in all_addresses.keys():
        if all_addresses[i]['name'] == NAME:
            temp_contact = i
            break

    newaddresses = [{'address': 'me@example.com'}, {
        'address': 'me2@example.com'}]

    result = contacts.update_contact(
        TOKEN, temp_contact, newaddresses=newaddresses)

    print(temp_contact)
    print(result)

    assert "error" not in result.keys()


def test_delete_contact():
    """
    """

    all_addresses = contacts.get_all(TOKEN)

    for i in all_addresses.keys():
        if all_addresses[i]['name'] == NAME:
            temp_contact = i
            break

    result = contacts.delete_contact(TOKEN, temp_contact)

    assert "error" not in result.keys()
