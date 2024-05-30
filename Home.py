import streamlit as sl
import pandas

sl.set_page_config(layout="wide")

col1, col2 = sl.columns(2)

with col1:
    sl.image("images/photo.png")

with col2:
    sl.title("Zamer Aeli")
    my_des = """
    Hey there, welcome to my portfolio! I’m all about that music life, especially when I’m jamming on the tabla. Chess is my go-to for strategic fun, and I can ace a Rubik's Cube in no time.

I’m a total nerd for learning, especially in programming. Python is my playground, and I’m diving into the world of ethical hacking for some extra excitement. My projects reflect this mix of interests, showcasing my knack for coding and problem-solving with a twist of creativity.

Join me on this journey through music, strategy, and tech wizardry. Let’s have a blast creating awesome stuff together!
"""
    sl.info(my_des)

content1 = """
Below you will find some of the apps I have build in python. Feel free to contact me!
"""
sl.write(content1)

col3, empty_col, col4 = sl.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        sl.image("images/" + row["image"])
        sl.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        sl.image("images/" + row["image"])
        sl.write(f"[Source Code]({row['url']})")
