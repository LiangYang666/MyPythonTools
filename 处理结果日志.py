import os

path = "E:\OneDrive - csu.edu.cn\Competitions\空天杯\决赛训练权重\结果日志"
if __name__ == "__main__":
    files = sorted(os.listdir(path))
    files = [x for x in files if x.endswith('.txt')]
    files_has_write = [False] * len(files)
    for i, file in enumerate(files):
        loss_point = 0
        false_alarm = 0
        continuity_loss = 0
        fpath = os.path.join(path, file)
        with open(fpath, 'r', encoding="utf-8") as f:
            lines = f.readlines()
        # print(lines)
        for line in lines:
            line = line.strip()
            if line.startswith('漏检点数'):
                loss_point += eval(line.split(":")[-1])
            elif line.startswith('虚警点数'):
                false_alarm += eval(line.split(":")[-1])
            elif line.startswith('轨迹连续性失分'):
                continuity_loss += eval(line.split(":")[-1])
            elif line.startswith('虚警总数'):
                files_has_write[i] = True
                break
        if not files_has_write[i]:
            print("writing to ", fpath)
            with open(fpath, 'a', encoding="utf-8") as f:
                f.write(f'漏检总数:{loss_point}\n')
                f.write(f'虚警总数:{false_alarm}\n')
                f.write(f'连续性失分总数:{continuity_loss}\n')




