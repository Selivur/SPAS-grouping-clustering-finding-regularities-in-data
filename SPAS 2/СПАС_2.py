#-*- coding: utf-8 -*-
from collections import Counter
import math
counter=0;
f= open("a.txt", "r")
text = f.read()
f.close()
f1= open("b.txt", "r")
text1 = f1.read()
f1.close()
cnt = Counter(text.lower().split())
cnt1 = Counter(text1.lower().split())
print(cnt)
print("\n")
print(cnt1)
number_of_files=2
word = "is"
def TF(cnt, word):
    global counter
    counter=counter+1
    return cnt[word]/len(cnt)
def IDF(num):
    global counter
    return math.log1p(num/counter)
tf2=TF(cnt1, word) #we need do it for all files
print("\n")
W=TF(cnt, word)*IDF(number_of_files)
print(W)