import telebot
from instaloader import Instaloader, Profile, ProfileNotExistsException, ConnectionException, LoginRequiredException
import requests
import io # Used for handling images in memory

# 1. Load configuration
# Replace with your NEW token from BotFather
TELEGRAM_TOKEN = '8530045809:AAEIgc6u1nGgHt5-QuPNzkh03pJ_A24X_Bk' 

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Initialize Instaloader
# Note: For heavy use, you must login. See "Notes" below.
loader = Instaloader()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "👋 *Hi! I am an Instagram Info Bot.*\n\n"
        "Send me a username (e.g., `cristiano`) and I will fetch:\n"
        "📸 Profile Picture\n"
        "👥 Follower Count\n"
        "📝 Bio\n\n"
        "_Note: Private profiles may strictly limit data._"
    )
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_username(message):
    username = message.text.strip().lower()
    
    # Basic cleanup: remove @ if user added it
    if username.startswith("@"):
        username = username[1:]
        
    # Send a "Loading" message because Instagram is slow
    status_msg = bot.reply_to(message, "🔍 Searching Instagram database...")

    try:
        # Fetch Profile
        profile = Profile.from_username(loader.context, username)
        
        # Get data
        followers = f"{profile.followers:,}" # Adds commas (e.g., 1,000,000)
        following = f"{profile.followees:,}"
        posts = f"{profile.mediacount:,}"
        bio = profile.biography
        pfp_url = profile.profile_pic_url
        full_name = profile.full_name
        is_private = "🔒 Yes" if profile.is_private else "rw No"

        # Prepare Caption
        caption = (
            f"👤 *Name:* {full_name}\n"
            f"🔗 *Username:* `@{username}`\n"
            f"👥 *Followers:* {followers}\n"
            f"👀 *Following:* {following}\n"
            f"📸 *Posts:* {posts}\n"
            f"🔐 *Private:* {is_private}\n\n"
            f"📝 *Bio:*\n{bio}"
        )

        # Download PFP to Memory (RAM) - No files saved to disk
        response = requests.get(pfp_url)
        if response.status_code == 200:
            photo_file = io.BytesIO(response.content)
            photo_file.name = f"{username}.jpg" # Telegram needs a filename hint

            # Send Photo with Caption
            bot.send_photo(
                message.chat.id, 
                photo=photo_file, 
                caption=caption, 
                parse_mode='Markdown'
            )
            
            # Delete the "Searching..." message
            bot.delete_message(message.chat.id, status_msg.message_id)
        else:
            bot.edit_message_text(f"Found profile, but couldn't download image. \n\n{caption}", 
                                  message.chat.id, status_msg.message_id)

    except ProfileNotExistsException:
        bot.edit_message_text("❌ Profile not found. Please check the spelling.", 
                              message.chat.id, status_msg.message_id)
        
    except LoginRequiredException:
        bot.edit_message_text("⚠️ Instagram redirected to login. The bot needs to be authenticated to view this profile.", 
                              message.chat.id, status_msg.message_id)
        
    except ConnectionException:
        bot.edit_message_text("⚠️ Connection error. Instagram might be blocking requests temporarily.", 
                              message.chat.id, status_msg.message_id)
        
    except Exception as e:
        bot.edit_message_text(f"❌ An error occurred: {str(e)}", 
                              message.chat.id, status_msg.message_id)

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()