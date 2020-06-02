from engine.base_engine import BaseChatEngine
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from engine.baidu.bd_engine import BdChatEngine

class ChatterbotEngine(BaseChatEngine):

    chatBot = ChatBot(
        'dp-chatbot',
        read_only=True,
        logic_adapter=[
            # 最佳匹配方式
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'maximum_similarity_threshold': 0.3,
                'default_response': "对不起，我无法理解您的意思",
                'statement_comparison_function':'chatterbot.comparisons.levenshtein_distance'
            }
        ],
        database_uri='sqlite:///database.db'
    )

    listTrainer = ListTrainer(chatBot)

    def __init__(self):
        self.bdEngine = BdChatEngine()


    def get_response(self,question):
        statement = self.chatBot.get_response(question)
        print(statement.confidence)
        if(statement.confidence<0.3):
            return self.bdEngine.get_response(question)+'\n'+'(没有解决您的问题？可选择呼叫人工服务)'
        else:
            return statement.text

    def train_qa(self, q, a):
        self.listTrainer.train([q, a])
