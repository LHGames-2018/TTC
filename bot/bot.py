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
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

  #      print("---")
  #      print(self.PlayerInfo.Position)
  #      print(self.PlayerInfo.CarriedResources)
  #      print(self.PlayerInfo.CarryingCapacity)
  #      print("---")

        if self.PlayerInfo.CarriedResources == 500:
            dir = 1
        else:
            dir = -1

        if Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y) == self.PlayerInfo.HouseLocation:
            return create_move_action(Point(dir, 0))
        elif (gameMap.getTileAt(Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y)) == TileContent.Player):
            return create_attack_action(Point(dir, 0))
        elif (gameMap.getTileAt(Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y)) == TileContent.House):
            return create_steal_action(Point(dir, 0))
        elif (gameMap.getTileAt(Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y)) == TileContent.Wall):
            return create_attack_action(Point(dir, 0))
        elif (gameMap.getTileAt(Point(self.PlayerInfo.Position.x + dir, self.PlayerInfo.Position.y)) == TileContent.Resource):
            return create_collect_action(Point(dir, 0))
        else:
            return create_move_action(Point(dir, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
