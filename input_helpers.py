# Functions related to generating or reading in
# data for the dogsvscats challenge

__author__ = "Ben Caine"
__email__ = "Bcaine0@gmail.com"
__date__ = "1/22/2016"

import sys

def read_stdin():
    for line in sys.stdin:
        import pdb; pdb.set_trace()
        print line

    return None

def format_input(data):
    data = [d.split(" ") for d in data.split("\n")]
    
    # Get rid of any starting or trailing empty strings
    if len(data[0]) == 0:
        data = data[1:]
    if len(data[-1:]) == 0:
        data = data[:-1]

    # Toss out the first row, which is unnecessary info
    data = data[1:]
    
    # Create structured data 
    # format: [{"header": [c, d, v], "votes": [['C1', 'D1'], [..]]}, {...}]
    test_cases = []
    
    next_header = 0
    for i, row in enumerate(data):
        if i == next_header:
            # If its not really a header, break
            if len(row) < 3: break                
            # Grab header, and calculate when the next is
            header = [int(val) for val in row]
            next_header += (header[2] + 1)
            # Create new case and skip to next row (first vote)
            test_cases.append({"header": header})
            continue
        
        # Add votes data to the case dictionary
        if "votes" in test_cases[-1]:
            test_cases[-1]["votes"].append(row)
        else:
            test_cases[-1]["votes"] = [row]
        
    return test_cases
