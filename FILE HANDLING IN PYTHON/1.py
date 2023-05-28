

import functools
f = open("story.txt","r")
def read(f):
 for line in f:
 print(line)
 
count=0
word=list()
for line in f:
 count=count +line.count("T")
 word=word + line.split(" ")
 
print("T = ",count)
print("total word = ",len(word))
f.close()
f = open("story.txt","r")
count=0
for line in f:
 count=count +line.count("T")
print("the = ",count)
f.close()
f = open("story.txt","r")
for line in f:
 words=line.split(" ")
 for word in words:
 if(len(word)>4):
 print(word,end=" ")
f.close()
47
f = open("story.txt","r")
count=0
for line in f:
 count=count +line.count("the")
 count=count +line.count("is")
 
print("is & the =",count)
f.close()
f = open("story.txt","r")
count==0
for line in f:
 count=count +line.count("e")
print("e =",count)
f.close()
f = open("story.txt","r")
count==0
for line in f:
 for a in line:
 if a.isupper():
 count+=1
print("Upper",count)
f.close()
f = open("story.txt","r")
count==0
for line in f:
 for a in line:
 if a.islower():
 count+=1
48
print("Upper",count)
f.close()
