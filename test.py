from controller import ChatController

ct = ChatController()

while True:
    try:
        txt = input()
        print(ct.start_chat(txt))
    except (KeyboardInterrupt,EOFError,SystemExit):
        break
