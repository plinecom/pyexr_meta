
file_path = "/root/exr/v001/V14_29_16A_rtc_v001.0001.exr"
fp = open(file_path, "rb")

magic = "762F3101"
version = "02"
flag = "000000"
# // A zero-length attribute name indicates the end of the header.
i = 0
for f in fp:
    str = f.split('\0')
    print str
    i += 1
    if i >= 10:
        break


#fp.readinto(_header)
fp.close()
