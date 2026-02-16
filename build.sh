#!/usr/bin/env bash
# Render build script

# Update system
apt-get update

# Install ffmpeg for video processing
apt-get install -y ffmpeg

# Install aria2 for fast downloads
apt-get install -y aria2

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Build completed successfully!"
