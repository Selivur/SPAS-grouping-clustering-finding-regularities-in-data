import re
import nltk
from nltk.probability import FreqDist
nltk.download('punkt')
f1= open("text/1.txt", "r", encoding="utf-8")
f2= open("text/2.txt", "r", encoding="utf-8")
f3= open("text/3.txt", "r", encoding="utf-8")
f4= open("text/4.txt", "r", encoding="utf-8")
f5= open("text/words.txt", "r", encoding="utf-8")
text1 =f1.read()
text2 =f2.read()
text3 =f3.read()
text4 =f4.read()
words =f5.read()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
cnt1 = re.sub('[^\w\s]','',text1.lower())
cnt2 = re.sub('[^\w\s]','',text2.lower())
cnt3 = re.sub('[^\w\s]','',text3.lower())
cnt4 = re.sub('[^\w\s]','',text4.lower())
stop_words=words.split()
data=(cnt1+" "+cnt2+" "+cnt3+" "+cnt4)
result=[]
trash=[]
for j in data.split():
        if j not in stop_words:
                result.append(j)
        else:
            trash.append(j)
# Tokenize
text_tokens = nltk.word_tokenize(" ".join(result))
# Frequency
freqDist = FreqDist(nltk.Text(text_tokens))
most_popular = freqDist.most_common(30)
freqDist.plot(30, cumulative=False)
trash_word_list=FreqDist(nltk.word_tokenize(" ".join(trash)))
with open('result.txt', 'w', encoding="utf8") as file:
    file.write(str(freqDist.most_common(len(freqDist))))
with open('trash.txt', 'w', encoding="utf8") as file:
    file.write(str(trash_word_list.most_common(len(trash_word_list))))