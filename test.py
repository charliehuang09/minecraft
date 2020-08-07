import mcpi.minecraft as minecraft
import mcpi.block as block
import math
import time


mc = minecraft.Minecraft.create("home.fipy.me",4711)

#     try:
#         blockType =input ('what is your blocktype?')
#         blockType = int (blockType)
#         mc.setBlock(1,1,1, blockType)
#     except:
#         print ('you did not enter a number')
#         building_block()
# building_block()


# basic stuff
# Needs improvement
# base 5 by 5
# blockType = 20
# y = 5
# for z in range (6,11):
#     for x in range (6,11):
#         mc.setBlock(x, y, z, blockType)

#3 by 3
# y = y + 1
# for z in range (7,10):
#     for x in range (7,10):
#         mc.setBlock(x, y, z, blockType)
#cheery on top
# y = y + 1
# mc.setBlock(8,y, 8, blockType)



# pos = mc.player.getTilePos()
# x = pos.x
# y = pos.y
# z = pos.z
# time.sleep (10)
# pos = mc.player.getTilePos()
# x2 = pos.x
# y2 = pos.y
# z2 = pos.z

# x3 = x - x2
# y3 = y - y2
# z3 = z - z2
# y3 = str(y3)
# x3 = str(x3) 
# z3 = str(z3)
# mc.postToChat ('the player tumbled down the hill  ' + x3 + 'x ' + y3 + 'y ' + z3 + 'z.')
# def whatever():
#     answer = input ('do you want to create a crater?')
#     if answer == 'No':
#         print ('Okay')
#         exit()
#     if answer == 'Yes':
#         mc.postToChat ('Boom!!')
#         pos = mc.player.getPos()
#         mc.setBlocks(pos.x + 10, pos.y + 10, pos.z + 10, pos.x - 10, pos.y - 10, pos.z - 10, 0)
        
        
#     else:
#         print ('say Yes or No!')
#         whatever()

# whatever()


