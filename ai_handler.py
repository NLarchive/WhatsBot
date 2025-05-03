"""
Google Gemini AI integration for WhatsBot
Author: nlarchive
Copyright (c) 2024 - MIT License
"""
import google.generativeai as genai
from config import Config

# Configure Google Generative AI
genai.configure(api_key=Config.GOOGLE_API_KEY)

def get_vetbot_response(user_message):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_message)
    return response.text
