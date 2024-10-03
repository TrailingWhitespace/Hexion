from hikari import Embed
from datetime import datetime

def create_embed(ctx, color = "#0000FF") -> Embed:
    em = Embed(color = color)
    em.set_footer(text=ctx.member.username, icon=ctx.member.avatar_url)
    em.timestamp = datetime.now().astimezone()
    return em
