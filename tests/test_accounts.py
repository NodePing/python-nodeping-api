#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from nodeping_api import accounts

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
NAME = "PYTEST_CREATED_SUBACCOUNT"
EMAIL = "me@example.com"


def test_get_account():
    """ tests getting an account with/without a customerid
    """

    # Tests get without a customerid
    token_only_result = accounts.get_account(TOKEN)

    customerid = next(iter(token_only_result))

    # Tests with customerid
    token_custid_result = accounts.get_account(TOKEN, customerid)

    # For this assert to work, both queries with/without customerid should work
    assert "_id" in token_custid_result.keys()


def test_get_account_fail():
    """ Tests getting an account with a bad token
    """

    invalid_token = "invalid-customer-token"

    assert accounts.get_account(invalid_token) == {'error': 'Token not found'}


def test_get_subaccount_fail():
    """ Tests getting a subaccount with a valid token, but invalid subaccount
    """

    invalid_subaccount = "20191108123456789"

    result = accounts.get_account(TOKEN, customerid=invalid_subaccount)

    assert result == {
        'error': 'You do not have the correct permissions for that account.'}


def test_create_subaccount():
    """ Creates a subaccount

    Will create a subaccount with a predefined name
    """

    result = accounts.create_subaccount(
        TOKEN, NAME, "PYTEST", EMAIL, "-6", "nam")

    assert "_id" in result.keys()


def test_update_subaccount():
    """ Test updating a parameter in a subaccount

    Will update an account with a predefined name
    """

    customer_accounts = accounts.get_account(TOKEN)

    for i in customer_accounts.keys():
        if customer_accounts[i]["name"] == NAME:
            subaccount = i
            break

    result = accounts.update_account(
        TOKEN, customerid=subaccount, location="eur")

    assert result["defaultlocations"] == ['eur']


def test_delete_subaccount():
    """ Test deleting a subaccount

    Will delete an account with a predefined name
    """

    customer_accounts = accounts.get_account(TOKEN)

    for i in customer_accounts.keys():
        if customer_accounts[i]["name"] == NAME:
            subaccount = i
            break

    result = accounts.delete_account(TOKEN, subaccount)

    assert result == {'success': 'Records queued for deletion.'}
