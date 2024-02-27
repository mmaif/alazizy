import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu5Dk0_-bKntee7PDsMBdSWITLJY6600wxf9C3Bp08FdKGvdzhQXQMTOzMKYvIimxY3cbaYTHCxyAss3S5DRdrq5PtHIxbNAc60iYK53_n6_WpoW8uZGLlG2-OGR4wr4de5czPKU7S0GoU4AG6QB29KZeaFMLjcNqOt21siDjmoePam-bbnfvR9m-vpE7E0v8HVQyOMsIjytFmtB_79eOFVou01OM0WiDT4Paz98hajVOuRK41ieDg5iBGdlxfxfOV-5i3eDfHbY-dbPYKFfV1a3oKifOGJU15zW9hB0AlulQElxmx1VKrD5AHxgJMH157VeFaBf0fp83-5Ymf-Ouo_g=")
BOT_TOKEN = getenv("BOT_TOKEN", "6521446876:AAED0jrQQBeV_0t4p8ZEmi4x_x-bmOKTlM0")
BOT_NAME = getenv("BOT_NAME", "Music Kayo")
API_ID = int(getenv("API_ID","6413284591"))
API_HASH = getenv("API_HASH","9f44d9895d05969ffeb75ddf232273fd")
OWNER_NAME = getenv("OWNER_NAME", "MA111Ag")
ALIVE_NAME = getenv("ALIVE_NAME", "Kayo")
BOT_USERNAME = getenv("BOT_USERNAME", "iiooqwbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "zzqtz")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "HHULHL")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "vlolv")
SUDO_USERS = list(map(int, getenv("SUDO_USERS","6413284591").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/06b651dc0d827b6887764.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RAZANALYAFAE/AQANI")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
