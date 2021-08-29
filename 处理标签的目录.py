path = "E:\OneDrive - csu.edu.cn\Competitions\空天杯\决赛训练权重\文件\primary_contest_train_data.txt---"
if __name__=="__main__":
    with open(path, 'r') as f:
        lines = f.readlines()
    lines = [x.replace("/media/D_4TB/zhouhongjie/KTB/yolov5-develop/runs/exp2_alltrain/", "/public/home/hpc204611038/Project/KTB/data/") for x in lines]
    with open(path, 'w') as f:
        f.writelines(lines)