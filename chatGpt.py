import openai
import yaml
with open("config.yaml") as f:
    config = yaml.load(f,Loader=yaml.FullLoader)
openai.api_key =config["openai_key"]


def chatGPT(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        top_p=1)
    return response.choices[0].text.strip()