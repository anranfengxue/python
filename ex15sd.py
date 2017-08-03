
filename = raw_input("Input your filename:")

txt = open(filename)

print "Here's your file %r:" % filename

print txt.read()
print txt.fileno()
print txt.flush()
print txt.isatty()

print txt.readline(2)
print txt.readlines(2)

print txt.tell()
txt = open(filename,'a')
print txt.writelines("what is the end?")
txt = open(filename,'r')
print txt.read()


txt.close()