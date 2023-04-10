import streamlit as st
import openai
import os
from text.functions import summarize

try:
	openai.api_key = os.getenv('OPENAI_KEY')

	st.title("Text Summarizer")

	# initialize state variable
	if "summary" not in st.session_state:
	    st.session_state["summary"] = ""

	input_text = st.text_area(label='Enter full text:', value="", height=250)

	st.button(
	    "submit",
	    on_click=summarize,
	    kwargs={"prompt": input_text}
	)

	# submit botton is pressed and generate the summary, state becomes "summary"
	output_text = st.text_area(label='Summarized text:', value=st.session_state["summary"], height=250)
except:
	st.write('There was an error =(')

# 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
