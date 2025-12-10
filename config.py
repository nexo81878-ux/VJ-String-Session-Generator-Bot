from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "15090477"))
API_HASH = environ.get("API_HASH", "2d81a0d94f0d111339c455a85f60e5c8")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "8524698471:AAEFavlhNg4Nrbibgoesftrwb1_Mr-1G13s")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "1715252294")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://xtrnexo:<db_password>@xtrnexo.b1ioawy.mongodb.net/?appName=xtrnexo")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
