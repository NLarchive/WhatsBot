# WhatsBot

A WhatsApp bot that uses Google's Gemini AI to respond to messages sent to your WhatsApp Business account.

**Author: nlarchive**  
**Copyright (c) 2024 - MIT License**

## Features

- Connects to WhatsApp Business API via webhooks
- Processes incoming messages
- Generates AI-powered responses using Google's Gemini-Pro model
- Sends responses back to users via WhatsApp
- Uses ngrok to expose your local server to the internet

## Prerequisites

- Python 3.11+
- WhatsApp Business Account
- Meta Developer Account
- Google AI API key (for Gemini)
- Ngrok account

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/NLarchive/WhatsBot.git
   cd WhatsBot
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv whatsbot
   source whatsbot/bin/activate  # On Windows: whatsbot\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following variables:
   ```
   ACCESS_TOKEN=your_meta_whatsapp_access_token
   VERIFY_TOKEN=your_custom_webhook_verification_token
   GOOGLE_API_KEY=your_google_ai_api_key
   NGROK_AUTH_TOKEN=your_ngrok_auth_token
   ```

## Configuration

Update the `config.py` file with your specific details if needed:
- `API_URL`: WhatsApp API endpoint
- `PHONE_NUMBER_ID`: Your WhatsApp Business phone number ID
- `VERSION`: WhatsApp API version

## Setup WhatsApp Business API

1. Create a Meta for Developers account at https://developers.facebook.com/
2. Set up a WhatsApp Business app in the Meta for Developers dashboard
3. Configure the Webhooks in the Meta dashboard:
   - Callback URL: Your ngrok URL + "/webhook" (e.g., https://your-ngrok-domain.ngrok-free.app/webhook)
   - Verify Token: Same value as your VERIFY_TOKEN in the .env file
   - Subscribe to the "messages" field

## Usage

1. Start the application:
   ```
   python app.py
   ```

2. The application will start a Flask server on port 5000 and create an ngrok tunnel.
3. Copy the ngrok URL (displayed in the console) and set it as your webhook URL in the Meta Developer Dashboard.
4. Messages sent to your WhatsApp Business number will now be processed by your bot and receive AI-generated responses.

## Project Structure

- `app.py`: Main application entry point
- `webhook.py`: Handles webhook requests from WhatsApp
- `whatsapp_handler.py`: Manages sending messages via WhatsApp API
- `ai_handler.py`: Processes messages using Google's Gemini AI
- `config.py`: Configuration settings

## Security Notes

- Never commit your .env file or secrets to version control
- Rotate your access tokens regularly
- Use environment variables for all sensitive credentials

## License

MIT

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements.