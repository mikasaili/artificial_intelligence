import os
from pyltp import Segmentor, Postagger, NamedEntityRecognizer

LTP_DIR='D:/software/installtion_package/ltp_data_v3.4.0/ltp_data_v3.4.0'  # ltp模型目录的路径

cws_model_path = os.path.join(LTP_DIR, 'cws.model')
pos_model_path = os.path.join(LTP_DIR, 'pos.model')
ner_model_path = os.path.join(LTP_DIR, 'ner.model')

segmentor = Segmentor()
segmentor.load(cws_model_path)

postagger = Postagger()
postagger.load(pos_model_path)

ner = NamedEntityRecognizer()
ner.load(ner_model_path)

text = ("李娜 ，1982年2月26日出生于湖北省武汉市，毕业于华中科技大学，中国女子网球 运动员 ，"
        "2008年北京奥运会女子单打第四名，2011年法国网球公开赛、2014年澳大利亚网球公开赛女子单打 冠军，亚洲第一位大满贯女子单打 冠军。")

# 对文本进行分词
words = segmentor.segment(text)

# 对分词结果进行词性标注
postags = postagger.postag(words)

# 对分词和词性标注结果进行命名实体识别
netags = ner.recognize(words, postags)

# 提取命名实体
merged_entities = []
current_entity = ""
current_entity_tag = ""
for word, netag, postag in zip(words, netags,postags):
    print(word,postag,netag)
    if (postag == "nh" and netag =="S-Nh" or netag =="S-Ns") or (postag == "n"and netag =="O"):
        if word not in merged_entities:
            merged_entities.append(word)

# 打印提取的实体
print("提取的实体:", merged_entities)

segmentor.release()
postagger.release()
ner.release()