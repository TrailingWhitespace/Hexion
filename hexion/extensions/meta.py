import lightbulb
from hexion import client
import time

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
        await ctx.edit_response(
            msg, f"Heartbeat: `{int(heartbeat):.2f}`ms\nRest API: `{int(stop):.2f}`ms"
        )
