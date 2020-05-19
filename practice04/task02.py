import graphics as gr

window = gr.GraphWin("House", 1200, 720)

sky = gr.Rectangle(gr.Point(0, 0), gr.Point(1200, 360))
sky.setFill('blue')
sky.draw(window)

sun = gr.Circle(gr.Point(900, 100), 60)
sun.setFill('yellow')
sun.draw(window)

cloud3 = gr.Circle(gr.Point(135, 80), 30)
cloud3.setFill('white')
cloud3.draw(window)

cloud4 = gr.Circle(gr.Point(155, 80), 30)
cloud4.setFill('white')
cloud4.draw(window)

cloud1 = gr.Circle(gr.Point(120, 100), 30)
cloud1.setFill('white')
cloud1.draw(window)

cloud2 = gr.Circle(gr.Point(150, 100), 30)
cloud2.setFill('white')
cloud2.draw(window)

cloud3 = gr.Circle(gr.Point(180, 100), 30)
cloud3.setFill('white')
cloud3.draw(window)

ground = gr.Rectangle(gr.Point(0, 361), gr.Point(1200, 720))
ground.draw(window)

house = gr.Rectangle(gr.Point(300, 480), gr.Point(500, 280))
house.setFill('grey')
house.setWidth(4)
house.draw(window)

roof = gr.Polygon(gr.Point(300, 279), gr.Point(500, 279), gr.Point(400, 159))
roof.setFill('red')
roof.setWidth(4)
roof.draw(window)

w_ow = gr.Rectangle(gr.Point(365, 415), gr.Point(431, 349))
w_ow.setFill('yellow')
w_ow.setWidth(3)
w_ow.draw(window)

window.getMouse()

window.close()
