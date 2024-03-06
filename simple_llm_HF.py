import os
from langchain_community.llms import HuggingFaceEndpoint
import gradio as gr

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "Rugi_Dong_Use_your_own_API_key"

llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")

def chatbot(prompt):
    return llm.invoke(prompt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(share=True)