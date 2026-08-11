import streamlit as st
import os
import time
import random

st.title("Hello Streamlit")
st.write("안녕하세요. 배포 참 쉽죠?")
st.write(time.strftime("%Y-%m-%d %H:%M:%S"))

st.title(":sparkles: 로또 생성기 :sparkles:")


def generate_lotto():
    lotto = [i + 1 for i in range(45)]
    random.shuffle(lotto)
    return lotto[:6]


button = st.button("로또를 생성해 주세요")

if button:
    for i in range(5):
        st.subheader(f"{i + 1} 행운의 번호 : :green[{generate_lotto()}]")
