import copy

class grid:
    def __init__(self, stat, dim):
        self.pre = None
        #stat是输入的二维列表棋盘状态，dim是输入的棋盘维数
        self.dim = dim
        self.targetGen()
        self.stat = stat
        self.find0pos()
        self.update() #更新启发函数的相关信息
    
    #生成目标状态
    def targetGen(self):
        target = []
        for i in range(self.dim):
            tmp = []
            for j in range(self.dim):
                tmp.append(i*self.dim+j+1)
            target.append(tmp)
        target[-1][-1] = 0
        self.target = target
    
    # f(n) = g(n) + h(n)
    def update(self):
        self.funcH()
        self.funcG()
        self.funcF()
    
    #启发函数F
    def funcF(self):
        self.F = self.G + self.H
    
    #G表示深度，也就是走的步数
    def funcG(self):
        if self.pre != None:
            self.G = self.pre.G + 1
        else:
            self.G = 0

    #H是和目标状态的曼哈顿距离之和
    def funcH(self):
        self.H = 0
        for i in range(self.dim):
            for j in range(self.dim):
                targetX = self.target[i][j]
                nowP = self.findx(targetX)
                self.H += abs(nowP[0]-i) + abs(nowP[1]-j)

    #输出当前棋盘状态
    def display(self):
        for i in range(self.dim):
             print(self.stat[i])
        print("F(n)=", self.F, ", G(n)=", self.G, ", H(n)=", self.H)
        print("-"*20)

    #打印出解路径
    def displayAns(self):
        ans = []
        ans.append(self)
        p = self.pre
        while(p):
            ans.append(p)
            p = p.pre
        ans.reverse()
        i = 0
        for step in ans:
            print("* STEP", i, ":")
            step.display()
            i += 1    

    #找到数字x的位置
    def findx(self, x):
        for i in range(self.dim):
            if x in self.stat[i]:
                j = self.stat[i].index(x)
                return [i,j]

    #找到空白格的位置
    def find0pos(self):
        self.zero = self.findx(0)

    #扩展当前状态，也就是上下左右移动。返回的是一个状态列表，也就是包含stat的列表
    def expand(self):
        i = self.zero[0]
        j = self.zero[1]
        gridList = []
        if j != 0: #空白格在非第一列的时候可以左移
            gridList.append(self.left())
        if i != 0:
            gridList.append(self.up())
        if i != self.dim-1:
            gridList.append(self.down())
        if j != self.dim-1:
            gridList.append(self.right())
        return gridList

    #deepcopy多维列表的复制，防止指针赋值将原列表改变
    #move只能移动行或列，即row和col必有一个为0
    #向某个方向移动
    def move(self,row,col):
        newStat = copy.deepcopy(self.stat)
        #交换对应数字和空白格
        tmp = self.stat[self.zero[0]+row][self.zero[1]+col]
        newStat[self.zero[0]][self.zero[1]] = tmp
        newStat[self.zero[0]+row][self.zero[1]+col] = 0
        return newStat

    def up(self):
        return self.move(-1,0)

    def down(self):
        return self.move(1,0)

    def left(self):
        return self.move(0,-1)

    def right(self):
        return self.move(0,1)