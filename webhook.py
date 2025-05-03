"""
WhatsBot webhook handler
Author: nlarchive
Copyright (c) 2024 - MIT License
"""
from flask import Flask, request, jsonify
import logging
from ai_handler import get_vetbot_response
from whatsapp_handler import send_whatsapp_message
import asyncio
from config import Config

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['GET', 'POST'])
async def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if mode and token:
            if mode == 'subscribe' and token == Config.VERIFY_TOKEN:
                print('WEBHOOK_VERIFIED')
                return challenge, 200
            else:
                return 'Verification token mismatch', 403
    elif request.method == 'POST':
        try:
            data = request.json
            print(data)

            if 'messages' in data['entry'][0]['changes'][0]['value']:
                user_message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
                user_phone = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

                if not user_message or not user_phone:
                    return jsonify({"error": "Missing message or phone"}), 400

                response_message = get_vetbot_response(user_message)
                await send_whatsapp_message(user_phone, response_message)

            elif 'statuses' in data['entry'][0]['changes'][0]['value']:
                print("Status update received.")
                pass

            else:
                logging.warning("Received an unknown webhook type.")
                return jsonify({"error": "Unknown webhook type"}), 400

            return jsonify({"status": "success"}), 200

        except (KeyError, IndexError) as e:
            logging.exception(f"Error extracting data from webhook: {e}")
            return jsonify({"error": "Invalid webhook data format"}), 400
        except Exception as e:
            logging.exception(f"An error occurred in the webhook: {e}")
            return jsonify({"error": "Webhook processing failed"}), 500
