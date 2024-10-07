import os

# Retrieve the token from Replit environment variables
TOKEN = os.environ['DISCORD_BOT_TOKEN']

if TOKEN is None:
  raise ValueError("Discord bot token not found in environment variables.")
import discord
import requests
import os
from dotenv import load_dotenv
from discord import Embed


async def send_chunked_message(channel, message):
  max_length = 2000
  for chunk in [
      message[i:i + max_length] for i in range(0, len(message), max_length)
  ]:
    await channel.send(chunk)


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  print(f'Message from {message.author}: {message.content}')
  if message.author == client.user:
    return

  if message.content.startswith('!lospokemon'):
    content = message.content.split()

    if len(content) != 2:
      await message.channel.send('Invalid input.\nUsage: !pokemon [pokemon]')
    else:
      pokemon_name = content[1]
      r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
      if r.status_code == 200:
        pokemon = r.json()
        type_names = ", ".join([
            poke_type['type']['name'] for poke_type in pokemon['types']
        ]).capitalize()

        height_in_feet = round((pokemon["height"] / 10) * 3.28084, 2)
        weight_in_pounds = round((pokemon["weight"] / 10) * 2.20462, 2)

        embed = Embed(
            title=f'{pokemon["name"].capitalize()} [#{pokemon["id"]}]',
            color=0x7289DA)
        embed.add_field(name='Type(s)', value=type_names, inline=False)
        embed.add_field(name='Height',
                        value=f'{height_in_feet} ft',
                        inline=True)
        embed.add_field(name='Weight',
                        value=f'{weight_in_pounds} lbs',
                        inline=True)
        embed.add_field(name='Base Experience',
                        value=pokemon["base_experience"],
                        inline=False)
        abilities = ", ".join(
            [ability["ability"]["name"] for ability in pokemon["abilities"]])
        embed.add_field(name='Abilities', value=abilities, inline=False)
        moves = ", ".join(
            [move["move"]["name"] for move in pokemon["moves"][:5]])
        embed.add_field(name='Some Moves', value=moves, inline=False)
        embed.add_field(name='Note',
                        value='This Pokémon is my favorite!',
                        inline=False)

        # Adding sprites to embed
        embed.set_image(
            url=pokemon["sprites"]["front_default"])  # Main image of the embed
        embed.set_thumbnail(
            url=pokemon["sprites"]["front_shiny"])  # Smaller image on the side

        if len(embed) > 6000:
          await send_chunked_message(message.channel, embed)
        else:
          await message.channel.send(embed=embed)

      elif r.status_code == 404:
        await message.channel.send('Pokemon not found.')


client.run(TOKEN)
