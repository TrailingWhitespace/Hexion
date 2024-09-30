import lightbulb
from hexion import client
import time
from datetime import datetime
from hexion.utils.embed import create_embed

loader = lightbulb.Loader()


@client.register
class Ping(
    lightbulb.SlashCommand, name="ping", description="Returns the latency of the bot."
):
    @lightbulb.invoke
    async def invoke(self, ctx):
        start = time.monotonic()
        msg = await ctx.respond("Pinging...")
        stop = (time.monotonic() - start) * 1000
        heartbeat = round(ctx.client.app.heartbeat_latency * 1000)
        em = create_embed(ctx)
        em.title = ":ping_pong: Pong!"
        em.add_field(name="**Heartbeat**", value=f"`{int(heartbeat):.2f}ms`")
        em.add_field(name="**Rest API**", value=f"`{int(stop):.2f}ms`")
        await ctx.edit_response(msg, content=None, embed=em)
