#Spoluautor tomáš tomášidlo

%%manim -qm CircleToSquare

class CircleToSquare(Scene):
    def construct(self):
        # Šestíúhelník
        hexagon = RegularPolygon(6, radius=1, color=BLUE)
        self.add(hexagon)

        # Kolečko
        circle = Circle(radius=1, color=RED)
        self.play(Transform(hexagon, circle))

        # Trojúhelník
        triangle = RegularPolygon(3, radius=1, color=GREEN)
        self.play(Transform(circle, triangle))
        self.wait()

        # Make JAPAN 
        orange_circle = Circle(radius=2, color=RED, fill_opacity=1)
        self.play(
            FadeOut(circle),
            Transform(hexagon, orange_circle)
        )    
        self.camera.background_color = WHITE
    
         # Textík
        text = Text("informatika, smysl zivota a jsem tygr", color=BLACK)
        self.play(Write(text))
        self.wait()
        self.wait()


        
