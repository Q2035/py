from wordcloud import WordCloud
from matplotlib import pyplot as plt

data = []
f = open(r"C:\Users\Q\Desktop\deal_chat_history.txt", encoding="utf-8")
line = f.readline()
while line:
    line = f.readline()
    if line.isspace():
        continue
    data.append(line.replace(" ", ""))
font = r'C:\Windows\Fonts\simhei.ttf'
wordcloud = WordCloud(background_color='white', width=1000, height=1000, margin=2, font_path=font).generate(''.join(data))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
