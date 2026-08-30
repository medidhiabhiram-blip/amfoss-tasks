import discord
from discord.ext import commands
import database as db

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="shop")
    async def shop(self, ctx):
        """Browse items available for purchase."""
        items = db.fetch_shop_items()
        embed = discord.Embed(
            title="🏪 The Berry Broker's Black Market",
            description="Use `!buy <item_name>` to acquire items.",
            color=discord.Color.blue()
        )
        for item in items:
            embed.add_field(
                name=f"{item['name']} — {item['cost']:,} Berries",
                value=f"Effect: *{item['effect']}*",
                inline=False
            )
        await ctx.send(embed=embed)

    @commands.command(name="buy")
    async def buy(self, ctx, *, item_name: str):
        """Buy an item from the shop using your wallet Berries."""
        item = db.get_shop_item_by_name(item_name)
        if not item:
            return await ctx.send("❌ The Broker doesn't stock any item by that name!")

        success = db.purchase_item(ctx.author.id, item["item_id"], item["cost"])
        if success:
            await ctx.send(f"🛒 **{ctx.author.display_name}** purchased **{item['name']}** for **{item['cost']:,} Berries**!")
        else:
            await ctx.send("❌ You don't have enough Berries in your wallet to buy this!")

    @commands.command(name="inventory")
    async def inventory(self, ctx):
        """View your currently owned items and their status."""
        items = db.get_user_inventory(ctx.author.id)
        embed = discord.Embed(
            title=f"🎒 {ctx.author.display_name}'s Ship Hold",
            color=discord.Color.dark_gold()
        )

        if not items:
            embed.description = "Your ship hold is currently empty."
        else:
            for item in items:
                status_icon = "🟢 Active" if item["status"] == "active" else "🔴 Spent"
                embed.add_field(
                    name=f"{item['name']} ({status_icon})",
                    value=f"Effect: {item['effect']}",
                    inline=False
                )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Shop(bot))