#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from nodeping_api import check_token, create_check, delete_checks, get_checks, update_checks, get_contacts

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.token
CUSTOMERID = parameters.customerid
CHECKID = parameters.checkid
DELETE_CHECKID = parameters.delete_checkid

class TestGet(unittest.TestCase):
    # Testing API token validity
    def test_is_valid(self):
        if not CUSTOMERID:
            self.assertNotEqual(
                str(check_token.info(TOKEN)),
                '{"error":"Token not found"}',
                "Caught that your token is not valid"
            )
        else:
            self.assertNotEqual(
                str(check_token.info(TOKEN, customerid=CUSTOMERID)),
                '{"error":"Token not found"}',
                "Caught that your token is not valid"
            )

    # Test getting account info
    def test_get_info(self):
        if not CUSTOMERID:
            self.assertNotEqual(
                check_token.info(TOKEN),
                "You have supplied an invalid API key",
                "Caught that your token is not valid"
            )
        else:
            self.assertNotEqual(
                check_token.info(TOKEN, customerid=CUSTOMERID),
                "You have supplied an invalid API key",
                "Caught that your token is not valid"
            )

    # Testing Check creation: DNS
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

    # Testing Check creation: FTP
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

    # Testing Check creation: PUSH
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

    # Test updating a check
    def test_update_check(self):

        fields = {"username": "fakeuser", "password": "123password"}

        query = get_checks.GetChecks(TOKEN, CUSTOMERID)
        all_results = query.all_checks()

        # Updates the FTP TEST LABEL check from creation earlier
        for key, value in all_results.items():
            if value['label'] == "FTP TEST LABEL":
                _id = value['_id']

        result = update_checks.update(TOKEN, _id, fields, customerid=CUSTOMERID)

        try:
            changed = result['change']
        except KeyError:
            self.assertFalse(False, "The check was not changed")
        else:
            self.assertTrue(changed)

    # Test removing checks
    def test_remove(self):

        remove_labels = ["FTP TEST LABEL", "DNS TEST LABEL", "PUSH TEST LABEL"]

        for label in remove_labels:
            if not DELETE_CHECKID:
                query = get_checks.GetChecks(TOKEN, CUSTOMERID)
                all_results = query.all_checks()

                for key, value in all_results.items():
                    if value['label'] == label:
                        queried_checkid = value['_id']
                        break

            if not DELETE_CHECKID and queried_checkid:
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

            result = delete_checks.remove(TOKEN, DELETE_CHECKID, customerid=CUSTOMERID)

            try:
                ok = result['ok']
            except KeyError:
                self.assertFalse(
                    False, "Error occurred removing. Not real checkid")
            else:
                self.assertEqual(ok, True)

    # Test getting all checks
    def test_get_all(self):
        if not CUSTOMERID:
            query = get_checks.GetChecks(TOKEN)
        else:
            query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID)

        self.assertNotEqual(query.all_checks(), "You have supplied an invalid API key", "Token not valid")

    # Test getting passing checks
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

    # Test getting failing checks
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
        
    # Test getting checks by ID
    def test_get_by_id(self):
        if not CUSTOMERID:
            query = get_checks.GetChecks(TOKEN, checkid=CHECKID)
        else:
            query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID, checkid=CHECKID)

        result = query.get_by_id()

        self.assertTrue(result['_id'], msg="The API token, customerid, or checkid may be invalid")

    # Test getting disabled checks
    def test_get_disabled_checks(self):
        if not CUSTOMERID:
            query = get_checks.GetChecks(TOKEN, checkid=CHECKID)
        else:
            query = get_checks.GetChecks(TOKEN, customerid=CUSTOMERID, checkid=CHECKID)

        result = query.disabled_checks()

        for key, value in result.items():
            self.assertEqual(value['type'], 'disabled', "A check was caught and not disabled")

    # Test getting last result for a check
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

    # Test getting contacts
    def test_get_contacts(self):
        result = get_contacts.get_all(TOKEN, customerid=CUSTOMERID)

        self.assertTrue(result, "No contacts gathered")


if __name__ == "__main__":
    unittest.main()