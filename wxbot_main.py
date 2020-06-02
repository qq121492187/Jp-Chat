from wxpy import *
import traceback
from controller import ChatController

chatController = ChatController()

bot = Bot()


@bot.register([Group], TEXT)
def auto_replay_group_at_msg(msg):
    
    if isinstance(msg.chat,Group)==False:
        return

    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        # 回复消息
        print(msg.text)
        try:
            sub_index= msg.text.find('\u2005')
            input = msg.text[sub_index+1:]
            print(input)
            replay = chatController.start_chat(input)
            print(replay)
        except Exception as e:
            print(e)
            traceback.print_exc()
        
        return replay


embed()
