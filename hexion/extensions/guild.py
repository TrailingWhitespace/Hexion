import lightbulb
from hexion.utils import create_embed
from PIL import Image

loader = lightbulb.Loader()


@loader.command
class Avatar(
    lightbulb.SlashCommand, name="avatar", description="Display's the avatar of a user."
):
    user = lightbulb.user(
        "user", "The user who's avatar needs to be displayed.", default=None
    )
    user_id = lightbulb.string("userid", "The user ID duh.", default=None)
    display = lightbulb.boolean(
        "display", "To display the server specific url.", default=None
    )
    size = lightbulb.integer("size", "The size of the avatar.", default=4096)

    @lightbulb.invoke
    async def invoke(self, ctx):
        await ctx.defer()
        user = ctx.interaction.user
        if self.user_id:
            user = await ctx.client.app.rest.fetch_user(self.user_id)
        if self.user and not self.user_id:
            user = self.user
        em = create_embed(ctx, color = user.accent_color)
        if not self.display:
            av = user.make_avatar_url(size=self.size)
        else:
            av = user.display_avatar_url

        if not av:
            av = user.default_avatar_url
        em.set_image(av).set_author(name=user.username, icon=av)
        em.title = f"{user.display_name}'s avatar"
        await ctx.respond(embed=em)


@loader.command
class Banner(
    lightbulb.SlashCommand, name="banner", description="Get the banner of a user."
):
    user = lightbulb.user(
        "user", "The user who's banner needs to be displayed.", default=None
    )

    @lightbulb.invoke
    async def invoke(self, ctx):
        user = ctx.interaction.user if not self.user else self.user
        user = await ctx.client.app.rest.fetch_user(user.id)
        em = create_embed(ctx, color = user.accent_color)
        img = user.banner_url
        if not user.banner_url:
            img = Image.new('RGB', (1080, 432), user.accent_color)
            img.save("./hexion/command_data/banner.png")
            img = "./hexion/command_data/banner.png"
        em.set_image(img).set_author(
            name=user.username, icon=user.avatar_url
        )
        em.title = f"{user.display_name}'s banner"
        await ctx.respond(embed=em)