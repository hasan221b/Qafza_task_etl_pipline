import pandas as pd
import requests
import time
import datetime
from extract import *
from clean import *
from manage_id import *

#file_path = r"C:\Users\hasan\OneDrive\Desktop\New folder (2)\app\channels_ids.json"

#channel_ids = load_channel_ids(file_path)

#current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the file path relative to the script's directory
#file_path = os.path.join(current_dir, "channels_ids.json")
file_path = "channels_ids.json"

# Load the JSON file
channel_ids = load_channel_ids(file_path)

channel_id = channel_ids.pop(0)

t0 = time.time()
vidlist = getvidIDs(channel_id)
t1 = time.time()
print("Videos extracting finished in",str(t1-t0), "seconds", "\n")

t00 = time.time()
data = df_making(vidlist)
t11 = time.time()
print("Comments extracting finished in",str(t11-t00), "seconds", "\n")


data = clean_dataframe(data)


data.loc[:, 'comment'] = data['comment'].apply(clean_text)
t22 = time.time()
data['sentiment'] = data['comment'].apply(get_sentiment)
t33 = time.time()
print("Sentiment extracting finished in",str(t33-t22), "seconds", "\n")

print(data)

save_channel_list(file_path,channel_ids)

print(channels_ids)
#current_dir = os.path.dirname(os.path.abspath(__file__))

#dfile_path = os.path.join(current_dir, "dataset.csv")
dfile_path = "dataset.csv"

data.to_csv(dfile_path, mode='a', header=False, index=False)

x = pd.read_csv("dataset.csv")
print(x)
