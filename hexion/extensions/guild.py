import lightbulb
from hexion import client
from hexion.utils import create_embed

loader = lightbulb.Loader()


@client.register
class Avatar(
    lightbulb.SlashCommand, name="avatar", description="Display's the avatar of a user."
):
    user = lightbulb.user(
        "user", "The user who's avatar needs to be displayed.", default=None
    )
    user_id = lightbulb.string("userid", "The user ID duh.", default = None
    )

    @lightbulb.invoke
    async def invoke(self, ctx):
        await ctx.defer()
        em = create_embed(ctx)
        user = ctx.interaction.user
        if self.user_id:                                               user = await ctx.client.app.rest.fetch_user(self.user_id)
        if self.user and not self.user_id:
            user = self.user
        em.set_image(user.avatar_url).set_author(
            name=user.username, icon=user.avatar_url
        )
        em.title = f"{user.display_name}'s avatar"
        await ctx.respond(embed=em)
