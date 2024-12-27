from os import getenv
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env if available


class Config(object):
    LOGGER = True

    # Basic Configuration
    API_ID = int(getenv("API_ID", 5047271))  # Default to 5047271
    API_HASH = getenv("API_HASH", "047d9ed308172e637d4265e1d9ef0c27")  # Default hash
    DEEP_API = getenv("DEEP_API")
    ARQ_API_KEY = getenv("ARQ_API_KEY", "VNXEHU-FAHIEH-NOIIBS-AXSBTV-ARQ")
    SPAMWATCH_API = getenv("SPAMWATCH_API", "t9HHtrsmy7faPQWloX8xCvdZK~puDP2RnHLpb~qijQqDj94mhcMQdDP_xO0a_Iwe")
    TOKEN = getenv("TOKEN", "7332398186:AAHG5L3MF-8BtP4ouR_9a_T2tBgje_GegN0")
    OWNER_ID = int(getenv("OWNER_ID", "1451534504"))  # Default owner ID
    OWNER_USERNAME = getenv("OWNER_USERNAME", "deweni2")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "hghgjkgjgjk")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002325247996"))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://smoka:smoka@cluster0.hyxdn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = getenv("DB_NAME", "Management")
    REDIS_URL = getenv(
        "REDIS_URL",
        "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default",
    )
    DATABASE_URL = getenv("DATABASE_URL")

    # PostgreSQL Fix
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
