from aiogram.filters import BaseFilter
from src.config import Config

class UserFilter(BaseFilter):
    async def __call__(self, message, event_from_user, bot):
        config: Config = bot['config'] if 'config' in bot else None
        if not config:
            return False
        return event_from_user.id not in config.tg_bot.admin_ids
