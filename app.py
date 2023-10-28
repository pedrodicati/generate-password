import streamlit as st
import string

from generate_passwords import create_password

st.set_page_config(
    page_title='Password Generator',
    page_icon='🔑',
    layout='wide'
)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Password Generator 🔑')
st.text('Generate a random password with the length and characters of your choice.')

st.sidebar.title('Settings')
length = st.sidebar.slider('Length', 4, 64, 8, 1)
chars = st.sidebar.multiselect('Characters', ['Letters', 'Digits', 'Punctuation'], ['Letters', 'Digits', 'Punctuation'])

if len(chars) == 0:
    chars = string.ascii_letters + string.digits + string.punctuation

if 'Letters' in chars:
    if 'Digits' in chars:
        if 'Punctuation' in chars:
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            chars = string.ascii_letters + string.digits
    else:
        if 'Punctuation' in chars:
            chars = string.ascii_letters + string.punctuation
        else:
            chars = string.ascii_letters
elif 'Digits' in chars:
    if 'Punctuation' in chars:
        chars = string.digits + string.punctuation
    else:
        chars = string.digits
else:
    chars = string.punctuation

st.text('Your password is:')
st.code(create_password(length, chars=chars), language='')

st.sidebar.markdown(
    """<p style='text-align: center; color: #888;'><small>Powered by <a href="https://github.com/pedrodicati">Pedro Dicati</a></small></p>""",
    unsafe_allow_html=True
)
