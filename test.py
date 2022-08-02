import time
import schedule
from pyrogram import Client
from datetime import datetime
from pyrogram.types import *


Api_id = 16974894
Api_Hash = 'a060e978a4868ca6fb59169dd219b7e4'
Admin = 2052217736
client = Client('Self' , Api_id , Api_Hash)



@client.on_message(group=12)
async def tm(_:Client,m:Message):


    # async def test():
    time = datetime.now().strftime('%H:%M')
    print(time)


            
    await client.send_message(1098371330,'This Is Test Message')


schedule.every(1).day.do(tm).at('22:20')

while True:
    schedule.run_pending()
    time.sleep(60)



client.run()