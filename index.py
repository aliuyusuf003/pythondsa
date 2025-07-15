#cool picture
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#iterate overpicture
#if 0, print('')
#if 1, print('*')
#use print('',end='')  to remove default newline

for img in picture:
    for pix in img:
        if pix == 1:
            print('*',end='')
        else:
           print(' ',end='')
    print('')
#    *    
#   ***   
#  *****  
# ******* 
#    *    
#    *    