from html import escape

import streamlit as st


st.set_page_config(page_title="My First App", layout="centered")

# The form submits the name only after the button is clicked.
with st.form("name_form"):
    name = st.text_input("Wpisz swoje imię")
    ok_clicked = st.form_submit_button("OK", use_container_width=True)

if ok_clicked:
    name = name.strip()

    if name:
        # escape() safely displays text entered by the user.
        st.html(
            f'<h1 style="color: #d62828; font-size: clamp(2.5rem, 8vw, 5rem); '
            f'text-align: center; overflow-wrap: anywhere;">{escape(name)}</h1>'
        )
    else:
        st.warning("Najpierw wpisz swoje imię.")
