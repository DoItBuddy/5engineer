# 5engineer

import streamlit as st
import pandas as pd
import numpy as np
import time  

st.title("Gautam sharma(title)")
st.header("Gautam sharma(header)")
st.subheader("gautam sharma(sub header)")
st.write("gautam sharma(text)")
st.markdown("gautam sharma(markdown)")
st.caption("gautam sharma(caption)")

st.image("flower.jpg")
st.audio("sound1.mp3")
st.video("video1.mp4")

st.checkbox("checkbox")
st.button("click button")
st.radio( "pick your sports ",['pune','mumbai','delhi','surat'])

st.selectbox("pick your sports ",['pune','mumbai','delhi','surat']) 
st.multiselect('pick favourite sports',['cricket','football','basketball'])
st.select_slider('give a remark',['bad', 'good', 'excellent'])
st.slider('your marks ', 0,100)

on=st.toggle("Active feature")
if on:
    st.write("Feature activated!")
    
number = st.number_input("Insert a number")
st.write("the current number is ",number)
                          
d = st.date_input("when's your birthday", value=None)
st.write("your birthday is: ",d) 

t =st.time_input ("set analarm for ", value=None)
st.write("alarm is set for",t)     

st.number_input("enter yor marks",0,100)
st.text_input("enter text")  
st.date_input("exam date")
st.time_input("exam time")
st.text_area("descrption")
st.file_uploader("upload file")
st.color_picker("choose a color")   

st.success("success")
st.error("error")
st.warning("warning")               
st.info("information")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("gautam sharma")
st.sidebar.image("flower.jpg")

df = pd.DataFrame (np.random.randn(50,20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)

df= pd.DataFrame(
    np.random.randn(10,5), columns=("col %d" % i for i in range(5))
)

st.table(df)

col1, col2, col3 =st.columns(3)
col1.metric("Temerature", "70 F", "1.2 F")
col2.metric ("wind", "9 mph", "-8%")
col3.metric("Humidity","86%", "4%")

prompt = st.chat_input("say something")
if prompt:
    st.write(f"user has sent the following promt: {prompt}")
    
with st.status("step 1"):
    st.write("step 2")
    time.sleep(1)
    st.write("step 3")
    time.sleep(1)
    st.write("step 4")
st.button("Rerun")
    
chart_data = pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.area_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.line_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.bar_chart(chart_data)

df = pd.DataFrame(
    np.random.randn(1000,2) / [70,60] + [47.76, -100.4],
    columns= ["lat","lon"])
st.map(df)

with st.chat_message("user"):
    st.write("Hello ji")
