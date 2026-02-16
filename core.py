# Core functions for video downloading and processing
# Enhanced with better error handling and retry logic

import os
import time
import datetime
import aiohttp
import aiofiles
import asyncio
import logging
import requests
import tgcrypto
import subprocess
import concurrent.futures

from utils import progress_bar
from pyrogram import Client
from pyrogram.types import Message

# Global retry counter
failed_counter = 0

def duration(filename):
    """Get video duration using ffprobe"""
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries",
             "format=duration", "-of",
             "default=noprint_wrappers=1:nokey=1", filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30
        )
        return float(result.stdout)
    except:
        return 0
    

def exec(cmd):
    """Execute shell command"""
    try:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.stdout.decode()
        print(output)
        return output
    except Exception as e:
        print(f"Error executing command: {e}")
        return ""


def pull_run(work, cmds):
    """Execute multiple commands concurrently"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:
        print("Waiting for tasks to complete")
        fut = executor.map(exec, cmds)


async def aio(url, name):
    """Async download for PDFs"""
    k = f'{name}.pdf'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=300)) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(k, mode='wb')
                    await f.write(await resp.read())
                    await f.close()
                    return k
                else:
                    return None
    except Exception as e:
        print(f"Download error: {e}")
        return None


async def download(url, name):
    """Download file (mainly for PDFs)"""
    ka = f'{name}.pdf'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=300)) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(ka, mode='wb')
                    await f.write(await resp.read())
                    await f.close()
                    return ka
                else:
                    print(f"Download failed with status: {resp.status}")
                    return None
    except Exception as e:
        print(f"Download error: {e}")
        return None


def parse_vid_info(info):
    """Parse video info from yt-dlp"""
    info = info.strip()
    info = info.split("\n")
    new_info = []
    temp = []
    
    for i in info:
        i = str(i)
        if "[" not in i and '---' not in i:
            while "  " in i:
                i = i.replace("  ", " ")
            i = i.strip()
            i = i.split("|")[0].split(" ", 2)
            try:
                if len(i) > 2 and "RESOLUTION" not in i[2] and i[2] not in temp and "audio" not in i[2]:
                    temp.append(i[2])
                    new_info.append((i[0], i[2]))
            except:
                pass
    
    return new_info


def vid_info(info):
    """Get video format info"""
    info = info.strip()
    info = info.split("\n")
    new_info = dict()
    temp = []
    
    for i in info:
        i = str(i)
        if "[" not in i and '---' not in i:
            while "  " in i:
                i = i.replace("  ", " ")
            i = i.strip()
            i = i.split("|")[0].split(" ", 3)
            try:
                if len(i) > 2 and "RESOLUTION" not in i[2] and i[2] not in temp and "audio" not in i[2]:
                    temp.append(i[2])
                    new_info.update({f'{i[2]}': f'{i[0]}'})
            except:
                pass
    
    return new_info


async def run(cmd):
    """Run async subprocess"""
    try:
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await proc.communicate()

        print(f'[{cmd!r} exited with {proc.returncode}]')
        
        if proc.returncode == 1:
            return False
        if stdout:
            return f'[stdout]\n{stdout.decode()}'
        if stderr:
            return f'[stderr]\n{stderr.decode()}'
    except Exception as e:
        print(f"Process error: {e}")
        return False


def old_download(url, file_name, chunk_size=1024 * 10):
    """Legacy download function"""
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
        
        r = requests.get(url, allow_redirects=True, stream=True, timeout=60)
        with open(file_name, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:
                    fd.write(chunk)
        return file_name
    except Exception as e:
        print(f"Download error: {e}")
        return None


def human_readable_size(size, decimal_places=2):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024.0 or unit == 'PB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


def time_name():
    """Generate timestamp filename"""
    date = datetime.date.today()
    now = datetime.datetime.now()
    current_time = now.strftime("%H%M%S")
    return f"{date} {current_time}.mp4"


async def download_video(url, cmd, name):
    """Download video with retry logic"""
    download_cmd = f'{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args "aria2c: -x 16 -j 32"'
    
    global failed_counter
    print(f"Download command: {download_cmd}")
    logging.info(download_cmd)
    
    try:
        k = subprocess.run(download_cmd, shell=True)
        
        # Retry logic for visionias
        if "visionias" in cmd and k.returncode != 0 and failed_counter <= 10:
            failed_counter += 1
            await asyncio.sleep(5)
            return await download_video(url, cmd, name)
        
        failed_counter = 0
        
        # Find downloaded file
        possible_files = [
            name,
            f"{name}.webm",
            f"{name.rsplit('.', 1)[0]}.mkv",
            f"{name.rsplit('.', 1)[0]}.mp4",
            f"{name}.mp4.webm"
        ]
        
        for file in possible_files:
            if os.path.isfile(file):
                return file
        
        # If no file found, return name
        return name
        
    except Exception as e:
        print(f"Download failed: {e}")
        return name


async def send_doc(bot: Client, m: Message, cc, ka, cc1, prog, count, name):
    """Send document to user"""
    try:
        reply = await m.reply_text(f"⬆️ **Uploading** » `{name}`")
        time.sleep(1)
        
        start_time = time.time()
        await m.reply_document(ka, caption=cc1)
        
        count += 1
        await reply.delete(True)
        
        time.sleep(1)
        os.remove(ka)
        time.sleep(3)
        
    except Exception as e:
        print(f"Document send error: {e}")


async def send_vid(bot: Client, m: Message, cc, filename, thumb, name, prog):
    """Send video to user with progress"""
    
    try:
        # Generate thumbnail
        subprocess.run(
            f'ffmpeg -i "{filename}" -ss 00:00:12 -vframes 1 "{filename}.jpg"',
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        await prog.delete(True)
        reply = await m.reply_text(f"⬆️ **Uploading...** - `{name}`")
        
        # Select thumbnail
        try:
            if thumb == "no" or not os.path.exists(thumb):
                thumbnail = f"{filename}.jpg" if os.path.exists(f"{filename}.jpg") else None
            else:
                thumbnail = thumb
        except:
            thumbnail = f"{filename}.jpg" if os.path.exists(f"{filename}.jpg") else None

        # Get duration
        dur = int(duration(filename))
        if dur == 0:
            dur = 1

        start_time = time.time()

        # Try to send as video
        try:
            await m.reply_video(
                filename,
                caption=cc,
                supports_streaming=True,
                height=720,
                width=1280,
                thumb=thumbnail,
                duration=dur,
                progress=progress_bar,
                progress_args=(reply, start_time)
            )
        except Exception as video_error:
            print(f"Video send failed, trying as document: {video_error}")
            # Fallback to document
            await m.reply_document(
                filename,
                caption=cc,
                progress=progress_bar,
                progress_args=(reply, start_time)
            )

        # Cleanup
        if os.path.exists(filename):
            os.remove(filename)
        
        if os.path.exists(f"{filename}.jpg"):
            os.remove(f"{filename}.jpg")
        
        await reply.delete(True)
        
    except Exception as e:
        print(f"Send video error: {e}")
        await m.reply_text(f"❌ **Upload failed:** {str(e)}")
        
        # Cleanup on error
        try:
            if os.path.exists(filename):
                os.remove(filename)
            if os.path.exists(f"{filename}.jpg"):
                os.remove(f"{filename}.jpg")
        except:
            pass


def cleanup_files(pattern="*.mp4"):
    """Clean up downloaded files"""
    import glob
    for file in glob.glob(pattern):
        try:
            os.remove(file)
        except:
            pass
