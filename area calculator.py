# Write code below 💖
#area calculator proyect 6/7/2024
print('Area Calculator')
print('1. Square')
print('2. Rectangle')
print('3. Triangle')
print('4. Circle')
print('5. Quit')

print('                                                         ')

shape=int(input('Choose the shape you want to calculate the area: '))
print('                                                         ')
if shape==1:
  square=int(input('side value:'))
  squareval=(square**2)
  print('The area is:') 
  print(squareval)

elif shape==2:
  length=int(input('length:'))
  width=int(input('width:'))
  Rectangle=(length*width)
  print('The area is:')
  print(Rectangle)

elif shape==3:
 height=int(input('height:'))
 base=int(input('base:'))
 Triangle=(height*base/2)
 print('The area is:')
 print(Triangle)

elif shape==4:
   pi=(3.14)
   radius= int(input('radius:'))
   Circle=(pi*radius**2)
   print('The area is:')
   print(Circle)

else:
   print('Thanks for using my area calculator, come back soon!')