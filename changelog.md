# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
(Placeholder for unreleased content)

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
