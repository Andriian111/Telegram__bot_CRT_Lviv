import os
BOT_TOKEN = '1504636935:AAFjWRcbFHxUaOCtv2XqPik2D3Cg6EIdnQA'
admin_id = '510598948'
ip='local'
BLOCKCYPHER='4907cb3eab25074096143afdb46f7964'
qiwi='715e2d4f5f521471f580d5964b7cf503'
wallet=+79761718773


# from .env import load_dotenv

# load_dotenv()

admins = [
    510598948
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}