# 引擎基类
# 所有引擎需要继承这个类
import abc


class BaseChatEngine(metaclass=abc.ABCMeta):

    # 获取回答
    @abc.abstractmethod
    def get_response(self, question):
        pass
    # 训练单层对话
    @abc.abstractmethod
    def train_qa(self, q, a):
        pass
