

class Bread():
    def bake():
        print('bread is baking')
    
class Cookie():
    def bake():
        print('cookie is baking')


# Cook is voilating the DIP because higher level function cook is depending on lower level class
def cook(food: str):
    if food == "bread":
        bread = Bread()
        bread.bake()
    if food == "cookies":
        cookies = Cookies()
        cookies.bake()

cook("cookies")


