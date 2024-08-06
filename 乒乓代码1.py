#尝试一下11胜的代码
import random
import time

def main():
    jiasheng=0#甲胜的局数
    yisheng=0#乙胜的局数
    jia=0#甲胜的回合数
    yi=0#乙胜的回合数
    j=1#第几局
    h=1#第几回合
    # 定义甲与乙，假定甲胜率为60%，乙先仍为60%
    while True:
        print('\n----------第',j,'局-----------')
        time.sleep(0.5)
        t=random.random()
        if t<0.5:
            print('甲先开球')
            i=1
        else:
            print('乙先开球')
            i=2
        time.sleep(1)
        while True:
            if jia!=10 or yi!=10:
                print("----------第",j,'局 第',h,'回合----------')
                time.sleep(0.5)
                if i==1:
                    if h%4==1 or h%4==2:
                        print('甲发球')
                        m=random.randint(1,10)
                    else:
                        print('乙发球')
                        m=random.randint(3,12)
                else:
                    if h%4==3 or h%4==0:
                        print('甲发球')
                        m=random.randint(1,10)
                    else:
                        print('乙发球')
                        m=random.randint(3,12)
                time.sleep(2)
                if m<=6:
                    print('甲胜1回合')
                    jia+=1
                else:
                    print('乙胜1回合')
                    yi+=1
                time.sleep(0.5)
                print('当前比分 甲:乙=',jia,':',yi)
                time.sleep(2)
                if jia==11:
                    print('\n第',j,'局甲胜')
                    j+=1
                    h=1
                    jiasheng+=1
                    jia,yi=0,0
                    break
                elif yi==11:
                    print('\n第',j,'局乙胜')
                    j+=1
                    h=1
                    yisheng+=1
                    jia,yi=0,0
                    break
                h+=1
            elif jia==10 and yi==10:
                print('加赛!')
                while True:
                    print("----------第",j,'局 第',h,'回合----------')
                    time.sleep(0.5)
                    if i==1:
                        if h%2==1:
                            print('甲发球')
                            m=random.randint(1, 10)
                        else:
                            print('乙发球')
                            m=random.randint(3, 12)
                    else:
                        if h%2==0:
                            print('甲发球')
                            m=random.randint(1, 10)
                        else:
                            print('乙发球')
                            m=random.randint(3, 12)
                    time.sleep(2)
                    if m<=6:
                        print('甲胜1回合')
                        jia+=1
                    else:
                        print('乙胜1回合')
                        yi+=1
                    time.sleep(0.5)
                    print('当前比分 甲:乙=',jia,':',yi)
                    time.sleep(2)
                    if jia-yi==2 or jia==21:
                        print('\n第',j,'局甲胜')
                        j+=1
                        h=1
                        jiasheng+=1
                        jia,yi=0,0
                        break
                    elif yi-jia==2 or yi==21:
                        print('\n第',j,'局乙胜')
                        j+=1
                        h=1
                        yisheng+=1
                        jia,yi=0,0
                        break
                    h+=1
                break
        time.sleep(1)
        print('当前赢的局数 甲:乙=',jiasheng,':',yisheng)
        time.sleep(3)
        if jiasheng==3:
            print('甲赢得了比赛!')
            break
        elif yisheng==3:
            print('乙赢得了比赛!')
            break

if __name__ == '__main__':
    main()
