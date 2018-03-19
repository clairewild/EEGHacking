import os
import pandas

raw_data_directory = "/Users/claire/EEGHacking/raw-data"
clean_data_directory = "/Users/claire/EEGHacking/clean-data"

for filename in os.listdir(raw_data_directory):
    full_path = os.path.join(raw_data_directory, filename)
    data_frame = pandas.read_csv(full_path)
    cleaned_data_frame = data_frame[pandas.notnull(data_frame['Delta_TP9'])]
    new_path = os.path.join(clean_data_directory, filename)
    
    cleaned_data_frame.reset_index().to_csv(new_path, index=False, header=False)