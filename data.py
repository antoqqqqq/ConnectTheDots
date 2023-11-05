def readfile(filename):
    try:
        with open(filename, 'r') as f:
            data_entries = []
            for line in f:
                #row(stage, number of moves, number of turns, time)
                row = []
                elements=line.strip('\n').split('-')
                row.append(elements[0])
                row.append(elements[1])
                row.append(elements[2])
                row.append(elements[3])

                data_entries.append(row)
            f.close()
        return data_entries
    except IOError:
        print("Error: could not read file " + filename)
def write_file(filename,text):
    try:
        element=text.split('-')
        data=[]
        data=readfile(filename)
        i=0
        for row in data:
            if (element[0]== row[0]):
                data[i] = element                                               
                break
            i=+1
        with open(filename, 'w') as f:
            for row in data:
                f.write(row[0]+'-'+row[1]+'-'+row[2]+'-'+row[3]+'\n')
    except IOError:
        print("Error: could not write file " + filename)
a=1
b=2
c=2
d=3
e=str(a)+"-"+str(b)+"-"+str(c)+"-"+str(d)
write_file('file_save_stage.txt',e)
