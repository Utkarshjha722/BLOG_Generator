# app.py - Your existing code stays mostly the same, but with a small modification to handle model path
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import os

def getLLMResponse(input_text, no_words, blog_style):
    # Check if model exists, if not guide user to run setup
    model_path = "models/llama-2-7b-chat.ggmlv3.q8_0.bin"
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model not found! Please run 'python download_models.py' first")
        
    llm = CTransformers(
        model=model_path,
        model_type="llama",
        config={'max_new_tokens': 256, 'temperature': 0.01}
    )
    
    # Rest of your code remains the same
    template = """
    Write a blog for {blog_style} job profile for a topic {input_text}
    within {no_words} words.
    """
    
    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", 'no_words'],
        template=template
    )
    
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    return response

# Your Streamlit UI code remains the same