import streamlit as sl
import pandas

sl.set_page_config(layout="wide")

col1, col2 = sl.columns(2)

with col1:
    sl.image("images/photo.png")

with col2:
    sl.title("Zamer Aeli")
    my_des = """
    Hi , I am Zamer! I am learning python and ethical hacking because I love doing it and also to raise my family. 
    I play chess and love to workout. I am a noob to programming and creating apps but I am trying hard to reach the greater heights. 
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
        print(row)

with col4:
    for index, row in df[10:].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        sl.image("images/" + row["image"])
        sl.write(f"[Source Code]({row['url']})")
