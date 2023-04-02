PDF Chatbot
PDF Chatbot is a Python application that allows you to have a conversation with an AI chatbot using text from a PDF file. The application uses the OpenAI API to generate responses to your messages.

Prerequisites
Before running the application, make sure you have the following installed:

Python 3
PyPDF2
openai
spacy
You will also need an OpenAI API key, which you can obtain from the OpenAI website.

Installation
Clone the repository to your local machine.
Install the required Python packages by running pip install -r requirements.txt in the project directory.
Download the en_core_web_lg model for spacy by running python -m spacy download en_core_web_lg in your terminal.
Set your OpenAI API key as the key variable in the pdf_chatbot.py file.
Usage
To use the application, follow these steps:

Save the PDF file you want to use in the same directory as the pdf_chatbot.py file.
Run the pdf_chatbot.py file using the command python pdf_chatbot.py in your terminal.
The application will prompt you to enter a message. Enter your message and press Enter to see the chatbot's response.
You can continue the conversation by entering another message, or type "finish" to end the conversation.
How it works
The application extracts text from the PDF file and splits it into chunks using the RecursiveCharactertextSplitter class. It then uses the en_core_web_lg model from spacy to compare each chunk to the user's message and find the most similar chunk. The most similar chunk is then used as the prompt for the OpenAI API, which generates a response to the user's message.

Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions are greatly appreciated!
