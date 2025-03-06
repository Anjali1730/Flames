import streamlit   # the command for creating virtual environment is python -m venu anyname(ex:env)
streamlit.header("FLAMES game")
s1=list(streamlit.text_input("Enter first name:"))
s2=list(streamlit.text_input("Enter second name:"))
for i in s1:
    if i in s2:
        s1.remove(i)
        s2.remove(i)
n=len(s1+s2)
s="FLAMES"
while len(s)>1:
    i=n%len(s)
    if i==-1:
        s=s[:len(s)-1]
    else:
        s=s[i+1:]+s[:i]
if streamlit.button("get results"):
    streamlit.success(s)
        