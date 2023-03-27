key="your openAI api Key "

file_path = "test.pdf"
import PyPDF2
import openai
import spacy





# first download the en_core_web_lg model
# use this command <python -m spacy download en_core_web_lg>
check = spacy.load('en_core_web_lg')
openai.api_key =key
def chatGPT(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        top_p=1)
    return response.choices[0].text.strip()
# prompt = " "
# while True :
#     prompt+=input("me : ")
#     r = chatGPT(prompt)
#     print("chat : " +r)
#     prompt += r

texts = []

with open(file_path,'rb') as f:

    pdf_reader = PyPDF2.PdfReader(f)
    all_texts = ""
    for page_num in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text()
        texts.append(page_text)
        # all_texts += page_text
# texts= all_texts.split(".")
print("if you want to finish this conversation , write ``finish``")
prompt = ""
while True:
    q = input("me : ")
    if q == "finish":
        break
    check_max = -1
    index = 1
    for i in range(len(texts)) :
        scor = check(q).similarity(check(texts[i]))
        if scor >check_max:
            check_max = scor
            index = i

    if index == 0:
        prompt += texts[index] + "\n" + texts[index+1]
    if index == len(texts) - 1 :
        prompt += texts[index -1 ] + "\n" + texts[index ]
    else:
        prompt += texts[index-1]+ "\n"+texts[index]+ "\n"+texts[index+1]





    prompt = prompt +q
    r = chatGPT(prompt)

    print("chat : "+ r)
    prompt += r

print("finish...")