from src.view.HomeScreen import HomeScreen
from src.controller.ControllerHomeScreen import ControllerHomeScreen


homeScreen = HomeScreen(600, 400, 'Tela Inicial')
controlerHomeScreen = ControllerHomeScreen(homeScreen)
homeScreen.mainloop()

