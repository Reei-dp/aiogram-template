from aiogram.dispatcher.middlewares.base import BaseMiddleware


class EnvironmentMiddleware(BaseMiddleware):
    def __init__(self, **kwargs):
        super().__init__()
        self.kwargs = kwargs

    async def __call__(self, handler, event, data):
        data.update(**self.kwargs)
        return await handler(event, data)
