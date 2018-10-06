from helper import *


class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):

        botviewminx = (self.PlayerInfo.Position.x - 10)  #max view of bot in all x and y positions
        botviewmaxx = (self.PlayerInfo.Position.x + 10)
        botviewminy = (self.PlayerInfo.Position.y - 10)
        botviewmaxy = (self.PlayerInfo.Position.y + 10)

        botnorth = Point(self.PlayerInfo.Position.x,self.PlayerInfo.Position.y-1)
        botsouth = Point(self.PlayerInfo.Position.x,self.PlayerInfo.Position.y+1)
        boteast = Point(self.PlayerInfo.Position.x,self.PlayerInfo.Position.x-1)
        botwest = Point(self.PlayerInfo.Position.x,self.PlayerInfo.Position.x+1)

        wallxy = []                 #arrays for position of all type of tiles
        housexy = []
        lavaxy = []
        resxy = []
        shopxy = []
        playerxy = []
                                              #detecte les tiles autour et met leur coordonnes
        for i in range(botviewminx, botviewmaxx):       # dans des array de leur type respectif.
            for j in range(botviewminy, botviewmaxy):
                pointxy=Point(i,j)
                if gameMap.getTileAt(pointxy) == TileContent.Wall:
                    wallxy.append(pointxy)
                elif gameMap.getTileAt(pointxy) == TileContent.House:
                    housexy.append(pointxy)
                elif gameMap.getTileAt(pointxy) == TileContent.Lava:
                    lavaxy.append(pointxy)
                elif gameMap.getTileAt(pointxy) == TileContent.Resource:
                    resxy.append(pointxy)
                elif gameMap.getTileAt(pointxy) == TileContent.Shop:
                    shopxy.append(pointxy)
                elif gameMap.getTileAt(pointxy) == TileContent.Player and pointxy != self.PlayerInfo.Position:
                    playerxy.append(pointxy)


        if gameMap.getTileAt(botnorth) == TileContent.Player:  #attaque autre joueur si a cote
            return create_attack_action(botnorth)
        elif gameMap.getTileAt(botsouth) == TileContent.Player:
            return create_attack_action(botsouth)
        elif gameMap.getTileAt(boteast) == TileContent.Player:
            return create_attack_action(boteast)
        elif gameMap.getTileAt(botwest) == TileContent.Player:
            return create_attack_action(botwest)
        elif gameMap.getTileAt(botsouth) == TileContent.Wall:
            return create_attack_action(botsouth)
        elif gameMap.getTileAt(boteast) == TileContent.Wall:
            return create_attack_action(boteast)
        elif gameMap.getTileAt(botwest) == TileContent.Wall:
            return create_attack_action(botwest)

        if len(playerxy) > 0:

            diffx = playerxy[0].x - self.PlayerInfo.Position.x
            diffy = playerxy[0].y - self.PlayerInfo.Position.y
            if abs(diffy) > abs(diffx):
                if diffy < 0:
                    return create_move_action(Point(0,1))
                else:
                    return create_move_action(Point(0,-1))
            else:
                if diffx < 0:
                    return create_move_action(Point(-1,0))
                else:
                    return create_move_action(Point(1,0))
        else:
            import random
            randommm = random.randint(0, 1)
            if randommm == 0:
                   return create_move_action(Point(0,-1))
            else:
                 return create_move_action(Point(-1,0))


        print(botviewminx)                  #affichage pour tester
        print(botviewmaxx)
        print(botviewminy)
        print(botviewmaxy)
        print("wall:")
        for n in wallxy:
            print(n)
        print(len(wallxy))
        print("house:")
        for n in housexy:
            print(n)
        print(len(housexy))
        print("lava:")
        for n in lavaxy:
            print(n)
        print(len(lavaxy))
        print("resource:")
        for n in resxy:
            print(n)
        print(len(resxy))
        print("shop:")
        for n in shopxy:
            print(n)
        print(len(shopxy))
        print("player:")
        for n in playerxy:
            print(n)
        print(len(playerxy))
        print("fin")




        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Point(-1,0))

        #return create_collect_action(Point(-1,0))


        


        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

       # if self.PlayerInfo.CarriedResources >= 500:
         #   dir = -1
        #else:
          #  dir = 1

       # for player in visiblePlayers:
           # if player.Position == player.HouseLocation and gameMap.getTileAt(Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y)) == TileContent.House:
             #   return create_attack_action(Point(dir, 0))

       # for player in visiblePlayers:
           # if player.Score == 0 and gameMap.getTileAt(Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y)) == TileContent.House:
             #   return create_move_action(Point(dir, 0))

       # if Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y) == self.PlayerInfo.HouseLocation:
            #return create_move_action(Point(dir, 0))
       # elif gameMap.getTileAt(Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y)) == TileContent.Player:
          #  return create_attack_action(Point(dir, 0))
       # elif gameMap.getTileAt(Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y)) == TileContent.House:
        #    return create_steal_action(Point(dir, 0))
       # elif gameMap.getTileAt(Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y)) == TileContent.Wall:
         #   return create_attack_action(Point(dir, 0))
       # elif gameMap.getTileAt(Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y)) == TileContent.Resource:
          #  return create_collect_action(Point(dir, 0))
      #  else:
          #  return create_move_action(Point(dir, 0))



    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
