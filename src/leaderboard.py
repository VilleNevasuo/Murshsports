from telegram import Update
from telegram.ext import CallbackContext
from src.gsClient import getClient

client = getClient()


def leaderboard(update: Update, context: CallbackContext):
    # Open the leaderboard sheet
    sheet = client.open("fitnessbot").sheet1

    # Get all records from the sheet
    values = sheet.get_all_values()

    # Sort the records by score in descending order
    leaderboard = sorted(values, key=lambda x: int(x[2]), reverse=True)

    # Format the leaderboard message
    leaderboard_message = "Leaderboard:\n"
    for i, values in enumerate(leaderboard, start=1):
        leaderboard_message += f"{i}. {values[1]}: {values[2]}\n"

    # Send the leaderboard message
    update.message.reply_text(leaderboard_message)
