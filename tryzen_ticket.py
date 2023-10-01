import sys
import discord
from discord.ui import Button, View
from discord.ext import commands
import asyncio
from config import *
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

GUILD_ID = 1137523440098746452
TEAM_ROLE =  1137523440459468849
TICKET_CHANNEL =  1137523442774712379
CATEGORY_ID =  1142232880995631104

@bot.event
async def on_ready():
    print("[Tryzen -  Systems] Ticket Bot ist online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="system.secondv.de"))


@bot.command('ticketmodul')
@commands.is_owner()
async def ticketmsg(ctx):
    button1 = Button(label="📩Allgemeine Anfragen", style=discord.ButtonStyle.blurple, custom_id="ticket_button")
    button2 = Button(label="🏛Fraktion und Unternehmen", style=discord.ButtonStyle.blurple, custom_id="ticket_button")
    button3 = Button(label="⚙️Bug Meldung", style=discord.ButtonStyle.blurple, custom_id="ticket_button")
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    embed = discord.Embed(color =0xff960f, description=f"Bevor du ein Ticket eröffnest, schaue vorher, ob sich deine Frage mit einem Blick in den Channel #bekannte-fehler oder spieler-helfen-spieler löst", title=f"[Second:V - Ticket System]")
    embed.add_field(name="Wichtig!", value="Sei möglichst präzise und überlege dir vorher, welche Informationen für uns wichtig sein können. Bei einem Bug report bitten wir dich Videos und Bilder direkt mit einzubinden.", inline=False)
    embed.set_author(name="Tryzen95", url="https://twitch.tv/tryzen95", icon_url="https://cdn.discordapp.com/attachments/1138798128510799943/1141502291397070908/Design_ohne_Titel_15.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1138798128510799943/1141502291397070908/Design_ohne_Titel_15.png")
    embed.set_footer(text="©Tryzen95 - Ticket Bot für Second:V")
    channel = bot.get_channel(TICKET_CHANNEL)
    await channel.send(embed=embed, view=view)
    await ctx.reply("[Second:V] Ticket Panel Gesendet!")
  
@bot.event
async def on_interaction(interaction):
    if interaction.channel.id == TICKET_CHANNEL:
        if "ticket_button" in str(interaction.data):
            guild = bot.get_guild(GUILD_ID)
            for ticket in guild.channels:
                if str(interaction.user.mention) in ticket.name:
                    embed = discord.Embed(description=f"Du kannst nur ein Ticket gleichzeitig öffnen!\nHier hast du bereits ein Ticket offen! {ticket.mention}")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    return

            category = bot.get_channel(CATEGORY_ID)
            ticket_channel = await guild.create_text_channel(f"ticket-{interaction.user}", category=category,
                                                            topic=f"Ticket von {interaction.user} \nClient-ID: {interaction.user.id}")

            await ticket_channel.set_permissions(guild.get_role(TEAM_ROLE), send_messages=True, read_messages=True, add_reactions=False,
                                                embed_links=True, attach_files=True, read_message_history=True,
                                                external_emojis=True)
            await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, add_reactions=False,
                                                embed_links=True, attach_files=True, read_message_history=True,
                                                external_emojis=True)
            embed = discord.Embed(description=f'Willkommen im Ticket bei Second:V {interaction.user.mention}!\n'
                                            f'Hier Kannst du gerne deine Probleme und Anliegen mit uns Teilen, Wir versuchen dir so schnell wie Möglich Support zu geben!\n'
                                            f'Ticket mit `!close` schließen!',                                  
                                color =0xff960f)
            embed.set_author(name=f'Neues Ticket!')
            mess_2 = await ticket_channel.send(embed=embed)
            embed = discord.Embed(title="📬 | Ticket geöffnet!",
                                description=f'Dein Ticket wurde erstellt! {ticket_channel.mention}',
                                color=discord.colour.Color.orange()
                                )

            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

@bot.command()
async def close(ctx):
    if "ticket-" in ctx.channel.name:
        embed = discord.Embed(
                description=f'Ticket schließt in 5 Sekunden automatisch!',
                color=16711680)
        await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await ctx.channel.delete()

bot.run(TOKEN) 









