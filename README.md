# python-nodeping-api

A Python2/3 library for managing checks, schedules, and contacts

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [python-nodeping-api](#python-nodeping-api)
    - [General Usage](#general-usage)
    - [Installation](#installation)
    - [Check token](#check-token)
        - [Checking validity](#checking-validity)
            - [Sample Code](#sample-code)
        - [Retrieving Account Info](#retrieving-account-info)
    - [Get Checks](#get-checks)
    - [Create Checks](#create-checks)
    - [Update Checks](#update-checks)
        - [Updating one](#updating-one)
        - [Updating many](#updating-many)
    - [Disable Checks](#disable-checks)
        - [Disable by Label](#disable-by-label)
        - [Disable by Target](#disable-by-target)
        - [Disable by Type](#disable-by-type)
        - [Disable All](#disable-all)
    - [Delete Checks](#delete-checks)
    - [Get Contacts](#get-contacts)
        - [Get All Contacts](#get-all-contacts)
        - [Get Contacts by Type](#get-contacts-by-type)
    - [Contact Groups](#contact-groups)
        - [Get Groups](#get-groups)
        - [Create Groups](#create-groups)
        - [Update Group](#update-group)
        - [Delete Group](#delete-group)
    - [Schedules](#schedules)
        - [Get Schedules](#get-schedules)
        - [Create Schedules](#create-schedules)
        - [Update Schedules](#update-schedules)
        - [Delete Schedules](#delete-schedules)

<!-- markdown-toc end -->



## General Usage

To use the NodePing API with Python2/3, you are required to use your
provided API token. You can find your API key on your NodePing account
under `Account Settings → API`.

You can also optionally provide a Sub Account ID which can be found
under `Account Settings → SubAccounts` and you will see the ID by its
name.

You can set these variables, for example, like so:

``` python
token = 'my-api-token'
customerid = 'your-subaccount-id'
```

## Installation

To install this package, run:

```
pip install nodeping-api
```

## Check token

This module lets you check if your token is valid and return info about
your account.

### Checking validity

The name of this function is `is_valid()`

This simply returns `True` or raises an exception if the key is not
valid.

#### Sample Code

``` python
>>> from nodeping_api import check_token

>>> valid_token = check_token.is_valid(token)
>>> print(valid_token)
True
```

Or if your key is invalid

``` python
>>> valid_token = check_token.is_valid(token)
False
```

### Retrieving Account Info

The name of this function is `info()`

This will return the contents from NodePing in a dictionary format. If
the token isn’t valid, nothing will be returned.

Example:

``` python
from nodeping_api import check_token

info = check_token.info(token)
```

This will return basic information about your account. Optionally, you
can do the same with a subaccount:

``` python
from nodeping_api import check_token

subacc_info = check_token.info(token, customerid=customerid)
```

## Get Checks

Get checks on your NodePing account via the `get_checks.py` module.

This module will get all checks that are specified, whether enabled or
disabled (excluding `disabled_checks()`, which will only get disabled
checks)

Lets you gather:

  - All checks

  - Passing checks

  - Failing checks

  - Disabled checks

  - Last result

Getting check info examples:

``` python
from nodeping_api import get_checks

# Optionally set customerid to your subaccount ID
query_nodeping = get_checks.GetChecks(token)

# Get all checks
all = query_nodeping.all_checks()

# Get passing checks
passing = query_nodeping.passing_checks()

# Get failing checks
failing = query_nodeping.failing_checks()

# Get disabled checks
disabled = query_nodeping.disabled_checks()

# Get last result
last = query_nodeping.last_result()


# Get check by ID
query_nodeping = get_checks.GetChecks(token, checkid=_id)
check = query_nodeping.get_by_id()
```

## Create Checks

Create checks on your NodePing account via the `create_check.py` module.

This module lets you create a check of any type and with your specified
parameters.

Example of creating an HTTP check:

``` python
def http():

    contacts = [{"contactkey": {"delay": 0, "schedule": "Days"}}]
    loc = "NAM"
    webserver = "https://example.com"

    result = create_check.http_check(
        token, webserver, label="http example.com", enabled=True, follow=True, runlocations=loc, notifications=contacts)

    pprint(result)
```

Example of creating a PUSH check:

``` python
def push(token, contacts, region):
    fields = {
        "apcupsd": {
            "name": "apcupsd",
            "min": 1,
            "max": 1
        },
        "load1min": {
            "name": "load.1min",
            "min": "0",
            "max": "4"
        },
        "load5min": {
            "name": "load.5min",
            "min": "0",
            "max": "2"
        },
        "memavail": {
            "name": "memavail",
            "min": "100",
            "max": "10000"
        }
    }

    results = create_check.push_check(
        token,
        label="Test PUSH",
        fields=fields,
        interval=1,
        runlocations=region,
        notifications=contacts
    )

    pprint(results)
```

## Update Checks

Update checks on your NodePing account via the `update_checks.py`
module.

This module lets you update one or many checks at once. To upate one
check, you will have to supply the Check ID and the fields you want to
change. To update many, you will have to create a list of Dheck IDs.

### Updating one

``` python
from nodeping_api import update_checks

checkid = '201205050153W2Q4C-0J2HSIRF'
fields = {"public": False, "interval": 15}

data = update_checks.update(token, checkid, fields)
```

The returned data will be the information about the check (with updated
values) in a dictionary format.

### Updating many

``` python
from nodeping_api import update_checks

checkid = ['201205050153W2Q4C-0J2HSIRF', '201205050153W2Q4C-4RZT8MLN']
fields = {"public": False, "interval": 15}

data = update_checks.update_many(token, checkids, fields)
```

The returned data will be the information about the checks (with updated
values) in a dictionary format.

## Disable Checks

Disable checks on your NodePing account via the `disable_check.py`
module.

This module lets you disable checks in various ways:

  - By label

  - By target

  - By type

  - All

This will not disable checks on subaccounts.

Set disable to True to disable checks, False to enable. Checks will only
be enabled if they have been disabled via this method.

<https://nodeping.com/docs-api-checks.html#disableall>

### Disable by Label

Specify the label of the check to be enabled/disabled

``` python
from nodeping_api import disable_check

label = "I dont need this"

# Disables the check
disable_check.disable_by_label(token, label, disable=True)
```

### Disable by Target

Specify the Check ID of the check to be enabled/disabled

``` python
from nodeping_api import disable_check

checkid = '201205050153W2Q4C-0J2HSIRF'

# Disables the check by ID
disable_check.disable_by_target(token, checkid, disable=True)
```

### Disable by Type

Specify the TYPE of checks to be disabled (such as PING checks)

``` python
from nodeping_api import disable_check

_type = 'PING'

# Disables the checks by type PING
disable_check.disable_by_type(token, _type, disable=True)
```

### Disable All

This disables all checks on the account

``` python
from nodeping_api import disable_check

# Disables the checks by type PING
disable_check.disable_all(token, disable=True)

# Disable all checks on subaccount
disable_check.disable_all(token, disable=True, customerid=subacc)
```

## Delete Checks

Delete checks on your NodePing account via the `delete_check.py` module.

This module will only remove checks one at a time by supplying your
Check ID.

Example:

``` python
from nodeping_api import delete_checks

checkid = '201205050153W2Q4C-0J2HSIRF'

data = delete_checks.remove(token, checkid)
```

Sample data returned:

`{'ok': True, 'id': '201205050153W2Q4C-0J2HSIRF'}`

Or if the check does not exist:

`{'error': 'Unable to find that check'}`

## Get Contacts

Get contacts on your NodePing account via the `get_contacts.py` module.

This module allows you to get all contacts on your account or by type
such as sms, email, webhook.

### Get All Contacts

``` python
from nodeping_api import get_contacts

contacts = get_contacts.get_all(token)
```

Sample data returned:

    {
      "201205050153W2Q4C-BKPGH": {
        "_id": "201205050153W2Q4C-BKPGH",
        "type": "contact",
        "customer_id": "201205050153W2Q4C",
        "name": "Foo Bar",
        "custrole": "owner",
        "addresses": {
          "K5SP9CQP": {
            "address": "foo@example.com",
            "status": "new"
          }
        }
      }
    }

When providing contacts for creating checks, the `K5SP9CQP` in this
example is the contact id you will need.

### Get Contacts by Type

``` python
from nodeping_api import get_contacts

contact_type = 'sms'

contacts = get_contacts.get_by_type(token, contact_type)
```

## Contact Groups

Manage contact groups on your NodePing account via the `group_contacts.py` module.

<https://nodeping.com/docs-api-contactgroups.html>

This module lets you manage contact groups in these ways:

  - Get contact groups

  - Create contact groups

  - Update contact groups

  - Delete contact groups
  
### Get Groups

``` python
from nodeping_api import group_contacts

# Get contact groups
groups = group_contacts.get_all(token)

# Get contact groups with SubAccount ID
subaccount_id = "your-subaccount-id"

groups = group_contacts.get_all(token, customerid=subaccount_id)
```

### Create Groups

To create a contact group, a name for the group is required. You can optionally
provide members for the contact group in a list. The member will be the key in
the addresses field for each contact. For example, if your contact data is this:

```
    {
      "201205050153W2Q4C-BKPGH": {
        "_id": "201205050153W2Q4C-BKPGH",
        "type": "contact",
        "customer_id": "201205050153W2Q4C",
        "name": "Foo Bar",
        "custrole": "owner",
        "addresses": {
          "K5SP9CQP": {
            "address": "foo@example.com",
            "status": "new"
          }
        }
      }
    }
```

Then the contact ID you need is "K5SP9CQP".

Example:

``` python
from nodeping_api import group_contacts

name = "sample_group"
my_members = ["K5SP9CQP", "D3RF9NQT"]

# Create group without members
empty_group = group_contacts.create_group(token, name)

# Create group with members
new_group = group_contacts.create_group(token, name, members=my_members)
```

### Update Group

Updating the group is the same idea as creating a group.

Example:

``` python
from nodeping_api import group_contacts

name = "sample_group"
new_name = "renamed"
my_members = ["K5SP9CQP", "D3RF9NQT"]

# Update group with new members
updated_group = group_contacts.update_group(token, name, members=my_members)

# Rename a group
renamed = group_contacts.update_group(token, new_name)
```

### Delete Group

To delete the group, you need to provide the group id, which can be found
when you get the groups.

Example:

``` python
from nodeping_api import group_contacts

group_id = "201205050153W2Q4C-G-1ZIYU"

# Delete the group
deleted = group_contacts.delete_group(token, group_id)
```

This will return a dictionary stating that the group was deleted:

`{'id': '201205050153W2Q4C-G-1ZIYU', 'ok': True}`

If it failed, a dictionary with the key error will be gathered.


## Schedules

Manage schedules on your NodePing account via the `schedules.py` module.

<https://nodeping.com/docs-api-schedules.html>

This module lets you manage checks in these ways:

  - Get schedules

  - Create schedules

  - Update schedules

  - Delete schedules

### Get Schedules

``` python
from nodeping_api import schedules

# Get all schedules
schedules = schedules.get_schedules(token)

# Get schedule by name
weekend_schedule = schedules.get_schedules(token, schedule="Weekends")
```

### Create Schedules

To create a schedule, you need to provide data for each day and what its
schedule will be like.

``` python
from nodeping_api import schedules

data = {'data': {'friday': {'exclude': False, 'time1': '8:00', 'time2': '23:00'},
                    'monday': {'allday': True},
                    'saturday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
                    'sunday': {'disabled': True},
                    'thursday': {'exclude': False, 'time1': '8:00', 'time2': '22:00'},
                    'tuesday': {'disabled': True},
                    'wednesday': {'exclude': True, 'time1': '18:30', 'time2': '20:30'}}}

schedule_name = 'myschedule'

created = schedules.create_schedule(token, data, schedule_name)
```

### Update Schedules

Updating schedules lets you update an entire day or a portion of it

``` python
from nodeping_api import schedules

data = {'data': {'saturday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},}}

schedule_name = 'myschedule'

updated = schedules.update_schedule(token, data, schedule_name)
```

### Delete Schedules

To delete a schedule, just provide its name

``` python
from nodeping_api import schedules

schedule_name = 'myschedule'

deleted = schedules.delete_schedule(token, schedule)
```

