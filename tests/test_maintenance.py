#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from nodeping_api import maintenance, create_check

try:
    import parameters
except ModuleNotFoundError:
    from . import parameters

TOKEN = parameters.TOKEN
NAME = "PYTEST_CREATED_MAINTENANCE"


# def test_create_ad_hoc():
#     """
#     """

#     # Check needs to be created to add check to maintenance

#     duration = 1
#     checklist = []
#     name = "PYTEST_AD_HOC"


def test_get_all():
    """
    """

    result = maintenance.get_maintenance(TOKEN)

    assert "error" not in result.keys()
