# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

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
