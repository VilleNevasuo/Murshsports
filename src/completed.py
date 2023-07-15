import datetime
from telegram import Update
from src.gsClient import getClient
from telegram.ext import CallbackContext
import gspread

client = getClient()


def completed(update: Update, context: CallbackContext):
    username = update.message.from_user.username

    # Open the leaderboard sheet
    sheet = client.open("fitnessbot").sheet1

    # Find the user's row
    try:
        cell = sheet.find(username)
    except gspread.exceptions.CellNotFound:
        update.message.reply_text("You are not in the challenge. Use /join to join.")
        return

    # Increment the user's score
    sheet.update_cell(
        cell.row, cell.col + 1, int(sheet.cell(cell.row, cell.col + 1).value) + 1
    )

    update.message.reply_text("Congratulations on completing the challenge!")
