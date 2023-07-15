from telegram.ext import Updater, CommandHandler, JobQueue
from dotenv import load_dotenv
import os
from src.completed import completed
from src.generator import generate_challenge
from src.gsClient import getClient
from src.join import join
from src.leaderboard import leaderboard
from src.currentchallenge import current_challenge

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
client = getClient()


def main():
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("join", join))
    dp.add_handler(CommandHandler("completed", completed))
    dp.add_handler(CommandHandler("leaderboard", leaderboard))
    dp.add_handler(CommandHandler("challenge", current_challenge))

    updater.start_polling()

    updater.idle()

    job_queue = JobQueue()
    job_queue.run_repeating(generate_challenge, interval=604800)  # Run every week


if __name__ == "__main__":
    main()
