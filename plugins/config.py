import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    API_ID = int(os.environ.get("API_ID", "21740783"))
    
    API_HASH = os.environ.get("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Speedwolf1:speedwolf24689@cluster0.rgfywsf.mongodb.net/")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002234974607"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "6299192020"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Awt_url_bot")
                                  
