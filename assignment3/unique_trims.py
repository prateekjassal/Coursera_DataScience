import MapReduce
import sys
import json

"""
Nucleotide Problem
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    nucleotide_id = record[0]
    nucleotide_sequence = record[1]
    mr.emit_intermediate(nucleotide_sequence[:-10],1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
