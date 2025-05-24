# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Rkn_Bots(object):
    
    # Rkn client config  ( required.. 😥)
    API_ID = os.environ.get("API_ID", "21185801")
    API_HASH = os.environ.get("API_HASH", "4235ef431f138309cb9f56ae179a24ba")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7953686463:AAH93rdtUOwKdqL3oKwl8VU_WkdBkrOH3yc")

    # start_pic
    RKN_PIC = os.environ.get("RKN_PIC", "https://envs.sh/sLE.jpg")

    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))

    # force subs channel ( required.. 😥)
    FORCE_SUB = os.environ.get("FORCE_SUB", "DEVILxAIRDROP") 
    
    # database config ( required.. 😥)
    DB_NAME = os.environ.get("DB_NAME", "AutoCaption_V05_Bot")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://6ijziglmyz:EdlupMESij8BXWh5@cluster0.lv5i1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # default caption 
    DEF_CAP = os.environ.get("DEF_CAP", "<b><a href='https://t.me/DEMANDxMOVIES'>{file_name} Main Telegram Channel: @BOTxUPDATE</a></b>",
    )

    # sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "CAACAgIAAxkBAAELFqBllhB70i13m-woXeIWDXU6BD2j7wAC9gcAAkb7rAR7xdjVOS5ziTQE")

    # admin id  ( required.. 😥)
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7057341064').split()]
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
