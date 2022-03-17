
import os
from typing import Optional

import nextcord
from nextcord.ext import commands

from utils import (
    daily_puzzle_id,
    generate_puzzle_embed,
    process_message_as_guess,
    random_puzzle_id,
)







class wordle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @nextcord.slash_command(name="play", description="Play Wordle Clone")
    async def slash_play(self,interaction: nextcord.Interaction):
        """This command has subcommands for playing a game of Wordle Clone."""
        pass


    @slash_play.subcommand(name="random", description="Play a random game of Wordle Clone")
    async def slash_play_random(self,interaction: nextcord.Interaction):
        embed = generate_puzzle_embed(interaction.user, random_puzzle_id())
        await interaction.send(embed=embed)


    @slash_play.subcommand(name="id", description="Play a game of Wordle Clone by its ID")
    async def slash_play_id(self,
        interaction: nextcord.Interaction,
        puzzle_id: int = nextcord.SlashOption(description="Puzzle ID of the word to guess"),
    ):
        embed = generate_puzzle_embed(interaction.user, puzzle_id)
        await interaction.send(embed=embed)


    @slash_play.subcommand(name="daily", description="Play the daily game of Wordle Clone")
    async def slash_play_daily(self,interaction: nextcord.Interaction):
        embed = generate_puzzle_embed(interaction.user, daily_puzzle_id())
        await interaction.send(embed=embed)





    @commands.group(invoke_without_command=True)
    async def play(self,ctx: commands.Context, puzzle_id: Optional[int] = None):
        """Play a game of Wordle Clone"""
        embed = generate_puzzle_embed(ctx.author, puzzle_id or random_puzzle_id())
        await ctx.reply(embed=embed, mention_author=False)


    @play.command(name="random")
    async def play_random(self,ctx: commands.Context):
        """Play a random game of Wordle Clone"""
        embed = generate_puzzle_embed(ctx.author, random_puzzle_id())
        await ctx.reply(embed=embed, mention_author=False)


    @play.command(name="id")
    async def play_id(self,ctx: commands.Context, puzzle_id: int):
        """Play a game of Wordle Clone by its ID"""
        embed = generate_puzzle_embed(ctx.author, puzzle_id)
        await ctx.reply(embed=embed, mention_author=False)


    @play.command(name="daily")
    async def play_daily(self,ctx: commands.Context):
        """Play the daily game of Wordle Clone"""
        embed = generate_puzzle_embed(ctx.author, daily_puzzle_id())
        await ctx.reply(embed=embed, mention_author=False)





    @commands.Cog.listener()
    async def on_message(self,message: nextcord.Message):
        """
        When a message is sent, process it as a guess.
        Then, process any commands in the message if it's not a guess.
        """
        processed_as_guess = await process_message_as_guess(self.bot, message)
        

def setup(bot):
    bot.add_cog(wordle(bot))
