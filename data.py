def readfile(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            for line in contents:
                elements=line.split('-')
                stage = elements[0]
                number_of_move =elements[1]
                number_of_turns =elements[2]
                time =elements[3]
    except IOError:
        print("Error: could not read file " + filename)
def write_file(filename,text):
    try:
        with open(filename, 'w') as f:
            f.write(text)
    except IOError:
        print("Error: could not write file " + filename)

    
