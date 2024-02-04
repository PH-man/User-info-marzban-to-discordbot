# bot.py

import discord
from discord.ext import commands, tasks
import datetime
import requests
from config import TOKEN, REPORT_CHANNEL_ID, LOG_CHANNEL_ID, LOGIN_URL, SECURE_URL, SYSTEM_URL, USERNAME, PASSWORD, API_BASE_URL ,MY_AD

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
info_command_count = 0

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await bot.change_presence(activity=discord.Game(name="type !vpn for more info"))
    daily_reset.start()
    print('------')

@bot.command(name='vpn')
async def display_telegram_url(ctx):
    global info_command_count
    info_command_count += 1
    await ctx.send(f'{MY_AD}')

@bot.command(name='dailyreport')
@commands.is_owner()
async def daily_report(ctx):
    global info_command_count
    channel = bot.get_channel(REPORT_CHANNEL_ID)
    await channel.send(f'Daily !vpn command count: {info_command_count}')

@tasks.loop(hours=24)
async def daily_reset():
    global info_command_count
    info_command_count = 0

@bot.command(name='log')
@commands.is_owner()
async def log_system_data(ctx):
    payload = {
        'username': USERNAME,
        'password': PASSWORD
    }

    response = requests.post(LOGIN_URL, data=payload)

    if response.status_code == 200:
        access_token = response.json().get('access_token')

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        system_response = requests.get(SYSTEM_URL, headers=headers)

        if system_response.status_code == 200:
            system_data = system_response.json()
            log_channel = bot.get_channel(LOG_CHANNEL_ID)
            await log_channel.send("System Information:")
            await log_channel.send(f"⚙️Version: {system_data['version']}")
            await log_channel.send(f"🔋 Total Memory: {system_data['mem_total'] / (1024 ** 2):.2f} MB")
            await log_channel.send(f"🪫Used Memory: {system_data['mem_used'] / (1024 ** 2):.2f} MB")
            await log_channel.send(f"🚀 CPU Cores: {system_data['cpu_cores']}")
            await log_channel.send(f"☄️ CPU Usage: {system_data['cpu_usage']}%")
            await log_channel.send(f"💰💳 Total Users: {system_data['total_user']}")
            await log_channel.send(f"🌐 Active Users: {system_data['users_active']}")
            await log_channel.send(f"💾 Incoming Bandwidth: {system_data['incoming_bandwidth'] / (1024 ** 3):.2f} GB")
            await log_channel.send(f"💾 Outgoing Bandwidth: {system_data['outgoing_bandwidth'] / (1024 ** 3):.2f} GB")
            await log_channel.send(f"⚡️ Incoming Bandwidth Speed: {system_data['incoming_bandwidth_speed'] / 1e6:.2f} Mbps")
            await log_channel.send(f"⚡️ Outgoing Bandwidth Speed: {system_data['outgoing_bandwidth_speed'] / 1e6:.2f} Mbps")
            await log_channel.send(f"--------------------------------------------")
        else:
            print(system_response.content)  # Print the response content for debugging
            await ctx.send(f"System request failed with status code: {system_response.status_code}")
    else:
        print(response.content)  # Print the response content for debugging
        await ctx.send(f"Login failed with status code: {response.status_code}")

USER_API_BASE_URL = f'{API_BASE_URL}user/'  # Constructing the complete user API base URL

@bot.command(name='userdetail')
async def user_detail(ctx, name):
    payload = {
        'username': USERNAME,
        'password': PASSWORD
    }

    response = requests.post(LOGIN_URL, data=payload)

    if response.status_code == 200:
        access_token = response.json().get('access_token')

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        user_api_url = f'{API_BASE_URL}{name}'  # Constructing the complete user API URL
        user_response = requests.get(user_api_url, headers=headers)

        if user_response.status_code == 200:
            user_data = user_response.json()
            used_traffic_gb = user_data.get('used_traffic', 0) / (1024 ** 3)
            data_limit_gb = user_data.get('data_limit', 0) / (1024 ** 3)
            lifetime_used_traffic_gb = user_data.get('lifetime_used_traffic', 0) / (1024 ** 3)
            expire_timestamp = user_data.get('expire', 0)
            expire_date = datetime.datetime.utcfromtimestamp(expire_timestamp).strftime('%Y-%m-%d %H:%M:%S')

            # sending detail to user private massage
            await ctx.author.send(f"User Details for {name}:\n"
                                  f"Used Traffic: {used_traffic_gb:.2f} GB\n"
                                  f"Data Limit: {data_limit_gb:.2f} GB\n"
                                  f"Lifetime Used Traffic: {lifetime_used_traffic_gb:.2f} GB\n"
                                  f"Expire Date: {expire_date}")
        else:
            print(user_response.content)  # Print the response content for debugging
            await ctx.send(f"User request failed with status code: {user_response.status_code}")
    else:
        print(response.content)  # Print the response content for debugging
        await ctx.send(f"Login failed with status code: {response.status_code}")

bot.run(TOKEN)
