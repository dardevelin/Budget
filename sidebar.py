from gi.repository import Gtk, Gio

class Sidebar():

    def __init__(self):

        # Define Widgets
        self.grid = Gtk.Grid()
        
        self.contentGrid = Gtk.Grid()
        
       
        self.menuListBox = Gtk.ListBox()
        self.subMenuListBox = Gtk.ListBox()

        self.menuScrolledWindow = Gtk.ScrolledWindow()
        self.subMenuScrolledWindow = Gtk.ScrolledWindow()
        self.contentScrolledWindow = Gtk.ScrolledWindow()
        
        self.menuViewport = Gtk.Viewport()
        self.subMenuViewport = Gtk.Viewport()
        self.contentViewport = Gtk.Viewport()
        
        self.categoryNotebook = Gtk.Notebook()
        
        self.menuButtons = []
        self.subMenuButtons = []
        
        self.categoryTitleLabel = Gtk.Label("Category")
        self.dateTitleLabel = Gtk.Label("Date")
        self.costTitleLabel = Gtk.Label("Cost")
        self.descriptionTitleLabel = Gtk.Label("Description")
        
        self.dummyLabel1 = Gtk.Label()
        self.dummyLabel2 = Gtk.Label()
        
        self.addEntryButton = Gtk.Button("Add")
        self.editEntryButton = Gtk.Button("Edit")
        self.addEntryPopover = Gtk.Popover.new(self.addEntryButton)
        self.editEntryPopover = Gtk.Popover.new(self.addEntryButton)
        
        self.topLeftLabel = Gtk.Label()
        self.topMiddleLabel = Gtk.Label()
        self.topRightLabel = Gtk.Label()
        
        self.monthSpentTotalLabel = Gtk.Label("$1,500")
        self.monthRemainingTotalLabel = Gtk.Label("$1,500")
        self.percBudgetTotalLabel = Gtk.Label("50.00%")
        
        self.entryRows = []

        self.menu = "All"
        self.subMenu = "All"

        # Set Offsets
        self.entryOffsetTop = 8
        
        self.categoryOffsetLeft = 1
        self.dateOffsetLeft = 2
        self.costOffsetLeft = 3
        self.descriptionOffsetLeft = 4
        self.editOffsetLeft = 5

        # Set Styling
        self.menuScrolledWindow.set_vexpand(True)
        self.menuScrolledWindow.set_property("width-request",200)
        
        self.subMenuScrolledWindow.set_vexpand(True)
        self.subMenuScrolledWindow.set_property("width-request",100)
        
        self.contentGrid.set_column_homogeneous(True)
        self.contentGrid.set_hexpand(True)
        
        self.categoryTitleLabel.set_markup("<b>Category</b>")
        self.dateTitleLabel.set_markup("<b>Date</b>")
        self.costTitleLabel.set_markup("<b>Cost</b>")
        self.descriptionTitleLabel.set_markup("<b>Description</b>")
        
        
        # Add items to Grid 
        self.menuViewport.add(self.menuListBox)
        self.subMenuViewport.add(self.subMenuListBox)
        
        self.menuScrolledWindow.add(self.menuViewport)
        self.subMenuScrolledWindow.add(self.subMenuViewport)
        self.contentScrolledWindow.add(self.contentViewport)
        
        self.grid.attach(self.menuScrolledWindow,0,0,1,1)
        self.grid.attach(self.subMenuScrolledWindow,2,0,1,1)
        self.grid.attach(self.contentScrolledWindow,1,0,1,1)

        # Build Content Area
        self.contentGrid.attach(self.topLeftLabel, self.dateOffsetLeft, 2, 1, 1)
        self.contentGrid.attach(self.topMiddleLabel, self.costOffsetLeft, 2, 1, 1)
        self.contentGrid.attach(self.topRightLabel, self.descriptionOffsetLeft, 2, 1, 1)
        
        self.contentGrid.attach(self.monthSpentTotalLabel, self.dateOffsetLeft, 3, 1, 1)
        self.contentGrid.attach(self.monthRemainingTotalLabel, self.costOffsetLeft, 3, 1, 1)
        self.contentGrid.attach(self.percBudgetTotalLabel, self.descriptionOffsetLeft, 3, 1, 1)
        
        self.contentGrid.attach(self.dummyLabel1, 1, 4, 5, 1)
        self.contentGrid.attach(self.addEntryButton, 2, 5, 1, 1)
        self.contentGrid.attach(self.editEntryButton, 4, 5, 1, 1)
        self.contentGrid.attach(self.dummyLabel2, 1, 6, 1, 1)
        
        self.contentGrid.attach(self.categoryTitleLabel, self.categoryOffsetLeft, 7, 1, 1)
        self.contentGrid.attach(self.dateTitleLabel, self.dateOffsetLeft, 7, 1, 1)
        self.contentGrid.attach(self.costTitleLabel, self.costOffsetLeft, 7, 1, 1)
        self.contentGrid.attach(self.descriptionTitleLabel, self.descriptionOffsetLeft, 7, 1, 1)
        
        self.contentViewport.add(self.contentGrid)
        

    def menu_clicked(self,button):
        (button.get_label())


    def menu_clicked(self,button):
        self.menu = button.get_label()
        self.filter_menu()
    
    def subMenu_clicked(self,button):
        self.subMenu = button.get_label()
        self.filter_subMenu()
    
    def filter_menu(self):
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][1].get_label().split()
            if self.menu == "All":
                if self.subMenu == "All":
                    self.categoryTitleLabel.show()
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month[0] == self.subMenu:
                    self.categoryTitleLabel.show()
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month[0] != self.subMenu:
                    self.categoryTitleLabel.show()
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()
            elif self.menu != "All":
                if self.entryRows[i][0].get_label() == self.menu:
                    if self.subMenu == "All":
                        self.categoryTitleLabel.hide()
                        self.entryRows[i][0].hide()
                        self.entryRows[i][1].show()
                        self.entryRows[i][2].show()
                        self.entryRows[i][3].show()
                    if self.subMenu == self.month[0]:
                        self.categoryTitleLabel.hide()
                        self.entryRows[i][0].hide()
                        self.entryRows[i][1].show()
                        self.entryRows[i][2].show()
                        self.entryRows[i][3].show()
                    if self.entryRows[i][0].get_label() != self.menu:
                        self.entryRows[i][0].hide()
                        self.entryRows[i][1].hide()
                        self.entryRows[i][2].hide()
                        self.entryRows[i][3].hide()
                elif self.entryRows[i][0].get_label() != self.menu:    
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()
            
    def filter_subMenu(self):
        for i in range (0,len(self.entryRows)):
            self.month = self.entryRows[i][1].get_label().split()
            if self.menu == "All":
                if self.subMenu == "All":
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month[0] == self.subMenu:    
                    self.entryRows[i][0].show()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month[0] != self.subMenu:
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()
            elif self.menu != "All":
                if self.month[0] == self.subMenu and self.entryRows[i][0].get_label() == self.menu:
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].show()
                    self.entryRows[i][2].show()
                    self.entryRows[i][3].show()
                elif self.month[0] != self.subMenu or self.entryRows[i][0].get_label() != self.menu:
                    self.entryRows[i][0].hide()
                    self.entryRows[i][1].hide()
                    self.entryRows[i][2].hide()
                    self.entryRows[i][3].hide()
                if self.subMenu == "All":
                    if self.entryRows[i][0].get_label() == self.menu:
                        self.entryRows[i][0].hide()
                        self.entryRows[i][1].show()
                        self.entryRows[i][2].show()
                        self.entryRows[i][3].show()
