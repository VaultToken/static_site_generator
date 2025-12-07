import os
import shutil

def clear_directory(path: str) -> None:
    if not os.path.exists(path):
        return

    for name in os.listdir(path):
        full_path = os.path.join(path, name)

        if os.path.isfile(full_path) or os.path.islink(full_path):
            #print(f"Deleting file: {full_path}")
            os.remove(full_path)
        elif os.path.isdir(full_path):
            #print(f"Deleting directory: {full_path}")
            shutil.rmtree(full_path)

def copy_recursive(src: str, dst: str) -> None:
    # Make sure destination directory exists
    os.makedirs(dst, exist_ok=True)

    for name in os.listdir(src):
        src_path = os.path.join(src, name)
        dst_path = os.path.join(dst, name)

        if os.path.isfile(src_path):
            #print("File:", src_path)
            shutil.copy2(src_path, dst_path)

        elif os.path.isdir(src_path):
            #print("Folder:", src_path)
            copy_recursive(src_path, dst_path)
