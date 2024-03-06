from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import wget
import os
import gradio as gr
import pysqlite3
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

# mengakses ke dokumen
url = "https://raw.githubusercontent.com/Ichsan-Takwa/Generative-AI-Labs/main/state_of_the_union"
output_path = "stateoftheunion.txt"  # nama file lokal

# Mengecek jika file sudah ada
if not os.path.exists(output_path):
    # mengunduh file menggunakan wget
    wget.download(url, out=output_path)

loader = TextLoader('stateoftheunion.txt')

openai_api_key = "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"
os.environ["OPENAI_API_KEY"] = openai_api_key

# mengakses data
data = loader.load()

# Membuat instance untuk mencari data
index = VectorstoreIndexCreator().from_loaders([loader])

# Menjalankan gradio
def summarize(query):
    return index.query(query)

iface = gr.Interface(fn=summarize, inputs="text", outputs="text")
iface.launch(share=True)