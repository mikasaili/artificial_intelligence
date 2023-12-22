import os
from pyltp import Segmentor
LTP_DIR=r'E:\myLTP\ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path=os.path.join(LTP_DIR,'cws.model') # 分词模型路径，模型名称为`cws.model`
segmentor=Segmentor()            # 初始化实例
segmentor.load(cws_model_path)   # 加载模型
words=segmentor.segment('我还没吃饭你吃饭了吗')   # 分词
print('\t'.join(words))
segmentor.release()       # 释放模型
