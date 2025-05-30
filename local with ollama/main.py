import streamlit as st
from streamlit.runtime.state import session_state
from scrape import (
        scrape_web,
        split_dom_content,
        clean_body_content,
        extract_body
    )
from parse import parse_with_ollama

st.title("AI Scrapper")

url=st.text_input("Enter a website url")

if st.button("Scrape site"):
    st.write("Scraping site")
    result=scrape_web(url)
    body_content=extract_body(result)
    clean_body=clean_body_content(body_content)

    st.session_state.dom_content=clean_body

    with st.expander("View dom content"):
        st.text_area("Dom content",clean_body,height=300)

if "dom_content" in st.session_state:
    parse_description=st.text_area("Describe what you want to parse")

    if st.button("Parse content"):
        if parse_description:
            st.write("Parsing content")

            dom_chunks=split_dom_content(st.session_state.dom_content)
            result=parse_with_ollama(dom_chunks,parse_description)
            st.write(result)
