import json
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Đọc dữ liệu từ tệp JSON
with open('good_labeled.json') as file:
    data = json.load(file)

# Đọc danh sách stopwords
with open('custom_stopwords.json') as file:
    stopwords_list = json.load(file)

# Tiền xử lý dữ liệu
stop_words = list(stopwords.words('english'))
stop_words.extend(stopwords_list)

def preprocess_text(text):
    text = re.sub(r'\W', ' ', text) 
    text = text.lower() 
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)  # Loại bỏ ký tự đơn lẻ
    text = re.sub(r'\^[a-zA-Z]\s+', ' ', text)  # Loại bỏ ký tự đầu dòng
    text = re.sub(r'\s+', ' ', text, flags=re.I)  # Loại bỏ khoảng trắng thừa
    text = ' '.join(word for word in text.split() if word not in stop_words)  # Loại bỏ stopwords
    return text

# Chuẩn bị dữ liệu huấn luyện
comments = []
labels = []
for entry in data:
    comment = entry['comment']
    label = entry['toxicity']
    comments.append(comment)
    labels.append(label)

# Tiền xử lý và mã hóa dữ liệu
vectorizer = CountVectorizer(stop_words=stop_words)
X = vectorizer.fit_transform(comments)

# Xây dựng mô hình Naive Bayes
model = MultinomialNB()

# Huấn luyện mô hình
model.fit(X, labels)

# Ghi dữ liệu đã được phân tích vào tệp JSON
for entry in data:
    comment = entry['comment']
    preprocessed_comment = preprocess_text(comment)
    comment_vector = vectorizer.transform([preprocessed_comment])
    toxicity = model.predict_proba(comment_vector)[0][1]
    
    entry['toxicity'] = toxicity
    
    

# Ghi dữ liệu đã được gán nhãn vào tệp JSON
with open('DATA_GOOD_FINAL.json', 'w') as file:
    json.dump(data, file, indent=4)
    print('Ghi dữ liệu thành công!')
