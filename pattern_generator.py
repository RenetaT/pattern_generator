from graphics import*
######## ask user ##########     

while True:
    winSize = int(input("Enter the size of the Window (5,7,9): "))
        
    if winSize in [5,7,9]:
        break
    print("Please enter a valid patch size - 5 or 9")
         
colors = ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]
    
while True:
    colorOne = input("Enter the first color, please(red,blue,green,orange,yellow,cyan): ")
    if colorOne in colors:
        break
    print("Invalid color, please choose from:", colors)
    
while True:
    colorTwo = input("Enter the second color, please(red,blue,green,orange,yellow,cyan): ")
    if colorTwo in colors and colorTwo != colorOne:
        break
    print("Invalid color, please choose from:", colors)

while True:
    colorThree = input("Enter the third color, please(red,blue,green,orange,yellow,cyan): ")
    if colorThree in colors and colorThree != colorOne and colorThree != colorTwo:
        break
    print("Invalid color, please choose from:", colors)

######## Penultimate  #########   

def rowOne(win, x, y,width,height,color):    
    
    for i in range(4):
        rectangle = Rectangle(Point(x, y), Point(x + width, y + height))
        rectangle.setFill(color)
        rectangle.setOutline("black")
        rectangle.draw(win)
        x += 25
        
def rowTwo(win, x, y,width,height,color):
    
    for i in range(3):
        
        rectangle = Rectangle(Point(x, y), Point(x + width, y + height))
        rectangle.setFill(color)
        rectangle.setOutline("black")
        rectangle.draw(win)
        x += 40
        
       
def drawPatternPenultimate(win,x ,y,color):    
    
    for row in range(10):
        if row % 2 == 0:
         rowOne(win, x, y,25,10,color)
        else:            
           rowTwo(win, x, y,20,10,color)
        y += 10
################# Final patch #######

def drawPatchFinal(win, xTopLeft, yTopleft,color):    
    point = Point(xTopLeft, yTopleft)
    step = 0
    for _ in range(10):
        p1 = Point(point.getX() + step, point.getY())
        p2 = Point(point.getX() + 100, point.getY() + 10 + step)
        line = Line(p1,p2)
        line.draw(win)
        line.setFill(color)
        step = step + 10
        
    point = Point(xTopLeft, yTopleft)
    step = 0
    for _ in range (10):
        p3 = Point(point.getX() , point.getY()+ step)
        p4 = Point(point.getX()+10+step ,point.getY()+100)
        line2 = Line(p3,p4)
        line2.draw(win)
        line2.setFill(color)
        step = step + 10
 
######## plain patch 
def plainPatch(win,xTopLeft,yTopleft,color):
        
    point = Point(xTopLeft,yTopleft)    
    rectangle = Rectangle(Point(point.getX(), point.getY()), Point(point.getX() + 100, point.getY() + 100))
    rectangle.setFill(color)
    rectangle.setOutline("black")
    rectangle.draw(win)
    
       
def main(winSize,colorOne,colorTwo,colorThree,colors):
    num = winSize*100
    win = GraphWin(" ", winSize*100,winSize*100)
    win.setBackground("white")

    for col in range(num):
        for row in range(num):
            x = col*100
            y = row*100
            if col %2==0:
                plainPatch(win, x, y, colorOne)
            else:
                plainPatch(win, x, y, colorTwo)            
            if row == col -1:
                plainPatch(win, x, y, colorThree)
            if row == col -2:
                plainPatch(win, x, y, colorThree)
            if row == col -3:
                plainPatch(win, x, y, colorThree)
            if row == col -4:
                plainPatch(win, x, y, colorThree)
            if row == col -5:
                plainPatch(win, x, y, colorThree)
            if row  == col -6:
                plainPatch(win, x, y, colorThree)
            if row == col -7:
                plainPatch(win, x, y, colorThree)
            if row == col -8:
                plainPatch(win, x, y, colorThree)
            if row==0 and col!=0:
                plainPatch(win, x, y, "white")
                drawPatchFinal(win, x, y,colorThree)
            if col == winSize -1 and row!=winSize-1:
                plainPatch(win, x, y, "white")
                drawPatchFinal(win, x, y,colorThree)            
            if col == 1 and row!=0 and row!=winSize-1:
                plainPatch(win, x, y, "white") 
                drawPatternPenultimate(win,x ,y,colorTwo)
            if col == 2 and row>1 and row!=winSize-1:
                plainPatch(win, x, y, "white") 
                drawPatternPenultimate(win,x ,y,colorOne)
            if col == 3 and row>2 and row!=winSize-1:
                plainPatch(win, x, y, "white") 
                drawPatternPenultimate(win,x ,y,colorTwo)
            if col == 4 and row>3 and row!=winSize-1:
                plainPatch(win, x, y, "white") 
                drawPatternPenultimate(win,x ,y,colorOne)
            if col == 5 and row>4 and row!=winSize-1:
                plainPatch(win, x, y, "white") 
                drawPatternPenultimate(win,x ,y,colorTwo)
            if col == 6 and row>5 and row!=winSize-1:
                plainPatch(win, x, y, "white") 
                drawPatternPenultimate(win,x ,y,colorOne)
            if col == 7 and row>6 and row!=winSize-1:
                plainPatch(win, x, y, "white") 
                drawPatternPenultimate(win,x ,y,colorTwo)
          
    
main(winSize,colorOne,colorTwo,colorThree,colors)


