#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from nodeping_api import get_checks, delete_checks
try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.token
CUSTOMERID = parameters.customerid
CHECKID = parameters.checkid


class TestGet(unittest.TestCase):
    def test_remove(self):

        remove_labels = ["FTP TEST LABEL", "DNS TEST LABEL", "PUSH TEST LABEL"]

        for label in remove_labels:
            if not CHECKID:
                query = get_checks.GetChecks(TOKEN, CUSTOMERID)
                all_results = query.all_checks()

                for key, value in all_results.items():
                    if value['label'] == label:
                        queried_checkid = value['_id']
                        break

            if not CHECKID and queried_checkid:
                result = delete_checks.remove(
                    TOKEN, queried_checkid, customerid=CUSTOMERID)

                try:
                    ok = result['ok']
                except KeyError:
                    self.assertFalse(
                        False, "Error occured removing. Not real checkid")
                else:
                    self.assertEqual
            else:
                self.assertFalse(False, "No checkid available for delete test")

            result = delete_checks.remove(TOKEN, CHECKID, customerid=CUSTOMERID)

            try:
                ok = result['ok']
            except KeyError:
                self.assertFalse(
                    False, "Error occurred removing. Not real checkid")
            else:
                self.assertEqual(ok, True)


if __name__ == "__main__":
    unittest.main()
