import glob
import pandas as pd

all_files = glob.glob(r"C:/Users/hp/PycharmProjects/bigdataProject/docs/*")

df_list = []

for file in all_files:
    df_list.append(pd.read_csv(str(file)))
df = pd.concat(df_list)
# Write the merged DataFrame to a new CSV file
df.to_csv('C:/Users/hp/PycharmProjects/bigdataProject/docs/merged_file.csv', index=False)