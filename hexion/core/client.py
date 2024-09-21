import hikari
import lightbulb
from hexion import extensions
from .. import config

bot = hikari.GatewayBot(token=config.TOKEN)

client = lightbulb.client_from_app(bot)


@bot.listen(hikari.StartingEvent)
async def on_starting(event):
    await client.load_extensions_from_package(extensions)
    await client.start()
