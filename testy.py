import tkinter 
from PIL import Image, ImageTk
import random
canvas = tkinter.Canvas(height=1000,width=1000,background='white')
canvas.pack()

'''for i in range(1,9):
    for j in range(1,9):
        if i % 2 ==0:
            if j % 2 == 0:
                canvas.create_rectangle(j*60,(i*60),(j*60)+60,(i*60)+60,fill='white',outline='black')
            else:
                 canvas.create_rectangle(j*60,(i*60),(j*60)+60,(i*60)+60, fill='#6B8E23', outline='black')
        else:
            if j % 2 == 0:
                canvas.create_rectangle(j*60,(i*60),(j*60)+60,(i*60)+60,fill='#6B8E23', outline='black')
            else:
                canvas.create_rectangle(j*60,(i*60),(j*60)+60,(i*60)+60,fill='white',outline='black')'''
plocha=[
    ['Bve','Bko','Bsl','Bkr','Bky','Bsl','Bko','Bve'],
    ['Bpe','Bpe','Bpe','Bpe','Bpe','Bpe','Bpe','Bpe'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['Wpe','Wpe','Wpe','Wpe','Wpe','Wpe','Wpe','Wpe'],
    ['Wve','Wko','Wsl','Wkr','Wky','Wsl','Wko','Wve'],
] 
obrazky=['Bve','Bko','Bsl','Bkr','Bky','Bpe','Wpe','Wve','Wko','Wsl','Wkr','Wky']
x=0
farby=[]
'''for i in obrazky:
    obr= Image.open(f'images/{i}.png')
    farby.append(obr.getpixel((1,1)))
    if x%2 == 0:
        for j in range(obr.width):
            for k in range(obr.height):
                if obr.getpixel((j,k)) == farby[-1]:
                    obr.putpixel((j, k), (farby[-1][0],farby[-1][1],farby[-1][2],0))    
    else:
        for j in range(obr.width):
            for k in range(obr.height):
                if obr.getpixel((j,k)) == farby[-1]:
                    obr.putpixel((j, k), (farby[-1][0],farby[-1][1],farby[-1][2],0))
    obr.save(f'images/{i}.png')
    x += 1
print(farby)
for i in range(180,660,60): #sachovnica
    for j in range(180,660,60):
        if (i//60) % 2 == 0:
            if (j//60) % 2 == 0:
                canvas.create_rectangle(j, i, j+60, i+60, fill='white', tag=f'{j},{i}')
            else:
                canvas.create_rectangle(j, i, j+60, i+60, fill='#6B8E23', tag=f'{j},{i}')
        else:
            if (j//60) % 2 == 0:
                canvas.create_rectangle(j, i, j+60, i+60, fill='#6B8E23', tag=f'{j},{i}')
            else:
                canvas.create_rectangle(j, i, j+60, i+60, fill='white', tag=f'{j},{i}')
        if j == 180:
            canvas.create_text(j-15, i+30,text=(i//60)-2, font='Helvetica 15')
        if i == 600:
            canvas.create_text(j+30, i+75, text=chr(64+(j//60)-2), font='Helvetica 15')         
        if plocha[(i//60)-3][(j//60)-3] != '.':
            tk_img = tkinter.PhotoImage(file=f'images/{plocha[(i//60)-3][(j//60)-3][:3]}.png')
            canvas.create_image(j+30, i+30, image = tk_img, tag = plocha[(i//60)-3][(j//60)-3])
            obrazky.append(tk_img)
while True:
    x = random.choice(obrazky)
    canvas.coords(x, 210, 330)
    canvas.tag_raise(x)
    canvas.after(1000)
    canvas.update()'''
def strihaj(meno_suboru, n):
    obr = Image.open(meno_suboru)
    zoz = []
    sir, vys = obr.width//n, obr.height
    for x in range(0, obr.width, sir):
        zoz.append(ImageTk.PhotoImage(obr.crop((x, 0, x+sir, vys))))
    return zoz


zoz = strihaj('images/CheckWkr.png', 12)

tk_id = canvas.create_image(200,200)
faza = 0
for i in range(24):
    canvas.itemconfig(tk_id, image=zoz[faza])
    faza = (faza + 1) % len(zoz)
    canvas.update()
    canvas.after(100)

tkinter.mainloop()


