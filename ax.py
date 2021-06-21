from pyrogram import Client
from pyrogram import filters
from random import choice

app = Client(
  'my_account'
)


@app.on_message(filters.command('ssot', prefixes='.') & filters.me)
def main(client, msg):
#  x = ['Иди нах', 'Узбагойся', 'Шо за долбоёб...', '🤬', 'Не, ну честно сказочный долбоёб']
  #msg.reply(choice(x))
  args = str(msg.text).split(' ', 2)
  
  for i in range(int(args[1])):
    app.send_message(msg.chat.id, args[2])
  
app.run()