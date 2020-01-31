# python-nodeping-api

A Python2/3 library for managing checks, schedules, and contacts

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [python-nodeping-api](#python-nodeping-api)
    - [General Usage](#general-usage)
    - [Installation](#installation)
    - [Verify API token](#verify-api-token)
        - [Checking validity](#checking-validity)
            - [Sample Code](#sample-code)
        - [Retrieving Account Info](#retrieving-account-info)
    - [Checks](#checks)
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
    - [Contacts](#contacts)
        - [Getting Contacts](#getting-contacts)
            - [Get All Contacts](#get-all-contacts)
            - [Get a Single Contact](#get-a-single-contact)
            - [Get Contacts by Type](#get-contacts-by-type)
        - [Create a Contact](#create-a-contact)
        - [Update a Contact](#update-a-contact)
        - [Delete a Contact](#delete-a-contact)
        - [Resetting a Password](#resetting-a-password)
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
    - [Maintenance](#maintenance)
        - [Get Maintenance](#get-maintenance)
        - [Create Maintenance](#create-maintenance)
        - [Update Maintenance](#update-maintenance)
        - [Delete Maintenance](#delete-maintenance)
    - [Notifications](#notifications)
        - [Notification Examples](#notification-examples)
    - [Results](#results)
        - [Getting Check Results](#getting-check-results)
        - [Get Uptime](#get-uptime)
        - [Getting Monthly Uptime Since 2019-02](#getting-monthly-uptime-since-2019-02)
        - [Getting Daily Uptime In Time Range](#getting-daily-uptime-in-time-range)
        - [Current Events](#current-events)
    - [Information](#information)
        - [Get Probe Info](#get-probe-info)
            - [Get NY Probe Info](#get-ny-probe-info)
        - [Get Location Information](#get-location-information)
            - [Get North America Info](#get-north-america-info)

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

## Verify API token

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

## Checks

### Get Checks

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

### Create Checks

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

### Update Checks

Update checks on your NodePing account via the `update_checks.py`
module.

This module lets you update one or many checks at once. To upate one
check, you will have to supply the Check ID, the type of check, and the fields you want to
change. To update many, you will have to create a dict of Check IDs.

#### Updating one

``` python
from nodeping_api import update_checks

checkid = '201205050153W2Q4C-0J2HSIRF'
checktype = 'PING'
fields = {"public": False, "interval": 15}

data = update_checks.update(token, checkid, checktype, fields)
```

The returned data will be the information about the check (with updated
values) in a dictionary format.

#### Updating many

``` python
from nodeping_api import update_checks

checkids = {'201205050153W2Q4C-0J2HSIRF': 'PING', '201205050153W2Q4C-4RZT8MLN': 'HTTP'}
fields = {"public": False, "interval": 15}

data = update_checks.update_many(token, checkids, fields)
```

The returned data will be the information about the checks (with updated
values) in a dictionary format.

### Disable Checks

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

#### Disable by Label

Specify the label of the check to be enabled/disabled

``` python
from nodeping_api import disable_check

label = "I dont need this"

# Disables the check
disable_check.disable_by_label(token, label, disable=True)
```

#### Disable by Target

Specify the Check ID of the check to be enabled/disabled

``` python
from nodeping_api import disable_check

checkid = '201205050153W2Q4C-0J2HSIRF'

# Disables the check by ID
disable_check.disable_by_target(token, checkid, disable=True)
```

#### Disable by Type

Specify the TYPE of checks to be disabled (such as PING checks)

``` python
from nodeping_api import disable_check

_type = 'PING'

# Disables the checks by type PING
disable_check.disable_by_type(token, _type, disable=True)
```

#### Disable All

This disables all checks on the account

``` python
from nodeping_api import disable_check

# Disables the checks by type PING
disable_check.disable_all(token, disable=True)

# Disable all checks on subaccount
disable_check.disable_all(token, disable=True, customerid=subacc)
```

### Delete Checks

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

## Contacts


### Getting Contacts

Get contacts on your NodePing account via the `contacts.py` module.

This module allows you to get all contacts on your account, get a single
contact, or get by type such as sms, email, webhook.

#### Get All Contacts

``` python
from nodeping_api import contacts

all_contacts = contacts.get_all(token)
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

#### Get a Single Contact

``` python
from nodeping_api import contacts

all_contacts = contacts.get_one(token, '201205050153W2Q4C-BKPGH')
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

#### Get Contacts by Type

``` python
from nodeping_api import contacts

contact_type = 'sms'

contacts_by_type = contacts.get_by_type(token, contact_type)
```

### Create a Contact

Create a new contact on your account. When creating an account, supply the name,
custrole (such as if they have view permissions or owner), and the addresses that
contact will use.

``` python
>>> from nodeping_api import contacts
>>> from pprint import pprint

>>> token = 'my-api-token'
>>> newaddresses = [{'address': 'me@example.com', 'type': 'email'}, {'address': 'me2@example.com', 'type': 'pagerduty'}, {'address': '1235558888', 'type': 'sms'}]
>>> name = "my new contact"

>>> new_contact = contacts.create_contact(token, name=name, newaddresses=newaddresses)

pprint(new_contact)
{'_id': '2019052211307H0IX-KR9CO',
 'addresses': {'JMMARFHQ': {'accountsuppressall': false, 'type': 'email',
                            'address': 'me2@example.com'},
               'NMYW1XC1': {'accountsuppressall': false, 'type': 'pagerduty',
                            'address': 'me@example.com'},
               'P080YGYO': {'accountsuppressall': false, type': 'sms',
                            'address': '1235558888'}},
 'customer_id': '2019052211307H0IX',
 'custrole': 'view',
 'name': 'my new contact',
 'sdomain': 'nodeping.com',
 'type': 'contact'}
```


### Update a Contact

You can also update existing created contacts based on their contact ID. You can
change its name, role, add contact addresses, or modify existing ones. Note that
when you are modifying existing contacts, you must supply the entire list of
contacts for that user. Missing entries will be removed.

In the example below, the updated contact is exactly the same as the contact
in the create contact example, but with the addresses updated as well as some
new addresses added.

https://nodeping.com/docs-api-contacts.html

``` python
>>> from nodeping_api import contacts
>>> from pprint import pprint

>>> token = 'my-api-token'
>>> contact_id = "2019052211307H0IX-KR9CO"
>>> newaddresses = [{'address': 'me@example.com'}, {'address': 'me2@example.com'}, {'address': '1235558888'}]
>>> addresses = {'JMMARFHQ': {'address': 'newme@example.com', 'accountsupressall': False}, 'NMYW1XC1': {'address': 'newme2@example.com', 'accountsupressall': False}, 'P080YGYO': {'address': '321444777', 'accountsuppressall': False}}

>>> pprint(contacts.update_contact(token, contact_id, addresses=addresses, newaddresses=newaddresses))

{'_id': '2019052211307H0IX-KR9CO',
 'addresses': {'8XK9OGNW': {'accountsuppressall': False,
                            'address': 'me2@example.com'},
               'CUSR6CTF': {'accountsuppressall': False,
                            'address': 'me@example.com'},
               'JMMARFHQ': {'accountsuppressall': False,
                            'address': 'newme@example.com'},
               'NMYW1XC1': {'accountsuppressall': False,
                            'address': 'newme2@example.com'},
               'P080YGYO': {'accountsuppressall': False,
                            'address': '321444777'},
               'VZ5HY05B': {'accountsuppressall': False,
                            'address': '1235558888'}},
 'customer_id': '2019052211307H0IX',
 'custrole': 'view',
 'name': 'my new contact',
 'sdomain': 'nodeping.com',
 'type': 'contact'}
```


### Delete a Contact

If you no longer need a contact, you can simply delete it by specifying its ID

``` python
from nodeping_api import contacts
from pprint import pprint

token = 'my-api-token'
contact_id = "2019052211307H0IX-KR9CO"

deleted = contacts.delete_contact(token, contact_id)
```

With the resulting output:

``` python
{'id': '2019052211307H0IX-KR9CO', 'ok': True}
```


### Resetting a Password

You can reset passwords for a contact by specifying their contact ID:

``` python
from nodeping_api import contacts

token = 'my-api-token'
contact_id = '2019052211307H0IX-KR9CO'

reset = 'contacts.reset_password(token, contact_id)
```

This will send a new password to the email address associated with that contact.


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

## Maintenance

Manage maintenances for your NodePing account via the `maintenance.py` module.

Get, create, update, and delete maintenances as well as create ad-hoc
maintenance schedules.

### Get Maintenance

You can get maintenances by id or all at once

``` python
from nodeping_api import maintenance

token = "my-api-token"
maintenanceid = "NZT101"

# Get maintenance
all_maintenance = maintenance.get_maintenance(token, maintenanceid=maintenanceid)

# Get all maintenances
one_maintenance = maintenance.get_maintenance(token)
```

### Create Maintenance

Create scheduled maintenances or an ad-hoc maintenance

``` python
from nodeping_api import maintenance

token = "my-api-token"
cron = "1 12 * * *"
duration = 30
name = "my_maintenance"
checklist = ["201911191441YC6SJ-4S9OJ78G","201911191441YC6SJ-XB5HUTG6"]

# Create ad-hoc maintenance
ad_hoc = maintenance.create_maintenance(token, duration, checklist, name=name, _id="ad-hoc") 

# Create scheduled maintenance
scheduled = maintenance.create_maintenance(token, duration, checklist,
    name=name, enabled=True, cron=cron)
```

### Update Maintenance

Update existing scheduled maintenances

``` python
from nodeping_api import maintenance

token = "my-api-token"
duration = "45"
name = "new name for schedule"
_id = "NZT101"
checklist = ["201911191441YC6SJ-4S9OJ78G","201911191441YC6SJ-XB5HUTG6"]

result = maintenance.update_maintenance(token, _id, duration, checklist, name=name)
```

### Delete Maintenance

Delete an existing scheduled maintenance

``` python
from nodeping_api import maintenance

token = "my-api-token"
_id = "NZT101"

deleted = maintenance.delete_maintenance(token, _id)
```


## Notifications

Get notifications for your NodePing account via the `notifications.py` module.

When getting notifications, you can limit how many you get by the number of hours,
number of notifications, if you want to collect from subaccounts or not, and by
check ID

### Notification Examples


Getting the last 100
``` python
from nodeping_api import notifications

token = 'my-api-token
limit = 100

last_notifications = notifications.get_notifications(token, limit=limit)
```

Getting results for a check ID for the last 2 hours
``` python
from nodeping_api import notifications

token = "my-api-token"
span = 2
check_id = '201205050153W2Q4C-0J2HSIRF'

last_notifications = notifications.get_notifications(token, check_id=check_id, span=span)
```


## Results

This module lets you get results and uptime for different checks at optionally given
time durations. To get an idea of what the output will look like from the API, you
can visit the documentation that shows what outputs you will get:

https://nodeping.com/docs-api-results.html


### Getting Check Results

Get the last 100 results for a check.

``` python
from nodeping_api import results

token = 'my-api-token
check_id = '201205050153W2Q4C-0J2HSIRF'
limit = 100

last_results = results.get_results(token, check_id, limit=limit)
```

Your output will consist of a list of dictionaries that will look like this:

``` python
[{
  "_id":"201205050153W2Q4C-0J2HSIRF-1345313038648",
  "ci":"201205050153W2Q4C",
  "t":"DNS",
  "tg":"8.8.8.8",
  "th":"5",
  "i":"5",
  "ra":"1345313029252",
  "q":"caRRa3op0v",
  "s":1345313038648,
  "sc":"Success",
  "su":true,
  "rt":77,
  "e":1345313038725,
  "l":{"1345313038648":"ca"}
}]
```

### Get Uptime

This lets you get the uptime percentages for the specified check. The output
will be a dictionary of the last days/months and their uptime and downtime.

### Getting Monthly Uptime Since 2019-02

With the API, monthly is the default interval, so you do not need to
specify "monthly" unless you want to.

``` python
from nodeping_api import results
from pprint import pprint

token = 'my-api-token
check_id = '201205050153W2Q4C-0J2HSIRF'

pprint(results.get_uptime(token, check_id, start="2019-02"))
```

With the output:

``` python
{'2019-02': {'down': 2808090, 'enabled': 2419200000, 'uptime': 99.884},
 '2019-03': {'down': 41679682, 'enabled': 2678398201, 'uptime': 98.444},
 '2019-04': {'down': 4511825, 'enabled': 2592000000, 'uptime': 99.826},
 '2019-05': {'down': 764817, 'enabled': 2678359942, 'uptime': 99.971},
 '2019-06': {'down': 5762929, 'enabled': 2592000000, 'uptime': 99.778},
 '2019-07': {'down': 3585847, 'enabled': 2661778859, 'uptime': 99.865},
 'total': {'down': 59113190, 'enabled': 15621737002, 'uptime': 99.622}}
```

### Getting Daily Uptime In Time Range

You can also get daily results on uptime. In addition to that, you can
specify the start/end dates. In this case, we will start on
2019-07-01 and collect to 2019-07-15

``` python
from nodeping_api import results
from pprint import pprint

token = 'my-api-token
check_id = '201205050153W2Q4C-0J2HSIRF'

start="2019-07-01"
end="2019-07-25"

pprint(results.get_uptime(token, check_id, interval="days", start=start, end=end))
```

With the output:

``` python
{'2019-07-01': {'down': 0, 'enabled': 86400000, 'uptime': 100},
 '2019-07-02': {'down': 0, 'enabled': 86400000, 'uptime': 100},
 '2019-07-03': {'down': 0, 'enabled': 86400000, 'uptime': 100},
 '2019-07-04': {'down': 0, 'enabled': 86400000, 'uptime': 100},
 '2019-07-05': {'down': 140740, 'enabled': 86400000, 'uptime': 99.837},
 '2019-07-06': {'down': 417545, 'enabled': 86400000, 'uptime': 99.517},
 '2019-07-07': {'down': 0, 'enabled': 86400000, 'uptime': 100},
 '2019-07-08': {'down': 144979, 'enabled': 86400000, 'uptime': 99.832},
 '2019-07-09': {'down': 0, 'enabled': 86400000, 'uptime': 100},
 '2019-07-10': {'down': 0, 'enabled': 86400000, 'uptime': 100},
 '2019-07-11': {'down': 0, 'enabled': 86400000, 'uptime': 100},
 '2019-07-12': {'down': 699479, 'enabled': 86400000, 'uptime': 99.19},
 '2019-07-13': {'down': 0, 'enabled': 86400000, 'uptime': 100},
 '2019-07-14': {'down': 0, 'enabled': 86400000, 'uptime': 100},
 'total': {'down': 1402743, 'enabled': 1209600000, 'uptime': 99.884}}
```

Note that all the results you get will also have a total downtime
for that give time range.


### Current Events

Retrieves information about current "events" for checks. Events include down events
and disabled checks. If you need a list of all checks with their passing/failing
state, please use the 'checks' list rather than this 'current' call.

``` python
from nodeping_api import results

token = 'my-api-token

current = results.get_current(token)
```


## Information

Get probe and location information via the `information.py` module.

### Get Probe Info

You can get information about all probes or a specific probe.
This information mirrors what is available on our FAQ:

https://nodeping.com/faq.html#ip-addresses


#### Get NY Probe Info

``` python
from nodeping_api import information
from pprint import pprint

token = 'my-api-token'
probe = "ny"

ny_probe = information.get_probe(token, probe=probe)
```

With the output:

``` python
{'country': 'US',
 'ipv4': '66.23.202.26',
 'ipv6': '2605:9f80:c000:127::2',
 'location': 'ny',
 'locationname': 'New York City, New York',
 'region': 'nam',
 'regionname': 'North America'}
```

### Get Location Information

With this function, you can get all probe information oa
information about probes in a region.

#### Get North America Info

``` python
from nodeping_api import information
from pprint import pprint

token = 'my-api-token'
location = 'nam'

nam_location = information.get_location(token, location=location)

```

With the output:

``` python
{'locations': ['il',
               'tx',
               'nj',
               'ga',
               'ca',
               'co',
               'wa',
               'ny',
               'py',
               'oh',
               'ut',
               'or',
               'fl'],
 'regionname': 'North America'}
```
