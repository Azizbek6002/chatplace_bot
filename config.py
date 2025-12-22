import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS").split(','))) if os.getenv("ADMIN_IDS") else []

STATS_CONFIG = {
    'default_period': 'monthly',  # monthly, weekly, daily
    'currency': 'so\'m',
    'currency_symbol': 'UZS',
    'default_graph_type': 'bar',  # bar, line, pie
    'max_rooms_per_floor': 22,
    'total_floors': 5,
    'monthly_fee': 2500000  # Oylik to'lov miqdori
}


# config.py fayliga quyidagilarni qo'shing:

# Asosiy sozlamalar
DEFAULT_LANGUAGE = 'uz'
BOT_NAME = "Yotoqxona Bot"
BOT_USERNAME = ""  # Bot username

# To'lov sozlamalari
MONTHLY_PAYMENT_AMOUNT = 250000  # Oylik to'lov summasi
CURRENCY = "so'm"
LATE_PAYMENT_FINE = 1  # Kechna to'lov jarimasi

# Vaqt sozlamalari
PAYMENT_DEADLINE_DAY = 10  # Oyning qaysi kunigacha to'lash kerak
NOTIFICATION_TIME = "09:00"  # Kundalik bildirishnoma vaqti

# Xavfsizlik sozlamalari
MAX_LOGIN_ATTEMPTS = 5
SESSION_TIMEOUT = 3600  # 1 soat
PASSWORD_MIN_LENGTH = 6

# Bildirishnoma sozlamalari
ENABLE_NOTIFICATIONS = True
SEND_TO_ALL = False
SEND_TO_ADMINS = True
SEND_TO_USERS = False

# Database sozlamalari
BACKUP_DIR = "backups/"
BACKUP_INTERVAL = 86400  # 24 soat
MAX_BACKUP_FILES = 30