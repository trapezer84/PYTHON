import glob

dir_lists = glob.glob("c:\\", recursive=True)

for dir in dir_lists:
    print(dir)

