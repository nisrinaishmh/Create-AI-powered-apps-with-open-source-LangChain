import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain_openai import ChatOpenAI
    
openai_api_key = "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"
os.environ["OPENAI_API_KEY"] = openai_api_key

# Mendefinisikan model AI
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key= openai_api_key
)

# Mendefinisikan PromptTemplate sebagai format prompt untuk input dari user
prompt = PromptTemplate(
    input_variables=["nama", "posisi", "perusahaan", "keterampilan", "pengalaman", "motivasi"],
    template="Buatlah surat lamaran kerja yang lengkap, rinci, padat, memotivasi, menarik bagi HRD, tepat, tegas formal, dan bermakna di perusahaan : {perusahaan},\n\n untuk melamar di posisi {posisi} di {perusahaan}. dengan keterampilan, pengalaman, dan motivasi sebagai berikut {keterampilan} {pengalaman} {motivasi}. dengan pendaftar bernama {nama}",
)

# Define a function to generate a cover letter using the llm and user input
def generate_cover_letter(nama: str, posisi: str, perusahaan: str, keterampilan: str, pengalaman: str, motivasi: str) -> str:
    formatted_prompt = prompt.format(nama=nama, posisi=posisi, perusahaan=perusahaan, keterampilan=keterampilan, pengalaman=pengalaman, motivasi=motivasi)
    response = llm.invoke(formatted_prompt).content
    return response

# Define the Gradio interface inputs
inputs = [
    gr.Textbox(label="Nama"),
    gr.Textbox(label="Posisi"),
    gr.Textbox(label="Perusahaan"),
    gr.Textbox(label="Keterampilan"),
    gr.Textbox(label="Pengalaman"),
    gr.Textbox(label="Motivasi")
]

# Define the Gradio interface output
output = gr.Textbox(label="Template Surat")

# Launch the Gradio interface
gr.Interface(fn=generate_cover_letter, inputs=inputs, outputs=output).launch(share=True)

