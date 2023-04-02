import yaml

from PineCone import put,get
import PyPDF2
from chatGpt import chatGPT
import spacy
# first download the en_core_web_lg model
# use this command <python -m spacy download en_core_web_lg>
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
check = spacy.load('en_core_web_lg')


file_path = config["file"]


texts = []

with open(file_path,'rb') as f:

    pdf_reader = PyPDF2.PdfReader(f)
    all_texts = ""

    for page_num in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text()
        texts.append(page_text)


def start():
    ids = ["text" + str(i) for i in range(len(texts))]
    vectors = [list(check(chunk).vector) for chunk in texts]
    print(put(ids,vectors))


# print(vectors)
# print("if you want to finish this conversation , write ``finish``")
# prompt = ""
# __start__()
# while True:
#     q = input("me : ")
#     if q == "finish":
#         break
#     # print(len(check(q).vector))
#
#     result = PineCone.get(check(q).vector)
#     print(result)








    # prompt = prompt +q
    # r = chatGPT(prompt)
    #
    # print("chat : "+ r)
    # prompt += r

print("finish...")