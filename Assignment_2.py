import os, random

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for i in range(1, 11):
        file_path = os.path.join(folder, f"file_{i}.txt")
        with open(file_path, "a+") as f:
            f.write(f"This is file number {i}")
    
def thanos_snap(folder):
    files = os.listdir(folder)
    half = len(files) // 2
    to_delete = random.sample(files, half)
    for f in to_delete:
        os.remove(os.path.join(folder, f))
    print(f"{half} files deleted.")
    print("Deleted files:")
    for f in to_delete:
        print(f)
        
path = r"C:\Users\el_bostan\Desktop\DEPI4\Assignment task 4"

create_folder(path)
thanos_snap(path)
