from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "24055131"))
API_HASH = getenv("API_HASH", "14e001ad50b6de6e4e411c6b80367125")
BOT_TOKEN = getenv("BOT_TOKEN", "5578917997:AAGaiwLXotQogqB5TWMIID-8U5n6WXVdP9w")
SESSION_NAME = getenv("SESSION_NAME", "AgDS5kwAJqced0KQZYYtPAutTbEortr6JMQJ0YNio9uUio22qHk4B6otHm3KSPp23QXg2lRMEDMCDftwMyPMs086QzjeDzHdYUY8TH9BOieezUWcFid4wkbbDXkZ1I8U3mWpNRNcMHWGUsQ2ohHJXGAQqBvkPK_evMAdhfxumYB6vYhq8_tVNw8nmOAbor4QbEp5luglH8MhSTXiZ5TaTtuBuJFuKtuJrPE8sY1L57_qisbKf3ibf3FN1wAVq481SiVGnN3gAHDPcgaAaU7fyYnt3R0gG4LUFkCZ_ertwQKDfROyOGcs5XMBo1AeRmCAx4F7HhBdQYc2xEK1rj4smQ3agUj-jwAAAAE2wM0eAA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "LLL7P")
ALIVE_NAME = getenv("ALIVE_NAME", "ToBy")
BOT_USERNAME = getenv("BOT_USERNAME", "RLRLBOT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/LLL7P/fede")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ZZZZ7LZ")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RRRJ6")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5072874938").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5072874938").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
