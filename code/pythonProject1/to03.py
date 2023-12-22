import re
import os
from pyltp import Segmentor, Postagger, NamedEntityRecognizer


def extract_relationships(name, text):
    if text is None:
        return None

    else:
        relationships = []

        # 定义关键词和模式
        isa_keywords = ["是一种", "第一位", "一位", "一名"]
        ako_keywords = ["一种", "一类", "一种类型", "类型"]

        # 定义正则表达式模式
        isa_pattern = re.compile(r'(?:.+?)\s*(' + '|'.join(isa_keywords) + r')\s*(.+)')
        ako_pattern = re.compile(r'(?:.+?)\s*(' + '|'.join(ako_keywords) + r')\s*(.+)')

        # 在文本中搜索关系
        for sentence in re.split('[。！？]', text):
            isa_match = isa_pattern.search(sentence)
            ako_match = ako_pattern.search(sentence)

            if isa_match:
                relationships.append((name, "isa", isa_match[2].strip(), sentence))
            # relationships.append((isa_match.group(1).strip(), "isa", isa_match.group(3).strip()))

            if ako_match:
                relationships.append((name, "ako", ako_match[2].strip(), sentence))

            if name in sentence and "是" in sentence:
                if ako_match is None:
                    LTP_DIR = 'D:/software/installtion_package/ltp_data_v3.4.0/ltp_data_v3.4.0'  # ltp模型目录的路径

                    cws_model_path = os.path.join(LTP_DIR, 'cws.model')
                    pos_model_path = os.path.join(LTP_DIR, 'pos.model')
                    ner_model_path = os.path.join(LTP_DIR, 'ner.model')

                    segmentor = Segmentor()
                    segmentor.load(cws_model_path)

                    postagger = Postagger()
                    postagger.load(pos_model_path)

                    ner = NamedEntityRecognizer()
                    ner.load(ner_model_path)

                    # 对文本进行分词

                    for sen in re.split(',', sentence):
                        words = segmentor.segment(sen)

                        # 对分词结果进行词性标注
                        postags = postagger.postag(words)

                        # 对分词和词性标注结果进行命名实体识别
                        netags = ner.recognize(words, postags)

                        # 提取命名实体
                        # merged_entities = []
                        # current_entity = ""
                        # current_entity_tag = ""

                        # 这两类出现较多且容易出错，故单独拎出来
                        if "小说" in sen:
                            relationships.append((name, "isa", "小说", sen))

                        if "图书" in sen:
                            relationships.append((name, "isa", "图书", sen))

                        for word, netag, postag in zip(words, netags, postags):
                            if postag == "n" and (name, "ako", word) not in relationships:
                                relationships = [rel for rel in relationships if
                                                 rel[1] != "ako"]  # Remove previous AKO relationship
                                relationships.append((name, "ako", word, sen))

                    segmentor.release()
                    postagger.release()
                    ner.release()

        return relationships


def shuchu(name, text):
    # sen = participle(text)
    # 提取关系
    result = extract_relationships(name, text)

    # 打印结果
    if result is None:
        return None
    else:
        return result
