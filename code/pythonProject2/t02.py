from transformers import pipeline

# 加载关系抽取模型
nlp = pipeline("relation-extraction")

# 示例文本
text = "李娜，1982年2月26日出生于湖北省武汉市，毕业于华中科技大学，中国女子网球运动员，2008年北京奥运会女子单打第四名，2011年法国网球公开赛、2014年澳大利亚网球公开赛女子单打冠军，亚洲第一位大满贯女子单打冠军。"

# 使用关系抽取模型
result = nlp(text)

# 打印结果
for item in result:
    print(f"实体1: {item['subject']}, 关系: {item['relation']}, 实体2: {item['object']}")