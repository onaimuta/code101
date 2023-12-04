import speedtest
# Speed test
st = speedtest.Speedtest()
# Download Speed
ds = st.download()
us = st.upload
print(ds)
print(us)