
try:
    import pkg_resources.py2_warn
    import pygame as pg
    import time
    import random
except ImportError:
    pass

pg.init()





def incresspeed(speed):
     speed = speed + 1
     return speed 


# food = {
#      'fx':200,
#      'fy':200,
# }

# class food():
     
#      fx = 200
#      fy = 200
#      def __init__(self):
#           self.fx = 200
#           self.fy = 200

#      def newfood(self):
#           print("new food cal")
#           food.fx = random.randrange(800-10)
#           food.fy = random.randrange(600-10)



dis_width = 800
dis_height = 600        
     
dis = pg.display.set_mode((dis_width+200,dis_height))
pg.display.set_caption('Show your art')
     
font_style = pg.font.SysFont("Arial", 30)
def message(msg, color,w,h):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [w/3, h/3])

# def newfood(self):
#           print("new food cal")
#           food.fx = random.randrange(800-10)
#           food.fy = random.randrange(600-10)


def mainloop():

     clock = pg.time.Clock()
     over = False
    
     pw = 10
     ph = 10
     x1 = 300
     y1 = 300
     fx = 200
     fy = 200

     # fx = 200
     # fy = 200
     newx = 0
     newy = 0
     col = (255,255,41)
     speed = 3

     
     
     while not over :
          for event in pg.event.get():
               if event.type == pg.QUIT:
                    over = True
               # print('event')
               
               if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                         newx = 10
                         newy = 0
                    if event.key == pg.K_LEFT:
                         newx = -10
                         newy =0
                    if event.key == pg.K_UP:
                         newy = -10
                         newx =0
                    if event.key == pg.K_DOWN:
                         newy = 10
                         newx = 0
                    if event.key == pg.K_0:
                         col = (243,47,255)
                    if event.key == pg.K_1:
                         col = (143,51,213)
                    if event.key == pg.K_2:
                         col = (14,45,255)
                    if event.key == pg.K_3:
                         col = (51,208,213)
                    if event.key == pg.K_4:
                         col = (49,158,32)
                    if event.key == pg.K_5:
                         col = (179,156,40)
                    if event.key == pg.K_6:
                         col = (21,162,222)
                    if event.key == pg.K_7:
                         col = (179,16,40)
                    if event.key == pg.K_8:
                         col = (19,156,140)
                    if event.key == pg.K_9:
                         col = (238,156,34)
                    if event.key == pg.K_SPACE:
                         print("stop")
                         newy = 0
                         newx = 0
                    if event.key == pg.K_s:
                         print("speed incres")
                         # incresspeed(speed)
                         speed = speed + 1
                    # if event.key == pg.K_p:
                         # print("tack the image of scrre")
                         # pg.image.save(dis, "screenshot.jpeg")


                    
          message("Create your free art",(0,5,255),800*3 ,100)
          message("press  numbers to ",(0,220,0),800*3+10  , 200)
          message("change color ",(0,220,0),800*3+10  , 250)
          message("space bar to stop ",(255,240,0),800*3+10  , 400)
          message("use arrow to move ",(255,240,0),800*3 ,500)
          message("S to speed",(255,240,0),800*3 ,600)
          message("p to tack image",(255,240,0),800*3 ,700)
          message("Dont hit the bordars",(255,0,0),800*3+10  , 800)

          
          if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <0:
               message("game over",(255,255,255),dis_width,dis_height)
               over=True
                    # newx =0
                    # newy =0
                    # print("hit the borders")


                    
          x1 += newx
          y1 += newy
          # dis.fill([255,255,255])
          

          # if x1 == food.fx and y1 == food.fy :
          #      print("hit")
          #      pw +=5
          #      ph +=5
               # food.newfood()
          
          pg.draw.rect(dis,(255,255,255),[0,0,800,600],5)
          pg.draw.rect(dis,col,[x1,y1,10,10])
          # pg.draw.rect(dis,(255,0,0),[food.fx,food.fy,10,10])
          # pg.draw.rect(dis,(243,47,255),[800 ,100 ,15,15])

          pg.display.update()
          clock.tick(speed)
     # dis.blit("game over", [dis_width/2, dis_height/2])
     pg.quit()
     quit()

if __name__ == "__main__":
    mainloop()

