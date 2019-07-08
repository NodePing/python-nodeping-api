#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from nodeping_api import create_check
try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.token
CUSTOMERID = parameters.customerid

class TestGet(unittest.TestCase):
    def test_dns_check(self):

        result = create_check.dns_check(
            TOKEN,
            customerid=CUSTOMERID,
            target="8.8.8.8",
            contentstring="167.114.101.137",
            dnstoresolve="nodeping.com",
            label="DNS TEST LABEL"
        )

        try:
            _id = result['_id']
        except KeyError:
            self.assertFalse(False, "You have supplied an invalid API key")
        else:
            self.assertTrue(result['_id'])

    def test_ftp_check(self):

        result = create_check.ftp_check(
            TOKEN,
            customerid=CUSTOMERID,
            target="ftp.example.com",
            label="FTP TEST LABEL",
            username="myuser",
            password="password123",
        )

        try:
            _id = result['_id']
        except KeyError:
            self.assertFalse(False, "You have supplied an invalid API key")
        else:
            self.assertTrue(result['_id'])

    def test_push_check(self):

        result = create_check.push_check(
            TOKEN,
            customerid=CUSTOMERID,
            label="PUSH TEST LABEL",
            fields=parameters.fields,
            oldresultfail=True
        )

        try:
            _id = result['_id']
        except KeyError:
            self.assertFalse(False, "You have supplied an invalid API key")
        else:
            self.assertTrue(result['_id'])


if __name__ == "__main__":
    unittest.main()