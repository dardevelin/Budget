from sidebar import Sidebar

class Income():

    def __init__(self, data):
        # Define Sidebar Menu
        self.data = data 
        self.view = Sidebar(self.data, "income") 
