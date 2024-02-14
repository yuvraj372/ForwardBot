from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", 27408009))
    API_HASH = environ.get("API_HASH", "67a4c23a65948a34172e8b79fb40cc9d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6826214775:AAFaj5z3bUBgNRin8oomk_gBIIFYLXP_ZvU") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Postlinksearchbot:yuvraj178@postlinksearchbot.3jxx286.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5882560951').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
