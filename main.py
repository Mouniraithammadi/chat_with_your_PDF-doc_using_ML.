import yaml

from PineCone import put,get
import PyPDF2
from chatGpt import answer , chatGPT
import spacy
# first download the en_core_web_lg model
# use this command <python -m spacy download en_core_web_lg>
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
check = spacy.load('en_core_web_lg')




paths = []
texts = []
import os

with open("data.txt","r",encoding="utf8") as f:
    data = f.read()

    chunkss = data.split(". ")
chunks = []

for i in range(0,len(chunkss),3):
    chunks.append(chunkss[i] + " " + chunkss[i + 1] + " " + chunkss[i + 2])





#
def start():
    ids = ["text" + str(i) for i in range(len(chunks))]
    vectors = [list(check(chunk).vector) for chunk in chunks]
    print(put(ids,vectors))

print("if you want to finish this conversation , write ``finish``")
prompt = ""
while True:
    q = input("me : ")
    if q == "finish":
        break
    result = get(check(q).vector)
    index = int(str(result["results"][0]["matches"][0]["id"]).replace("text",""))



    reply = chatGPT(q=q , text=chunks[index])
    print("doc : " + reply)



    # prompt = prompt +q
    # r = chatGPT(prompt)
    #
    # print("chat : "+ r)
    # prompt += r

print("finish...")