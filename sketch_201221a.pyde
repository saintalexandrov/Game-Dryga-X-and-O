# keep state of each square on board
top_left = 0 # 0 empty, 1 - x, 2 - 0
top_middle = 0
top_right = 0

middle_left = 0
middle_middle = 0 
middle_right = 0

bottom_left = 0
bottom_middle = 0 
bottom_right = 0

# turn 
turn = 2

n = 0

# manage if game is over 
global game_over# False - game is on, True - game over
game_over = False 

def setup():
    size(700, 700)
    
def draw():
    
    # draw game board
    for y in range (3):
        for x in range(3):
            rect(200*x,200*y,200,200)
            
            
    
    ###########################
    # TOP ROW
    
    # top left
    if top_left == 2:
        # draw top left O                
        ellipse(100,100,150,150)
        
    elif top_left == 1:               
        # draw top left X
        line(0,0,200,200)
        line(200,0,0,200)
        
    
    # top middle
    
    if top_middle == 2:
        ellipse(300,100,150,150)  
    elif top_middle == 1:
        line(200,0,400,200)
        line(400,0,200,200)
    # top right
    
    if top_right == 2:
        ellipse(500,100,150,150)  
    elif top_right == 1:
        line(400,0,600,200)
        line(600,0,400,200)
    
    ###########################
    # MIDDLE ROW
    
    
    # middle left
   
    if middle_left == 2: 
        ellipse(100,300,150,150)
    elif middle_left == 1:
        line(0,200,200,400)
        line(200,200,0,400)
    
    # middle middle
    
    if middle_middle == 2:
        ellipse(300,300,150,150) 
    elif middle_middle == 1:
        line(200,200,400,400)
        line(400,200,200,400)
    
    # middle right
    if middle_right == 2:
        ellipse(500,300,150,150)  
    elif middle_right == 1:
        line(400,200,600,400)
        line(600,200,400,400)
    
    
    ###########################
    # BOTTOM ROW
    
    # bottom left  
      
    if bottom_left == 2:
        ellipse(100,500,150,150)  
    elif bottom_left == 1:
        line(0,400,200,600)
        line(200,400,0,600) 
    
    # bottom middle
    
    if bottom_middle == 2:
        ellipse(300,500,150,150)  
    elif bottom_middle == 1:
        line(200,400,400,600)
        line(400,400,200,600)  
    
    # bottom right
    if bottom_right == 2:
        ellipse(500,500,150,150)  
    elif bottom_right == 1:
        line(400,400,600,600)
        line(600,400,400,600)
    
    if game_over: #  == True:
        if turn == 1:
            #font = createFont("LetterGothicStd.ttf", 32);
            #textFont(font);  
            #text("game over - X wins!", 10, 10)
            textSize(32)
            stroke(255,0,0);
            text("Player 1 won!", 86, 646);
            
        if turn == 2:
            #text("game over - Y wins!",10, 10)
            textSize(32)
            stroke(0,255,10);
            text("Player 2 won!", 86, 646);
            
        global n
        if n == 1:
            line(0,100,600,100)    
        if n == 2:
            line(0,300,600,300)
        if n == 3:
            line(0,500,600,500)
        if n == 4:
            line(100,0,100,600)
        if n == 5:
            line(300,0,300,600)
        if n == 6:
            line(500,0,500,600)    
        if n == 7:
            line(2,8,598,592)        
        if n == 8:
            line(597,2,3,598)
            
                                            
def swith_turns():
        global turn    
        # switch turns
        if turn == 1:
            turn = 2 
        else:
            turn = 1  
            
def mousePressed():
    println( [mouseX, mouseY] )
    global top_left, top_middle, top_right 
    global middle_left, middle_middle, middle_right
    global bottom_left, bottom_middle, bottom_right
    global game_over
    global n
    if (mouseX > 0 and mouseX < 200) and (mouseY > 0 and mouseY < 200) :
        top_left = turn
        swith_turns()        
    elif (mouseX > 200 and mouseX < 300) and (mouseY > 0 and mouseY < 200) :
        top_middle = turn
        swith_turns()       
    elif (mouseX > 400 and mouseX < 600) and (mouseY > 0 and mouseY < 200) :
        top_right = turn
        swith_turns() 
    elif (mouseX > 0 and mouseX < 200) and (mouseY > 200 and mouseY < 400) :
        middle_left = turn
        swith_turns()    
    elif (mouseX > 200 and mouseX < 400) and (mouseY > 200 and mouseY < 400) :
        middle_middle = turn
        swith_turns()    
    elif (mouseX > 400 and mouseX < 600) and (mouseY > 200 and mouseY < 400) :
        middle_right = turn
        swith_turns()   
    elif (mouseX > 0 and mouseX < 200) and (mouseY > 400 and mouseY < 600) :
        bottom_left = turn
        swith_turns() 
    elif (mouseX > 200 and mouseX < 400) and (mouseY > 400 and mouseY < 600) :
        bottom_middle = turn
        swith_turns()   
    elif (mouseX > 400 and mouseX < 600) and (mouseY > 400 and mouseY < 600) :
        bottom_right = turn
        swith_turns()  
          
    if top_left == 1 and top_middle == 1 and top_right == 1:
        print("winner! middle row 1")
        n = 1
        game_over = True
        fill(245);
        textSize(14);
        text("dfs", 30, 100)
        
    if top_left == 2 and top_middle == 2 and top_right == 2 :
        print("winner! middle row 1")
        n = 1
        game_over = True  
             
    # check for winners 
    if middle_left == 1 and middle_middle ==1 and middle_right == 1:
        print("winner! middle row 1")
        n = 2
        game_over = True
        
    # check for winners 
    if middle_left == 2 and middle_middle == 2 and middle_right == 2:
        print("winner! middle row 2")
        n = 2
        game_over = True
        
    if bottom_left == 1 and bottom_middle == 1 and bottom_right == 1:
        print("winner! middle row 2")
        n = 3
        game_over = True
        
    if bottom_left == 2 and bottom_middle == 2 and bottom_right == 2:
        print("winner! middle row 2")
        n = 3
        game_over = True   
     
    if bottom_left == 1 and middle_left == 1 and top_left == 1:
        print("winner! middle row 2")
        n = 4
        game_over = True 
           
    if bottom_left == 2 and middle_left == 2 and top_left == 2:
        print("winner! middle row 2")
        n = 4
        game_over = True 
        
    if top_middle == 1 and middle_middle == 1 and bottom_middle == 1:
        print("winner! middle row 2")
        n = 5
        game_over = True
        
    if top_middle == 2 and middle_middle == 2 and bottom_middle == 2:
        print("winner! middle row 2")
        n = 5
        game_over = True              
                            
    if top_right == 1 and middle_right == 1 and bottom_right == 1:
        print("winner! middle row 2")
        n = 6
        game_over = True                                 
                                                
    if top_right == 2 and middle_right == 2 and bottom_right == 2:
        print("winner! middle row 2")
        n = 6
        game_over = True                                                      
                                                                    
    if top_left == 1 and middle_middle == 1 and bottom_right == 1:
        print("winner! middle row 2")
        n = 7
        game_over = True                                                                          
                                                                                        
    if top_left == 2 and middle_middle == 2 and bottom_right == 2:
        print("winner! middle row 2")
        n = 7
        game_over = True                                                                                              
    if top_right == 1 and middle_middle == 1 and bottom_left == 1:
        print("winner! middle row 2")
        n = 8
        game_over = True 
               
    if top_right == 2 and middle_middle == 2 and bottom_left == 2:
        print("winner! middle row 2")
        n = 8
        game_over = True                                                                                                        
                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                
    print("game")
    # player 1`s turn  
    #top_left = 1                 
