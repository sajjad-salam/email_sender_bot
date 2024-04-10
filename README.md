# Email Sending Telegram Bot

This Telegram bot script allows you to send emails via Telegram. You can configure the sender's email, password, recipient's email, subject, message, interval between messages, and the number of messages to be sent.

## Requirements

- Python 3.x
- telebot
- smtplib
## Configuration & RUNING
0. Install the required packages by running `pip install -r requirements.txt`
1. Set up a Telegram bot and obtain the bot token.
2. Replace `'توكنك'` with your bot token. in line 51 in `main.py`.
3. Customize the allowed users by adding their user IDs to the `allowed_users` list. in line 76 in `main.py`
4. now just run the bot by `python main.py`

## Usage

1. Start the bot.
2. Use the provided buttons to add recipients, senders, set email subject and message, set interval, set message count, and start sending emails.
3. The bot will send emails according to the configured settings.

## Important Notes

- Make sure to keep your email credentials secure.
- Use this bot responsibly and ensure compliance with email service provider policies.
- Error handling is implemented to handle potential issues during the email sending process.
- Make sure your Telegram bot is set up to handle commands and callback queries.

## Contributors

- [Your Name](https://github.com/sajjad-salam)

Feel free to contribute, report issues, or suggest improvements by creating a pull request or opening an issue on GitHub.

