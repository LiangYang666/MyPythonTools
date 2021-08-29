import os
import shutil

if __name__ == "__main__":
    source_dir = "C:\\source_dir"
    dst_dir = "C:\\dst_dir"
    imgs = os.listdir(dir)
    sorted(imgs)
    for i, img_name in enumerate(imgs):
        if i % 500 == 0:
            shutil.copyfile(os.path.join(source_dir, img_name), os.path.join(dst_dir, img_name))
