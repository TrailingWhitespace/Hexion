import hikari
import lightbulb
from hexion import extensions, config
from motor.motor_asyncio import AsyncIOMotorClient

bot = hikari.GatewayBot(token=config.TOKEN)
client = lightbulb.client_from_app(bot)

db_client = AsyncIOMotorClient(config.MONGODB)
db= db_client.get_database("hexion")
misc_collection = db.misc

@bot.listen(hikari.StartingEvent)
async def on_starting(event):
    await client.load_extensions_from_package(extensions)
    await client.start()
