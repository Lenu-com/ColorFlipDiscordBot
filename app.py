import os
import discord
from now import fetch_now
from color_flip import ColorFlip
from filepath import INPUT_PATH


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def is_image(attachment: discord.Attachment) -> bool:
    return attachment.content_type.startswith('image')


@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return
    
    if not message.mentions:
        return

    if len(message.attachments) == 0:
        return

    for attachment in message.attachments:
        if is_image(attachment):
            input_file_name = f'{fetch_now()}.jpg'
            input_path = os.path.join(INPUT_PATH, input_file_name)
            await attachment.save(input_path)
            output_path = ColorFlip.fetch_output_img(input_file_name)
            await message.channel.send(file=discord.File(output_path))
            os.remove(input_path)
            os.remove(output_path)
            
            
client.run(os.environ['DISCORD_API_KEY'])