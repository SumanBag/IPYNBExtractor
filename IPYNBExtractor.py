#######
#
# Author: Akshay Gupta
# Description: 
#               Python3 script to read IPYNB files and 
#               extract the source code written inside
#               the cells and convert it into a .py file.
#
######
import sys
import json


try:
    fread=open(sys.argv[1],mode="r")
    fwrite=open(sys.argv[2],mode="w")
    data=fread.read()
    fread.close()
    jdata=json.loads(data)
    #print(jdata)
    for a in jdata['cells']:
        if a["cell_type"] in "code":
            for b in a["source"]:
                fwrite.write(b)
            fwrite.write("\n")
    fwrite.close()
except IndexError:
    hlp="""
    Usage: python3 IPYNBExtractor.py <inputFile> <outputFile>
            inputFile= IPYNB file to read
            outputFile= PY file to write
    """
    print(hlp)
