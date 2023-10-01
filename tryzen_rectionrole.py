import sys
import discord
import discord.ui
from discord.ui import Button, View
import datetime
from datetime import datetime
from discord.ext import commands
from config import *
import os
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('[Tryzen - System] Reaction Role bot ist Online')
    bot.add_view(Roles())
    
class Roles(discord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
  @discord.ui.button(label = "Verifizieren", custom_id = "Verifizieren", style = discord.ButtonStyle.green)
  async def button1(self, interaction, button):
    role = 1137523440098746453
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("Du hast die Role Entfernt!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("Du hast dich Verifiziert!", ephemeral = True)
          
@bot.command()
async def roles(ctx):
    embed = discord.Embed(color =0xff960f, description=f"» Willkommen auf dem Discord von Second:V™ Du kannst hier mit einer Reaktion auf den Emoji deinen Account Verifizieren.", title=f"Second:V | Verifizierung")
    embed.add_field(name="Wichtig!", value="Mit dem Klick auf die Role Bestätigst du das Discord Server Regelwerk Gelesen und Verstanden zu haben und dich an an die Regeln zu Halten. Viel Spaß und Herzlich Willkommen auf Second:V Roleplay.", inline=False)
    embed.add_field(name="Links", value="Webpage: https://second-v.de/", inline=False)
    embed.set_author(name="Second:V | Tryzen95", url="https://twitch.tv/tryzen95", icon_url="https://cdn.discordapp.com/attachments/1138798128510799943/1141502291397070908/Design_ohne_Titel_15.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1138798128510799943/1141502291397070908/Design_ohne_Titel_15.png")
    embed.set_footer(text="©Tryzen95 - ReactRoleBot für Second:V")
    await ctx.send(embed = embed, view = Roles())
    await ctx.reply("[Second:V] Role Panel Gesendet!")


@bot.command()
async def tsip(ctx):
    await ctx.send('Hier einmal unser TS IP  ts.second-v.de')

@bot.command()
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)
@bot.command()
async def clear10(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return




bot.run(TOKEN) 