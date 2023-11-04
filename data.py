def readfile(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except IOError:
        print("Error: could not read file " + filename)
def create_file(filename,text):
    try:
        with open(filename, 'w') as f:
            f.write(text)
    except IOError:
        print("Error: could not create file " + filename)

    
