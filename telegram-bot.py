import json
from flask import Flask, request
from telegram import Bot
import asyncio
import os

# Initialize Flask app for webhook
app = Flask(__name__)

# Telegram bot configuration
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 7750990228:AAEDVqsYO5lqYmBsnUp-2ETOHbxLFAnuoVY)
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 5920415808)
bot = Bot(token=TELEGRAM_TOKEN)

# Webhook endpoint to receive Grafana alerts
@app.route('/webhook', methods=['POST'])
async def webhook():
    try:
        # Get JSON data from Grafana alert
        alert_data = request.get_json()
        if not alert_data:
            return 'No data received', 400

        # Extract alert details
        state = alert_data.get('state', 'unknown')
        title = alert_data.get('title', 'No title')
        message = alert_data.get('message', 'No message')
        rule_name = alert_data.get('ruleName', 'Unknown rule')
        eval_matches = alert_data.get('evalMatches', [])

        # Format the alert message
        alert_message = f"🚨 *Grafana Alert: {title}*\n"
        alert_message += f"State: {state.upper()}\n"
        alert_message += f"Rule: {rule_name}\n"
        alert_message += f"Message: {message}\n"
        if eval_matches:
            alert_message += "\n*Metrics:*\n"
            for match in eval_matches:
                metric = match.get('metric', 'unknown')
                value = match.get('value', 'unknown')
                alert_message += f"- {metric}: {value}\n"

        # Send message to Telegram
        await bot.send_message(
            chat_id=CHAT_ID,
            text=alert_message,
            parse_mode='Markdown'
        )
        return 'Alert sent', 200

    except Exception as e:
        print(f"Error processing webhook: {e}")
        return f"Error: {e}", 500

# Health check endpoint
@app.route('/')
def health():
    return 'Telegram bot is running', 200

if __name__ == '__main__':
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)