file_location="C:\\Users\\noudu\\OneDrive\\Desktop\\Python2\\demo\\demo.txt"
file_location_write="C:\\Users\\noudu\\OneDrive\\Desktop\\Python2\\demo\\demo_write.txt"
file_object=open(file_location,'r')
print(file_object.readlines())
file_object.close()

file_object=open(file_location_write,'w')
file_object.write("this is new file")


new_one=["this \n", "is \n", "new \n", "file \n" ]
for new in new_one:
    file_object.write(new)
file_object.close()
