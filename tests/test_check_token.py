#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from nodeping_api import check_token
try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.token
CUSTOMERID = parameters.customerid


class TestGet(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()