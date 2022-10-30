x=600
y=600
def setup():
   size(500,500)
   fill(random(0,255),random(0,255),random(0,255))
def draw():
    global x,y
    ellipse(250,250,x,y)
    x=x-10
    y=y-10
    stroke(random(0,255),random(0,255),random(0,255))
    
