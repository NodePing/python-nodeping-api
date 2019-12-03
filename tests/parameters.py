""" Parameters for tests
"""

TOKEN = ""
CUSTOMERID = ""

FIELDS = {
    "apcupsd": {
        "name": "apcupsd",
        "min": 1, "max": 1
    }, "load1min": {
        "name": "load.1min",
        "min": "0",
        "max": "4"
    }, "load5min": {
        "name": "load.5min",
        "min": "0",
        "max": "2"
    }, "memavail": {
        "name": "memavail",
        "min": "100",
        "max": "10000"
    }
}

CHECK_TYPES = [
    'audio',
    'dns',
    'ftp',
    'httpcontent',
    'push'
]
