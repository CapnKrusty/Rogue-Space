import data as g
import environ,tile,math
import misc
import component as comp

class Ship():
    def __init__(self,model,x = 1000,y = 1000, heading = 90, name = "Unknown ship"):
        self.type = model
        
        self.xPos = x
        self.yPos = y
        self.heading = heading
        self.velocity = 0
        self.targetHeading = self.heading
        self.velocity = self.velocity
        
        self.speed = 100
        
        self.map = []
        self.entMap = []
        self.components = []
        self.width = 0
        self.height = 0
        
        self.name = name
        
        self.turnRate = 0
        self.enginePower = 0
        
        if model == 1:
            self.name = "Sitting Duck"
            self.image = tile.Tile(character = "\u0108",fontsize = g.MINISIZE, heading = self.heading)
            self.makeShip([
                [g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.CTRLS,g.E.WALL1,g.E.LASER],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.SPACE],
                [g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE],
])
        elif model == 2:
            self.name = "Behemoth"
            self.makeShip([ [g.E.FLOOR if i % 2 ==1 else g.E.FLOOR for i in range (55)] for i in range (30)] )
            self.image = tile.Tile(character = "\u0107",fontsize = g.MINISIZE, heading = self.heading)
        elif model == 3:
            self.name = "Frigate"
            self.image = tile.Tile(character = "\u00C5",fontsize = g.MINISIZE, heading = self.heading)
            self.makeShip([
            [g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.SPACE],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.SPACE],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.SPACE],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.CTRLS,g.E.WALL1,g.E.LASER],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.SPACE],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.SPACE],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.SPACE],
            [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.SPACE],
            [g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE]          
                           
                           ])
        elif model == 4:
            self.name = "Fighter"
            self.image = tile.Tile(character = "x",fontsize = g.MINISIZE, heading = self.heading)
            self.makeShip([
                [g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE],
                [g.E.SPACE,g.E.MANUV,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE,g.E.SPACE,g.E.SPACE,g.E.SPACE,g.E.SPACE],
                [g.E.SPACE,g.E.SPACE,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE,g.E.SPACE,g.E.SPACE,g.E.SPACE,g.E.SPACE],
                [g.E.SPACE,g.E.ENGNE,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE],
                [g.E.SPACE,g.E.SPACE,g.E.WALL1,g.E.SNSOR,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.CTRLS,g.E.WALL1,g.E.LASER],
                [g.E.SPACE,g.E.ENGNE,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE],
                [g.E.SPACE,g.E.SPACE,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE,g.E.SPACE,g.E.SPACE,g.E.SPACE,g.E.SPACE],
                [g.E.SPACE,g.E.MANUV,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE,g.E.SPACE,g.E.SPACE,g.E.SPACE,g.E.SPACE],
                [g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE],
                
                  ])
            
            misc.printComponents(self)
            self.components[3].action.link(self.components[4].action,description = "Fire main laser")
            self.components[3].action.link(self.components[4].action,1,description = "Fire main laser heroically")
            self.components[3].action.link(comp.MultiAction(self.components[1].action , self.components[5].action) , 0 , description = "Rev the engines")
            self.components[3].action.link(self.components[2].action,1,description = "View enemy ship 1" )
            self.components[3].action.link(self.components[2].action,2,description = "View enemy ship 2" )
            self.components[3].action.link(self.components[0].action,1,description = "Turn Right")
            
    def makeShip(self,text):
        g.MWIDTH
        g.MHEIGHT
        g.SHIPS.append(self)
        width = len(text[0])
        height = len(text)
        xfiller = yfiller = 5
        if width < g.Xt:
            xfiller = (g.Xt-len(text[0])) // 2 + 5
            width = g.Xt

        if height < g.Yt:
            yfiller = (g.Yt-len(text))//2 + 5
            height = g.Yt 
        
        for i in range(yfiller):## top filler stars
            self.map.append([environ.Environ(g.E.SPACE) for i in range(width+10)])   
        for y in range(len(text)):
            self.map.append([])##new y row
            for i in range(xfiller):##left filler
                self.map[y+yfiller].append(environ.Environ(g.E.SPACE))
            for x in range(len(text[0])):#content
                newE = environ.Environ(text[y][x],owner = self)
                self.map[y+yfiller].append(newE)
                if newE.component:
                    self.components.append(newE.component)
            for i in range(xfiller):#right filler
                self.map[y+yfiller].append(environ.Environ(g.E.SPACE))
        for i in range(yfiller):# bottom filler stars
            self.map.append([environ.Environ(g.E.SPACE) for i in range(width+10)])
        
        self.width = g.MWIDTH = width+10
        self.height = g.MHEIGHT = height+10
        
        self.entMap = [[None for i in range(self.width)] for j in range(self.height)]
        
        self.calculateStats()

    def take_turn(self):
        dx = math.cos(math.radians(self.heading))
        dy = math.sin(math.radians(self.heading))
        
        self.xPos += dx*self.velocity
        self.yPos -= dy*self.velocity
        print(self.name)
        print("Turn rate: ",self.turnRate)
        print ("Current: " , self.heading , "Target: " , self.targetHeading)
        if self.heading != self.targetHeading:
            
            turnDir = self.shortestWayToHeading(self.heading,self.targetHeading)
            if turnDir == "Clockwise":
                ##    target is greater, going past    ##
                if (self.heading - self.turnRate < 0) and ((self.heading - self.turnRate) % 360 < self.targetHeading): 
                    self.heading = self.targetHeading
                elif self.heading - self.turnRate < self.targetHeading and not self.targetHeading > self.heading:
                    self.heading = self.targetHeading
                else:
                    self.heading = (self.heading - self.turnRate) % 360
            else:
                if (self.heading + self.turnRate > 360) and ((self.heading + self.turnRate) % 360 > self.targetHeading):
                    self.heading = self.targetheading
                elif self.heading + self.turnRate > self.targetHeading and not self.targetHeading < self.heading:
                    self.heading = self.targetHeading
                else:
                    self.heading = (self.heading + self.turnRate) % 360
                
        return 100

    def calculateStats(self):
        for component in self.components:
            if component.type == g.C.ENGINE:
                self.enginePower += component.power
            elif component.type == g.C.MANEUVER:
                self.turnRate += component.power
                
    def updateDirArrow(self):
        self.image.updateArrow(self.heading)
        
    def shortestWayToHeading(self,currentAngle,targetAngle):
        if (targetAngle - currentAngle) % 360 < 180:
            return "Counterclockwise"
        else:
            return "Clockwise"
