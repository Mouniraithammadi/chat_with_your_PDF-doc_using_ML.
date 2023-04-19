import openai
import yaml
with open("config.yaml") as f:
    config = yaml.load(f,Loader=yaml.FullLoader)
openai.api_key =config["openai_key"]


def chatGPT(q , text):
    context =  "You are a chatbot that communicate in any language the user ask you , you are friendly and intelligence and assist the users from recivung a text from a document and reply for the questions (the text start with 'from the text : ' and the question start with 'question : '. all that is replying for the users questions , and read the text  and based on it and send just the question reply ." \
               " from the  text : " + text + " , question : " + q
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=context,
        max_tokens=1500,
        top_p=1)
    return response.choices[0].text.strip()


def answer(q , text):



    context = [{"role": "system",
                "content": "You are a chatbot that communicate in any language the user ask you , you are friendly and intelligence and assist the users from recivung a text from a document and reply for the questions (the text start with 'from the text : ' and the question start with 'question : '. all that is replying for the users questions , and read the text  and based on it and send just the question reply ." }]  + [
                  {"role": "user","content": "from the  text : " + text},{"role": "user","content":"question : "+ q}]

    r = openai.Completion.create(
    engine="davinci",
    prompt=context,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)


    reply = r["choices"][0]['message']['content']



    return reply