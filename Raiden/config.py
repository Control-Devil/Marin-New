
import os
import json

if not __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    sys.exit(1)

def get_user_list(config, key):
    with open("{}/Raiden/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    TOKEN = ""  # Take from @BotFather
    OWNER_ID = (
          # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = ""
    API_HASH = None  # for purge stuffs
    API_ID = None

    # RECOMMENDED
    DB_URL = "awoo" # bsdk apna db daalna
    MESSAGE_DUMP = -1001501815938  # needed to make sure 'save from' messages persist
    REDIS_URL = ""  # needed for afk module, get from redislab
    LOAD = []
    SUPPORT_CHAT = "RaidenXSupport"  # Your own group for support, do not add the @
    NO_LOAD = []
    WEBHOOK = False
    URL = None
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    DEV_USERS = get_user_list("elevated_users.json", "devs") # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = get_user_list("elevated_users.json", "sudos") # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = get_user_list("elevated_users.json", "whitelist")  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DEMONS = get_user_list("elevated_users.json", "demon")
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    SQLALCHEMY_DATABASE_URI = 'something://somewhat:user@hosturl:port/databasename'  # needed for any database modules
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  # banhammer marie sticker
    ALLOW_EXCL = True # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = False  # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = ""  # OpenWeather API
    SPAMWATCH_API = ""  # Your SpamWatch token
    WALL_API = None


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
