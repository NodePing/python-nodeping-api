# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
(Placeholder for unreleased content)

# [1.2.0]

2020-09-15

### Fixed

Fixed the `disabled_checks` function to check the `enable` field to see if the check is inactive or not.

### Added

- Added the uptime parameter to `get_checks`
- Added a `get_many_checks` function to `get_checks` which can get a list of checks
- Added an offset variable for `results.get_uptime`
- Added a `get_event` function to `results.py` to retrieve events for checks

## [1.1.4]

2020-08-25

### Added
- Added the `servername` variable to `create_check.ssl_check`

## [1.1.3]

2020-07-16

### Fixed
- Failed import fixed for Python 2.7

## [1.1.2]

2020-05-06

### Added
- Support for getting diagnostics data <https://nodeping.com/docs-api-diagnostics.html>

## [1.1.1]

### Added
- Support for creating AGENT checks <https://nodeping.com/agent_check.html>
- Test added for creating an AGENT check

## [1.1]

### Added
- Support for the new maintenance functionality <https://nodeping.com/docs-api-maintenance.html>

## [1.0]

### Added
- New tests via pytest
- Code reuse was simplified with a couple functions in a _utils.py file for simple URL creation as well as a function that will escape strings that are used in URLs

### Changed
- Error outputs are different. Instead of ambiguous errors or 403 Forbidden results due to an invalid token or customerid, error responses given directly from the API will be provided in dictionary format.

### Fixed
- group_contacts.py update_groups got a required vairable "name" for the name of the contact group that will be modified. Previously, group changes resulted in a new group being created instead of updated.


## [0.9.9_3]

### Changed
- Added Spec10DNS create check functionality
- Added Spec10RDDS create check functionality
- Added a verify parameter to verify DNSSEC when creating a DNS check (default is False)

### Fixed
- Contacts were not being created properly outside of email and sms contact types.
  - Refer to the README and contacts.create_contact docstring. Instead of a list of addresses, it is now a list of dictionaries with the address and type.

## [0.9.9] - 2019-08-10

### Changed
- update_checks.update
  - **checktype** parameter now required. This is the TYPE for the check (PING, HTTP, DNS, etc.)
- update_checks.update_many
  - The `checkids` type was changed to a dictionary from a list to match the checktype with the check
  - When updating many checks, the dict would look like {checkid1: TYPE, checkid2: TYPE}
  
  
### Fixed
- update_checks.update properly updates all fields. The lack of checktype could cause some fields for a check to not update
- update_checks.update_many properly updates all fields, for the same reason as above.
