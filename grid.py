import pygame

class Grid:
    def __init__(self):
        self.previous=[-1,-1]
        self.count=0
        self.gameover=''
        self.grid_lines=[((0,200),(600,200))
                        ,((0,400),(600,400))
                        ,((200,0),(200,600))
                        ,((400,0),(400,600))]
        self.cell_lines =[((10,70),(190,70))
                        ,((70,10),(70,190))
                        ,((10,130),(190,130))
                        ,((130,10),(130,190))
                        ,((210,270),(390,270))
                        ,((270,210),(270,390))
                        ,((210,330),(390,330))
                        ,((330,210),(330,390))
                        ,((210,70),(390,70))
                        ,((270,10),(270,190))
                        ,((210,130),(390,130))
                        ,((330,10),(330,190))
                        ,((10,270),(190,270))
                        ,((70,210),(70,390))
                        ,((10,330),(190,330))
                        ,((130,210),(130,390))
                        ,((330,10),(330,190))
                        ,((410,270),(590,270))
                        ,((470,210),(470,390))
                        ,((410,330),(590,330))
                        ,((530,210),(530,390))
                        ,((330,10),(330,190))
                        ,((10,470),(190,470))
                        ,((70,410),(70,590))
                        ,((10,530),(190,530))
                        ,((130,410),(130,590))
                        ,((410,70),(590,70))
                        ,((470,10),(470,190))
                        ,((410,130),(590,130))
                        ,((530,10),(530,190))
                        ,((10,470),(190,470))
                        ,((70,410),(70,590))
                        ,((10,530),(190,530))
                        ,((130,410),(130,590))
                        ,((410,470),(590,470))
                        ,((470,410),(470,590))
                        ,((410,530),(590,530))
                        ,((530,410),(530,590))
                        ,((210,470),(390,470))
                        ,((270,410),(270,590))
                        ,((210,530),(390,530))
                        ,((330,410),(330,590))]
        self.matrix=[[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]],[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]]
        self.wins=[[0,0,0],[0,0,0],[0,0,0]]
    def draw(self,screen):
        for line in self.grid_lines:
            pygame.draw.line(screen,(255,255,255),line[0],line[1],1)
        for line in self.cell_lines:
            pygame.draw.line(screen,(0,255,0),line[0],line[1],1)

    def display(self,i,j):
        print(self.matrix[i][j])
    
    def mark(self,x,y,screen):
        x1=x//200
        y1=y//200
        x2=x-(x1*200)
        y2=y-(y1*200)
        if y2<=70:
            if x2<=70:
                x3=0
                y3=0
            elif x2>=130:
                x3=0
                y3=2
            else :
                x3=0
                y3=1
        elif y2>=130:
            if x2<=70:
                x3=2
                y3=0
            elif x2>=130:
                x3=2
                y3=2
            else :
                x3=2
                y3=1
        else :
            if x2<=70:
                x3=1
                y3=0
            elif x2>=130:
                x3=1
                y3=2
            else :
                x3=1
                y3=1
        if (self.matrix[y1][x1][x3][y3]==0 and self.previous[0]==-1 and self.previous[1]==-1) or (self.matrix[y1][x1][x3][y3]==0 and self.previous[0]==x1 and self.previous[1]==y1):
            if self.count%2==0:
                self.matrix[y1][x1][x3][y3]='O' 
                d=self.pic(x1,y1,y3,x3,'O')
                self.win(y1,x1,'O',screen)
            else :
                self.matrix[y1][x1][x3][y3]='X'
                d=self.pic(x1,y1,y3,x3,'X')
                self.win(y1,x1,'X',screen)
            self.previous[0]=y3
            self.previous[1]=x3
            return d
        else:
            self.count=self.count-1
            return(-1,-1)

    def pic(self,a,b,c,d,m):
        a1=a*200
        b1=b*200
        c1=c*60
        d1=d*60
        af=a1+10+c1
        bf=b1+10+d1
        return (af,bf)
        
    def win(self,a,b,m,screen):
        matrix=self.matrix[a][b]
        if (matrix[0][0]==m and matrix[0][1]==m and matrix[0][2]==m) or (matrix[1][0]==m and matrix[1][1]==m and matrix[1][2]==m) or (matrix[2][0]==m and matrix[2][1]==m and matrix[2][2]==m) or (matrix[0][0]==m and matrix[1][1]==m and matrix[2][2]==m) or (matrix[0][2]==m and matrix[1][1]==m and matrix[2][0]==m) or (matrix[0][0]==m and matrix[1][0]==m and matrix[2][0]==m) or (matrix[0][1]==m and matrix[1][1]==m and matrix[2][1]==m) or (matrix[0][2]==m and matrix[1][2]==m and matrix[2][2]==m):
            if self.wins[a][b]==0 :
                self.wins[a][b]=m
        matrix=self.wins
        if (matrix[0][0]==m and matrix[0][1]==m and matrix[0][2]==m) or (matrix[1][0]==m and matrix[1][1]==m and matrix[1][2]==m) or (matrix[2][0]==m and matrix[2][1]==m and matrix[2][2]==m) or (matrix[0][0]==m and matrix[1][1]==m and matrix[2][2]==m) or (matrix[0][2]==m and matrix[1][1]==m and matrix[2][0]==m) or (matrix[0][0]==m and matrix[1][0]==m and matrix[2][0]==m) or (matrix[0][1]==m and matrix[1][1]==m and matrix[2][1]==m) or (matrix[0][2]==m and matrix[1][2]==m and matrix[2][2]==m):
            if m=='O':
                self.gameover='O'
            else:
                self.gameover='X'
                