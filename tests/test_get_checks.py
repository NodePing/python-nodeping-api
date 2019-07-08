#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from nodeping_api import get_checks
try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.token
CUSTOMERID = parameters.customerid
CHECKID = parameters.checkid

class TestGet(unittest.TestCase):
    def test_get_all(self):
        if not CUSTOMERID:
            query = get_checks.GetChecks(TOKEN)
        else:
            query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)

        self.assertNotEqual(query.all_checks(), "You have supplied an invalid API key", "Token not valid")

    def test_passing_checks(self):
        if not CUSTOMERID:
            query = get_checks.GetChecks(TOKEN)
        else:
            query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)

        result = query.passing_checks()

        for key, value in result.items():
            try:
                state = value['state']
            except KeyError:
                self.assertFalse(False, "Caught a value that doesn't have state")

            self.assertEqual(state, 1, "Should be 1 for passing")

    def test_failing_checks(self):
        if not CUSTOMERID:
            query = get_checks.GetChecks(TOKEN)
        else:
            query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)

        result = query.failing_checks()

        for key, value in result.items():
            try:
                state = value['state']
            except KeyError:
                self.assertFalse(False, "Caught a value that doesn't have state")

            self.assertEqual(state, 0, "Should be 0 for passing")
        
    def test_get_by_id(self):
        if not CUSTOMERID:
            query = get_checks.GetChecks(TOKEN, checkid=CHECKID)
        else:
            query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID, checkid=CHECKID)

        result = query.get_by_id()

        self.assertTrue(result['_id'], msg="The API token, customerid, or checkid may be invalid")

    def test_get_disabled_checks(self):
        if not CUSTOMERID:
            query = get_checks.GetChecks(TOKEN, checkid=CHECKID)
        else:
            query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID, checkid=CHECKID)

        result = query.disabled_checks()

        for key, value in result.items():
            self.assertEqual(value['type'], 'disabled', "A check was caught and not disabled")

    def test_last_result(self):
        if not CUSTOMERID:
            query = get_checks.GetChecks(TOKEN, checkid=CHECKID)
        else:
            query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID, checkid=CHECKID)

        result = query.last_result()

        try:
            has_error = result['error']
        except KeyError:
            self.assertTrue(result['_id'], True)
        else:
            self.assertFalse(False)



if __name__ == "__main__":
    unittest.main()