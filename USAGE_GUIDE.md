# 📖 Complete Usage Guide

## 🎯 Quick Start

### Step 1: Setup
1. Get your Telegram credentials from https://my.telegram.org
2. Create a bot using @BotFather on Telegram
3. Edit `vars.py` with your credentials
4. Install dependencies: `pip install -r requirements.txt`
5. Install ffmpeg and aria2c on your system

### Step 2: Run Bot
```bash
python main.py
```

### Step 3: Use Bot
1. Open bot in Telegram
2. Send `/upload`
3. Upload TXT file
4. Follow prompts
5. Get your videos!

---

## 📝 TXT File Examples

### Example 1: Basic Format
```
Introduction to Python : https://example.com/video1.m3u8
Variables and Data Types : https://example.com/video2.mp4
Functions in Python : https://example.com/video3.mp4
```

### Example 2: ClassPlus Links
```
Lecture 1 : https://videos.classplusapp.com/xxxx/video.m3u8
Lecture 2 : https://videos.classplusapp.com/yyyy/video.m3u8
```

### Example 3: YouTube Links
```
Tutorial Part 1 : https://youtube.com/watch?v=xxxxx
Tutorial Part 2 : https://youtu.be/yyyyy
```

### Example 4: Google Drive
```
Notes PDF : https://drive.google.com/file/d/xxxxx/view
Video Lecture : https://drive.google.com/file/d/yyyyy/view
```

### Example 5: Mixed Sources
```
Intro Video : https://youtube.com/watch?v=xxxxx
Class Notes : https://drive.google.com/file/d/yyyyy
Live Class Recording : https://videos.classplusapp.com/zzzzz/video.m3u8
```

---

## 🎬 Quality Selection Guide

| Quality | Resolution | Best For | File Size |
|---------|-----------|----------|-----------|
| 144p | 256x144 | Preview only | Smallest |
| 240p | 426x240 | Very slow internet | Very small |
| 360p | 640x360 | Mobile viewing | Small |
| 480p | 854x480 | Mobile/Tablet | Medium |
| **720p** | 1280x720 | **Recommended** | **Balanced** |
| 1080p | 1920x1080 | HD viewing | Large |

**💡 Recommendation:** Use 720p for best quality-size balance

---

## 🖼️ Thumbnail Guide

### Valid Thumbnail URLs
✅ `https://graph.org/file/xxxxx.jpg`
✅ `https://i.imgur.com/xxxxx.png`
✅ `https://example.com/image.jpg`

### Invalid Formats
❌ `graph.org/file/xxxxx.jpg` (missing https://)
❌ `https://drive.google.com/...` (not direct link)
❌ Local file paths

### How to Get Thumbnail URL
1. Upload image to https://telegra.ph/
2. Right-click image → Copy image address
3. Use that URL in bot

Or use: `no` to skip thumbnail

---

## 💬 Caption Examples

### Example 1: Simple
```
Downloaded by Advanced Bot
```

### Example 2: Detailed
```
📚 Course: Python Masterclass
👨‍🏫 Instructor: John Doe
🎓 Quality: 720p HD

Join @YourChannel for more!
```

### Example 3: With Emojis
```
🎬 Video Lecture
📅 Date: 2024
⭐ Premium Content
```

Or use: `no` for default caption

---

## 🔧 Troubleshooting

### Issue: "No valid links found"

**Cause:** Incorrect TXT format

**Solution:**
- Check format: `Name : URL`
- Ensure UTF-8 encoding
- No extra spaces before/after
- Each link on new line

### Issue: "Download failed"

**Cause:** Invalid URL or network issue

**Solution:**
- Test URL in browser
- Check internet connection
- Try different quality
- Check if platform is supported

### Issue: "Could not convert string to float"

**Cause:** Old version bug

**Solution:**
- Use this updated version
- Error is fixed in new code

### Issue: "Upload failed"

**Cause:** File too large or telegram issue

**Solution:**
- Check file size (max 2GB)
- Wait and retry
- Check bot permissions

### Issue: "Thumbnail error"

**Cause:** Invalid URL or inaccessible image

**Solution:**
- Use direct image URL
- Test URL in browser
- Or send `no` to skip

---

## 📊 Performance Tips

### 1. Internet Speed
- Stable connection required
- 5 Mbps+ recommended for 720p
- Wired connection preferred

### 2. Quality Selection
- Start with 480p or 720p
- Test with 2-3 videos first
- Adjust based on results

### 3. Batch Size
- Start with 5-10 videos
- Increase gradually
- Monitor for errors

### 4. Thumbnail
- Use lightweight images
- Direct URLs only
- Test before batch

### 5. Server/VPS
- Use for large batches
- Stable power supply
- Good bandwidth

---

## 🎓 Advanced Usage

### Custom Batch Names
```
Examples:
- "Python Course - Module 1"
- "UPSC 2024 - History"
- "Mathematics - Chapter 5"
- "01) DAY 1 - PLANNER COURSE"
```

### Starting Number
Useful for:
- Resuming failed batch
- Continuing from middle
- Custom numbering

Example:
- Total links: 20
- Failed at: 8
- Restart from: 8

### Quality Selection
Advanced users can edit code for custom quality:
```python
quality_map = {
    "144": "256x144",
    "240": "426x240",
    # Add custom resolutions
}
```

---

## 🚀 Platform-Specific Tips

### ClassPlus
- Links usually work directly
- May need login token update
- Check URL accessibility

### YouTube
- All qualities supported
- Age-restricted may fail
- Geo-restricted may fail

### Google Drive
- Public links only
- Private links need access
- Large files may timeout

### M3U8 Streams
- Most reliable format
- Good quality-size ratio
- Fast download

### MPD Streams
- Auto-converts to M3U8
- May need specific player
- Quality varies

---

## 💾 File Management

### Downloaded Files
Location: Bot's working directory
Cleanup: Automatic after upload

### Failed Downloads
- Listed at end
- Save for retry
- Check error messages

### Logs
Location: `bot.log`
Contains:
- Download history
- Error details
- User actions

---

## 🔐 Security Tips

1. **Keep credentials private**
   - Never share API_ID, API_HASH
   - Never share BOT_TOKEN
   - Use environment variables

2. **Bot permissions**
   - Only necessary permissions
   - Regular access review
   - Monitor usage

3. **Content rights**
   - Only personal content
   - Respect copyright
   - No piracy

---

## 📱 Mobile Usage

### Telegram App
1. Open bot
2. Use commands
3. Upload TXT from phone storage
4. Receive videos in chat

### Browser
1. Open Telegram Web
2. Find your bot
3. Same functionality
4. Download to computer

---

## 🎉 Best Practices

### Before Starting
✅ Test with 2-3 videos first
✅ Check all URLs work
✅ Prepare thumbnail
✅ Plan batch name
✅ Choose right quality

### During Download
✅ Keep device awake
✅ Stable internet
✅ Monitor progress
✅ Note errors

### After Completion
✅ Verify all videos
✅ Check quality
✅ Note failures
✅ Retry if needed

---

## 📞 Getting Help

### Self-Help
1. Check this guide
2. Read error messages
3. Check logs
4. Test with single video

### Common Solutions
- Restart bot: `/stop` then restart
- Check internet connection
- Verify TXT format
- Update credentials
- Clear cache

---

## 🎯 Success Checklist

Before uploading TXT file:
- [ ] File format correct
- [ ] All URLs accessible
- [ ] UTF-8 encoding
- [ ] No empty lines
- [ ] Proper separators

Before starting download:
- [ ] Good internet connection
- [ ] Bot running properly
- [ ] Enough storage space
- [ ] Credentials configured
- [ ] Dependencies installed

---

## 💡 Pro Tips

1. **Naming Convention**
   Use consistent naming in TXT:
   ```
   01) Introduction : url
   02) Variables : url
   03) Functions : url
   ```

2. **Quality vs Size**
   - 360p: ~50-100 MB/hour
   - 480p: ~100-200 MB/hour
   - 720p: ~200-400 MB/hour
   - 1080p: ~400-800 MB/hour

3. **Thumbnail**
   Create once, use for all:
   - Upload to telegra.ph
   - Save URL
   - Use in every batch

4. **Caption Template**
   Prepare template:
   ```
   📚 [Course Name]
   📅 [Date]
   🎓 [Quality]
   
   @YourChannel
   ```

5. **Batch Strategy**
   - Small batches (10-20) for reliability
   - Large batches (50+) for bulk
   - Test batch before full run

---

**Happy Learning! 🎓**
