import os
import discord
from dotenv import load_dotenv, find_dotenv
import deepl

load_dotenv(find_dotenv())
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

DEEPL_TOKEN = os.getenv("DEEPL_TOKEN")
translator = deepl.Translator(DEEPL_TOKEN)

intents = discord.Intents.default()
intents.members=True
intents.message_content=True

#all available DeepL languages, not every language has a emoji though
flags = {
"🇦🇷": "ar", # Argentinien (Argentina)
"🇧🇬": "bg", # Bulgarien (Bulgaria)
"🇨🇿": "cs", # Tschechien (Czech Republic)
"🇩🇰": "da", # Dänemark (Denmark)
"🇩🇪": "de", # Deutschland (Germany)
"🇬🇷": "el", # Griechenland (Greece)
"🇬🇧": "en-gb", # Vereinigtes Königreich (United Kingdom)
"🇺🇸": "en-us", # US
"🇪🇸": "es", # Spanien (Spain)
"🇪🇪": "et", # Estland (Estonia)
"🇫🇮": "fi", # Finnland (Finland)
"🇫🇷": "fr", # Frankreich (France)
"🇭🇺": "hu", # Ungarn (Hungary)
"🇮🇩": "id", # Indonesien (Indonesia)
"🇮🇹": "it", # Italien (Italy)
"🇯🇵": "ja", # Japan
"🇰🇷": "ko", # Südkorea (South Korea)
"🇱🇹": "lt", # Litauen (Lithuania)
"🇱🇻": "lv", # Lettland (Latvia)
"🇳🇴": "nb", # Norwegisch (Bokmål) (Norwegian Bokmål)
"🇳🇱": "nl", # Niederlande (Netherlands)
"🇵🇱": "pl", # Polen (Poland)
"🇵🇹": "pt", # Portugal (Portugal - all Portuguese varieties mixed)
"🇷🇴": "ro", # Rumänien (Romania)
"🇷🇺": "ru", # Russland (Russia)
"🇸🇰": "sk", # Slowakei (Slovakia)
"🇸🇮": "sl", # Slowenien (Slovenia)
"🇸🇪": "sv", # Schweden (Sweden)
"🇹🇷": "tr", # Türkei (Turkey)
"🇺🇦": "uk", # Ukraine
"🇨🇳": "zh", # China
}


class MyClient(discord.Client):    

    async def on_ready(self):
        print("Logged in as {}".format(client.user.name))
        await client.change_presence(activity=discord.Game("DeepL"), status=discord.Status.online)

    async def on_message(self, message):
        if message.author == client.user:
            return
        print(f'Message from {message.author}: {message.content}')

    async def on_reaction_add(self,reaction,user):
        print(f'{user} reacted with emoji {reaction.emoji} on {reaction.message.content}')

        if reaction.emoji in flags:
            lang = flags[reaction.emoji]
            print(f'Emoji is the flag of {lang}')
            await reaction.message.reply(translator.translate_text(reaction.message.content, target_lang=lang),mention_author=True)
        else:
            print('No flag found')
            
client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
