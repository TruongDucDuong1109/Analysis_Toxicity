import json
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp JSON
def read_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Visualize dữ liệu thành biểu đồ cột
def plot_toxicity(ax, data, title):
    ids = [entry['id'] for entry in data]
    toxicities = [entry['toxicity'] for entry in data]
    
    ax.bar(ids, toxicities, color='blue')
    ax.set_xlabel('ID')
    ax.set_ylabel('Toxicity')
    ax.set_title(title)

# Đường dẫn tới các tệp JSON
good_data = read_data('DATA_GOOD_FINAL.json')
toxic_data = read_data('DATA_TOXIC_FINAL.json')

# Tạo một lưới biểu đồ 1x2
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Trực quan hóa dữ liệu
plot_toxicity(axs[0], good_data, 'Good Data')
plot_toxicity(axs[1], toxic_data, 'Toxic Data')

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()
