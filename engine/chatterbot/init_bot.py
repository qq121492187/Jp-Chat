# 初始化chatterbot的训练
# 初始训练只需加载一次

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from config import chat_config
import corpus_data_loader as data_loader
import os

chatBot = ChatBot('dp-chatbot',database_uri='sqlite:///database.db')
listTrainer = ListTrainer(chatBot)

# listTrainer.export_for_training('./ex_data.json')

def init_standard_corpus():
    # 加载预料
    # corpus = data_loader.loadTsvData(chat_config['init_corpus'])
    corpus = data_loader.loadTsvData(os.path.dirname(__file__)+'/clean_chat_corpus/xiaomei_inner_v1.tsv')
    # 训练初始数据集
    listTrainer.train(corpus)

def init_dp_b_corpus():
    import xlrd
    book = xlrd.open_workbook(os.path.dirname(__file__)+'/clean_chat_corpus/dp_b_corpus.xlsx')
    sheet1 = book.sheet_by_index(0)
    sheet2 = book.sheet_by_index(1)

    corpus = []
    for i in range(sheet1.nrows):
        if i<1 == True:
            continue

        corpus.append(sheet1.cell_value(i,3))
        corpus.append(sheet1.cell_value(i,4))

    for j in range(sheet2.nrows):
        if j < 1 == True:
            continue

        corpus.append(sheet2.cell_value(j,3))
        corpus.append(sheet2.cell_value(j,4))
    
    #训练数据
    listTrainer.train(corpus)

# init_dp_b_corpus()

