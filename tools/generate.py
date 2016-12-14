#!/usr/bin/env python3
import sys
import os

class DatabaseDbParseError(Exception):
    pass

def parse_and_write_to(input_fn, output, unlimited):
	input_line = 0
	with open(input_fn, "rt") as input:
		for line in input:
			input_line+=1
			if len(line.strip())>0 and line.strip()[0]!="#":
				toks = line.strip().split(" ")
				if not unlimited and len(toks)!=2:
					raise DatabaseDbParseError("Expected two tokens on line " 
							+ str(input_line)+" in file "+input_fn+" got "+str(len(toks)))
				elif unlimited and len(toks)!=1:
					raise DatabaseDbParseError("Expected one token on line "
							+ str(input_line)+" in file "+input_fn+" got "+str(len(toks)))
				
				if unlimited:
					output.write(toks[0]+" -1\n")
				else:
					output.write(toks[0]+" "+toks[1]+"\n")

with open(sys.argv[1], "wt") as output:
	for dir in sys.argv[2:]:
		for file in os.listdir(dir):
			parse_and_write_to(os.path.join(dir, file), output, "unlimited" in dir)
		