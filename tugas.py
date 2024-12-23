import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

with st.sidebar :
    selected = option_menu ('Rekaputasi',  ['Tamu Keseluruhan','Tamu Rentan Usia', 'Tamu Jenis kelamin', 'Tamu Hadiah'], default_index=0)

if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Nama","Alamat","Email","Pesan"])

st.title("Buku Tamu Digital")

with st.form(key='data_form'):
    Nama = st.text_input("Nama")
    Alamat = st.text_input("Alamat")
    Email = st.text_input("Email")
    Pesan = st.text_input("Pesan")

    submit_button = st.form_submit_button("Tambah Data")

if submit_button:
    new_data = pd.DataFrame([[Nama,Alamat,Email,Pesan]], columns=["nama","alamat","email","pesan"])
    st.session_state.data = pd.concat([st.session_state.data], ignore_index=True)

# latihan
st.title('Buku Tamu Digital')

# Full example of using the with notation
st.header('Rekaputasi Keseluruhan')

with st.form('my_form'):
    st.subheader('**Input your profile!**')

    # Input widget
    Nama = st.text_input("Nama")
    coffee_bean_val = st.selectbox('Jenis Kelamin', ['Pria', 'Wanita'])
    coffee_roast_val = st.selectbox('Usia', ['<20', '>20', 'dsb'])
    brewing_val = st.selectbox('Alamat', ['Jakarta', 'Bogor', 'Depok', 'Tangerang', 'Bekasi'])
    serving_type_val = st.selectbox('Hadiah', ['Gift', 'Money'])
    owncup_val = st.checkbox('Hadir')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have input:
        - Nama: `{Nama}`
        - Jenis Kelamin: `{coffee_bean_val}`
        - Usia: `{coffee_roast_val}`
        - Alamat: `{brewing_val}`
        - Hadiah: `{serving_type_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write(' place your guest!')



if "scores" not in st.session_state:
    st.session_state.scores = [
        {"name": "Zaidaan", "umur": 10, "pesan": 20},
    ]

def new_scores():
    st.session_state.scores.append(
        {
            "name": st.session_state.name,
            "umur": st.session_state.umur,
            "pesan": st.session_state.pesan,
        }
    )

st.write("# Add a new guest!")
with st.form("new_score", clear_on_submit=True):
    name = st.text_input("Name", key="name")
    pushups = st.number_input("Umur", key="umur", step=1, value=0, min_value=0)
    situps = st.number_input("Jenis Kelamin", key="pesan", step=1, value=0, min_value=0)
    st.form_submit_button("Submit", on_click=new_scores)



score_df = pd.DataFrame(st.session_state.scores)
score_df["keterangan"] = score_df["umur"] + score_df["pesan"]

st.write(score_df)