import os
import random
from dotenv import load_dotenv
from telegram.ext import CallbackContext
from src.gsClient import getClient

load_dotenv()
GROUP_ID = os.getenv("TELEGRAM_GROUP_ID")

client = getClient()


def generate_challenge(context: CallbackContext):
    # Open the challenges sheet
    sheet = client.open("challenges").sheet1

    # Pick a random challenge
    challenge = random.choice(sheet.get_all_values())

    # Move the challenge to the used challenges sheet
    used_challenges_sheet = client.open("used challenges").sheet1
    used_challenges_sheet.append_row([challenge])
    sheet.delete_rows(sheet.find(challenge).row)

    # Announce the new challenge
    context.bot.send_message(
        chat_id=GROUP_ID, text=f"The new challenge is: {challenge}"
    )
