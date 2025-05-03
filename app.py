"""
Main entry point for WhatsBot application
Author: nlarchive
Copyright (c) 2024 - MIT License
"""
import asyncio
from pyngrok import ngrok
from webhook import app
from config import Config

if __name__ == "__main__":
    # Ngrok setup
    ngrok.set_auth_token(Config.NGROK_AUTH_TOKEN)
    public_url = ngrok.connect(5000, bind_tls=True, hostname="curious-monster-amusing.ngrok-free.app")
    print(f"Public URL: {public_url}")

    # Run the Flask app with asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.run())
    loop.close()
