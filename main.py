import streamlit as st
import spacy_streamlit
from spacy_streamlit import visualize_ner
import spacy

st.title('Data Redaction App')
st.subheader('Input Text and click enter to begin')
nlp = spacy.load("en_core_web_sm")
text = st.text_area('Input Text Here', height=400, max_chars=None, key=None, help=None)
doc = nlp(text)
visualize_ner(doc, labels=nlp.get_pipe("ner").labels)
for ent in reversed(doc.ents):
    # text = text[:ent.start_char] + ent.label_ + text[ent.end_char:]
    text = text[:ent.start_char] + "#REDACTED#" + text[ent.end_char:]


st.subheader('Redacted Results')
st.write(text)
