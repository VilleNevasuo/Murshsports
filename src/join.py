from telegram import Update
from telegram.ext import CallbackContext
import gspread

from src.gsClient import getClient

client = getClient()


def join(update: Update, context: CallbackContext):
    username = update.message.from_user.username
    id: str = str(update.message.from_user.id)

    # Open the leaderboard sheet
    sheet = client.open("fitnessbot").sheet1

    # Check if the user is already in the leaderboard
    try:
        sheet.find(id)
        update.message.reply_text("You have already joined the challenge!")
    except gspread.exceptions.CellNotFound:
        # If not, add the user to the leaderboard
        sheet.append_row([id, username, "0"])
        update.message.reply_text("You have been added to the challenge! Good luck!")
