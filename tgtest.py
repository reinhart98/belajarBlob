from pytel import tg

telegram = tg.Telegram('unix:///tmp/tg.sock') # For Unix Domain Socket
# telegram = tg.Telegram('tcp://127.0.0.1:4444') # For TCP socket

message = 'Dude! Whats?'
telegram.send_message('David Reinhart', 'hallo 'message)
