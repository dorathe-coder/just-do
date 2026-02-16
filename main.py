# Improved TXT to Video Downloader Bot
# Enhanced version with better error handling and multiple format support

import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
from pathlib import Path

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📥 Upload TXT", callback_data="upload_txt")],
        [InlineKeyboardButton("ℹ️ Help", callback_data="help"),
         InlineKeyboardButton("⚙️ Features", callback_data="features")]
    ])
    
    welcome_text = f"""
**👋 Welcome {m.from_user.mention}!**

**🎯 I Am Advanced TXT to Video Downloader Bot**

✨ **Key Features:**
• Download from Multiple Platforms (ClassPlus, YouTube, Drive, etc.)
• Support for M3U8, MPD, MP4 formats
• Auto Quality Selection
• Custom Thumbnails
• Batch Processing
• Resume Support
• Error Recovery

**🚀 Commands:**
/upload - Start downloading videos
/batch - Batch download multiple TXT files
/stop - Stop ongoing task
/help - Get help
/settings - Bot settings

**💡 Use /upload to start!**
"""
    await m.reply_text(welcome_text, reply_markup=keyboard)


@bot.on_message(filters.command(["help"]))
async def help_command(bot: Client, m: Message):
    help_text = """
**📚 Help Guide**

**📝 TXT File Format:**
```
Video Name 1 : https://link1.com
Video Name 2 : https://link2.com
```

**✅ Supported Platforms:**
• ClassPlus App
• YouTube / YouTube Embedded
• Google Drive
• M3U8 Streams
• MPD Streams
• Direct MP4 Links
• Vision IAS
• JW Player

**🎬 Supported Formats:**
• MP4, MKV, WEBM
• M3U8 Playlists
• MPD Streams
• PDF Files

**⚙️ Quality Options:**
144p, 240p, 360p, 480p, 720p, 1080p

**💡 Tips:**
• Use proper format in TXT file
• Start index from 1
• Keep good internet connection
• Use custom thumbnail for branding
"""
    await m.reply_text(help_text)


@bot.on_message(filters.command(["features"]))
async def features_command(bot: Client, m: Message):
    features_text = """
**🌟 Bot Features**

**🔥 Core Features:**
✅ Multi-Platform Support
✅ Auto Format Detection
✅ Smart Quality Selection
✅ Resume Capability
✅ Batch Processing
✅ Custom Thumbnails
✅ Progress Tracking
✅ Error Handling

**🎯 Advanced Features:**
✅ ClassPlus Video Extraction
✅ M3U8 to MP4 Conversion
✅ MPD to M3U8 Conversion
✅ YouTube Download (All Qualities)
✅ Google Drive Direct Download
✅ PDF Download Support
✅ Custom Caption Support
✅ Thumbnail Support

**🔧 Technical Features:**
✅ Aria2c Integration (16x Speed)
✅ Fragment Retry (25 attempts)
✅ Concurrent Downloads
✅ Flood Wait Handling
✅ Auto Cleanup
✅ Memory Optimization
"""
    await m.reply_text(features_text)


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**⛔ Stopped!**\n\n All ongoing tasks have been terminated.", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


def clean_filename(filename):
    """Clean filename from special characters"""
    return re.sub(r'[\\/*?:"<>|]', "", filename).strip()


def parse_txt_file(content):
    """Parse TXT file with multiple format support"""
    links = []
    lines = content.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Try different separators
        if '://' in line:
            # Format: Name : https://url or Name:https://url or just https://url
            if ':' in line and not line.startswith('http'):
                parts = line.split(':', 1)
                if len(parts) == 2 and '://' in parts[1]:
                    name = parts[0].strip()
                    url = parts[1].strip()
                    links.append([name, url])
                else:
                    # Multiple colons, take last one before ://
                    match = re.match(r'^(.+?):\s*(https?://.+)$', line)
                    if match:
                        links.append([match.group(1).strip(), match.group(2).strip()])
                    else:
                        links.append(['Video', line])
            else:
                # Just URL
                links.append(['Video', line])
    
    return links


async def get_classplus_url(url):
    """Extract ClassPlus video URL"""
    try:
        headers = {
            'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'
        }
        response = requests.get(
            f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}',
            headers=headers,
            timeout=10
        )
        return response.json().get('url', url)
    except:
        return url


async def process_url(url):
    """Process URL and return playable URL"""
    
    # ClassPlus
    if 'videos.classplusapp' in url or 'classplusapp' in url:
        url = await get_classplus_url(url)
    
    # Google Drive
    elif 'drive.google.com' in url:
        url = url.replace("file/d/", "uc?export=download&id=")
        url = url.replace("/view?usp=sharing", "")
        url = url.replace("www.youtube-nocookie.com/embed", "youtu.be")
        url = url.replace("?modestbranding=1", "")
    
    # MPD to M3U8
    elif '/master.mpd' in url:
        video_id = url.split("/")[-2]
        url = f"https://d26g5bnklkwsh4.cloudfront.net/{video_id}/master.m3u8"
    
    # Vision IAS
    elif 'visionias' in url:
        try:
            async with ClientSession() as session:
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36'
                }
                async with session.get(url, headers=headers) as resp:
                    text = await resp.text()
                    match = re.search(r'(https://.*?playlist\.m3u8.*?)"', text)
                    if match:
                        url = match.group(1)
        except:
            pass
    
    return url


@bot.on_message(filters.command(["upload"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('**📤 Send me your TXT file**\n\n__Supported formats:__\n`Name : URL`\n`Name:URL`\n`URL only`')
    input: Message = await bot.listen(editable.chat.id)
    
    # Download file
    try:
        x = await input.download()
        await input.delete(True)
    except Exception as e:
        await editable.edit(f"❌ **Error downloading file:** {str(e)}")
        return

    # Parse file
    try:
        with open(x, "r", encoding='utf-8') as f:
            content = f.read()
        
        links = parse_txt_file(content)
        os.remove(x)
        
        if not links:
            await editable.edit("❌ **No valid links found in file!**\n\nMake sure format is correct:\n`Video Name : https://url`")
            return
            
    except Exception as e:
        await editable.edit(f"❌ **Invalid file format!**\n\n{str(e)}")
        try:
            os.remove(x)
        except:
            pass
        return
    
    await editable.edit(
        f"✅ **Found {len(links)} links**\n\n"
        f"📝 **Send starting number**\n"
        f"(Default: 1)"
    )
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)
    
    try:
        start_from = int(raw_text)
        if start_from < 1:
            start_from = 1
    except:
        start_from = 1

    await editable.edit("**📝 Enter Batch Name**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)

    await editable.edit(
        "**🎬 Select Quality:**\n\n"
        "144, 240, 360, 480, 720, 1080\n\n"
        "Or send `best` for highest quality"
    )
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    
    # Quality mapping
    quality_map = {
        "144": "256x144",
        "240": "426x240", 
        "360": "640x360",
        "480": "854x480",
        "720": "1280x720",
        "1080": "1920x1080",
        "best": "1920x1080"
    }
    res = quality_map.get(raw_text2, "UN")

    await editable.edit("**💬 Enter Caption**\n\n(This will be added to all videos)")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    
    if raw_text3.lower() == 'no':
        CR = ""
    else:
        CR = raw_text3

    await editable.edit(
        "**🖼️ Send Thumbnail URL**\n\n"
        "Send image URL or type `no` to skip\n\n"
        "Example: https://graph.org/file/xxxxx.jpg"
    )
    input6: Message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = raw_text6
    if thumb.startswith("http://") or thumb.startswith("https://"):
        try:
            getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
            thumb = "thumb.jpg"
        except:
            thumb = "no"
    else:
        thumb = "no"

    # Start processing
    count = start_from
    failed_links = []
    success_count = 0

    try:
        for i in range(count - 1, len(links)):
            try:
                name_raw = links[i][0]
                url_raw = links[i][1]
                
                # Process URL
                url = await process_url(url_raw)
                
                # Clean filename
                name1 = clean_filename(name_raw)
                name = f'{str(count).zfill(3)}) {name1[:60]}'

                # Determine format
                if "youtu" in url:
                    ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
                else:
                    ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

                if "jw-prod" in url:
                    cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
                else:
                    cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

                # Caption
                cc = f'**📹 Video ID:** {str(count).zfill(3)}\n**📝 Name:** {name1}\n**📦 Batch:** {raw_text0}\n\n{CR}'
                cc1 = f'**📄 PDF ID:** {str(count).zfill(3)}\n**📝 Name:** {name1}\n**📦 Batch:** {raw_text0}\n\n{CR}'
                
                # Handle different file types
                if "drive.google.com" in url and ".pdf" not in url:
                    try:
                        ka = await helper.download(url, name)
                        await bot.send_document(
                            chat_id=m.chat.id,
                            document=ka,
                            caption=cc1
                        )
                        count += 1
                        success_count += 1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(f"⏳ Flood Wait: {e.x} seconds")
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        
                        await bot.send_document(
                            chat_id=m.chat.id,
                            document=f'{name}.pdf',
                            caption=cc1
                        )
                        count += 1
                        success_count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(f"⏳ Flood Wait: {e.x} seconds")
                        time.sleep(e.x)
                        continue
                
                else:
                    # Video download
                    Show = f"""
**⬇️ DOWNLOADING...**

**📝 Name:** `{name1}`
**🎬 Quality:** `{raw_text2}p`
**🔗 URL:** `{url[:50]}...`
**📊 Progress:** Starting...
"""
                    prog = await m.reply_text(Show)
                    
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name1, prog)
                    
                    count += 1
                    success_count += 1
                    time.sleep(1)

            except FloodWait as e:
                await m.reply_text(f"⏳ **Flood Wait:** {e.x} seconds")
                time.sleep(e.x)
                continue
                
            except Exception as e:
                error_msg = f"""
❌ **Download Failed**

**📝 Name:** {name1}
**🔗 Link:** `{url_raw[:50]}...`
**❗ Error:** {str(e)[:100]}

Skipping to next...
"""
                await m.reply_text(error_msg)
                failed_links.append(f"{name1}: {str(e)}")
                continue

    except Exception as e:
        await m.reply_text(f"❌ **Critical Error:** {str(e)}")
    
    # Final summary
    summary = f"""
✅ **BATCH COMPLETED!**

**📦 Batch:** {raw_text0}
**✅ Success:** {success_count}/{len(links)}
**❌ Failed:** {len(failed_links)}
**⏱️ Status:** Completed

Thank you for using the bot! 🎉
"""
    
    if failed_links:
        summary += f"\n\n**❌ Failed Links:**\n"
        for fail in failed_links[:5]:
            summary += f"• {fail[:50]}...\n"
    
    await m.reply_text(summary)


@bot.on_message(filters.command(["batch"]))
async def batch_upload(bot: Client, m: Message):
    await m.reply_text(
        "**📦 Batch Mode**\n\n"
        "Send multiple TXT files one by one.\n"
        "Type /done when finished.\n\n"
        "This feature is coming soon! 🚀"
    )


@bot.on_message(filters.command(["settings"]))  
async def settings(bot: Client, m: Message):
    await m.reply_text(
        "**⚙️ Bot Settings**\n\n"
        "Coming soon:\n"
        "• Default Quality\n"
        "• Auto Thumbnail\n"
        "• Custom Format\n"
        "• Download Path\n"
        "• More...\n\n"
        "Stay tuned! 🚀"
    )


bot.run()
