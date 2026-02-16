# Alternative entry point
# Can be used instead of main.py

import os
import sys

# Set up environment
if __name__ == "__main__":
    print("🚀 Starting Advanced TXT to Video Downloader Bot...")
    print("📝 Loading configuration...")
    
    try:
        # Import and run main
        import main
        print("✅ Bot started successfully!")
        
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        sys.exit(1)
