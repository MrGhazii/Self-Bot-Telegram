# -*-coding:utf8-*-
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import *
import os
from datetime import datetime,date
import asyncio
from pyrogram.raw import functions
import requests
import random
import schedule
import time
import psutil
import pytz
from pyrogram.errors import FloodWait
import re
from hurry.filesize import size
import subprocess
#------------------# database #------------------#
# db = peewee.SqliteDatabase('MyDatabase')

# class User(peewee.Model):
#     class Meta:
#         database =db
#         name = peewee.CharField()
#         chat_id = peewee.IntegerField()
#         status =peewee.CharField()

#Bot Info
Api_id = 10738780
Api_Hash = '2d62c557a5c027d591c281f27d9f8a2c'
Admin = 5097492329
client = Client('Self' , Api_id , Api_Hash)

#------------------# Ping Pong #------------------#
@client.on_message()
async def main(_:Client,m:Message):
    
    text = m.text


    if text == 'Ping':
        mychar = ''
        for char in 'PONG':
            mychar+= char
            await m.edit(f'**{mychar}**')

    if text == 'Online':
        await m.edit('**yₒᵤᵣ ₛₑₗf ᵢₛ ₒₙₗᵢₙₑ**')

    if text == 'Speed Test':
        await m.edit(1)
        await m.edit(2)
        await m.edit(3)
        await m.edit(4)
        await m.edit(5)
        await m.edit(6)
        await m.edit(7)
        await m.edit(8)
        await m.edit(9)
        await m.edit(10)
        await m.edit('''
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
''')
        await m.edit('''
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
''')
        await m.edit('''
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
''')
        await m.edit('''
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
''')
        await m.edit('''
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
''')
        await m.edit('''
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
''')
        await m.edit('''
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥
''')
        await m.edit('''
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟥🟥🟥🟥🟥🟥🟥🟥
''')
        await m.edit('''
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟩🟩🟩🟩🟩🟩🟩🟩🟩
''')
        await m.edit('S')
        await m.edit('Sp')
        await m.edit('Spe')
        await m.edit('Spee')
        await m.edit('Speed')
        await m.edit('Speed T')
        await m.edit('Speed Te')
        await m.edit('Speed Tes')
        await m.edit('Speed Test')
        await m.edit('Speed Test C')
        await m.edit('Speed Test Co')
        await m.edit('Speed Test Com')
        await m.edit('Speed Test Comp')
        await m.edit('Speed Test Compl')
        await m.edit('Speed Test Comple')
        await m.edit('Speed Test Complet')
        await m.edit('Speed Test Complete')
        await m.edit('Speed Test Completed')
        await m.edit('Speed Test Completed ✅')


    if text == 'Memory':
        # total = psutil.virtual_memory().total
        await m.edit(f'''
〰️Memory〰️

Total : {size(psutil.virtual_memory().total)}B

Available : {size(psutil.virtual_memory().available)}B

Usage : {psutil.virtual_memory().percent}MB

Used : {size(psutil.virtual_memory().used)}B    
''')

    if text == 'Id':
        id = m.reply_to_message.from_user.id
        await m.edit(f'`{id}`')





#------------------# Help #------------------#
@client.on_message(filters.user(Admin),group=1)
async def help(_:Client,m:Message):

    text = m.text

    if text == 'Help':
        await m.edit('''
〰️Self Help List〰️

`Tools` -> امکانات

➖➖➖➖➖➖➖

`Group` -> راهنما گروه

➖➖➖➖➖➖➖

`Account` -> راهنما اکانت

➖➖➖➖➖➖➖

`Fun` -> راهنمای سرگرمی

➖➖➖➖➖➖➖

`Evall` -> کد تستر

➖➖➖➖➖➖➖

`Action` -> اکشن ها

➖➖➖➖➖➖➖

`Enemy` -> منو افزودن دشمن
        
➖➖➖➖➖➖➖
        
Created By @mrqhazi
''')

    if text == 'Tools':
        await m.edit('''
〰️Tools〰️

`Ping or Online` -> وضعیت آنلاینی

`Speed Test` -> تست سرعت

`Status` -> تاریخ

`Memory` -> مصرف رم



`Time` -> زمان

`Id` [reply] -> ایدی عددی فرد

`Boldmode` [On & Off] -> بولد متن

`Spoiler` [Text] -> نوشتن متن با اسپویلر

`Reaction` [emoji] -> ری اکشن به پیام

`Font` [Name] -> فونت اسم

`Lock Pv` -> قفل پیوی

`Unlock Pv` -> بازکردن پیوی

`Join` [link without @] -> عضویت در گروه
        
`Leave` -> ترک گروه

`Create SuperGroup` [Name] -> ساخت گروه

`Delete SuperGroup` -> حذف گروه

`Create Channel` [Name] -> ساخت کانال

`Delete Channel` -> حذف کانال
''')


    if text == 'Group':
        await m.edit('''
〰️Channel & Group〰️      
        
`Pin` & `Unpin` [reply] -> پین و حذف پین 

`Unpin All` [reply] -> حذف تمامی پیام های پین شده

`Ban` [reply] -> اخراج فرد 

`Change Photo` [reply] ->  تنظیم عکس گروه و کانال

`Delete Photo` ->  حذف عکس گروه و کانال

`Change Username` [username] -> تغییر یوزرنیم گروه و کانال

`Change Title` [Title] -> تغییر اسم گروه و کانال

`Change Description` [Description] -> تغییر بیو گروه و کانال

`Slow Mode` [Seconds] -> تنظیم حالت آهسته بر حسب ثانیه

`Slow Mode 0` -> خاموش کردن حالت آهسته  
              
''')

    if text == 'Account':
        await m.edit('''
〰️Account〰️       
        
`Change Name` [text] -> تعویض اسم اکانت

`Delete Name` -> حذف اسم اکانت

`Change Bio` [text] -> تعویض بیو

`Delete Bio` -> حذف بیو اکانت  

`Block` [Reply] -> بلاک کردن
''')

    if text == 'Fun':
        await m.edit('''
〰️Fun〰️     

`Bk` -> بکیرم
        
`Balon` -> بادکنک

`Rb` [emoji]

`Heart` -> قلب

`heart2` -> قلب 2

`heart3` -> قلب 3

`Progress` -> پیشروی
''')

    if text == 'Evall':
        await m.edit('''
〰️Eval〰️     

/py3
`your code here`
''')

    if text == 'Action':
        await m.edit('''
〰️Action〰️ 

`Typing` [On & Off] -> حالت تایپینگ

`Playing` [On & Off] -> حالت بازی

`Upload Photo` [On & Off] -> حالت اپلود عکس

''')

    if text == 'Enemy':
        await m.edit('''
〰️Enemy〰️        
       
`Add Enemy` [Reply] -> افزودن انمی

`Enemy List` -> لیست انمی 

`Clear Enemy List` -> حذف تمامی ایدی ها

`Enemy On` -> فعال کردن حالت انمی

`Enemy Off` -> غیرفعال کردن حالت انمی               
''')
# #------------------# BoldMode #------------------#
@client.on_message(filters.me,group=2)
async def bold(_:Client,m:Message):
    text = m.text
    try:
        if os.path.exists('Boldmode.txt'):
            mode = open('Boldmode.txt').read()
            
        else:
            mode = 'Off'
        
        if mode == 'On':
            await m.edit(f'**{text}**')
        if text.startswith('Boldmode'):
            command = text.replace('Boldmode ','')
            
            if command in ('On','Off'):
                open('E:\Python\MyProject\Cli\Boldmode.txt','w',encoding='utf8').write(command)
                
                if command == 'On':
                    char = 'روشن'
                    await m.edit(f'**حالت بولد {char} شد ✅**')
                else:
                    char = 'خاموش'
                    await m.edit(f'**حالت بولد {char} شد ❌**')
    except:
        pass

#------------------# Time And Status #------------------#
@client.on_message(filters.me,group=3)
async def status(_:Client,m:Message):
    text = m.text

    time_h = datetime.now().strftime('%H') #hour
    time_m = datetime.now().strftime('%M') #minute
    time_s = datetime.now().strftime('%S') #second
    time_d = datetime.now().strftime('%A')  #day
    time_mo = datetime.now().strftime('%B') #Month
    datetoday = date.today()
    time = f'{time_h} : {time_m} : {time_s}'

    if text == 'Time': #show time
        await m.edit(f'⌚️Time : {time}')
    
    elif text == 'Status': #today status
        await m.edit(f'''Today Status

📅Date : {datetoday}

⌚️Time : {time}

☀️Day : {time_d}

♋️Month : {time_mo}
''')

    # try:
    #     while True:
    #         now = datetime.now(pytz.timezone('Asia/Tehran'))
    #         time = now.strftime('%H:%M')
    #         new_name = f'| {time}'

    #         await asyncio.sleep(50)
    #         await client.update_profile(last_name=new_name)
    #         # print('profile updated')
    # except FloodWait as e:
        
    #     print(e)
    #     # await client.send_message(-1001625272240,'Have To Sleep '+e.seconds+' Seconds')
    #     await asyncio.sleep(e.x)

# #------------------# Love #------------------#
@client.on_message(filters.me,group=4)
async def love(_:Client,m:Message):

    text = m.text


#------------------#  pv Lock Unlock #------------------#
@client.on_message(filters.private,group=5)
async def lock(_:Client,m:Message):
    text = m.text
    #lock pv
    if text == 'Lock Pv':
        open('pv','w').write('yes')
        await m.edit('**Lock Pv Enable** 🔒')
    #unlock pv
    if text == 'Unlock Pv':
        open('pv','w').write('no')
        await m.edit('**Lock Pv Disable** 🔓')
    #delete message
    lock = open('pv').read()
    islock = True if lock == 'yes' else False
    if islock:
        await m.delete()

#------------------#  Action #------------------#
@client.on_message(filters.private,group=6)
async def Action(_:Client,m:Message):
    text = m.text
    chat_id = m.chat.id
    user = m.from_user.id

#Typing
    if user == Admin:
        if text == 'Typing On':
            open('typing mode','w').write('on') #write 'on' in file
            await m.edit('**Typing Mode Enable**')

        if text == 'Typing Off':
            open('typing mode','w').write('off') #write 'off' in file
            await m.edit('**Typing Mode Disable**')
    
    typing = open('typing mode').read() #read file
    on_or_off = True if typing == 'on' else False #

    if on_or_off and m.chat.type == 'private':
        await client.send_chat_action(chat_id ,'typing')
 
#Playing
    if user == Admin:
        if text == 'Playing On':
            open('Playing','w').write('on') #write 'on' in file
            await m.edit('**Playing Mode Enable**')

        if text == 'Playing Off':
            open('playing','w').write('off') #write 'off' in file
            await m.edit('**Playing Mode Disable**')
    
    playing = open('Playing').read() #read file
    ply = True if playing == 'on' else False #

    if ply and m.chat.type == 'private':
        await client.send_chat_action(chat_id ,'playing')

#upload
    if user == Admin:
        if text == 'Upload Photo On':
            open('Upload_Photo','w').write('on') #write 'on' in file
            await m.edit('**Upload Photo Mode Enable**')

        if text == 'Upload Photo Off':
            open('Upload_Photo','w').write('off') #write 'off' in file
            await m.edit('**Upload Photo Mode Disable**')
    
    sp = open('Upload_Photo').read() #read file
    speak = True if sp == 'on' else False #

    if speak and m.chat.type == 'private':
        await client.send_chat_action(chat_id ,'upload_photo')

#cancel

    if user == Admin:
        if text == 'Cancel Action':
            await client.send_chat_action(chat_id, 'cancel')
            await m.edit('**All Chat Action Removed**')

# #------------------# enemy #------------------#
@client.on_message(filters.user(Admin),group=7)
async def enemypanel(_:Client,m:Message):

    text = m.text
    chat_id = m.chat.id
    user = m.from_user.id
        
#enemy mode (on or off)
    if text == 'Enemy On':
        open('enemy','w').write('on')
        await m.edit('**Enemy Mode Enable**')
        
    if text == 'Enemy Off':
        open('enemy','w').write('off')
        await m.edit('**Enemy Mode Disable**')


#add enemy
    try:
        if text == 'Add Enemy':
            user_id = m.reply_to_message.from_user.id 
            open('enemylist','a+').write('\n'+str(user_id))
            await m.edit('**User Added To EnemyList**')
    except Exception as err:
            channel_chat_id = '-1001625272240'
            await client.send_message(channel_chat_id ,err)

#Show Enemy List
    if text == 'Enemy List':
        enemylist = open('enemylist',encoding='utf8').read()
        if len(enemylist) > 1:
            await m.edit(enemylist)
        elif len(enemylist) < 1:
            await m.edit('**Enemy List Empty**')

#clear enemy list
    if text == 'Clear Enemy List':
        open('enemylist','w').flush()
        await m.edit('**Enemy List Has Been Clear**')


#------------------# enemy run #------------------#
@client.on_message(group=8)
async def enemy(_:Client,m:Message):
    text = m.text
    chat_id = m.chat.id


    fosh = [
    
'''کص ننت''',
'''محو نشو کیری''',
'''کیرم تو ناموس مادرت باع''',
'''مادر استعفا دهنده از کارخونه ي برازرز بالا  باش''',
'''کوشی پس بیناموص بالا باش''',
'''مادر کصع مگ باتو نیسم میگم بالا باش ''',
'''خارکصده مادر زیر خاب''',
'''کیری بی هویت ناموص کیر دزد بالا میگم''',
'''داش ناموصتو خوردم نمیخای بیای بالا''',
'''خیخیخیخخیخیخخیخیخیخخیخیخیخخیخیخی''',
'''تو گه خوردی اومدی پیوی شاخ شدی''',
'''چرا رفتي تو کس ننت؟''',
'''چرا خايه هامو زخم کردي؟''',
'''ناموس کص ممبر بالا باش تو دیدم باش ناموس فشاری شده''',
'''دارم مادرتو میگام بی ناموس''',
'''خخخخخخخخخخخخخخخخخخخخخخخخخخخخخخ''',
'''ناموس يتيم در يتيم خانه بالا باش''',
'''لش ناموص مگه ب این سادگیاس در رفتن''',
'''کیر ب کص یوری مادرت بره بیناموص ممبرک''',
'''کیرم تو کص ناموست بره الهی''',
'''تخخخخخخخخخخخخخخخخخخخخ''',
'''چرا نميبينمت توي بيناموسو؟''',
'''ای ترسو ممبر بی هویت رفتی تو کص ننت قایم شدی ؟''',
'''ميگم کصصصص ننتتتتتت''',
'''مادر بی هویت بالا باش بت میگم''',
'''ناموص گراز راهی برای فرار نداری''',
'''کصصصصصصصصصصصصصصصصص ننتتتتتتتتتتتتت''',
'''بالا باش کص ممبر''',
'''مادر زجه زن کیر خور''',
'''خخخخخخخخخخخخخخخخخخخخخخخخ''',
'''داش چص تایپ شدی رف بالا باش تایپ بده''',
'''چرا انق زیر کیرمی داش نمیرسی بم خخخ''',
'''باید پا بزنی برسی رسیدن به من به این سادگی نیص چصک''',
'''تو چيت به من ميخوره اخه''',
'''مادرتو گاييدم فرار نکن گفتم''',
'''پخخخخخخخخخخخخخخخخخخخخخخخخ'''

]


#run
    try:
        enemy_status = open('enemy').read() #enemy on & off status
        on_or_off = True if enemy_status == 'on' else False

        send = random.choice(fosh)
        
        enemylist = open('enemylist').read() #lists of enemy id
        
        
        if on_or_off:
            if str(m.from_user.id) in enemylist: #search for user id in enemylist
                await m.reply_text(send)
    except:
        pass


#------------------# account #------------------#
@client.on_message(filters.me,group=9)
async def account(_:Client,m:Message):
    try:

        text = m.text
        chat_id = m.chat.id
        user = m.from_user.id

#Change Name
        if text.startswith('Change Name'):
            name = text.replace('Change Name ','')
            await client.update_profile(first_name=name)
            await m.edit('**Your Name Has Been Changed**')
#Delete Name
        if text == 'Delete Name':
            await client.update_profile(first_name='ㅤㅤㅤㅤㅤ')
            await m.edit('**Your Name Has Been Deleted**')
            
#change Bio
        if text.startswith('Change Bio'):
            mybio = text.replace('Change Bio ','')
            await client.update_profile(bio=mybio)
            await m.edit('**Your Bio Has Been Changed**')
#Delete Bio
        if text == 'Delete Bio':
            await client.update_profile(bio='')
            await m.edit('**Your Bio Has Been Deleted**')
#Block User
        if text == 'Block':
            # print(m)
            await client.block_user(user_id= m.reply_to_message.from_user.id)
            await m.edit('**User Has Been Blocked**')
    except:
        pass

#------------------# Font #------------------#
@client.on_message(filters.me,group=10)
async def font(_:Client,m:Message):
    try:
        text = m.text
        chat_id = m.chat.id

        if text.startswith('Font'):
            textrep = text.replace('Font ','')
            font = requests.get(f"http://api.codebazan.ir/font/?text={textrep}") #web services
            await m.edit(font.text) #show font


        if text.startswith('Spoiler'):
            message_id = m.message_id

            spoil = text.replace('Spoiler ','')
            await client.send_message(chat_id,f'|| {spoil} ||')
            await client.delete_messages(chat_id,message_id) #delete Spoiler text

        if text.startswith('Reaction'):
            reaction = text.replace('Reaction ','')
            await client.send_reaction(chat_id,m.reply_to_message.message_id,f'{reaction}')


    except:
        pass
        
        
#------------------# Channel & Group #------------------#
@client.on_message(filters.me,group=11)
async def group(_:Client,m:Message):
    try:
        text = m.text
        chat_id = m.chat.id #get chat id
        # user_id = m.reply_to_message.from_user.id #get user id
        # message_id = m.reply_to_message.message_id #reply message id
        # photo = m.reply_to_message.photo.file_id
            
            
#join group
        
        if text.startswith('Join'):
            chat = text.replace('Join ','')
            await client.join_chat(chat)
            await m.edit('**Join Successful**')

#leave chat
        if text =='Leave':
            await client.leave_chat(chat_id)
            await m.edit('**Leave Successful**')

#pin 
        if text == 'Pin':
            
            await client.pin_chat_message(chat_id,message_id=m.reply_to_message.message_id)
            await m.edit('**Pin Successful**')
#unpin
        if text == 'Unpin':
            
            await client.unpin_chat_message(chat_id,message_id=m.reply_to_message.message_id)
            await m.edit('**Pin Successful Removed**')
#unpin All
        if text == 'Unpin All':
            
            await client.unpin_all_chat_messages(chat_id)
            await m.edit('**All Pin Successful Removed**')
#ban member
        if text == 'Ban':
            await client.kick_chat_member(chat_id,user_id= m.reply_to_message.from_user.id)
            await m.edit('**User Has Been Baned**')
#unban member
        if text == 'Unban':
            await client.unban_chat_member(chat_id,user_id= m.reply_to_message.from_user.id)
            await m.edit('**User Unban Successful**')
#set group photo
        if text == 'Change Photo':
            await client.set_chat_photo(chat_id,photo= m.reply_to_message.photo.file_id)
            await m.edit('**Photo Change Successful**')
#delete group photo
        if text == 'Delete Photo':
            await client.delete_chat_photo(chat_id)
            await m.edit('**Photo Delete Successful**')
#update chat username
        if text.startswith('Change Username'):
            username = text.replace('Change Username ','')
            await client.update_chat_username(chat_id,username)
            await m.edit('**Username Change Successful**')
#create channel
        if text.startswith('Create Channel'):
            title1 = text.replace('Create Channel ','')
            await client.create_channel(title1,description= 'This Channel Created By Self')
            await m.edit('**Channel Successfuly Created**')
#Delete channel
        if text == 'Delete Channel':
            await client.delete_channel(chat_id)
            await m.edit('**Channel Successfuly Deleted**')
#Create SuperGroup
        if text.startswith('Create SuperGroup'):
            SuperGroup = text.replace('Create SuperGroup ','')
            await client.create_supergroup(SuperGroup,description= 'This SuperGroup Created By Self')
            await m.edit('**SuperGroup Successfuly Created**')
#Delete SuperGroup
        if text.startswith('Delete SuperGroup'):
            await client.delete_supergroup(chat_id)
            await m.edit('**SuperGroup Successfuly Deleted**')
#Change Title
        if text.startswith('Change Title'):
            title2 = text.replace('Change Title ','')
            await client.set_chat_title(chat_id,title2)
            await m.edit('**Title Successfuly Changed**')
#Change Description
        if text.startswith('Change Description'):
            des = text.replace('Change Description ','')
            await client.set_chat_description(chat_id,des)
            await m.edit('**Description Successfuly Changed**')
#Slow Mode
        if text.startswith('Slow Mode'):
            sec = text.replace('Slow Mode ','')
            await client.set_slow_mode(chat_id,int(sec))
            await m.edit('**Slow Mode Set Successful**')

    except:
        pass

#------------------# Sargarmi #------------------#
@client.on_message(filters.me,group=12)
async def sargarmi(_:Client,m:Message):

    text = m.text
    chat_id = m.chat.id
#Bk
    if text == 'Bk':
        await m.edit('''
🤤🤤🤤🤤
🤤         🤤
🤤           🤤
🤤        🤤
🤤🤤🤤🤤
🤤         🤤
🤤           🤤
🤤           🤤
🤤        🤤
🤤🤤🤤🤤
''')
        await asyncio.sleep(1)

        await m.edit('''
😂         😂
😂       😂
😂     😂
😂   😂
😂😂
😂   😂
😂      😂
😂        😂
😂          😂
😂            😂
''')

#Balon
    if text == 'Balon':
        await m.edit('🌵ــــــــــــــــــــــــــــــــــ🎈')
        await m.edit('🌵ـــــــــــــــــــــــــــــــــ🎈')
        await m.edit('🌵ــــــــــــــــــــــــــــــــ🎈')
        await m.edit('🌵ـــــــــــــــــــــــــــــــ🎈')
        await m.edit('🌵ــــــــــــــــــــــــــــــ🎈')
        await m.edit('🌵ـــــــــــــــــــــــــــــ🎈')
        await m.edit('🌵ــــــــــــــــــــــــــــ🎈')
        await m.edit('🌵ـــــــــــــــــــــــــــ🎈')
        await m.edit('🌵ــــــــــــــــــــــــــ🎈')
        await m.edit('🌵ـــــــــــــــــــــــــ🎈')
        await m.edit('🌵ـــــــــــــــــــــــ🎈')
        await m.edit('🌵ـــــــــــــــــــــ🎈')
        await m.edit('🌵ـــــــــــــــــــ🎈')
        await m.edit('🌵ـــــــــــــــــ🎈')
        await m.edit('🌵ـــــــــــــــ🎈')
        await m.edit('🌵ــــــــــــ🎈')
        await m.edit('🌵ــــــــــ🎈')
        await m.edit('🌵ـــــــــ🎈')
        await m.edit('🌵ــــــــ🎈')
        await m.edit('🌵ــــــ🎈')
        await m.edit('🌵ــــ🎈')
        await m.edit('🌵ـــ🎈')
        await m.edit('🌵ــ🎈')
        await m.edit('🌵ـ🎈')
        await m.edit('🌵💥🎈')
        await m.edit('💥Bommmm💥')

#Rb

    if text.startswith('Rb'):
        rb = text.replace('Rb ','')
        
        await m.edit(f'''
(\_/)
( •.• )
({rb})
''')


#Heart


    if text == 'Heart':
        await m.edit('❤️')
        await asyncio.sleep(3)
        await m.edit('💙')
        await asyncio.sleep(3)
        await m.edit('💛')
        await asyncio.sleep(3)
        await m.edit('💚')
        await asyncio.sleep(3)
        await m.edit('🤎')
        await asyncio.sleep(3)
        await m.edit('🧡')
        await asyncio.sleep(3)
        await m.edit('🤍')
        await asyncio.sleep(3)
        await m.edit('🖤')
        await asyncio.sleep(3)
        await m.edit('❣️')
        await asyncio.sleep(3)
        await m.edit('💜')
        await asyncio.sleep(3)
        await m.edit('💞')
        await asyncio.sleep(3)
        await m.edit('💕')
        await asyncio.sleep(3)
        await m.edit('💗')
        await asyncio.sleep(3)
        await m.edit('💓')
        await asyncio.sleep(3)
        await m.edit('💝')
        await asyncio.sleep(3)
        await m.edit('💖')
        await asyncio.sleep(3)
        await m.edit('My heart beats only for you🚶🏾‍♂️♥️')
        await asyncio.sleep(30)
        await m.delete()

    if text == 'Heart2':
        await m.edit('❤️💙')
        await asyncio.sleep(1)
        await m.edit('💙❤️')
        await asyncio.sleep(1)
        await m.edit('💛💚')
        await asyncio.sleep(1)
        await m.edit('💚💛')
        await asyncio.sleep(1)
        await m.edit('🧡🤎')
        await asyncio.sleep(1)
        await m.edit('🤎🧡')
        await asyncio.sleep(1)
        await m.edit('🖤🤍')
        await asyncio.sleep(1)
        await m.edit('🤍🖤')
        await asyncio.sleep(1)
        await m.edit('💜❣️')
        await asyncio.sleep(1)
        await m.edit('❣️💜')
        await asyncio.sleep(1)
        await m.edit('💕💞')
        await asyncio.sleep(1)
        await m.edit('💞💕')
        await asyncio.sleep(1)
        await m.edit('💓💗')
        await asyncio.sleep(1)
        await m.edit('💗💓')
        await asyncio.sleep(1)
        await m.edit('💖💝')
        await asyncio.sleep(1)
        await m.edit('💝💖')
        await asyncio.sleep(1)
        await m.edit('🖤')

#Heart2
    if text == 'Heart3':
        
        await m.edit('💚💛🧡❤️')
        await asyncio.sleep(1)
        await m.edit('💙💚💜🖤')
        await asyncio.sleep(1)
        await m.edit('❤️🤍🧡💚')
        await asyncio.sleep(1)
        await m.edit('🖤💜💙💚')
        await asyncio.sleep(1)
        await m.edit('🤍🤎❤️💙')
        await asyncio.sleep(1)
        await m.edit('🖤💜💚💙')
        await asyncio.sleep(1)
        await m.edit('💝💘💗💘')
        await asyncio.sleep(1)
        await m.edit('❤️🤍🤎🧡')
        await asyncio.sleep(1)
        await m.edit('💕💞💓🤍')
        await asyncio.sleep(1)
        await m.edit('💜💙❤️🤍')
        await asyncio.sleep(1)
        await m.edit('💙💜💙💚')
        await asyncio.sleep(1)
        await m.edit('🧡💚🧡💙')
        await asyncio.sleep(1)
        await m.edit('💝💜💙❤️')
        await asyncio.sleep(1)
        await m.edit('💞🖤💙💚')
        await asyncio.sleep(1)
        await m.edit('💛🧡❤️💚')

#Progress

    if text == 'Progress':
        await m.edit('**Progress started**')
        await asyncio.sleep(1)
        await m.edit('▪️10%')
        await m.edit('▪️▪️20%')
        await m.edit('▪️▪️▪️30%')
        await m.edit('▪️▪️▪️▪️40%')
        await m.edit('▪️▪️▪️▪️▪️50%')
        await m.edit('▪️▪️▪️▪️▪️▪️60%')
        await m.edit('▪️▪️▪️▪️▪️▪️▪️70%')
        await m.edit('▪️▪️▪️▪️▪️▪️▪️▪️80%')
        await m.edit('▪️▪️▪️▪️▪️▪️▪️▪️▪️90%')
        await m.edit('▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️100%')
        await m.edit('**Progress Completed ✅**')


#------------------# Eval #------------------#
# @client.on_message(filters.me,group=13)
# def txt(_:Client,m:Message):
#     chat_id = m.chat.id
#     try:
#         text = m.text

#         if text.startswith('/py3'):
#             command = text.replace('/py3\n','')
#             ev = eval(command)
#             m.edit(f'''
# Eval Input :

# `{command}`
            
# Eval Output :
# `{m.outgoing}`
# ''')
            
#         print(ev)
#     except UnboundLocalError:

#         pass
#     except Exception as error:

#         m.edit(f'''
# Eval Input :

# `{command}`
            
# Eval Output :
# `{error}`
# ''')

#------------------# Spammer Count #------------------#
@client.on_message(filters.me,group=14)
async def txt(_:Client,m:Message):
    text = m.text
    chat_id = m.chat.id

    if text.startswith('Spammer Count'):
        spammer = text.replace('Spammer Count ','')
        open('Spammer','w').write(spammer)
        await m.edit(f'**Spammer Count Set Successful**')

#------------------# Run Spammer#------------------#
@client.on_message(filters.user(Admin),group=15)
async def txt(_:Client,m:Message):
    text = m.text
    chat_id = m.chat.id


    if text.startswith('Spam'):
        val = text.replace('Spam ','')
        count = open('Spammer').read()

        # for i in val:
        #     await client.send_message(chat_id,f'{val}')


        # value = 0
        # while value < int(count) :
        #     await client.send_message(chat_id,f'salam')
        #     time.sleep(0.3)
        #     value += 1

        





    # now = datetime.now(pytz.timezone('Asia/Tehran'))
#     time = now.strftime('%H:%M')
#     new_name = f'| {time}'

#     # await asyncio.sleep(50)
#     pyrogram.raw.functions.account.UpdateProfile(
#         first_name='⸸ʳᵉᶻᵃ⸼',
#         last_name= new_name
#     )
#     # print('profile updated')

# schedule.every(60).seconds.do(txt)
    
    # print('namal')

    # if text == 'Usage':
    #     mem = str(psutil.virtual_memory()[3])
    #     memory = mem[0:1]
    #     memo = mem[1:4]
    #     await m.edit('Ram Usage : '+memory+'.'+memo)
    #     print(memory)
    #     await m.edit('Ram Usage : '+str(mem))



#     text = m.text
#     IS_LOOP_RUNNING = True

    # if text.startswith == '!timebio':
    #     on_or_off = text.replace('!timebio ','').strip()
    #     if on_or_off in ('on','off'):
    #         IS_LOOP_RUNNING = True if on_or_off == 'on' else False
    #         if on_or_off == 'on':
    #             action = 'روشن'
    #         else:
    #             action = 'خاموش'
    #         await m.edit('ساعت بیو {action} شد')




        
        
        





        # while True:
        #     await asyncio.sleep(200)
        #     channel_chat_id = '-1001625272240'
        #     await client.send_message(channel_chat_id ,flood)

print('started')
client.run()