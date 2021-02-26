from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= ""
    APP_ID = 
    API_HASH = ""
    OWNER_ID = 
    AUTH_CHANNEL = []
    INDEX_LINK = ""
    DESTINATION_FOLDER = "" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """xxxxxxxxxx"""
    UPLOAD_AS_DOC = "True" #True if want upload as document,False if want upload to streaming for video only
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
