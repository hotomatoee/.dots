import telebot
from instaloader import Instaloader, Profile
import os
import requests

# Replace with your Telegram bot token
TELEGRAM_TOKEN = '8530045809:AAEIgc6u1nGgHt5-QuPNzkh03pJ_A24X_Bk'

bot = telebot.TeleBot(TELEGRAM_TOKEN)
loader = Instaloader()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Send me an Instagram username (without @) to get their profile picture, followers count, and bio.")

@bot.message_handler(func=lambda message: True)
def handle_username(message):
    username = message.text.strip()
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
        bot.reply_to(message, f"Followers: {followers}\nBio: {bio}")
        
        # Clean up
        os.remove(pfp_path)
        
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}. Make sure the username is correct and the profile is public.")

if __name__ == '__main__':
    bot.polling()