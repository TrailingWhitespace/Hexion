from hikari import Embed
from datetime import datetime


def create_embed(ctx):
    em = Embed(color="#0000FF")
    em.set_footer(text=ctx.member.username, icon=ctx.member.avatar_url)
    em.timestamp = datetime.now().astimezone()
    return em
