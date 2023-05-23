import speedtest

test = speedtest.Speedtest()
download =  test.download()
upload = test.upload()
print(download)
print(upload)