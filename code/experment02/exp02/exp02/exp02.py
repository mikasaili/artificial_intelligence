def forward_maximum_matching(text, dictionary):
    result = []
    max_length = max(len(word) for word in dictionary)

    while text:
        word = text[:max_length]
        while word not in dictionary and len(word) > 1:
            word = word[:-1]
        result.append(word)
        text = text[len(word):]

    return result

# 以提供的实体为词典
entity = "大东镇"
entity_dict = [entity]

# 提取实体
text_to_segment = ("大东镇隶属于江苏省淮安市涟水县，位于涟水县域中东部，现有20030人，"
                   "东隔古盐河与黄营乡相望，南与小李集工业园区为邻，西与时码交界，北与东胡集镇毗连。"
                   "地处闽粤两省四县(平和、永定、饶平、大埔)八镇交界处，是山、边、穷的革命老区，又是全省40个扶贫开发重点镇之一。"
)
result_entities = forward_maximum_matching(text_to_segment, entity_dict)

print("提取的实体：", result_entities)