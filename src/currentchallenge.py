from telegram import Update
from telegram.ext import CallbackContext
from src.gsClient import getClient

client = getClient()


def current_challenge(update: Update, context: CallbackContext):
    # Open the used challenges sheet
    sheet = client.open("fitnessbot").get_worksheet(1)

    # Get the last challenge from the sheet
    last_row = len(sheet.get_all_values())
    challenge = sheet.cell(last_row, 1).value

    # Send the challenge to the user
    update.message.reply_text(f"The current challenge is: {challenge}")
