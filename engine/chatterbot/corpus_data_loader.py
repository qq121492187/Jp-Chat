# 语料数据加载


# 加载tsv数据集
def loadTsvData(fileName):
    if fileName.endswith('.tsv') == False:
        raise Exception('请加载tsv格式文件')

    with open(fileName, encoding='utf-8') as f:
        data = f.read().replace('\t', '\n')

    return data.split('\n')
