import layer.filter
import config
import layer.transform

class ChatController:

    def __init__(self):
        self.engineName = config.chat_config['default_engine']
        self.chatEngine = self.get_engine(self.engineName)
        self.chatEngineCache = {self.engineName:self.chatEngine}

    def start_chat(self, input_text):
        # 输入过滤层
        filter_text = layer.filter.input_filter(input_text)

        # 选择引擎
        config_engine_name = config.chat_config['default_engine']

        if(config_engine_name != self.engineName):
            # 切换了引擎，需要重新加载
            self.chatEngine = self.get_engine(config_engine_name)
            self.engineName = config_engine_name

        # 获取回话
        output_text = self.chatEngine.get_response(filter_text)

        # 输出转换
        output_text = layer.transform.output_trans(output_text)

        # 输出过滤
        output_text = layer.filter.output_filter(output_text)

        # 输出
        return output_text

    def get_engine(self, name):
        if(name == 'cb'):
            from engine.chatterbot.chatterbot_engine import ChatterbotEngine
            engine = ChatterbotEngine()
        elif(name == 'bd'):
            from engine.baidu.bd_engine import BdChatEngine
            engine = BdChatEngine()
        else:
            from engine.chatterbot.chatterbot_engine import ChatterbotEngine
            engine = ChatterbotEngine()

        return engine
