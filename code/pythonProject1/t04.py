import json
import to03


def extract_info_from_jsonl(jsonl_file):
    c = 0
    count = 0
    nameLast = [0] * 100000
    summaryLast = [None] * 100000
    with open(jsonl_file, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line.strip())

            name = data.get('name')
            summary = data.get('summary', '')
            nameLast[count] = name
            summaryLast[count] = summary

            nameLast[count] = name
            summaryLast[count] = summary
            count += 1

    return nameLast, summaryLast


nameLast1, summaryLast1 = extract_info_from_jsonl('D:\\courseware\\人工智能与知识工程\\experiment_data.jsonl')
count = 0
with open('D:\\courseware\\人工智能与知识工程\\answer2.txt', 'w',encoding='utf-8') as file:
    # 写入文本内容
    for i in range(100000):
        a = to03.shuchu(nameLast1[i], summaryLast1[i])
        if not a:
            count += 1
        else:
            file.write(str(a))
            file.write("\n")
        print(i)
