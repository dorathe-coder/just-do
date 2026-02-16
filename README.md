# 🎬 Advanced TXT to Video Downloader Bot

Professional Telegram bot for downloading videos from TXT files with support for multiple platforms.

## 🌟 Features

### Core Features
- ✅ Multi-Platform Support (ClassPlus, YouTube, Drive, etc.)
- ✅ Auto Format Detection
- ✅ Smart Quality Selection (144p - 1080p)
- ✅ Resume Capability
- ✅ Batch Processing
- ✅ Custom Thumbnails
- ✅ Progress Tracking
- ✅ Advanced Error Handling

### Supported Platforms
- 📱 ClassPlus App
- 🎥 YouTube (All formats)
- 📁 Google Drive
- 🌐 M3U8 Streams
- 📺 MPD Streams
- 🎬 Direct MP4 Links
- 📚 Vision IAS
- 🎮 JW Player
- 📄 PDF Files

### Technical Features
- ⚡ Aria2c Integration (16x parallel downloads)
- 🔄 Fragment Retry (25 attempts)
- 📊 Real-time Progress Bar
- 🛡️ Flood Wait Handling
- 🧹 Auto Cleanup
- 💾 Memory Optimization

## 📋 Requirements

- Python 3.9+
- FFmpeg (for video processing)
- Aria2c (for fast downloads)

## 🚀 Installation

### 1. Clone Repository
```bash
git clone <your-repo>
cd <repo-folder>
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install System Dependencies
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg aria2

# For other systems, install ffmpeg and aria2c
```

### 4. Configuration
Edit `vars.py` and add your credentials:
```python
API_ID = "your_api_id"
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
```

### 5. Run Bot
```bash
python main.py
```

## 📝 TXT File Format

Your TXT file should be in one of these formats:

### Format 1 (Recommended)
```
Video Name 1 : https://example.com/video1.m3u8
Video Name 2 : https://example.com/video2.mp4
Video Name 3 : https://youtube.com/watch?v=xxxxx
```

### Format 2
```
Video Name 1:https://example.com/video1.m3u8
Video Name 2:https://example.com/video2.mp4
```

### Format 3 (URL Only)
```
https://example.com/video1.m3u8
https://example.com/video2.mp4
```

## 🎯 Usage

### Basic Usage
1. Start bot: `/start`
2. Send command: `/upload`
3. Upload your TXT file
4. Follow the prompts:
   - Enter starting number (default: 1)
   - Enter batch name
   - Select quality (144, 240, 360, 480, 720, 1080)
   - Enter caption (or 'no')
   - Send thumbnail URL (or 'no')
5. Bot will process all videos!

### Commands
- `/start` - Start bot and show menu
- `/upload` - Upload TXT file and start download
- `/help` - Show help guide
- `/features` - List all features
- `/stop` - Stop ongoing task
- `/settings` - Bot settings (coming soon)
- `/batch` - Batch mode (coming soon)

## 🎬 Quality Options

Choose from:
- 144p (256x144)
- 240p (426x240)
- 360p (640x360)
- 480p (854x480)
- 720p (1280x720) ⭐ Recommended
- 1080p (1920x1080)
- best (Highest available)

## 🔧 Advanced Features

### Custom Thumbnails
- Send any image URL
- Format: `https://example.com/thumb.jpg`
- Supports: JPG, PNG, WEBP

### Caption Support
- Add custom caption to all videos
- Supports markdown formatting
- Auto-adds batch info

### Error Recovery
- Auto-retry on network errors
- Skip failed videos
- Continue from last position
- Detailed error logging

## 🐛 Troubleshooting

### Common Issues

**1. "No valid links found"**
- Check TXT file format
- Ensure proper encoding (UTF-8)
- Check for empty lines

**2. "Download failed"**
- Verify URL is accessible
- Check internet connection
- Try different quality

**3. "Could not convert string to float"**
- This is fixed in new version
- Update to latest code

**4. "Thumbnail error"**
- Use direct image URL
- Ensure URL is accessible
- Or use 'no' to skip

### Getting Telegram Credentials

1. Go to https://my.telegram.org
2. Login with your phone number
3. Go to "API Development Tools"
4. Create new application
5. Copy API_ID and API_HASH

### Getting Bot Token

1. Open Telegram
2. Search for @BotFather
3. Send `/newbot`
4. Follow instructions
5. Copy bot token

## 📊 Performance

- Download Speed: Up to 16x parallel
- Upload Speed: Optimized streaming
- Memory Usage: Auto-cleanup
- Error Rate: < 1% with retry

## 🔒 Security

- No data storage
- Auto file cleanup
- Secure API handling
- Private processing

## 🤝 Contributing

Contributions welcome! Please:
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 📜 License

This project is for educational purposes only.

## ⚠️ Disclaimer

- Respect copyright laws
- Use for personal content only
- No guarantee for third-party content
- Use at your own risk

## 💡 Tips

1. **Start Small**: Test with 2-3 videos first
2. **Good Internet**: Stable connection required
3. **Right Format**: Follow TXT format exactly
4. **Quality Choice**: 720p is best balance
5. **Thumbnail**: Use direct image URLs
6. **Batch Name**: Keep it short and clear

## 🆘 Support

For issues and questions:
- Check troubleshooting section
- Review TXT format
- Verify credentials
- Check internet connection

## 🎉 Acknowledgments

- Pyrogram team
- yt-dlp developers
- aria2c project
- All contributors

## 📈 Changelog

### Version 2.0 (Latest)
- ✅ Fixed TXT parsing issues
- ✅ Added multiple format support
- ✅ Improved error handling
- ✅ Enhanced progress bar
- ✅ Better URL processing
- ✅ Added retry logic
- ✅ Improved ClassPlus support
- ✅ Fixed caption issues
- ✅ Better thumbnail handling
- ✅ Added help commands

### Version 1.0
- Initial release

## 🚀 Future Updates

Coming soon:
- [ ] Batch mode for multiple TXT files
- [ ] Settings panel
- [ ] Auto quality selection
- [ ] Download queue
- [ ] History tracking
- [ ] More platform support
- [ ] Admin panel
- [ ] Statistics
- [ ] And more...

---

**Made with ❤️ for the community**

**Happy Downloading! 🎬**
