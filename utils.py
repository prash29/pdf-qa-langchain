from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
import fitz
from PIL import Image
import gradio as gr
import os

count, n = 0, 0
chat_history = []
chain = ""


def setAPIKey(api_key):
    """
    Function to set the OpenAPI Key in the environment variable
    """
    os.environ["OPENAI_API_KEY"] = api_key
    return True


def enable_set_api():
    """
    Function that enables text box to set API Key
    """
    return


def add_text_input(history, text):
    if not text:
        raise gr.Error("Please enter text!")
    history.append((text, ""))
    return history


def process_pdf_file(file, temperature=0.9):
    if not os.environ["OPENAI_API_KEY"]:
        raise gr.Error(
            "No OPENAI_API_KEY set in the environment! Use os.environ and set your key"
        )

    doc_loader = PyPDFLoader(file.name)
    docs = doc_loader.load()

    embeddings = OpenAIEmbeddings()

    pdf = Chroma.from_documents(docs, embeddings)

    chain = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(temperature=temperature),
        retriever=pdf.as_retriever(search_kwargs={"k": 1}),
        return_source_documents=True,
    )
    return chain


def generate_response(history, query, button):
    """Generates the response based on chat input and history
    """
    global count, n, chat_history, chain

    if not button:
        raise gr.Error(message="Upload a PDF! ")

    if count == 0:
        chain = process_pdf_file(button)
        count += 1

    result = chain(
        {"question": query, "chat_history": chat_history}, return_only_outputs=True
    )

    chat_history.append([query, result["answer"]])
    n = list(result["source_documents"][0])[1][1]["page"]

    for char in result["answer"]:
        history[-1][-1] += char

    return history, " "


def render_file(file):
    """
    Renders an image of a specific page of the PDF file
    """

    global n
    doc = fitz.open(file.name)
    page = doc[n]
    # Render the page as a PNG image with a resolution of 300 DPI
    pix = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72))
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return image
