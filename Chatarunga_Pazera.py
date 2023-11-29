import tkinter 
from PIL import Image, ImageTk
class Gamestate:
    def __init__(self):
        self._natahu = 'W'
        self._plocha = [
            ['Bve1','Bko1','Bsl1','Bkr','Bky','Bsl2','Bko2','Bve2'],
            ['Bpe1','Bpe2','Bpe3','Bpe4','Bpe5','Bpe6','Bpe7','Bpe8'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['Wpe1','Wpe2','Wpe3','Wpe4','Wpe5','Wpe6','Wpe7','Wpe8'],
            ['Wve1','Wko1','Wsl1','Wkr','Wky','Wsl2','Wko2','Wve2']]
        self.promoW = ['Wky1','Wky2','Wky3','Wky4','Wky5','Wky6','Wky7','Wky8']
        self.promoB = ['Bky1','Bky2','Bky3','Bky4','Bky5','Bky6','Bky7','Bky8']
        self.kralW = (7, 3)
        self.kralB = (0, 3)
        self._checknutyW = False
        self._checknutyB = False
        self.rows={0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8}
        self.cols={0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}
        self._game_on = True
        self.game_started = False
        ############################################################################################ zaciatocny screen
        self.base_screen=[]
        Plocha.canvas = tkinter.Canvas(width=800,height=800, bg='#6B8E23')
        Plocha.canvas.pack()
        Plocha.canvas.create_text(400,200, text='Chatarunga', font=('Helvetica','80','bold'), tag='Slon_base_screen')
        for i in range(8):
            for j in range(8):
                if i==0 or j==0 or i==7 or j==7:
                    tk_img = tkinter.PhotoImage(file='images/Slonik_Logo.png')
                    Plocha.canvas.create_image((i*100)+50,(j*100)+50, image = tk_img, tag='Slon_base_screen')
                    self.base_screen.append(tk_img)

        self.startgame_button = tkinter.Button(text='Start a game of Chatarunga', height= 5, width=21, command = self.start)
        self.startgame_button.place(x=300, y=400)
        self.instructions_button = tkinter.Button(text='Game rules',height= 5, width=10, command = self.explainer)
        self.instructions_button.place(x=455, y=400)
        self.restart = tkinter.Button(text='Play again', height= 3, width=10, command = self.reset)
        

    def start(self):
        self.game_started = True
        Plocha()  
        self.file = open('Moves.txt','w')
        self.file.write(f'New game\nMoves\n')
        Plocha.canvas.delete('Slon_base_screen')
        self.startgame_button.place(x=3000, y=750)
        self.instructions_button.place(x=25, y=700)
        self.draw_White = tkinter.Button(text='Ask black for draw', height= 3, width=16, command = self.draw_requestW)
        self.draw_Black = tkinter.Button(text='Ask white for draw', height= 3, width=16, command = self.draw_requestB)
        self.draw_White.place(x=10, y=500)
        self.draw_Black.place(x=10, y=300)
        
    def reset(self): #po skonceni hry tlacidlom resetnem vsetko
        Plocha.canvas.delete('End')
        self._natahu = 'W'
        self._plocha = [
            ['Bve1','Bko1','Bsl1','Bkr','Bky','Bsl2','Bko2','Bve2'],
            ['Bpe1','Bpe2','Bpe3','Bpe4','Bpe5','Bpe6','Bpe7','Bpe8'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['Wpe1','Wpe2','Wpe3','Wpe4','Wpe5','Wpe6','Wpe7','Wpe8'],
            ['Wve1','Wko1','Wsl1','Wkr','Wky','Wsl2','Wko2','Wve2']]
        self.promoW = ['Wky1','Wky2','Wky3','Wky4','Wky5','Wky6','Wky7','Wky8']
        self.promoB = ['Bky1','Bky2','Bky3','Bky4','Bky5','Bky6','Bky7','Bky8']
        self.kralW = (7, 3)
        self.kralB = (0, 3)
        self._checknutyW = False
        self._checknutyB = False
        self._game_on = True     
        self.file = open('Moves.txt','w')
        self.file.write(f'New game\nMoves\n') 
        self.instructions_button.place(x=25, y=700)
        self.draw_White.place(x=10, y=500)
        self.draw_Black.place(x=10, y=300)
        self.restart.place(x=4000, y=400)
        for i in range(8): # deletnutie piecov
            for j in range(8):
                Plocha.canvas.delete(f'{self._plocha[i][j]}')
                Plocha.canvas.delete(f'{self.promoB[i]}')
                Plocha.canvas.delete(f'{self.promoW[i]}')

        Plocha()

    def explainer(self):
        if self._game_on == False:
            self._game_on = True
            Plocha.canvas.delete('game_rules')
            self.instructions_button['text'] = 'Game rules'
            self.instructions_button['width'] = 10
            self.instructions_button['height'] = 5
            if self.game_started == True:
                self.instructions_button.place(x=25, y=700)
                self.draw_White.place(x=10, y=500)
                self.draw_Black.place(x=10, y=300)
            else:
                self.startgame_button.place(x=300, y=400)
                self.instructions_button.place(x=455, y=400)

        else:
            self._game_on = False
            tk_img = tkinter.PhotoImage(file='images/Game_rules.png')
            Plocha.canvas.create_image(400,400, image = tk_img, tag='game_rules')
            self.base_screen.append(tk_img)
            self.startgame_button.place(x=3000, y=750)
            self.instructions_button.place(x=675, y=725)
            self.draw_White.place(x=3000, y=500)
            self.draw_Black.place(x=3000, y=300)
            self.instructions_button['text'] = 'Hide, game rules'
            self.instructions_button['width'] = 15
            self.instructions_button['height'] = 2
            

    @property
    def game_on(self):
        return self._game_on   

    @property
    def gplocha(self):
        return self._plocha
    
    def presun(self, vycistit, zmenit):
        if self._plocha[vycistit[0]][vycistit[1]] == 'Wkr':
            self.kralW = (zmenit[0], zmenit[1])
        elif self._plocha[vycistit[0]][vycistit[1]] == 'Bkr':
            self.kralB = (zmenit[0], zmenit[1]) 
        self._plocha[zmenit[0]][zmenit[1]] = self._plocha[vycistit[0]][vycistit[1]]
        self._plocha[vycistit[0]][vycistit[1]] = '.'
    
    @property
    def natahu(self):
        return self._natahu

    @natahu.setter
    def natahu(self, tah):
        self._natahu = tah
    
    @property
    def checkW(self):
        return  self._checknutyW

    @checkW.setter
    def checkW(self, diff):
        self._checknutyW = diff

    @property
    def checkB(self):
        return self._checknutyB

    @checkB.setter
    def checkB(self, diff):
        self._checknutyB = diff

    def valid_moves(self, figure, row, col, rekurzivne = False, mode = 'normal'):#rekurzivne = false znamena ze ju volam primarne a nie cez king_under_attack ani cez pinned, mode urcuje ci su pinned, to checkujem a ked tak zmenim ak su 
        moves = []
        if figure != ('Wkr' or 'Bkr') and rekurzivne == False:
            if self.pinned(row, col) == 'zboku':
                if figure == 'Wky' or  figure == 'Bky' or figure == 'Wsl' or figure == 'Bsl' or figure =='Wko' or figure == 'Bko' or figure == 'Wpe' or figure == 'Bpe':
                    return moves
                else:
                    mode = 'zboku'
            elif self.pinned(row,col) == 'zpredu':
                if figure == 'Wky' or  figure == 'Bky' or figure == 'Wsl' or figure == 'Bsl' or figure =='Wko' or figure == 'Bko':
                    return moves
                else:
                    mode = 'zpredu'
                
            
        if figure == 'Wpe':
            if mode == 'zpredu':
                if self._plocha[row-1][col] == '.':
                    moves.append((row-1, col))
            else:
                if rekurzivne == True: #utocne moves iba kvoli king_under_attack 
                    if col == 0:
                        moves.append((row-1, col+1))
                    elif col == 7:
                        moves.append((row-1, col-1))
                    else:
                        moves.append((row-1, col+1))
                        moves.append((row-1, col-1))

                else:
                    if self._plocha[row-1][col] == '.':
                        moves.append((row-1, col))
                    if col == 0:
                        if self._plocha[row-1][col+1] != '.' and self._plocha[row-1][col+1][0] != 'W':
                            moves.append((row-1, col+1))
                    elif col == 7:
                        if self._plocha[row-1][col-1] != '.' and self._plocha[row-1][col-1][0] != 'W':
                            moves.append((row-1, col-1))
                    else:
                        if self._plocha[row-1][col+1] != '.' and self._plocha[row-1][col+1][0] != 'W':
                            moves.append((row-1, col+1))
                        if self._plocha[row-1][col-1] != '.' and self._plocha[row-1][col-1][0] != 'W':
                            moves.append((row-1, col-1))

        elif figure == 'Bpe':
            if mode == 'zpredu':
                if self._plocha[row+1][col] == '.':
                    moves.append((row+1, col))
            else:    
                if rekurzivne == True: #tiez len utocne moves 
                    if col == 0:
                        moves.append((row+1, col+1))
                    elif col == 7:
                        moves.append((row+1, col-1))
                    else:
                        moves.append((row+1, col+1))
                        moves.append((row+1, col-1))
                else:
                    if self._plocha[row+1][col] == '.':
                        moves.append((row+1, col))
                    if col == 0:
                        if self._plocha[row+1][col+1] != '.' and self._plocha[row+1][col+1][0] != 'B':
                            moves.append((row+1, col+1))
                    elif col == 7:
                        if self._plocha[row+1][col-1] != '.' and self._plocha[row+1][col-1][0] != 'B':
                            moves.append((row+1, col-1))
                    else:
                        if self._plocha[row+1][col+1] != '.' and self._plocha[row+1][col+1][0] != 'B':
                            moves.append((row+1, col+1))
                        if self._plocha[row+1][col-1] != '.' and self._plocha[row+1][col-1][0] != 'B':
                            moves.append((row+1, col-1))

        elif figure == 'Wve':
            if mode == 'zboku':
                for j in range(col+1,8,1):
                    if self._plocha[row][j] == '.':
                        moves.append((row,j))
                    elif self._plocha[row][j] != '.':
                        if self._plocha[row][j][0] == 'W':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((row,j))
                            break

                for j in range(col-1,-1,-1):
                    if self._plocha[row][j] == '.':
                        moves.append((row,j))
                    elif self._plocha[row][j] != '.':
                        if self._plocha[row][j][0] == 'W':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((row,j))
                            break
                        
            elif mode == 'zpredu':
                for i in range(row+1,8,1):
                    if self._plocha[i][col] == '.':
                        moves.append((i,col))
                    elif self._plocha[i][col] != '.':
                        if self._plocha[i][col][0] =='W':
                            if rekurzivne == True:
                                moves.append((i,col))    
                            break
                        else:
                            moves.append((i,col))
                            break

                for i in range(row-1,-1,-1):
                    if self._plocha[i][col] == '.':
                        moves.append((i,col))
                    elif self._plocha[i][col] != '.':
                        if self._plocha[i][col][0] == 'W':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((i,col))
                            break

            else:
                for i in range(row+1,8,1):
                    if self._plocha[i][col] == '.':
                        moves.append((i,col))
                    elif self._plocha[i][col] != '.':
                        if self._plocha[i][col][0] =='W':
                            if rekurzivne == True:
                                moves.append((i,col))    
                            break
                        else:
                            moves.append((i,col))
                            break

                for i in range(row-1,-1,-1):
                    if self._plocha[i][col] == '.':
                        moves.append((i,col))
                    elif self._plocha[i][col] != '.':
                        if self._plocha[i][col][0] == 'W':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((i,col))
                            break

                for j in range(col+1,8,1):
                    if self._plocha[row][j] == '.':
                        moves.append((row,j))
                    elif self._plocha[row][j] != '.':
                        if self._plocha[row][j][0] == 'W':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((row,j))
                            break

                for j in range(col-1,-1,-1):
                    if self._plocha[row][j] == '.':
                        moves.append((row,j))
                    elif self._plocha[row][j] != '.':
                        if self._plocha[row][j][0] == 'W':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((row,j))
                            break
            
        elif figure == 'Bve':
            if mode == 'zboku':
                for j in range(col+1,8,1):
                    if self._plocha[row][j] == '.':
                        moves.append((row,j))
                    elif self._plocha[row][j] != '.':
                        if self._plocha[row][j][0] == 'B':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((row,j))
                            break

                for j in range(col-1,-1,-1):
                    if self._plocha[row][j] == '.':
                        moves.append((row,j))
                    elif self._plocha[row][j] != '.':
                        if self._plocha[row][j][0] == 'B':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((row,j))
                            break

            elif mode == 'zpredu':
                for i in range(row+1,8,1):
                    if self._plocha[i][col] == '.':
                        moves.append((i,col))
                    elif self._plocha[i][col] != '.':
                        if self._plocha[i][col][0] =='B':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((i,col))
                            break

                for i in range(row-1,-1,-1):
                    if self._plocha[i][col] == '.':
                        moves.append((i,col))
                    elif self._plocha[i][col] != '.':
                        if self._plocha[i][col][0] == 'B':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((i,col))
                            break
                
            else:
                for i in range(row+1,8,1):
                    if self._plocha[i][col] == '.':
                        moves.append((i,col))
                    elif self._plocha[i][col] != '.':
                        if self._plocha[i][col][0] =='B':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((i,col))
                            break

                for i in range(row-1,-1,-1):
                    if self._plocha[i][col] == '.':
                        moves.append((i,col))
                    elif self._plocha[i][col] != '.':
                        if self._plocha[i][col][0] == 'B':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((i,col))
                            break

                for j in range(col+1,8,1):
                    if self._plocha[row][j] == '.':
                        moves.append((row,j))
                    elif self._plocha[row][j] != '.':
                        if self._plocha[row][j][0] == 'B':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((row,j))
                            break

                for j in range(col-1,-1,-1):
                    if self._plocha[row][j] == '.':
                        moves.append((row,j))
                    elif self._plocha[row][j] != '.':
                        if self._plocha[row][j][0] == 'B':
                            if rekurzivne == True:
                                moves.append((i,col)) 
                            break
                        else:
                            moves.append((row,j))
                            break    

        elif figure == 'Wko':
            if row < 6 and col < 7:
                if self._plocha[row+2][col+1] == '.':
                    moves.append((row+2, col+1))
                elif self._plocha[row+2][col+1][0] == 'B':
                    moves.append((row+2, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row+2, col+1))

            
            if row < 6 and col > 0:
                if self._plocha[row+2][col-1] == '.':
                    moves.append((row+2, col-1))
                elif self._plocha[row+2][col-1][0] == 'B':
                    moves.append((row+2, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row+2, col-1))
            
            if row < 7 and col < 6:
                if self._plocha[row+1][col+2] == '.':
                    moves.append((row+1, col+2))
                elif self._plocha[row+1][col+2][0] == 'B':
                    moves.append((row+1, col+2))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col+2))

            if row < 7 and col > 1:
                if self._plocha[row+1][col-2] == '.':
                    moves.append((row+1, col-2))
                elif self._plocha[row+1][col-2][0] == 'B':
                    moves.append((row+1, col-2))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col-2))
            
            if row > 1 and col < 7:
                if self._plocha[row-2][col+1] == '.':
                    moves.append((row-2, col+1))
                elif self._plocha[row-2][col+1][0] == 'B':
                    moves.append((row-2, col+1)) 
                else:
                    if rekurzivne == True:
                        moves.append((row-2, col+1))

            if row > 1 and col > 0:
                if self._plocha[row-2][col-1] == '.':
                    moves.append((row-2, col-1))
                elif self._plocha[row-2][col-1][0] == 'B':
                    moves.append((row-2, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row-2, col-1))
            
            if row > 0 and col < 6:
                if self._plocha[row-1][col+2] == '.':
                    moves.append((row-1, col+2))
                elif self._plocha[row-1][col+2][0] == 'B':
                    moves.append((row-1, col+2))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col+2))
            
            if row > 0 and col > 1:
                if self._plocha[row-1][col-2] == '.':
                    moves.append((row-1, col-2))
                elif self._plocha[row-1][col-2][0] == 'B':
                    moves.append((row-1, col-2))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col-2))

        elif figure == 'Bko':
            if row < 6 and col < 7:
                if self._plocha[row+2][col+1] == '.':
                    moves.append((row+2, col+1))
                elif self._plocha[row+2][col+1][0] == 'W':
                    moves.append((row+2, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row+2, col+1))
            
            if row < 6 and col > 0:
                if self._plocha[row+2][col-1] == '.':
                    moves.append((row+2, col-1))
                elif self._plocha[row+2][col-1][0] == 'W':
                    moves.append((row+2, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row+2, col-1))
            
            if row < 7 and col < 6:
                if self._plocha[row+1][col+2] == '.':
                    moves.append((row+1, col+2))
                elif self._plocha[row+1][col+2][0] == 'W':
                    moves.append((row+1, col+2))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col+2))

            if row < 7 and col > 1:
                if self._plocha[row+1][col-2] == '.':
                    moves.append((row+1, col-2))
                elif self._plocha[row+1][col-2][0] == 'W':
                    moves.append((row+1, col-2))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col-2))
            
            if row > 1 and col < 7:
                if self._plocha[row-2][col+1] == '.':
                    moves.append((row-2, col+1))
                elif self._plocha[row-2][col+1][0] == 'W':
                    moves.append((row-2, col+1)) 
                else:
                    if rekurzivne == True:
                        moves.append((row-2, col+1))

            if row > 1 and col > 0:
                if self._plocha[row-2][col-1] == '.':
                    moves.append((row-2, col-1))
                elif self._plocha[row-2][col-1][0] == 'W':
                    moves.append((row-2, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row-2, col-1))
            
            if row > 0 and col < 6:
                if self._plocha[row-1][col+2] == '.':
                    moves.append((row-1, col+2))
                elif self._plocha[row-1][col+2][0] == 'W':
                    moves.append((row-1, col+2))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col+2))
            
            if row > 0 and col > 1:
                if self._plocha[row-1][col-2] == '.':
                    moves.append((row-1, col-2))
                elif self._plocha[row-1][col-2][0] == 'W':
                    moves.append((row-1, col-2))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col-2))

        elif figure == 'Wsl':
            if row < 6 and col < 6:
                if self._plocha[row+2][col+2] == '.':
                    moves.append((row+2, col+2))
                elif self._plocha[row+2][col+2][0] == 'B':
                    moves.append((row+2, col+2))
                else:
                    if rekurzivne == True:
                        moves.append((row+2, col+2))

            if row < 6 and col > 1:
                if self._plocha[row+2][col-2] == '.':
                    moves.append((row+2, col-2))
                elif self._plocha[row+2][col-2][0] == 'B':
                    moves.append((row+2, col-2))
                else:
                    if rekurzivne == True:
                        moves.append((row+2, col-2))

            if row > 1 and col < 6:
                if self._plocha[row-2][col+2] == '.':
                    moves.append((row-2, col+2))
                elif self._plocha[row-2][col+2][0] == 'B':
                    moves.append((row-2, col+2))
                else:
                    if rekurzivne == True:
                        moves.append((row-2, col+2))

            if row > 1 and col > 1:
                if self._plocha[row-2][col-2] == '.':
                    moves.append((row-2, col-2))
                elif self._plocha[row-2][col-2][0] == 'B':
                    moves.append((row-2, col-2))
                else:
                    if rekurzivne == True:
                        moves.append((row-2, col-2))

        elif figure == 'Bsl':
            if row < 6 and col < 6:
                if self._plocha[row+2][col+2] == '.':
                    moves.append((row+2, col+2))
                elif self._plocha[row+2][col+2][0] == 'W':
                    moves.append((row+2, col+2))
                else:
                    if rekurzivne == True:
                        moves.append((row+2, col+2))

            if row < 6 and col > 1:
                if self._plocha[row+2][col-2] == '.':
                    moves.append((row+2, col-2))
                elif self._plocha[row+2][col-2][0] == 'W':
                    moves.append((row+2, col-2))
                else:
                    if rekurzivne == True:
                        moves.append((row+2, col-2))

            if row > 1 and col < 6:
                if self._plocha[row-2][col+2] == '.':
                    moves.append((row-2, col+2))
                elif self._plocha[row-2][col+2][0] == 'W':
                    moves.append((row-2, col+2))
                else:
                    if rekurzivne == True:
                        moves.append((row-2, col+2))

            if row > 1 and col > 1:
                if self._plocha[row-2][col-2] == '.':
                    moves.append((row-2, col-2))
                elif self._plocha[row-2][col-2][0] == 'W':
                    moves.append((row-2, col-2))
                else:
                    if rekurzivne == True:
                        moves.append((row-2, col-2))
                    
        elif figure == 'Wkr':
            if row < 7:
                if self._plocha[row+1][col] == '.':
                    moves.append((row+1, col))
                elif self._plocha[row+1][col][0] == 'B':
                    moves.append((row+1, col))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col))

            if row > 0:
                if self._plocha[row-1][col] == '.':
                    moves.append((row-1, col))
                elif self._plocha[row-1][col][0] == 'B':
                    moves.append((row-1, col))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col))

            if col < 7:
                if self._plocha[row][col+1] == '.':
                    moves.append((row, col+1))
                elif self._plocha[row][col+1][0] == 'B':
                    moves.append((row, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row, col+1))

            if col > 0:
                if self._plocha[row][col-1] == '.':
                    moves.append((row, col-1))
                elif self._plocha[row][col-1][0] == 'B':
                    moves.append((row, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row, col-1))

            if row < 7 and col < 7:
                if self._plocha[row+1][col+1] == '.':
                    moves.append((row+1, col+1))
                elif self._plocha[row+1][col+1][0] == 'B':
                    moves.append((row+1, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col+1))

            if row < 7 and col > 0:
                if self._plocha[row+1][col-1] == '.':
                    moves.append((row+1, col-1))
                elif self._plocha[row+1][col-1][0] == 'B':
                    moves.append((row+1, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col-1))

            if row > 0 and col < 7:
                if self._plocha[row-1][col+1] == '.':
                    moves.append((row-1, col+1))
                elif self._plocha[row-1][col+1][0] == 'B':
                    moves.append((row-1, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col+1))

            if row > 0 and col > 0:
                if self._plocha[row-1][col-1] == '.':
                    moves.append((row-1, col-1))
                elif self._plocha[row-1][col-1][0] == 'B':
                    moves.append((row-1, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col-1))

            if rekurzivne == False:
                moves2 = []
                for i in moves:
                    if self.king_under_attack(i,'W') == False and self.next_round_check(i, (row, col)) == True:
                        moves2.append(i)
                        
                moves = moves2
            
        elif figure == 'Bkr':
            if row < 7:
                if self._plocha[row+1][col] == '.':
                    moves.append((row+1, col))
                elif self._plocha[row+1][col][0] == 'W':
                    moves.append((row+1, col))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col))

            if row > 0:
                if self._plocha[row-1][col] == '.':
                    moves.append((row-1, col))
                elif self._plocha[row-1][col][0] == 'W':
                    moves.append((row-1, col))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col))

            if col < 7:
                if self._plocha[row][col+1] == '.':
                    moves.append((row, col+1))
                elif self._plocha[row][col+1][0] == 'W':
                    moves.append((row, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row, col+1))

            if col > 0:
                if self._plocha[row][col-1] == '.':
                    moves.append((row, col-1))
                elif self._plocha[row][col-1][0] == 'W':
                    moves.append((row, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row, col-1))

            if row < 7 and col < 7:
                if self._plocha[row+1][col+1] == '.':
                    moves.append((row+1, col+1))
                elif self._plocha[row+1][col+1][0] == 'W':
                    moves.append((row+1, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col+1))

            if row < 7 and col > 0:
                if self._plocha[row+1][col-1] == '.':
                    moves.append((row+1, col-1))
                elif self._plocha[row+1][col-1][0] == 'W':
                    moves.append((row+1, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col-1))

            if row > 0 and col < 7:
                if self._plocha[row-1][col+1] == '.':
                    moves.append((row-1, col+1))
                elif self._plocha[row-1][col+1][0] == 'W':
                    moves.append((row-1, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col+1))

            if row > 0 and col > 0:
                if self._plocha[row-1][col-1] == '.':
                    moves.append((row-1, col-1))
                elif self._plocha[row-1][col-1][0] == 'W':
                    moves.append((row-1, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col-1))

            if rekurzivne == False:
                moves2 = []
                for i in moves:
                    if self.king_under_attack(i,'B') == False and self.next_round_check(i, (row, col)) == True:
                        moves2.append(i)
                moves = moves2

        elif figure == 'Wky':
            if row < 7 and col < 7:
                if self._plocha[row+1][col+1] == '.':
                    moves.append((row+1, col+1))
                elif self._plocha[row+1][col+1][0] == 'B':
                    moves.append((row+1, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col+1))

            if row < 7 and col > 0:
                if self._plocha[row+1][col-1] == '.':
                    moves.append((row+1, col-1))
                elif self._plocha[row+1][col-1][0] == 'B':
                    moves.append((row+1, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col-1))

            if row > 0 and col < 7:
                if self._plocha[row-1][col+1] == '.':
                    moves.append((row-1, col+1))
                elif self._plocha[row-1][col+1][0] == 'B':
                    moves.append((row-1, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col+1))

            if row > 0 and col > 0:
                if self._plocha[row-1][col-1] == '.':
                    moves.append((row-1, col-1))
                elif self._plocha[row-1][col-1][0] == 'B':
                    moves.append((row-1, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col-1))

        elif figure == 'Bky':
            if row < 7 and col < 7:
                if self._plocha[row+1][col+1] == '.':
                    moves.append((row+1, col+1))
                elif self._plocha[row+1][col+1][0] == 'W':
                    moves.append((row+1, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col+1))

            if row < 7 and col > 0:
                if self._plocha[row+1][col-1] == '.':
                    moves.append((row+1, col-1))
                elif self._plocha[row+1][col-1][0] == 'W':
                    moves.append((row+1, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row+1, col-1))

            if row > 0 and col < 7:
                if self._plocha[row-1][col+1] == '.':
                    moves.append((row-1, col+1))
                elif self._plocha[row-1][col+1][0] == 'W':
                    moves.append((row-1, col+1))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col+1))

            if row > 0 and col > 0:
                if self._plocha[row-1][col-1] == '.':
                    moves.append((row-1, col-1))
                elif self._plocha[row-1][col-1][0] == 'W':
                    moves.append((row-1, col-1))
                else:
                    if rekurzivne == True:
                        moves.append((row-1, col-1))
        
        if ((self.checkB == True and figure[0]=='B')  or (self.checkW == True and figure[0]=='W')) and rekurzivne != True: #pozeranie ci je move mozny a nebude stale existovat check, po nom nasledne vyhodenie ho ak check zostane
            moves2 = []
            for i in moves:
                if self.next_round_check(i, (row, col)) == True: #True znamena ze je valid 
                    moves2.append(i)
            moves = moves2  
        return moves
   
   
    def king_under_attack(self, policko, farba): #pozeram ci nemam checknuteho krala, 
        if farba == 'W': #ohrozenie bieleho krala
            for i in range(8):
                for j in range(8):
                    if self._plocha[i][j] == '.':
                        pass
                    elif self._plocha[i][j][0] == farba:
                        pass
                    else:
                        if policko in self.valid_moves(self._plocha[i][j][:3], i, j, True): #self.KralW
                            return True 
            return False
        else: #ohrozenie cierneho krala 
            for i in range(8):
                for j in range(8):
                    if self._plocha[i][j] == '.':
                        pass
                    elif self._plocha[i][j][0] == farba:
                        pass
                    else:
                        if policko in self.valid_moves(self._plocha[i][j][:3], i, j, True): #self.kralB
                            return True
            return False   

  
    def promotion(self, farba, stlpec, odkial):
        if farba == 'W':
            self._plocha[0][stlpec] = f'{self.promoW.pop(0)}'
            self._plocha[1][odkial] = '.'
            return self._plocha[0][stlpec]

        else:
            self._plocha[7][stlpec] = f'{self.promoB.pop(0)}'
            self._plocha[6][odkial] = '.'
            return self._plocha[7][stlpec] 
            
    def pinned(self, row, col): #na urcenie figuriek co sa nemozu uhnut vezy lebo by spôsobili check
        farba = self._plocha[row][col][0] 
        if farba == 'W':
            if row == self.kralW[0]:
                for i in range(8):
                    if self._plocha[row][i][:3]== 'Bve':
                        if (row, col) in self.valid_moves('Bve', row, i, 'pinned'):
                            if self.kralW in self.valid_moves('Bve', row, col, 'pinned'):
                                return 'zboku'
            if col == self.kralW[1]:                
                for i in range(8):
                    if self._plocha[i][col][:3]== 'Bve':
                        if (row, col) in self.valid_moves('Bve', i, col, 'pinned'):
                            if self.kralW in self.valid_moves('Bve', row, col, 'pinned'):
                                return 'zpredu'
            
        else:
            if row == self.kralB[0]:
                for i in range(8):
                    if self._plocha[row][i][:3]== 'Wve':
                        if (row, col) in self.valid_moves('Wve', row, i, 'pinned'):
                            if self.kralB in self.valid_moves('Wve', row, col, 'pinned'):
                                return 'zboku'
            if col == self.kralB[1]:               
                for i in range(8):
                    if self._plocha[i][col][:3]== 'Wve':
                        if (row, col) in self.valid_moves('Wve', i, col, 'pinned'):
                            if self.kralB in self.valid_moves('Wve', row, col, 'pinned'):
                                return 'zpredu'
        return False

    def next_round_check(self, move, pos): #simulej move ak stale je king_under_attack returnem false co vyhodi move z moznych
        attacknute = self._plocha[move[0]][move[1]] 
        attacker = self._plocha[pos[0]][pos[1]]
        self._plocha[pos[0]][pos[1]] = '.'
        self._plocha[move[0]][move[1]] =  attacker
        if attacker[0] == 'W':
            if attacker == 'Wkr':
                self.kralW = move
            if self.king_under_attack(self.kralW, 'W') == True:
                self._plocha[move[0]][move[1]] = attacknute
                self._plocha[pos[0]][pos[1]] = attacker
                if attacker == 'Wkr':
                    self.kralW = pos
                return False
            else:
                self._plocha[move[0]][move[1]] = attacknute
                self._plocha[pos[0]][pos[1]] = attacker
                if attacker == 'Wkr':
                    self.kralW = pos
                return True
        else:
            if attacker == 'Bkr':
                self.kralB = move
            if self.king_under_attack(self.kralB, 'B') == True:
                self._plocha[move[0]][move[1]] = attacknute
                self._plocha[pos[0]][pos[1]] = attacker
                if attacker == 'Bkr':
                    self.kralB = pos
                return False
            else:
                self._plocha[move[0]][move[1]] = attacknute
                self._plocha[pos[0]][pos[1]] = attacker
                if attacker == 'Bkr':
                    self.kralB = pos
                return True
        
    def mate(self, farba):
        if farba == 'W': 
            for i in range(8):
                for j in range(8):
                    if self._plocha[i][j] == '.':
                        pass
                    elif self._plocha[i][j][0] != farba:
                        pass
                    else:
                        if len(self.valid_moves(self._plocha[i][j][:3], i, j)) > 0: 
                            return False
            return True
        else: #ohrozenie cierneho krala 
            for i in range(8):
                for j in range(8):
                    if self._plocha[i][j] == '.':
                        pass
                    elif self._plocha[i][j][0] != farba:
                        pass
                    else:
                        if len(self.valid_moves(self._plocha[i][j][:3], i, j)) > 0: 
                            return False
            return True   
    
    def pat(self, farba):
        if farba == 'W': 
            if len(self.valid_moves('Wkr',self.kralW[0],self.kralW[1]))==0:
                for i in range(8):
                    for j in range(8):
                        if self._plocha[i][j] == '.':
                            pass
                        elif self._plocha[i][j][0] != farba:
                            pass
                        else:
                            if len(self.valid_moves(self._plocha[i][j][:3], i, j)) > 0: 
                                return False
                return True
            else:
                return False
        else: #ohrozenie cierneho krala 
            if len(self.valid_moves('Bkr',self.kralB[0],self.kralB[1]))==0:
                for i in range(8):
                    for j in range(8):
                        if self._plocha[i][j] == '.':
                            pass
                        elif self._plocha[i][j][0] != farba:
                            pass
                        else:
                            if len(self.valid_moves(self._plocha[i][j][:3], i, j)) > 0: 
                                return False
                return True
            else:
                return False
        
    def draw_requestW(self):
        if self.draw_White['text'] == 'Ask black for draw':
            self._game_on = False
            self.draw_White['text'] = 'Decline'
            self.draw_White['bg'] = 'red'
            self.draw_Black['text'] = 'Accept draw'
            self.draw_Black['bg'] = 'green'

        elif self.draw_White['text'] == 'Decline':
            self._game_on = True
            self.draw_White['text'] = 'Ask black for draw'
            self.draw_Black['text'] = 'Ask white for draw'
            self.draw_White['bg'] = 'white'
            self.draw_Black['bg'] = 'white'

        elif self.draw_White['text'] == 'Accept draw':
            Plocha.remiza(Plocha)
            self.draw_White['bg'] = 'white'
            self.draw_Black['bg'] = 'white'
            self.draw_White['text'] = 'Ask black for draw'
            self.draw_Black['text'] = 'Ask white for draw'
            self.file.close()

    def draw_requestB(self):
        if self.draw_Black['text'] == 'Ask white for draw':
            self._game_on = False
            self.draw_White['text'] = 'Accept draw'
            self.draw_White['bg'] = 'green'
            self.draw_Black['text'] = 'Decline'
            self.draw_Black['bg'] = 'red'

        elif self.draw_Black['text'] == 'Decline':
            self._game_on = True
            self.draw_Black['text'] = 'Ask white for draw'
            self.draw_White['text'] = 'Ask black for draw'
            self.draw_White['bg'] = 'white'
            self.draw_Black['bg'] = 'white'

        elif self.draw_Black['text'] == 'Accept draw':
            Plocha.remiza(Plocha)
            self.draw_White['bg'] = 'white'
            self.draw_Black['bg'] = 'white'
            self.draw_Black['text'] = 'Ask white for draw'
            self.draw_White['text'] = 'Ask black for draw'
            self.file.close()
                   
       

 
class Plocha:
    canvas = None
    def __init__(self):
        self.black_zoz = self.strihaj('images/CheckBkr.png', 12)
        self.white_zoz = self.strihaj('images/CheckWkr.png', 12)
        ###################################################################################################### animacia
        self.obrazky = []
        self.zafarbene = []
        self.odlozW = [(690, 50),(690, 90),(690, 130),(690,170),(690, 210),(690, 250), (690, 290),(690, 330),(730, 50),(730, 90),(730, 130),(730,170),(730, 210),(730, 250), (730, 290),(730,330)]
        self.odlozB = [(690, 800-50),(690, 800-90),(690, 800-130),(690, 800-170),(690, 800-210),(690, 800-250), (690,800-290),(690,800-330),(730, 800-50),(730, 800-90),(730, 800-130),(730, 800-170),(730, 800-210),(730, 800-250), (730, 800-290),(730, 800-330)]
        for i in range(180,660,60): #sachovnica
            for j in range(180,660,60):
                if (i//60) % 2 == 0:
                    if (j//60) % 2 == 0:
                        self.canvas.create_rectangle(j, i, j+60, i+60, fill='white', tag=f'{j},{i}')
                    else:
                        self.canvas.create_rectangle(j, i, j+60, i+60, fill='#6B8E23', tag=f'{j},{i}')
                else:
                    if (j//60) % 2 == 0:
                        self.canvas.create_rectangle(j, i, j+60, i+60, fill='#6B8E23', tag=f'{j},{i}')
                    else:
                        self.canvas.create_rectangle(j, i, j+60, i+60, fill='white', tag=f'{j},{i}')
                if j == 180:
                    self.canvas.create_text(j-15, i+30,text=(i//60)-2, font='Helvetica 15')
                if i == 600:
                    self.canvas.create_text(j+30, i+75, text=chr(64+(j//60)-2), font='Helvetica 15')         
                if hra.gplocha[(i//60)-3][(j//60)-3] != '.':
                    tk_img = tkinter.PhotoImage(file=f'images/{hra.gplocha[(i//60)-3][(j//60)-3][:3]}.png')
                    self.canvas.create_image(j+30, i+30, image = tk_img, tag = hra.gplocha[(i//60)-3][(j//60)-3])
                    self.obrazky.append(tk_img)  
        self.canvas.create_text(400,100, text='Chatarunga', font=('Helvetica','60','bold'))
        self.canvas.create_text(725,780, text='Gained material',font=('Helvetica','10'))
        self.canvas.create_text(725,20, text='Gained material',font=('Helvetica','10'))
        self.canvas.bind("<Button-1>",self.klik)
        self.canvas.create_text(100,100,text='Nobody is under check', tag='sach')
        self.canvas.create_text(100, 400, text= 'On move: ')
        self.canvas.create_rectangle(85,415,115,445, fill='White', outline='black', width='3',tag='Onmove')
        self.on_move(hra.natahu)
        
    def strihaj (self, meno_suboru, n):
        obr = Image.open(meno_suboru)
        zoz = []
        sir, vys = obr.width//n, obr.height
        for x in range(0, obr.width, sir):
            zoz.append(ImageTk.PhotoImage(obr.crop((x, 0, x+sir, vys))))
        return zoz
    
    def anim (self, zoz, figure):
        faza = 0
        for i in range(24):
            self.canvas.itemconfig(figure, image=zoz[faza])
            faza = (faza + 1) % len(zoz)
            self.canvas.update()
            self.canvas.after(100)
        self.canvas.itemconfig(figure, image=zoz[11])


    def klik(self,event):
        if hra.game_on == True:
            x = event.x
            y = event.y
            if ((x//60)-3)<8 and ((x//60)-3)>-1 and ((y//60)-3)>-1 and ((y//60)-3)<8 and len(self.zafarbene) == 0:
                self.zakliknuta(hra.gplocha[(y//60)-3][(x//60)-3], (x,y))
                if len(self.zafarbene) != 0:
                    self.possible_moves(hra.valid_moves(hra.gplocha[(y//60)-3][(x//60)-3][:3],(y//60)-3,(x//60)-3))
            elif ((x//60)-3)<8 and ((x//60)-3)>-1 and ((y//60)-3)>-1 and ((y//60)-3)<8 and len(self.zafarbene) > 1:
                if ((x//60)*60, (y//60)*60) in self.zafarbene[1:]:
                    self.pohyb(self.zafarbene[0], ((x//60)*60, (y//60)*60))
                else:
                    self.zakliknuta()  
            else:
                self.zakliknuta()

    def pohyb(self, tag, position): #graficke premiestnenie figurky
        hra.file.write(f'{hra.gplocha[(tag[1]//60) -3][(tag [0]//60) - 3]}: {hra.rows[position[1]//60 -3]}{hra.cols[position[0]//60 -3]}\n')
        if hra.gplocha[position[1]//60 -3] [position[0]//60 -3] == '.': #promotion White
            if hra.gplocha[(tag[1]//60) -3][(tag [0]//60) - 3][:3]=='Wpe' and (position[1]//60)-3 == 0:
                self.canvas.delete(hra.gplocha[(tag[1]//60) -3][(tag [0]//60) - 3])
                tk_img = tkinter.PhotoImage(file=f'images/Wky.png')
                self.canvas.create_image(position[0]+30, position[1]+30, image = tk_img, tag = hra.promotion('W', (position[0]//60) -3, (tag[0]//60)-3))
                self.obrazky.append(tk_img)  

            elif hra.gplocha[(tag[1]//60) -3][(tag [0]//60) - 3][:3]=='Bpe' and (position[1]//60)-3 == 7: #promotion Black
                self.canvas.delete(hra.gplocha[(tag[1]//60) -3][(tag [0]//60) - 3])
                tk_img = tkinter.PhotoImage(file=f'images/Bky.png')
                self.canvas.create_image(position[0]+30, position[1]+30, image = tk_img, tag = hra.promotion('B', (position[0]//60) -3, (tag[0]//60)-3))
                self.obrazky.append(tk_img)  

            else:
                self.canvas.coords(hra.gplocha[(tag[1]//60) -3][(tag [0]//60) - 3], position[0]+30, position[1]+30)
                self.canvas.tag_raise(f'{hra.gplocha[tag[1]//60 -3][tag [0]//60 - 3]}')
                hra.presun((tag[1]//60 -3, tag [0]//60 - 3), (position[1]//60 -3, position[0]//60 -3))
        

        else:
            self.odloz(hra.gplocha[position[1]//60 -3][position[0]//60 -3])
            self.canvas.tag_raise(hra.gplocha[position[1]//60 -3][position[0]//60 -3])
            if hra.gplocha[(tag[1]//60) -3][(tag [0]//60) - 3][:3]=='Wpe' and (position[1]//60)-3 == 0: #promotion White
                self.canvas.delete(hra.gplocha[(tag[1]//60) -3][(tag [0]//60) - 3])
                tk_img = tkinter.PhotoImage(file=f'images/Wky.png')
                self.canvas.create_image(position[0]+30, position[1]+30, image = tk_img, tag = hra.promotion('W', (position[0]//60)-3, (tag[0]//60)-3))
                self.obrazky.append(tk_img)  
                
            elif hra.gplocha[(tag[1]//60) -3][(tag [0]//60) - 3][:3]=='Bpe' and (position[1]//60)-3 == 7: #promotion Black
                self.canvas.delete(hra.gplocha[(tag[1]//60) -3][(tag [0]//60) - 3])
                tk_img = tkinter.PhotoImage(file=f'images/Bky.png')
                self.canvas.create_image(position[0]+30, position[1]+30, image = tk_img, tag = hra.promotion('B', (position[0]//60) -3,  (tag[0]//60)-3))
                self.obrazky.append(tk_img)

            else:
                self.canvas.coords(f'{hra.gplocha[tag[1]//60 -3][tag [0]//60 - 3]}', position[0]+30, position[1]+30)
                self.canvas.tag_raise(f'{hra.gplocha[tag[1]//60 -3][tag [0]//60 - 3]}')
                hra.presun((tag[1]//60 -3, tag [0]//60 - 3), (position[1]//60 -3, position[0]//60 -3))
        
        
        if hra.natahu == 'W':
            if hra.king_under_attack(hra.kralB, 'B') == True:
                self.check(True, 'Black')
                hra.checkB = True
                if hra.mate('B') == True:
                    self.finish('W')
                    hra.file.close()
            else:
                self.check(False, 'Black')
                if hra.pat('B') == True:
                    self.remiza()
                    hra.file.close()
            hra.checkW = False
            hra.natahu = 'B'
        else:
            if hra.king_under_attack(hra.kralW, 'W') == True:
                self.check(True, 'White')
                hra.checkW = True
                if hra.mate('W') == True:
                    self.finish('B')
                    hra.file.close()
            else:
                self.check(False, 'White')
                if hra.pat('W') == True:
                    self.remiza()
                    hra.file.close()
            hra.checkB = False
            hra.natahu = 'W'

        self.on_move(hra.natahu)
        self.zakliknuta()

    def zakliknuta(self, figure=None, position=None): #vyber figurky
        if figure is None:
            if len(self.zafarbene)>0:
                for i in self.zafarbene:
                    if (i[0]//60) % 2 == 0 and (i[1]//60) % 2== 0:
                        self.canvas.itemconfig(f'{(i[0]//60)*60},{(i[1]//60)*60}', fill='white')
                        
                    elif (i[0]//60) % 2 == 1 and (i[1]//60) % 2== 0:
                        self.canvas.itemconfig(f'{(i[0]//60)*60},{(i[1]//60)*60}', fill='#6B8E23')
                        
                    elif (i[0]//60) % 2 == 0 and (i[1]//60) % 2== 1:
                        self.canvas.itemconfig(f'{(i[0]//60)*60},{(i[1]//60)*60}', fill='#6B8E23')

                    else:
                        self.canvas.itemconfig(f'{(i[0]//60)*60},{(i[1]//60)*60}', fill='white')
                        
                self.zafarbene.clear()
        else:
            if len(self.zafarbene)>0:
                for i in self.zafarbene:
                    if (i[0]//60) % 2 == 0 and (i[1]//60) % 2== 0:
                        self.canvas.itemconfig(f'{(i[0]//60)*60},{(i[1]//60)*60}', fill='white')
                        
                    elif (i[0]//60) % 2 == 1 and (i[1]//60) % 2== 0:
                        self.canvas.itemconfig(f'{(i[0]//60)*60},{(i[1]//60)*60}', fill='#6B8E23')
                        
                    elif (i[0]//60) % 2 == 0 and (i[1]//60) % 2== 1:
                        self.canvas.itemconfig(f'{(i[0]//60)*60},{(i[1]//60)*60}', fill='#6B8E23')

                    else:
                        self.canvas.itemconfig(f'{(i[0]//60)*60},{(i[1]//60)*60}', fill='white')
                        
                self.zafarbene.clear() 
            if hra.gplocha[(position[1]//60)-3][(position[0]//60)-3] == '.':
                pass
            elif hra.gplocha[(position[1]//60)-3][(position[0]//60)-3][0] != hra.natahu:
                pass
            else: 
                self.zafarbene.append((position[0],position[1]))
                self.canvas.itemconfig(f'{(self.zafarbene[-1][0]//60)*60},{(self.zafarbene[-1][1]//60)*60}', fill='#d2bb0a')
                
    def possible_moves(self, moznosti):
        if len(moznosti) > 0:
            for i in moznosti:
                self.zafarbene.append(((i[1]+3)*60, (i[0]+3)*60))
                if hra.gplocha[i[0]][i[1]] == '.':
                    self.canvas.itemconfig(f'{(i[1]+3)*60},{(i[0]+3)*60}', fill='#9645b9')
                else:
                    self.canvas.itemconfig(f'{(i[1]+3)*60},{(i[0]+3)*60}', fill='#ad050e')

    def odloz(self, figurka):
        if figurka[0] == 'W':
            self.canvas.coords(figurka,self.odlozW[0][0],self.odlozW[0][1])
            self.odlozW.pop(0)
        else:
            self.canvas.coords(figurka,self.odlozB[0][0],self.odlozB[0][1])
            self.odlozB.pop(0)

    def on_move(self, farba):
        if farba == 'W':
            self.canvas.itemconfig('Onmove', fill='white')
        else:
            self.canvas.itemconfig('Onmove', fill='black')
    
    def check(self, je, farba):
        if je == True:
            self.canvas.itemconfig('sach', text= f'{farba} is under check!!!')
            self.canvas.itemconfig('sach', fill='red')
            self.zakliknuta()
            if farba == 'Black':
                self.zafarbene.append(((hra.kralB[1]+3)*60,(hra.kralB[0]+3)*60))
                self.canvas.itemconfig(f'{(hra.kralB[1]+3)*60},{(hra.kralB[0]+3)*60}', fill='#ad050e')
                self.anim(self.black_zoz, 'Bkr')
            else:
                self.zafarbene.append(((hra.kralW[1]+3)*60,(hra.kralW[0]+3)*60))
                self.canvas.itemconfig(f'{(hra.kralW[1]+3)*60},{(hra.kralW[0]+3)*60}', fill='#ad050e')
                self.anim(self.white_zoz, 'Wkr')

        else:
            self.canvas.itemconfig('sach', text= 'Nobody is under check')
            self.canvas.itemconfig('sach', fill='black')

    def finish(self, Winner):
        self.obrazky = []
        if Winner == 'W':
            tk_img = tkinter.PhotoImage(file='images/White_Wscreen.png')
            self.canvas.create_image(400, 400, image = tk_img, tag = 'End')
            self.obrazky.append(tk_img)  
        else:
            tk_img = tkinter.PhotoImage(file='images/Black_Wscreen.png')
            self.canvas.create_image(400, 400, image = tk_img, tag = 'End')
            self.obrazky.append(tk_img)  
            
        hra.restart.place(x=400,y=400)
        hra.instructions_button.place(x=3000, y=400)
        hra.draw_Black.place(x=3000, y=400)
        hra.draw_White.place(x=3000, y=400)
        self.canvas.delete('sach')

    def remiza(self):
        self.obrazky = []
        tk_img = tkinter.PhotoImage(file='images/Draw_Wscreen.png')
        self.canvas.create_image(400, 400, image = tk_img, tag = 'End')
        self.obrazky.append(tk_img)     
        hra.restart.place(x=400,y=400)
        hra.instructions_button.place(x=3000, y=400)
        hra.draw_Black.place(x=3000, y=400)
        hra.draw_White.place(x=3000, y=400)
        self.canvas.delete('sach')

hra=Gamestate()
tkinter.mainloop()
