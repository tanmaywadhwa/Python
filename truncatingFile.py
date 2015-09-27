from sys import argv

script,filename = argv

print "opening current file"
file = open(filename,'w')

print "sure you want to do this? press ctrl + c now if not!"
raw_input("?")

print "Erasing the current file"
file.truncate()
print "Deleted!! huhahaha"
print "enter 3 lines to write"
file.write(raw_input()+"\n")
file.write(raw_input()+"\n")
file.write(raw_input()+"\n")

print "done! closing file"
file.close()

print "file written and closed. Bbye"

