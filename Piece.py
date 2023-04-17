

class Piece:
    def __init__(self, colour, isMaster, row=0, col =0):
        self.isMaster = isMaster
        self.colour = colour
        self.row =row 
        self.col =col

    def setTile(self, tile):
        '''Place piece on a tile'''

    def get_colour(self):
        if(self.colour == True):
            return "Red"
        else:
            return "Blue"