from enumaration import *
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
def read_stage(filename):
    try:
        with open(filename, 'r') as f:
            a=[]
            tiles_with_dot = []
            for line in f:
                a.append(list(line.strip('\n').split('-')))
            stage=a[0][0]
            n_tiles_perRow=a[1][0]
            number_node=a[2][0]
            y=3
            for i in range(int(number_node)):
                node1=a[y][0].split(',')
                node2=a[y][1].split(',')
                color=a[y][2].split(',')
                y+=1


                tiles_with_dot.append(((int(node1[0]),int(node1[1])),(int(node2[0]),int(node2[1])), (int(color[0]),int(color[1]),int(color[2]))))
            f.close()          
        return int(stage),int(n_tiles_perRow),int(number_node),tiles_with_dot
    except IOError:
        print("Error: could not read file " + filename)


