from src.config import load_config


async def send_logs_to_admins(message, msg_text):
    config = load_config()
    for admin_id in config.tg_bot.admin_ids:
        await message.bot.send_message(admin_id, msg_text)
