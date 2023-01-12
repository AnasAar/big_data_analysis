import zipfile
import glob

all_files = glob.glob(r"files\*")
i= 0
for file in all_files:
    if '.zip' in str(file):
        print(str(file)[6:])
        with zipfile.ZipFile(str(file), "r") as zip_ref:
            zip_ref.extractall("files")
print(i)


