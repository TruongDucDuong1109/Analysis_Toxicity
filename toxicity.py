import json
import re

# Đọc dữ liệu từ tệp JSON
with open('datagood.json') as file:
    data = json.load(file)

# Xây dựng danh sách bình luận từ dữ liệu JSON
comments = [entry['comment'] for entry in data]

# Danh sách từ dừng tùy chỉnh
file_path = 'custom_stopwords.json'
with open(file_path, 'r') as file:
    custom_stopwords = json.load(file)

# Gán nhãn độc tính (toxicity)
toxicity_labels = []
for comment in comments:
    has_toxic_word = any(word in comment for word in custom_stopwords)
    if has_toxic_word:
        toxicity_labels.append(1)  # Gán nhãn 1 nếu có từ độc tính
    else:
        toxicity_labels.append(0)  # Gán nhãn 0 nếu không có từ độc tính

# Gán nhãn độc tính vào dữ liệu
for i, entry in enumerate(data):
    entry['toxicity'] = toxicity_labels[i]

# Ghi dữ liệu đã được gán nhãn vào tệp JSON
with open('good_labeled.json', 'w') as file:
    json.dump(data, file, indent=4)


