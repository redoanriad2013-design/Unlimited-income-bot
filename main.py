
import logging
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📝 কাজ ▸", "💵 ব্যালেন্স"],
        ["💰 টাকা উত্তোলন", "🎁 My Referrals"],
        ["🎭 সাপোর্ট", "👶 আমি নতুন"],
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, persistent=True
    )

    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"হ্যালো {user_name}! 👋\nআমাদের বোর্ডে স্বাগতম। নিচের অপশনগুলো থেকে সিলেক্ট করুন:",
        reply_markup=reply_markup,
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📝 কাজ ▸":
        sub_keyboard = [
            ["📧 Gmail কাজ >", "💬 WhatsApp কাজ"],
            ["📱 anymail/Number", "🔙 ফিরে যান"],
        ]
        reply_markup = ReplyKeyboardMarkup(sub_keyboard, resize_keyboard=True)
        await update.message.reply_text(
            "সিলেক্ট করুন:", reply_markup=reply_markup
        )

    elif text == "📧 Gmail কাজ >":
        await update.message.reply_text("📧 Gmail সংক্রান্ত কাজের নিয়ম ও লিংক।")

    elif text == "💬 WhatsApp কাজ":
        await update.message.reply_text(
            "💬 WhatsApp সংক্রান্ত কাজের বিস্তারিত।"
        )

    elif text == "💵 ব্যালেন্স":
        await update.message.reply_text("💰 আপনার বর্তমান ব্যালেন্স: ৳ 0.00")

    elif text == "💰 টাকা উত্তোলন":
        await update.message.reply_text(
            "🏧 টাকা তোলার মাধ্যম:\n1. বিকাশ\n2. নগদ\n3"
        )

    elif text == "🎁 My Referrals":
        user_id = update.effective_user.id
        await update.message.reply_text(
            f"🔗 আপনার রেফারেল লিংক:\nhttps://t.me/{context.bot.username}?start={user_id}"
        )

    elif text == "🎭 সাপোর্ট":
        await update.message.reply_text(
            "📞 সাহায্যের জন্য যোগাযোগ করুন: @redoan768"
        )

    elif text == "👶 আমি নতুন":
        await update.message.reply_text("📖 নিয়ম দেখতে হেল্প ভিডিও দেখুন।")

    elif text == "🔙 ফিরে যান":
        await start(update, context)


def main():
    # '8839815804:AAE5g57VNnvNE0gK_Ii5INqcGIVCBbRTKL0' 
    app = Application.builder().token("8839815804:AAE5g57VNnvNE0gK_Ii5INqcGIVCBbRTKL0").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
                
