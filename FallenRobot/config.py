class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 9774346
    API_HASH = "a92aed7d74654a563af4b07efbcd88e9"

    CASH_API_KEY = "SBG7THOFCOCG9ECV"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "none"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001844573348)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://ZoMusic:Rextor99@zomusic.iabfu0l.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/5355e70d885f0781d7410.jpg"

    SUPPORT_CHAT = "ZOIDsSupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5620597185:AAFeONfKCXg17IUt5nFm7g-LDgAAiOR8C4Q"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "SXB4XEFZEXRV"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 907544310  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = [-1001844573348]  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
