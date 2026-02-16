# 🚀 Render Deployment Guide

## ✅ Prerequisites (Already Done)
- [x] GitHub repository created
- [x] All files uploaded
- [x] API_ID: 31708653
- [x] API_HASH: 618773cba18e732111276d01571a928f
- [x] BOT_TOKEN: (You have it)

---

## 📝 Step-by-Step Deployment

### Step 1: Upload New Files to GitHub

Upload these **3 NEW files** to your GitHub repository:

1. **render.yaml** (New file)
2. **build.sh** (New file)
3. **.gitignore** (New file)

And **REPLACE** this file:
4. **requirements.txt** (Updated with gunicorn)

---

### Step 2: Create Render Account

1. Go to: https://render.com
2. Click "Get Started for Free"
3. Sign up with your **GitHub account** (easiest way)
4. Authorize Render to access your GitHub

---

### Step 3: Deploy from GitHub

1. After login, click **"New +"** button (top right)
2. Select **"Web Service"**
3. Click **"Connect account"** if GitHub not connected
4. Find your repository **"just"** in the list
5. Click **"Connect"**

---

### Step 4: Configure Service

Fill the form:

**Basic Settings:**
- **Name:** `video-bot` (or any name you like)
- **Region:** `Singapore` (closest to India)
- **Branch:** `main` (or `master`)
- **Root Directory:** Leave blank
- **Runtime:** `Python 3`
- **Build Command:** `bash build.sh`
- **Start Command:** `python main.py`

**Instance Type:**
- Select **"Free"** plan

---

### Step 5: Add Environment Variables

Scroll down to **"Environment Variables"** section:

Click **"Add Environment Variable"** and add these **3 variables**:

1. **Variable 1:**
   - Key: `API_ID`
   - Value: `31708653`

2. **Variable 2:**
   - Key: `API_HASH`
   - Value: `618773cba18e732111276d01571a928f`

3. **Variable 3:**
   - Key: `BOT_TOKEN`
   - Value: Your bot token (from BotFather)
   - Example: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

---

### Step 6: Deploy!

1. Click **"Create Web Service"** button at the bottom
2. Render will start building your bot
3. Wait 5-10 minutes for deployment
4. Look for **"Live"** status with green dot ✅

---

## 🎯 After Deployment

### Check if Bot is Running:

1. Open Telegram
2. Search for your bot username
3. Send `/start`
4. You should get welcome message! 🎉

### Monitor Logs:

- Go to Render dashboard
- Click on your service
- Click **"Logs"** tab
- You can see bot activity here

---

## 🔧 Troubleshooting

### If deployment fails:

**Check Logs:**
- Go to "Logs" tab in Render
- Look for error messages

**Common Issues:**

1. **Build Failed:**
   - Check if all files uploaded correctly
   - Verify requirements.txt

2. **Bot Not Responding:**
   - Check environment variables spelling
   - Verify BOT_TOKEN is correct
   - Check API_ID and API_HASH

3. **Service Keeps Restarting:**
   - Check logs for errors
   - Verify credentials

---

## 💡 Important Notes

### Free Plan Limitations:
- ✅ Always running (24/7)
- ✅ 750 hours/month free
- ⚠️ Sleeps after 15 min inactivity (wakes on request)
- ⚠️ Limited resources (enough for bot)

### Keep Bot Active:
You can use **UptimeRobot** (free) to ping your bot every 5 minutes:
1. Go to: https://uptimerobot.com
2. Add monitor with your Render URL
3. Bot will never sleep!

---

## 🎉 Success Checklist

After deployment:
- [ ] Service shows "Live" status
- [ ] Bot responds to `/start`
- [ ] Can upload TXT file
- [ ] Downloads working
- [ ] No errors in logs

---

## 📞 Need Help?

If something doesn't work:
1. Check Render logs first
2. Verify all environment variables
3. Test bot commands one by one
4. Check GitHub files are uploaded

---

## 🔄 How to Update Bot

When you want to update code:
1. Push changes to GitHub
2. Render auto-deploys (if enabled)
3. Or click "Manual Deploy" in Render

---

**Your bot will be live 24/7 on Render! 🚀**

**Good luck! 🎊**
