#_*_ coding:utf-8 _*_;

def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # 返回处理后的结果
    d,c=line.strip().split(" ");
    d=list(d);
    c=list(c);
    for i in range(0,len(d)):
        for j in range(0,len(c)):
            if(d[i]==c[j]):
                c[j]=-1;
                flag=1;
                break;
            flag=0;

        if(flag==1):
            continue;
        else:
            return "false";
            break;

    return "true";




    # print(c)
    # return



print(solution("aa aab"))

# str="aaa";
# a=list(str);
# print(a)