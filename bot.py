import asyncio
import discord
from discord.ext import commands
import logging
from aiogram import Bot, Dispatcher, executor, types


tg_tkn = 'YOUR_TELEGRAM_BOT_TOKEN'
tg_bot = Bot(tg_tkn)
dp = Dispatcher(tg_bot)
 
ds_tkn = 'YOU_DISCORD_BOT_TOKEN'
ds_bot = discord.Client()


event_loop = asyncio.get_event_loop()


@ds_bot.event
async def on_message(ds_message):
    if ds_message.author.id == DISCORD_USER_ID:  #YOU can delete this IF, if you want to everybody could write to your btidge bot 
        global ds_author
        ds_author = ds_message.author
        await tg_bot.send_message(TELEGRAM_USER_ID, ds_message.content)
    await asyncio.sleep(0.5)    
        
@dp.message_handler()
async def echo(message):
    if message.from_user.id == TELEGRAM_USER_ID:  #YOU can delete this IF, if you want to everybody could write to your btidge bot
        await ds_author.send(message.text)
    await asyncio.sleep(0.5)


runall = [
        asyncio.ensure_future(ds_bot.start(ds_tkn, bot=True, reconnect=True)),
        asyncio.ensure_future(executor.start_polling(dp, loop=event_loop, skip_updates=True))
        ]

event_loop.run_forever(asyncio.gather(*runall))
