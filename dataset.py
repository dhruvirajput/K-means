import pandas as pd
import numpy as np

def load_dataset(filename, filetype='csv', header=True):
    in_file = open(filename)
    data = []
    header_row = ''

    # Read the file line by line into instance structure
    for line in in_file.readlines():

        # Skip comments
        if not line.startswith("#"):
            
            # TSV file
            if filetype == 'tsv':
                if header:
                    header_row = line.strip().split('\t')
                else:
                    raw = line.strip().split('\t')
                    
            # CSV file
            elif filetype =='csv':
                if header:
                    header_row = line.strip().split(',')
                else:
                    raw = line.strip().split(',')
            
            # Neither = problem
            else:
                print ('Invalid file type')
                exit()

            # Append to dataset appropriately
            if not header:
                data.append(raw)
            header = False
    
    # Build a new dataframe of the data instance list of lists and return
    df = pd.DataFrame(data, columns=header_row)
    return df


def to_numeric(dataset, attr_name):
    
    # Get unique entries in column
    unique_vals = dataset[attr_name].unique()
    
    # Create dict
    val_dict = {}
    for val in unique_vals:
        if not val in val_dict:
            val_dict[val] = len(val_dict)
    
    # Replace values in attr_name col as per dict
    dataset[attr_name].replace(val_dict, inplace=True)
    #print val_dict
    # Return dataset and value dictionary
    return dataset, val_dict
  

def from_str(dataset, attrs):
  
    # Make conversions on list of attributes
    if type(attrs) == list:
        for attr_name in attrs:
            dataset[attr_name] = dataset[attr_name].astype(float)

    # Make conversion on single attribute
    else:
        data[attrs] = data[attrs].astype(float).fillna(0.0)
    
    # Return dataset after conversion
    return dataset


def to_matrix(dataset):
        
    return dataset.as_matrix()