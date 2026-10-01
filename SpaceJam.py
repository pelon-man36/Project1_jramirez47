from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.obj")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)

        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setScale(100)
        self.Planet1.setPos(150, 5000, 67)
        tex = self.loader.loadTexture("./Assets/Planets/Planet1.jpg")
        self.Planet1.setTexture(tex, 1)

        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setScale(100)
        self.Planet2.setPos(0, 3000, 80)

        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setScale(100)
        self.Planet3.setPos(-150, 2000, 40)

        # Add a couple of more planets (6 in total); Load and set textures to everything.






app = MyApp()
app.run()