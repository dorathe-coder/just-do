# Logging configuration
# Simple logging setup for bot

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def log_download(video_name, status, error=None):
    """Log download activity"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if status == "success":
        logger.info(f"[{timestamp}] ✅ Downloaded: {video_name}")
    elif status == "failed":
        logger.error(f"[{timestamp}] ❌ Failed: {video_name} - Error: {error}")
    elif status == "started":
        logger.info(f"[{timestamp}] 🔄 Starting: {video_name}")

def log_user_action(user_id, username, action):
    """Log user actions"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"[{timestamp}] 👤 User: {username} ({user_id}) - Action: {action}")

def log_error(error_msg):
    """Log errors"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.error(f"[{timestamp}] 🚨 Error: {error_msg}")

def log_info(info_msg):
    """Log information"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"[{timestamp}] ℹ️ Info: {info_msg}")
