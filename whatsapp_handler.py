"""
WhatsApp messaging handler module for WhatsBot
Author: nlarchive
Copyright (c) 2024 - MIT License
"""
import aiohttp
from config import Config

async def send_whatsapp_message(to, text):
    url = f"{Config.API_URL}"
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    headers = {
        'Authorization': f'Bearer {Config.ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            return await response.json()
