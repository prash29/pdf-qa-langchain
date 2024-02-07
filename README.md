# pdf-qa-langchain

## Overview

PDF-QA is a local app through which you can interact with a PDF document using a chatbot-style interface. It uses Langchain, Gradio and OpenAI's GPT models to allow the user to ask questions related to the document's content and receive informative responses. 

## Prerequisites

Before running the application, ensure you have the following prerequisites installed:

- Python 3.x
- Required packages listed in `requirements.txt`:
`pip install -r requirements.txt`
- OpenAI API key: Obtain your API key from [OpenAI](https://platform.openai.com/docs/overview). For further instructions, refer [here](https://platform.openai.com/docs/quickstart?context=python) 
Note: Keep your OpenAI API key safe and save it locally


## Demo Screenshot
![Demo Snapshot](demo-snapshot.png)

## Instructions

1. After cloning the repository, on a terminal, run the following command:
`python main.py`
2. You should see something like this on your terminal:
`Running on local URL:  http://127.0.0.1:7860

To create a public link, set `share=True` in `launch()`.`

Click on the local URL to use the interface

3. Copy your OpenAI API key in text box that says 'Enter your OpenAI API Key'.

