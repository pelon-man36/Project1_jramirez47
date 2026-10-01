from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        tex_UNI = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
        self.Universe.setTexture(tex_UNI, 1)

        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setScale(100)
        self.Planet1.setPos(150, 5000, 67)
        tex1 = self.loader.loadTexture("./Assets/Planets/Planet1.jpg")
        self.Planet1.setTexture(tex1, 1)

        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setScale(100)
        self.Planet2.setPos(0, 3000, 80)
        tex2 = self.loader.loadTexture("./Assets/Planets/Planet2.png")
        self.Planet2.setTexture(tex2, 1)

        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setScale(100)
        self.Planet3.setPos(-150, 2000, 40)
        tex3 = self.loader.loadTexture("./Assets/Planets/Planet3.png")
        self.Planet3.setTexture(tex3, 1)

        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setScale(100)
        self.Planet4.setPos(200, 1000, 90)
        tex4 = self.loader.loadTexture("./Assets/Planets/Planet4.png")
        self.Planet4.setTexture(tex4, 1)

        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setScale(100)
        self.Planet5.setPos(-150, 1000, 30)
        tex5 = self.loader.loadTexture("./Assets/Planets/Planet5.png")
        self.Planet5.setTexture(tex5, 1)

        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setScale(100)
        self.Planet6.setPos(200, 6000, 0)
        tex6 = self.loader.loadTexture("./Assets/Planets/Planet6.png")
        self.Planet6.setTexture(tex6, 1)

        self.Station = self.loader.loadModel("./Assets/Space_Station/SpaceStation1B/spaceStation.egg")
        self.Station.reparentTo(self.render)
        self.Station.setScale(50)
        self.Station.setPos(5000, 400, 70)






app = MyApp()
app.run()