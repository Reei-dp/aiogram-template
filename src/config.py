import configparser
from dataclasses import dataclass
from pathlib import Path


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot


def load_config(config_path: Path | None = None) -> Config:
    """
    Load configuration from config.ini file.
    
    Args:
        config_path: Path to config.ini file. If None, looks for config.ini in project root.
    
    Returns:
        Config object with bot token and admin IDs (empty list if no admins specified).
    
    Raises:
        FileNotFoundError: If config.ini file is not found.
        ValueError: If required configuration values are missing or invalid.
    """
    if config_path is None:
        config_path = Path(__file__).parent.parent / "config.ini"
    
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    parser = configparser.ConfigParser()
    parser.read(config_path, encoding='utf-8')
    
    if 'bot' not in parser:
        raise ValueError("Section [bot] not found in config.ini")
    
    bot_section = parser['bot']
    
    token = bot_section.get('token')
    if not token:
        raise ValueError("bot.token is required in config.ini")
    
    admin_ids_str = bot_section.get('admin_ids', '').strip()
    admin_ids = []
    
    if admin_ids_str:
        try:
            admin_ids = [int(x.strip()) for x in admin_ids_str.split(',') if x.strip()]
        except ValueError as e:
            raise ValueError(
                f"Invalid admin_ids format in config.ini: {e}. "
                "Expected comma-separated integers, e.g., admin_ids = 123456789, 987654321"
            )
    
    return Config(
        tg_bot=TgBot(
            token=token,
            admin_ids=admin_ids
        )
    )
