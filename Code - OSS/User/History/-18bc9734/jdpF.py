import telebot
from instaloader import Instaloader, Profile
import os
import requests

# === ADD THESE ===
IG_USERNAME = 'gadeti7238'  # e.g., 'scraper_test_123'
IG_PASSWORD = 'BugabooGallloooo1231'
# =====================

TELEGRAM_TOKEN = '8530045809:AAEIgc6u1nGgHt5-QuPNzkh03pJ_A24X_Bk'
bot = telebot.TeleBot(TELEGRAM_TOKEN)
loader = Instaloader()

# LOGIN AT STARTUP (saves session to avoid re-logging)
if IG_USERNAME and IG_PASSWORD:
    try:
        loader.login(IG_USERNAME, IG_PASSWORD)
        print("✅ Logged in – blocks bypassed!")
    except Exception as e:
        print(f"❌ Login failed: {e}. Check credentials or use a new account.")
else:
    print("⚠️ No login – expect 401 errors soon.")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Send me an Instagram username (without @) to get their profile picture, followers count, and bio.")

@bot.message_handler(func=lambda message: True)
def handle_username(message):
    username = message.text.strip().lower()  # Auto-fix case
    if 'christiano' in username:
        username = 'cristiano'  # Common typo fix
    try:
        profile = Profile.from_username(loader.context, username)
       
        # Get data
        followers = profile.followers
        bio = profile.biography
        pfp_url = profile.profile_pic_url
       
        # Download PFP temporarily
        pfp_path = f"{username}.jpg"
        response = requests.get(pfp_url)
        with open(pfp_path, 'wb') as f:
            f.write(response.content)
       
        # Send PFP
        with open(pfp_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
       
        # Send details
        bot.reply_to(message, f"✅ Followers: {followers:,}\nBio: {bio}")
       
        # Clean up
        os.remove(pfp_path)
       
    except Exception as e:
        error_str = str(e)
        if "401" in error_str or "fail" in error_str:
            bot.reply_to(message, "🚫 Instagram rate-limited (401). Wait 10-30 mins, or add IG login to the code.")
        elif "ProfileNotExists" in error_str:
            bot.reply_to(message, f"❌ Profile '{username}' not found. Try 'cristiano' (no 'h').")
        else:
            bot.reply_to(message, f"❌ Error: {error_str}")

if __name__ == '__main__':
    bot.polling()