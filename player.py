import mcpi.minecraft as minecraft


mc = minecraft.Minecraft.create("mc.fipy.me")
entityIds = mc.getPlayerEntityIds()
for id in entityIds:
    print(id)

playerPos = mc.player.getPos()

print(playerPos)