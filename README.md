# Aiogram Template

A clean and structured template project for building Telegram bots using [aiogram](https://docs.aiogram.dev/) framework (version 3.21+).

## Features

- 🏗️ **Clean Architecture** - Well-organized project structure with separation of concerns
- 🔧 **Configuration Management** - Easy configuration through INI files
- 🎯 **Filter System** - Built-in user filtering (admin/non-admin)
- 🎨 **Keyboard Support** - Ready-to-use keyboard utilities (inline and reply)
- 📊 **Middleware Support** - Environment middleware for dependency injection
- 📝 **Logging** - Structured logging with admin notification utilities
- 🔄 **State Management** - FSM (Finite State Machine) support for conversation flows

## Project Structure

```
aiogram-template/
├── config.ini.example          # Example configuration file
├── requirements.txt            # Python dependencies
├── LICENSE                     # License file
├── README.md                   # This file
└── src/
    ├── __init__.py
    ├── main.py                 # Application entry point
    ├── config.py               # Configuration loader
    ├── filters/                # Custom filters
    │   ├── __init__.py
    │   └── user.py             # User filter (admin/non-admin)
    ├── handlers/               # Message and callback handlers
    │   ├── __init__.py
    │   └── user.py             # User-related handlers
    ├── keyboards/              # Keyboard builders
    │   ├── __init__.py
    │   ├── reply.py            # Reply keyboard utilities
    │   └── user/               # User-specific keyboards
    │       ├── __init__.py
    │       ├── inline.py       # Inline keyboard builders
    │       ├── reply.py        # Reply keyboard builders
    │       └── util.py         # Keyboard utilities
    ├── middlewares/            # Custom middlewares
    │   ├── __init__.py
    │   └── environment.py      # Environment middleware for DI
    ├── misc/                   # Miscellaneous utilities
    │   ├── __init__.py
    │   ├── logs.py             # Logging utilities
    │   ├── singleton.py        # Singleton pattern implementation
    │   └── states.py           # FSM state definitions
    ├── models/                 # Data models
    │   └── __init__.py
    └── services/               # External service integrations
        └── __init__.py
```

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd aiogram-template
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the bot:
```bash
cp config.ini.example config.ini
```

Edit `config.ini` and add your bot token and admin IDs:
```ini
[bot]
token = your_bot_token_here
admin_ids = 123456789, 987654321
```

To get a bot token:
1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow the instructions
3. Copy the token provided by BotFather

To find your admin user ID:
1. Search for [@userinfobot](https://t.me/userinfobot) on Telegram
2. Start a conversation and it will show your user ID
3. Add multiple admin IDs separated by commas

## Configuration

The project uses an INI file for configuration. Create a `config.ini` file in the project root:

```ini
[bot]
token = your_bot_token_here
admin_ids = 123456789, 987654321
```

### Configuration Options

- `token` (required): Your Telegram bot token obtained from BotFather
- `admin_ids` (optional): Comma-separated list of Telegram user IDs that should have admin privileges

## Usage

### Running the Bot

Start the bot with:
```bash
python -m src.main
```

Or:
```bash
python src/main.py
```

The bot will start polling for updates from Telegram.

### Creating Handlers

Add new handlers in the `src/handlers/` directory:

```python
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Hello! Welcome to the bot.")
```

Then register the router in `src/main.py`:
```python
from src.handlers.your_handler import router as your_router

dp.include_router(your_router)
```

### Using Filters

The template includes a `UserFilter` that can be used to restrict handlers to non-admin users:

```python
from src.filters.user import UserFilter

@router.message(Command("user_command"), UserFilter())
async def user_only_handler(message: Message):
    await message.answer("This command is available only to regular users.")
```

The `UserFilter` returns `True` if the user is not an admin, allowing you to filter out admin users from specific handlers.

### Adding Middlewares

Use the `EnvironmentMiddleware` to inject dependencies into handlers:

```python
from src.middlewares.environment import EnvironmentMiddleware

config = load_config()
dp.message.middleware(EnvironmentMiddleware(config=config))
```

Access injected data in handlers through the `data` parameter:
```python
async def handler(message: Message, data: dict):
    config = data['config']
```

## Development

### Code Structure Guidelines

- **Handlers**: Place all message and callback handlers in `src/handlers/`
- **Filters**: Create custom filters in `src/filters/`
- **Keyboards**: Build keyboard layouts in `src/keyboards/`
- **Services**: Add external service integrations in `src/services/`
- **Models**: Define data models in `src/models/`

### Adding Dependencies

Add new Python packages to `requirements.txt`:
```txt
aiogram~=3.21
your-package==1.0.0
```

Then install:
```bash
pip install -r requirements.txt
```

## Features Explained

### User Filter

The `UserFilter` class checks if a user is not an admin. It accesses the configuration from the bot's data dictionary and compares the user's ID against the admin IDs list.

### Environment Middleware

The `EnvironmentMiddleware` allows you to inject dependencies (like configuration, database connections, etc.) into all handlers without explicitly passing them.

### Logging Utilities

The `send_logs_to_admins` function in `src/misc/logs.py` can be used to send log messages to all configured admin users.

### Singleton Pattern

A singleton metaclass is available in `src/misc/singleton.py` for creating singleton classes when needed.

## Troubleshooting

### Bot doesn't start

- Verify `config.ini` exists and contains a valid token
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Ensure the bot token is correct and hasn't been revoked

### Admin filter not working

- Verify admin IDs are correctly formatted in `config.ini` (comma-separated integers)
- Check that the configuration is properly loaded and injected via middleware

### Import errors

- Make sure you're running from the project root directory
- Verify your Python path includes the project root
- Check that all `__init__.py` files are present in package directories

## License

See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Resources

- [Aiogram Documentation](https://docs.aiogram.dev/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Python Documentation](https://docs.python.org/3/)

## Support

For issues, questions, or contributions, please open an issue on the repository.

