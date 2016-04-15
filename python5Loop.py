#import stuff
import os
#import time

import pandas as pd
import pprint


#some vars
root = '/media/sf_Shared/Learn-Python/gmw/'
save = '/media/sf_Shared/Learn-Python/'
files = os.listdir(root)

#get the file type
def get_type(file):
    """

    :param file: File to parse - takes only .txt
    :return: Returns list of types
    """

    if file.endswith('.txt'):
        #Split file if txt and add to list if not a number
        file = (file[:-4].split('_'))
        result = []
        for f in file:
            if not f.isdigit():
                result.append(f)

        return result


#get count of NaN in CSV for dictionary
def get_keys(file):
    """

    :param file: File to process - takes only .txt
    :return: Returns Dictionary with Columnname as Key and number of NaN as value
    """
    if file.endswith('.txt'):
        loc = root + file
        #process CSV
        df = pd.read_csv(loc)
        #sum up NaN
        nanSeries = df.isnull().sum()
        #series to dict
        dict = nanSeries.to_dict()

    return dict


#Routine to process files
#Open file for writing
out = open(save + 'output.txt', 'w')

try:
    for f in files:
        if f.endswith('.txt'):
            #Give user feedback
            print "Processing file: %s" %(f)
            #write stuff to file
            print >> out, "Filename: " + str(root) + str(f)
            print >> out, "Filetype: ", get_type(f)
            print >> out, "KeyValue NaN:\n"
            pprint.pprint(get_keys(f), out)
            print >> out, "\n\n\n"
            #time.sleep(1)
except:
    print "Error in: %s" %(f)

#Close file after writing
out.close()

#Give feedback
print "Done"