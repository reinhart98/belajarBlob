from pytg import Telegram
from pytg.utils import coroutine
#from pytg.sender import Sender
#from pytg.receiver import Receiver
import logging
#logging.basicConfig(level=logging.DEBUG)


tg = Telegram(
	telegram="/home/odroid/tg/bin/telegram-cli",
	pubkey_file="/home/odroid/tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender

#sender.send_msg("David_Reinhart", u"Hello World!")


def main_loop():
	while not QUIT:
		msg = yield # it waits until it got a message, stored now in msg.
		b = yield msg
		print("Message: ", msg.text)
		
receiver.start()

# let "main_loop" get new message events.
# You can supply arguments here, like main_loop(foo, bar).
receiver.message(main_loop())
# now it will call the main_loop function and yield the new messages.