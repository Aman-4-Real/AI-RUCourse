from Grid import *
import random

#随机生成初始状态
def statRandomGen(dim):
    orderlst = []
    res = []
    for i in range(dim*dim):
        orderlst.append(i+1)
    orderlst[-1] = 0
    random.shuffle(orderlst)
    for i in range(dim):
        tmp = orderlst[i*dim:(i+1)*dim]
        res.append(tmp)
    return res
    
    
#判断状态g是否在状态集合中，g是对象，gList是对象列表
#返回的结果是一个列表，第一个值是真假，如果是真则第二个值是g在gList中的位置索引
def isin(g,gList):
    gstat=g.stat
    statList=[]
    for i in gList:
        statList.append(i.stat)
    if gstat in statList:
        res=[True,statList.index(gstat)]
    else:
        res=[False,0]
    return res

#计算逆序数之和
def InvNum(nums):
    num = 0
    tmp = [i for item in nums for i in item]
    for i in range(len(tmp)):
        if tmp[i] != 0:
            for j in range(i):
                if tmp[j] > tmp[i]:
                    num += 1
    return num

#根据逆序数之和判断所给问题是否可解
def judge(src, target):
    N1 = InvNum(src)
    N2 = InvNum(target)
#     print(N1, N2)
    if N1%2 == N2%2:
        print("The problem has a solution, in searching...")
        return True
    else:
        return False

#Astar算法的函数
def Astar(startStat, dim):
    #open和closed存的是grid对象
    open = []
    closed = []
    #初始化状态
    g = grid(startStat, dim)
    #检查是否有解
    if judge(startStat, g.target) != True:
        print("No solution!")
        exit(1)

    open.append(g)
    #time变量用于记录遍历次数
    time = 0
    #当open表非空时进行遍历
    while(open):
        #根据启发函数值对open进行排序，默认升序
        open.sort(key=lambda G:G.F)
        #找出启发函数值最小的进行扩展
        minFStat=open[0]
        #检查是否找到解，如果找到则从头输出移动步骤
        if minFStat.H == 0:
            print("Search times:",time, " Steps:",minFStat.G)
            print("The each step of moving:")
            minFStat.displayAns()
            break

        #走到这里证明还没有找到解，对启发函数值最小的进行扩展
        open.pop(0)
        closed.append(minFStat)
        expandStats = minFStat.expand()
        #遍历扩展出来的状态
        for stat in expandStats:
            #将扩展出来的状态（二维列表）实例化为grid对象
            tmpG = grid(stat, dim)
            #指针指向父节点
            tmpG.pre = minFStat
            #初始化时没有pre，所以G初始化时都是0
            #在设置pre之后应该更新G和F
            tmpG.update()
            #查看扩展出的状态是否已经存在与open或closed中
            findstat = isin(tmpG, open)
            findstat2 = isin(tmpG, closed)
            #在closed中,判断是否更新
            if findstat2[0] == True and tmpG.F < closed[findstat2[1]].F:
                closed[findstat2[1]] = tmpG
                open.append(tmpG)
                time += 1
            #在open中，判断是否更新
            if findstat[0] == True and tmpG.F < open[findstat[1]].F:
                open[findstat[1]] = tmpG
                time+=1
            #tmpG状态不在open中，也不在closed中
            if findstat[0] == False and findstat2[0] == False:
                open.append(tmpG)
                time += 1

N = eval(input("Please input the dimension of the grid:"))
# stat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [0, 14, 15, 13]]
stat = statRandomGen(N)
print("The init state is:")
for i in range(N):
    print(stat[i])
Astar(stat, N)