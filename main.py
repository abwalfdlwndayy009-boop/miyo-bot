from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

TOKEN = "8967421113:AAG8-DXwN82dx-gfVJxTBxC9iSMJWR_jW5k"
GROUP_ID = -1002070178350

async def send_miyo(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=GROUP_ID, text="میو")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات فعاله!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.job_queue.run_repeating(send_miyo, interval=360, first=10)
    app.run_polling()

if __name__ == "__main__":
    main()
