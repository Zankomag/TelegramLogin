from telethon.sync import TelegramClient
from telethon import errors
import sys

api_id = API_ID
api_hash = "API_HASH"
phone = input('Enter phone (+123456789): ')

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except errors.SessionPasswordNeededError:
        client.sign_in(phone, password = input("Enter two-step password: "))
