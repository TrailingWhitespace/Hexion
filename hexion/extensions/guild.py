import lightbulb
from hexion import client
from hexion.utils import create_embed

loader = lightbulb.Loader()

@client.register
class Avatar(lightbulb.SlashCommand,
             name = "avatar",
             description = "Display's the avatar of a user."):

    user = lightbulb.user("user", "The user who's avatar needs to be displayed.",
                          default = None)

    @lightbulb.invoke
    async def invoke(self, ctx):
        await ctx.defer()
        em = create_embed(ctx)
        if not self.user:
            user = ctx.interaction.user
        else:
            user = self.user
        em.set_image(user.avatar_url).set_author(name = user.username, icon = user.avatar_url)
        em.title = f"{user.display_name}'s avatar"
        await ctx.respond(embed = em)
        
