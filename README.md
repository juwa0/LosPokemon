# Pokémon Discord Bot

This is a Discord bot that allows users to look up detailed information about Pokémon using the [PokéAPI](https://pokeapi.co/). Users can get information such as a Pokémon's type, height, weight, abilities, base experience, and more by typing commands directly into a Discord channel.

## Features

- Look up Pokémon by name.
- Get information on:
  - Type(s)
  - Height and Weight (converted to feet and pounds)
  - Base Experience
  - Abilities
  - Moves (up to 5)
  - Sprites (Regular and Shiny)
- Handles large messages by chunking them if needed.
- Informs the user if the Pokémon isn't found.

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Pokemon-Discord-Bot.git
cd Pokemon-Discord-Bot
```

### 2. Install Dependencies

Ensure you have Python installed (version 3.6 or later). Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

> Note: If you're using Replit, you can skip this step as Replit handles dependencies automatically.

### 3. Set Up Environment Variables

The bot requires a **Discord bot token** to function. In Replit, add the token securely using Replit's Secrets feature:

1. Click the lock icon on the left sidebar in Replit.
2. Add a new secret:
   - Name: `DISCORD_BOT_TOKEN`
   - Value: Your Discord bot token.

If you're running locally, you can use a `.env` file to store the token. Create a `.env` file in the root directory and add the following:

```
DISCORD_BOT_TOKEN=your_discord_bot_token_here
```

### 4. Running the Bot

In Replit or your local environment, simply run the `main.py` file:

```bash
python main.py
```

The bot will start and connect to your Discord server. Once connected, you should see a message in the console saying:

```
We have logged in as <bot_username>
```

## Usage

Once the bot is online in your Discord server, you can use the following command to get Pokémon information:

- **Command**: `!lospokemon <pokemon_name>`
  
  Example:

  ```bash
  !lospokemon pikachu
  ```

The bot will respond with an embedded message containing information about the specified Pokémon, including its type(s), height, weight, base experience, abilities, moves, and images.

## Example Output

Here’s an example of what you’ll see when you use the bot:

```
Pikachu [#25]
Type(s): Electric
Height: 1.31 ft
Weight: 13.23 lbs
Base Experience: 112
Abilities: Static, Lightning Rod
Some Moves: Thunder Shock, Quick Attack, Iron Tail, Electro Ball, Growl
Note: This Pokémon is my favorite!
```

As well as an image of the regular and shiny sprites of the Pokemon**

## Dependencies

- **discord.py**: For interacting with the Discord API.
- **requests**: For fetching Pokémon data from the PokéAPI.
- **dotenv**: For managing environment variables (if you're using `.env` files).

To install dependencies, run:

```bash
pip install discord.py requests python-dotenv
```
