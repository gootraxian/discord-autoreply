import discord
import os
import threading
from discord.ext import commands
from http.server import HTTPServer, BaseHTTPRequestHandler

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        await message.channel.send(
            "Hello! I don't receive DMs. Create a ticket in my Discord (https://discord.gg/f7X3sh2PBk)."
        )

    await bot.process_commands(message)

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_health_server():
    port = int(os.getenv("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    print(f"Health server running on port {port}")
    server.serve_forever()

threading.Thread(target=run_health_server, daemon=True).start()

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
