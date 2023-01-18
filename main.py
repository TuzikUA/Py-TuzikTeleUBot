from pyrogram import Client, filters
from random import choice
from pyrogram import errors, enums, Client, filters, types
from datetime import datetime
import platform



api_id = 22470515 
api_hash = "7d3f6bce86912dc08944807cd7f09b51"
app = Client("account", api_id, api_hash) 

prefix = '.'

@app.on_message(filters.command('tid',prefixes=prefix) & filters.me)
async def my_handler(client, message):
    print(message)
    
@app.on_message(filters.command('help',prefixes=prefix) & filters.me)  
async def tmat_com(_, msg):
    await msg.edit("Помощь команды: .help список команд .tid получить информацию об чате .tmat куча матов(высер агро школньика) .tjoke рандом андекдот  .treac [количество]поставить реакцию в группе .tinfo информация о юзерботе .tpon текст из слов пон .tpozdr поздравляет пользователя с праздником")


@app.on_message(filters.command('tmat',prefixes=prefix) & filters.me)  
async def tmat_com(_, msg):
    await msg.edit('Заткни свое ебало я тебя в рот ебал блядина ебучая что бы тебя поездом перехуярило тварь ебучая соси хуй пидрила я тебя на хую вертел тварюка хуйлуша ')

from random import choice

jokes = [
  'На соревнованиях по плаванию электрик Олег замкнул тройку лидеров.',
  'Сын червечок подходит к маме "Мам, а где папа?" она отвечает: "C мужиками на рыбалку уехал.".',
  ]

@app.on_message(filters.command('joke',prefixes=prefix) & filters.me)  
async def tmat_com(_, msg):
    await msg.edit(choice(jokes))

@app.on_message(filters.command('treact',prefixes=prefix) & filters.me)
async def reac_com(_,msg: types.Message):

    try:limit = str(msg.text).split(' ')[1]
    except IndexError:await warn(app,msg,'Введите лимит!');return None

    try:emoji = str(msg.text).split(' ')[2]
    except IndexError:emoji = '🔥' 

    try:chat = str(msg.text).split(' ')[3]
    except IndexError:chat = None

    chat_id = msg.chat.id
    await msg.delete()
    async for m in app.get_chat_history(chat_id,int(limit)):
        try:
            await app.send_reaction(chat_id,m.id,emoji)
        except errors.exceptions.bad_request_400.MessageNotModified:
            pass

@app.on_message(filters.command('tinfo',prefixes=prefix) & filters.me)  
async def tinfo_com(_, msg):
    await msg.edit(f"Ваша система: {str(platform.system())} Версия бота: 3.1 gb ссылка на код юзербота https://github.com/TuzikUA/Py-TuzikTeleUBot ")

@app.on_message(filters.command('tpon',prefixes=prefix) & filters.me)  
async def tpon_com(_, msg):
    await msg.edit("пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон пон")

@app.on_message(filters.command('tpozdr',prefixes=prefix) & filters.me)  
async def tpozdr_com(_, msg):
    await msg.edit("Поздравляю тебя с праздником,желаю тебе счастья здоровья и всего наилучшего,успехов в жизни тебе <3")

def run():
    print("ЮзерБот от Тузика помогали рим мир к и пурпл,версия 3.1 global update,спасибо за использование юзербота <3")
    print(f"Ваша система: {str(platform.system())}")
    app.run()

run()
