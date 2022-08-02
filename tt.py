from email import message
from pyrogram import Client
from datetime import datetime,date
import schedule
import time
import random
Api_id = 16974894
Api_Hash = 'a060e978a4868ca6fb59169dd219b7e4'
Admin = 2052217736
client = Client('Self' , Api_id , Api_Hash)

try:
    def job():
        with client:
            

            listtxt = [
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
            tex = random.choice(listtxt)
            print(tex)
            client.send_message(1098371330,tex)


    # schedule.every().day.at('19:31').do(job)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
except Exception as err:
    print(err)



client.run()
print('Client Started')