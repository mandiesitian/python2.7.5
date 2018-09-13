#_*_ coding:utf-8 _*_;

def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # 返回处理后的结果
    data=line.strip().split(" ")
    over=True;
    over_all=True;
    data_list=[]
    count=1;
    die = 0;
    newdie=0;

    while(over_all):
        while(over):
            data=int(data)-2;

            print(data)




# solution("1 12 3 6 10")
print(solution("1 12 3 6 10"))