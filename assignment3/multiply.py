import MapReduce
import sys
import json

"""
Matrix Multiplication
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: document identifier
    # value: document contents
    matrix_name = record[0]
    matrix_row = record[1]
    matrix_column = record[2]
    matrix_value = record[3]
    for i in range(0,5):
        if matrix_name=='a':
            mr.emit_intermediate(str(matrix_row)+str(i),str(matrix_value)+'_'+str(matrix_column))
        else:
            mr.emit_intermediate(str(i)+str(matrix_column),str(matrix_value)+'_'+str(matrix_row))

def reducer(key, list_of_values):
    # Extract the suffix from the values to pair up values that have to be multiplied
    pairs = {}
    for value in list_of_values:
        suffix = value[-1:]
        pairs.setdefault(suffix,[])
        pairs[suffix].append(value[:-2])        
    
    result = 0
    for k in pairs.keys():
        l = pairs[k]
        if len(l)==2:
            result += int(l[0])*int(l[1])
    #print str(key) +': '+str(result)
    mr.emit((int(key[0]),int(key[1]),int(result)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
