try:
    klu1 = open("sample.txt","w")
    try:
        klu1.write("This is s1 section")
    finally:
        klu1.close()
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    klu1.close()