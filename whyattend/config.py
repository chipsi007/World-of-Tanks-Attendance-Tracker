"""
    Application Configuration
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    This file should be used as a template and overview
    of all available options. Put your local deployment
    settings into local_config.py, which overrides these
    defaults. (see bottom of file)
"""

import datetime

# Set timezone of the server. Europe/Amsterdam for EU cluster.
SERVER_TIMEZONE = 'Europe/Amsterdam'
# List of possible timezones for users to select when creating battles.
USER_TIMEZONES = ('Europe/Amsterdam',
                  'Europe/London',
                  'Europe/Helsinki')

# Database URI (see http://docs.sqlalchemy.org/en/latest/core/engines.html#supported-databases)
DATABASE_URI = 'mysql://user@host/database?charset=utf8&use_unicode=0'  # forces UTF-8 encoding in DB

# Path to temporary folder for OpenID authentication files
OID_STORE_PATH = 'tmp/oid'

# The key is used to sign the session cookies. Set it to some random value, e.g.
# generated by running python -c "import os; print(os.urandom(24))"
SECRET_KEY = ''

# Clan abbreviations
CLAN_NAMES = ['CLAN', 'STRONK']
CLAN_IDS = {
    'CLAN': '23456789',
    'STRONK': '34567890'
}

# Temporary folder for uploaded replays
UPLOAD_FOLDER = 'tmp/uploads'

# Wargaming.net API token and base URL
# API tokens can be generated using the Wargaming Developer Partner program
# The API token should be a "Server" token with the public IP address of your server
# Otherwise Wargaming's API will deny requests from the tracker.
API_URL = 'http://api.worldoftanks.eu/'
API_TOKEN = ''

# WoT Server region code
WOT_SERVER_REGION_CODE = 'eu'

# Key/Password to trigger administrative functions such as clan member synchronization
# via the /sync-players URL (see README).
API_KEY = 'mysecretkey'

# Map WoT API clan roles to displayed name
ROLE_LABELS = {
    "personnel_officer": "Personnel Officer",
    "quartermaster": "Quartermaster",
    "executive_officer": "Executive Officer",
    "recruit": "Recruit",
    "private": "Private",
    "commander": "Commander",
    "reservist": "Reservist",
    "combat_officer": "Combat Officer",
    "recruitment_officer": "Recruitment Officer",
    "intelligence_officer": "Intelligence Officer"
}

# List of player names that can do everything
ADMINS = ['fantastico', ]

# Permission configuration. E.g. let only leader and treasurer create battles.
CREATE_BATTLE_ROLES = ('commander', 'executive_officer', 'quartermaster')
DELETE_BATTLE_ROLES = ('commander', 'executive_officer', 'quartermaster')
PAYOUT_ROLES = ('commander', 'executive_officer', 'quartermaster')
ADMIN_ROLES = ('commander', )
PLAYER_PERFORMANCE_ROLES = ('commander', )
COMMANDED_ROLES = ('commander', 'executive_officer')
DOWNLOAD_REPLAY_ROLES = ('commander', 'personnel_officer', 'executive_officer', 'private',
                         'combat_officer', 'recruitment_officer', 'intelligence_officer', 'quartermaster')

# How long after the battle date should reserves be able to sign in themselves
RESERVE_SIGNUP_DURATION = datetime.timedelta(days=7)
# Allow/disallow signup by players. If disallowed, only members with a position in CREATE_BATTLE_ROLES can do it
RESERVE_SIGNUP_ALLOWED = False

# Should replays be stored in the database?
STORE_REPLAYS_IN_DB = True

# Logfile
ERROR_LOG_FILE = '/tmp/error.log'
LOG_FILE = '/tmp/whyattend.log'

# Celery task queue settings
# See http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#choosing-a-broker
# Currently not really used.
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

# Customize the "Links" menu shown in the tracker
MENU_LINKS = [
    ('Clan Forum', '#forum'),
    ('Global Map', 'http://worldoftanks.eu/clanwars/maps/globalmap/'),
    ('Campaign Map', 'http://worldoftanks.eu/clanwars/eventmap/'),
]

# The URL prefix for the CW map that battle schedule links should lead to,
# The province ID gets appended, e.g. "?province=ML_17"
MAP_URL = "http://worldoftanks.eu/clanwars/maps/globalmap/"

# Subdomain of the CW map Ajax URLs, e.g. "http://cw1.worldoftanks.eu"
# In EU, cw1 is the regular map, cw2 is the campaign map
MAP_SUBDOMAIN = "http://cw1.worldoftanks.eu"
MAP_REGIONS = [1, 2, 3]  # 3 map regions with IDs 1,2,3 in EU

# Enable/disable showing certain statistics in the trackers
STATISTICS_VISIBLE = {
    'win_rate_by_commander': True,
}

# Override settings with local config, if present.
# In the local_config.py the following lines should be removed
try:
    from local_config import *
except ImportError:
    pass
