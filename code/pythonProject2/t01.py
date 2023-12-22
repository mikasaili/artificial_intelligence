import spacy
# 加载 spaCy 模型
nlp = spacy.load("en_core_web_sm")
def extract_relationships(text):
    relationships = []
    # 使用 spaCy 进行文本处理
    doc = nlp(text)
    print(doc)
    # 提取名词短语
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    print(noun_phrases)
    print(len(noun_phrases))
    # 构建关系
    for i in range(len(noun_phrases) - 1):
        relationships.append((noun_phrases[i], "isa", noun_phrases[i + 1]))
        relationships.append((noun_phrases[i], "ako", noun_phrases[i + 1]))

    return relationships

# 示例文本
text = "苹果是一种水果。橙子是一种柑橘类水果。水果是食物的一种。"

# 提取关系
result = extract_relationships(text)

# 打印结果
for relationship in result:
    print(relationship)