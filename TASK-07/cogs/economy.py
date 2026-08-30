import random
import discord
from discord.ext import commands
import database as db
from one_piece_api import fetch_grand_line_intel

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bounty")
    async def bounty(self, ctx):
        """Check your current Berry balance."""
        pirate = db.get_or_create_pirate(ctx.author.id)
        embed = discord.Embed(
            title=f"☠️ {ctx.author.display_name}'s Bounty Ledger",
            color=discord.Color.gold()
        )
        embed.add_field(name="Wallet Stash", value=f"🪙 {pirate['wallet']:,} Berries", inline=True)
        embed.add_field(name="Bank Reserve", value=f"🏦 {pirate['bank']:,} Berries", inline=True)
        embed.add_field(name="Total Bounty", value=f"⚔️ {pirate['wallet'] + pirate['bank']:,} Berries", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="setsail")
    @commands.cooldown(1, 86400, commands.BucketType.user)  # 24-hour cooldown
    async def set_sail(self, ctx):
        """Claim daily Berries like raiding a merchant ship at dawn."""
        loot = random.randint(200, 500)
        db.update_wallet(ctx.author.id, loot)
        await ctx.send(f"🌅 **{ctx.author.display_name}** set sail at dawn and raided a merchant vessel, netting **{loot:,} Berries**!")

    @set_sail.error
    async def set_sail_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            hours, remainder = divmod(int(error.retry_after), 3600)
            minutes, seconds = divmod(remainder, 60)
            await ctx.send(f"⏳ Calm Belt waters! You can set sail again in **{hours}h {minutes}m {seconds}s**.")

    @commands.command(name="trade")
    async def trade(self, ctx, target: discord.Member, amount: int):
        """Trade Berries with another pirate."""
        if target.bot:
            return await ctx.send("🏴‍☠️ Marines don't deal with bot scallywags!")
        if target.id == ctx.author.id:
            return await ctx.send("🏴‍☠️ You can't trade Berries with yourself!")
        if amount <= 0:
            return await ctx.send("🏴‍☠️ You must trade at least 1 Berry!")

        success = db.transfer_berries(ctx.author.id, target.id, amount)
        if success:
            await ctx.send(f"🤝 **{ctx.author.display_name}** successfully transferred **{amount:,} Berries** to **{target.display_name}**!")
        else:
            await ctx.send("❌ You don't have enough Berries in your wallet stash!")

    @commands.command(name="raid")
    @commands.cooldown(1, 600, commands.BucketType.user)  # 10-minute cooldown
    async def raid(self, ctx, target: discord.Member):
        """Attempt to raid a rival crew's wallet stash."""
        if target.id == ctx.author.id or target.bot:
            return await ctx.send("🏴‍☠️ Invalid target for a raid!")

        attacker = db.get_or_create_pirate(ctx.author.id)
        defender = db.get_or_create_pirate(target.id)

        if defender["wallet"] < 50:
            return await ctx.send(f"🏴‍☠️ **{target.display_name}** is too poor to raid! Leave them be.")

        # 45% success chance
        if random.random() < 0.45:
            stolen_percent = random.uniform(0.1, 0.3)
            stolen_amount = int(defender["wallet"] * stolen_percent)
            db.update_wallet(target.id, -stolen_amount)
            db.update_wallet(ctx.author.id, stolen_amount)
            await ctx.send(f"🗡️ **RAID SUCCESSFUL!** {ctx.author.display_name} ambushed {target.display_name}'s ship and made off with **{stolen_amount:,} Berries**!")
        else:
            penalty = int(attacker["wallet"] * 0.15)
            db.update_wallet(ctx.author.id, -penalty)
            db.update_wallet(target.id, penalty)
            await ctx.send(f"💥 **RAID FAILED!** {target.display_name}'s crew fought back! {ctx.author.display_name} dropped **{penalty:,} Berries** while retreating.")

    @commands.command(name="worstgeneration")
    async def worst_generation(self, ctx):
        """View top 5 richest pirates on the server."""
        top_pirates = db.get_top_pirates(5)
        embed = discord.Embed(
            title="🏴‍☠️ The Worst Generation — Top Bounties",
            color=discord.Color.dark_purple()
        )
        
        for idx, row in enumerate(top_pirates, 1):
            user = self.bot.get_user(row["user_id"])
            username = user.display_name if user else f"Pirate ID {row['user_id']}"
            embed.add_field(
                name=f"#{idx} {username}",
                value=f" Total Bounty: **{row['total_bounty']:,} Berries**",
                inline=False
            )
        await ctx.send(embed=embed)

    @commands.command(name="logpose")
    async def log_pose(self, ctx):
        """Spin the Log Pose for random Grand Line intel."""
        async with ctx.typing():
            intel = await fetch_grand_line_intel()
        await ctx.send(intel)

async def setup(bot):
    await bot.add_cog(Economy(bot))