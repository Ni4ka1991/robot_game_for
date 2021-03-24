#!/usr/bin/env Python3
from os import system
from random import randint


#a - move left
#d - move right
#w - move up
#s - move down


#DATA

 #Field parameters

height  = int( input( "Insert the height of field. Optimal 20. >>> " ))
width   = int( input( "Insert the width of field. Optimal 20. >>> " ))


 #coordinates


roboX        = randint( 0, height )
roboY        = randint( 0, width )



bomb_1X      = randint( 0, height )
bomb_1Y      = randint( 0, width)

bomb_2X      = randint( 0, height )
bomb_2Y      = randint( 0, width)

money_bag_1X = randint( 0, height )
money_bag_1Y = randint( 0, width)

money_bag_2X = randint( 0, height )
money_bag_2Y = randint( 0, width)

heart_1X     = randint( 0, height )
heart_1Y     = randint( 0, width)

heart_2X     = randint( 0, height )
heart_2Y     = randint( 0, width)


 #robo parameters

charge    = 100 #percents
hp        = 100 #percents
money     = 0   #$


#LOGIC

while True:
 system( "clear" )
 
 #if robo in good condition
 if(( hp > 0) and (charge > 0 )):
  
  #meeting results
   
   #with bombs
  if((( roboX == bomb_1X ) and ( roboY == bomb_1Y )) or (( roboX == bomb_2X) and (roboY == bomb_2Y ))):
   hp -= 20
   
   #with hearts 
  elif((( roboX == heart_1X ) and ( roboY == heart_1Y )) or (( roboX == heart_2X) and (roboY == heart_2Y ))):
   
   if(( hp < 100 ) and ( charge < 100 )):
    hp += 20
   
    if( charge <= 50 ):
     charge += 50
   
    else:
     charge = 100
   
   #with money_bags 
  elif((( roboX == money_bag_1X ) and ( roboY == money_bag_1Y )) or (( roboX == money_bag_2X) and (roboY == money_bag_2Y ))):
   money  += 20
   charge += 10
 
#if robo in bad condition  
 else:
  if( charge == 0 ):
   print( "Battery low. Game over" )
   break
    
  elif( hp == 0 ):
   print( "Health points = 0. Game over" )
   break
   
   
 
 
 #Display robo parameters

 print( "Your robot parameters:\nhp = %d"%hp + " %" )
 print( "\nBattery Charging Indicator:" )
 print( "%d"%charge + " %")
 print( "=" * charge )
 print( "\nMoney = %d"%money + " $")
 print( "ACTUAL COORDINATES: X = %d; Y = %d\n"%( roboX, roboY ))


# ############# DRAWING THE MAP #######################
 
 for y in range( 1, width + 1 ):
  for x in range( 1, height + 1 ):
   
#robo

   if(( roboX == x ) and ( roboY == y )):
    print( "R ", end="" )

#bombs 1 and 2

   elif(( bomb_1X == x ) and ( bomb_1Y == y )):
    print( "B ", end = "" )
   
   elif(( bomb_2X == x ) and ( bomb_2Y == y )):
    print( "B ", end = "" )

#money-bags 1 and 2

   elif(( money_bag_1X == x ) and ( money_bag_1Y == y )):
    print( "M ", end = "" )
   
   elif(( money_bag_2X == x ) and ( money_bag_2Y == y )):
    print( "M ", end = "" )
   
#hearts 1 and 2

   elif(( heart_1X == x ) and ( heart_1Y == y )):
    print( "H ", end = "" )

   elif(( heart_2X == x ) and ( heart_2Y == y )):
    print( "H ", end = "" )
   
 # ----  
   else:
    print("- ", end="")    

  print( )


# #################### CONTROLS #####################

 direction = input( "dir ( w/s/a/d/x ) > " )
  
 
 if( direction == "a" ):
  if( roboX > 0 ): 
   roboX -= 1
   charge -= 5
  else:
   roboX = 5
   roboY = 5
   print( "Change direction. You can move only in right." )
   input( "hit ENTER to continue" )

 if( direction == "d" ):
  if( roboX < height ):
   roboX += 1
   charge -= 5
  else:
   roboX = 5
   roboY = 5
   print( "Change direction. You can move only in left." )
   input( "hit ENTER to continue" )

 if( direction == "s" ):
  if( roboY < width ):
   roboY += 1
   charge -= 5
  else:
   roboY = 5
   roboX = 5
   print( "Change direction. You can move only in up." )
   input( "hit ENTER to continue ")

 if( direction == "w" ):
  if( roboY > 0 ):
   roboY -= 1
   charge -= 5
  else:
   roboY = 5
   roboX = 5
   print( "Change direction. You can move only in down." )
   input( "hit ENTER to continue" )

 if( direction == "x" ):
  system( "clear" )
  print( "Thank you for playing!" )
  break





