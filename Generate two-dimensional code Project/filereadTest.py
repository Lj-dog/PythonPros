
def ReadTxt(file_name):
    dict = {}
    file = open(file_name,'r')
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(',')
        dict[parts[0]] = (parts[1],parts[2])
    return dict


dict = ReadTxt("./PanelInfo.txt")
for di in dict.keys():
    print(f"{di},{dict[di]}")