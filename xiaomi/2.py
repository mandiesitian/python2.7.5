#_*_ coding:utf-8 _*_;
def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # 返回处理后的结果
    data=line.strip().split(",");
    print(data);
    list1=[];
    for i in range(0,len(data)):
        list1=data.remove(data[i]);
        print(list1)



    return



solution(" -1,0,1,2,-1,-4")














