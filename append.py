
try:
    fp=open('student.csv','a')
    print(fp)
    print("file is open")

except FileNotFoundError:

    print("no such file found, please create it")
	
finally:

   fp.close()	
	