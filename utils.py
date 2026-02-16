# Utility functions for bot
# Enhanced progress bar and helper functions

import time
import math
import os
from datetime import datetime, timedelta
from pyrogram.errors import FloodWait


class Timer:
    """Timer class for rate limiting updates"""
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False


def hrb(value, digits=2, delim="", postfix=""):
    """Return a human-readable file size"""
    if value is None:
        return None
    
    chosen_unit = "B"
    for unit in ("KB", "MB", "GB", "TB", "PB"):
        if value > 1024:
            value /= 1024
            chosen_unit = unit
        else:
            break
    
    return f"{value:.{digits}f}{delim}{chosen_unit}{postfix}"


def hrt(seconds, precision=0):
    """Return a human-readable time delta as a string"""
    pieces = []
    value = timedelta(seconds=seconds)
    
    if value.days:
        pieces.append(f"{value.days}d")

    seconds = value.seconds

    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}h")
        seconds -= hours * 3600

    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}m")
        seconds -= minutes * 60

    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}s")

    if not precision:
        return "".join(pieces)

    return "".join(pieces[:precision])


# Global timer instance
timer = Timer()


async def progress_bar(current, total, reply, start):
    """Enhanced progress bar with better visuals"""
    if timer.can_send():
        now = time.time()
        diff = now - start
        
        if diff < 1:
            return
        
        try:
            # Calculate percentage
            perc = f"{current * 100 / total:.1f}%"
            
            # Calculate speed
            elapsed_time = round(diff)
            speed = current / elapsed_time if elapsed_time > 0 else 0
            
            # Calculate ETA
            remaining_bytes = total - current
            if speed > 0:
                eta_seconds = remaining_bytes / speed
                eta = hrt(eta_seconds, precision=1)
            else:
                eta = "-"
            
            # Format values
            sp = str(hrb(speed)) + "/s"
            tot = hrb(total)
            cur = hrb(current)
            
            # Progress bar
            bar_length = 12
            completed_length = int(current * bar_length / total)
            remaining_length = bar_length - completed_length
            progress_bar_visual = "█" * completed_length + "░" * remaining_length
            
            # Create progress text
            progress_text = f"""
**⬆️ UPLOADING...**

╭━━━━━━━━━━━━━━━━━━╮
│ {progress_bar_visual} │ **{perc}**
╰━━━━━━━━━━━━━━━━━━╯

**📊 Status:**
├ 🚀 **Speed:** `{sp}`
├ 📦 **Uploaded:** `{cur}` / `{tot}`
├ ⏱️ **ETA:** `{eta}`
└ ⏳ **Time:** `{hrt(elapsed_time)}`

**🤖 Powered by Advanced Downloader**
"""
            
            await reply.edit(progress_text)
            
        except FloodWait as e:
            time.sleep(e.x)
        except Exception as e:
            print(f"Progress bar error: {e}")


def format_time(seconds):
    """Format seconds into readable time"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    if hours > 0:
        return f"{int(hours)}h {int(minutes)}m {int(secs)}s"
    elif minutes > 0:
        return f"{int(minutes)}m {int(secs)}s"
    else:
        return f"{int(secs)}s"


def estimate_time(current, total, start_time):
    """Estimate remaining time"""
    elapsed = time.time() - start_time
    if current == 0:
        return "Calculating..."
    
    rate = current / elapsed
    remaining = (total - current) / rate
    
    return format_time(int(remaining))


def clean_url(url):
    """Clean and validate URL"""
    url = url.strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url


def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '')
    
    # Remove extra spaces
    filename = ' '.join(filename.split())
    
    # Limit length
    if len(filename) > 200:
        filename = filename[:200]
    
    return filename


def get_file_size(filepath):
    """Get file size in human readable format"""
    try:
        size = os.path.getsize(filepath)
        return hrb(size)
    except:
        return "Unknown"


def create_progress_string(current, total):
    """Create simple progress string"""
    percentage = (current / total) * 100
    filled = int(percentage / 10)
    bar = '█' * filled + '░' * (10 - filled)
    return f"{bar} {percentage:.1f}%"
