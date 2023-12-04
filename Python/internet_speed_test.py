import speedtest
# Speed test
st = speedtest.Speedtest()
# Download Speed
ds = st.download()
print(ds)