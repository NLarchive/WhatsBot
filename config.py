"""
Configuration module for WhatsBot
Author: nlarchive
Copyright (c) 2024 - MIT License
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    API_URL = os.getenv("API_URL")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    VERSION = os.getenv("VERSION")
    PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")
