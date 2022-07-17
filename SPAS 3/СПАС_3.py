from collections import Counter
import re
import csv
f1= open("text/1.txt", "r", encoding="utf-8")
f2= open("text/2.txt", "r", encoding="utf-8")
f3= open("text/3.txt", "r", encoding="utf-8")
f4= open("text/4.txt", "r", encoding="utf-8")
text1 =f1.read()
text2 =f2.read()
text3 =f3.read()
text4 =f4.read()
f1.close()
f2.close()
f3.close()
f4.close()
cnt1 = Counter(re.sub('[^\w\s]','',text1.lower()).split())
cnt2 = Counter(re.sub('[^\w\s]','',text2.lower()).split())
cnt3 = Counter(re.sub('[^\w\s]','',text3.lower()).split())
cnt4 = Counter(re.sub('[^\w\s]','',text4.lower()).split())
word1=input("enter 1 word:\n")
word2=input("enter 2 word:\n")
word3=input("enter 3 word:\n")
word4=input("enter 4 word:\n")
word5=input("enter 5 word:\n")
def count(cnt,w1, w2, w3, w4, w5):
    sum=cnt[w1]+cnt[w2]+cnt[w3]+cnt[w4]+cnt[w4]+cnt[w5]
    return sum
a=[count(cnt1, word1,word2,word3,word4,word5),count(cnt2, word1,word2,word3,word4,word5),count(cnt3, word1,word2,word3,word4,word5),count(cnt4, word1,word2,word3,word4,word5)]
name=["1.txt","2.txt","3.txt","4.txt"]
i=0
while i!=4:
    print(name[a.index(max(a))]+": "+str(max(a)))
    a[a.index(max(a))]=-i-1
    i=i+1
cnt5=cnt1+cnt2+cnt3+cnt4
answer = sorted(cnt5.items())
with open("answer.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(answer)