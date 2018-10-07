from helper import *


class Bot:
    def __init__(self):
        self.gohorizontale = True
        pass

    def pythagore(Point):
        hyp = math.sqrt((Point.x) ^ 2 + (Point.y) ^ 2)
        return hyp


    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo
        playerxy = playerInfo.Position
        #print(playerxy)

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        actualbotposition = Point(self.PlayerInfo.Position.x, self.PlayerInfo.Position.y)
        botviewminx = (self.PlayerInfo.Position.x - 10)  #max view of bot in all x and y positions
        botviewmaxx = (self.PlayerInfo.Position.x + 10)
        botviewminy = (self.PlayerInfo.Position.y - 10)
        botviewmaxy = (self.PlayerInfo.Position.y + 10)

        nord = Point(0,-1)
        sud = Point(0,1)
        est = Point(1,0)
        ouest = Point(-1,0)

        botnorth = Point(self.PlayerInfo.Position.x,self.PlayerInfo.Position.y-1)
        botsouth = Point(self.PlayerInfo.Position.x,self.PlayerInfo.Position.y+1)
        boteast = Point(self.PlayerInfo.Position.x+1,self.PlayerInfo.Position.y)
        botwest = Point(self.PlayerInfo.Position.x-1,self.PlayerInfo.Position.y)

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
                elif gameMap.getTileAt(pointxy) == TileContent.Player and pointxy != actualbotposition: #pour pas se prendre lui meme
                    playerxy.append(pointxy)
        #print(len(playerxy))
        #print(self.gohorizontale)


        #
        #
        # if len(playerxy) == 0 and self.gohorizontale == True:       #bouge droite/sud si action libre
        #     if gameMap.getTileAt(boteast) == TileContent.Wall:
        #         print("attaque mur est")
        #         return create_attack_action(est)
        #     self.gohorizontale = False
        #     print(" move horison est")
        #     return create_move_action(est)
        # elif len(playerxy) == 0 and self.gohorizontale == False:
        #     if gameMap.getTileAt(botsouth) == TileContent.Wall:
        #         print("attaque mur sud")
        #         return create_attack_action(sud)
        #     self.gohorizontale = True
        #     print(" move verticale sud")
        #     return create_move_action(Point(sud))
        #
        # if len(playerxy) !=0                        #si proche
        #     if playerxy[0].x > actualbotposition.x:
        #         return create_move_action(est)
        #     elif playerxy[0].x < actualbotposition.x:
        #         return create_move_action(ouest):
        #     if playerxy[0].y > actualbotposition.y:
        #         return create_move_action(sud)
        #     elif playerxy[0].y < actualbotposition.y:
        #         return create_move_action(nord)
        #
        # if gameMap.getTileAt(botnorth) == TileContent.Wall:  # attaque Mur si a cote
        #     print("attaque mur nord")
        #     return create_attack_action(Point(0, -1))
        # elif gameMap.getTileAt(botsouth) == TileContent.Wall:
        #     print("attaque mur sud")
        #     return create_attack_action(Point(0, 1))
        # elif gameMap.getTileAt(boteast) == TileContent.Wall:
        #     print("attaque mur est")
        #     return create_attack_action(Point(1, 0))
        # elif gameMap.getTileAt(botwest) == TileContent.Wall:
        #     print("attaque mur west")
        #     return create_attack_action(Point(-1, 0))
        #


        # if gameMap.getTileAt(botnorth) == TileContent.Player:  #attaque autre joueur si a cote
        #     return create_attack_action(botnorth)
        # elif gameMap.getTileAt(botsouth) == TileContent.Player:
        #     return create_attack_action(botsouth)
        # elif gameMap.getTileAt(boteast) == TileContent.Player:
        #     return create_attack_action(boteast)
        # elif gameMap.getTileAt(botwest) == TileContent.Player:
        #     return create_attack_action(botwest)
        #
        # if gameMap.getTileAt(botnorth) == TileContent.Resource:  #collecte ressource si a cote
        #     return create_collect_action(botnorth)
        # elif gameMap.getTileAt(botsouth) == TileContent.Resource:
        #     return create_collect_action(botsouth)
        # elif gameMap.getTileAt(boteast) == TileContent.Resource:
        #     return create_collect_action(boteast)
        # elif gameMap.getTileAt(botwest) == TileContent.Resource:
        #     return create_collect_action(botwest)



#        print(botviewminx)                  #affichage pour tester
 #       print(botviewmaxx)
  #      print(botviewminy)
   #     print(botviewmaxy)
    #    print("wall:")
     #   for n in wallxy:
      #      print(n)
       # print(len(wallxy))
        #print("house:")
#        for n in housexy:
 #           print(n)
  #      print(len(housexy))
   #     print("lava:")
    #    for n in lavaxy:
     #       print(n)
      #  print(len(lavaxy))
       # print("resource:")
        #for n in resxy:
         #   print(n)
#        print(len(resxy))
 #       print("shop:")
  #      for n in shopxy:
   #         print(n)
    #    print(len(shopxy))
     #   print("player:")
      #  for n in playerxy:
       #print(len(playerxy))
#        print("fin")
        if gameMap.getTileAt(botnorth) == TileContent.Player:  # attaque autre joueur si a cote
            print("attaqueplayer")
            return create_attack_action(nord)
        elif gameMap.getTileAt(botnorth) == TileContent.Wall:  # attaque autre joueur si a cote
            print("attaqueWall")
            return create_attack_action(nord)
        else:
            print("move up")
            return create_move_action(nord)

        # Write your bot here. Use functions from aiHelper to instantiate your actions.

        #return create_collect_action(Point(-1,0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
