from kivy.app import App
import kivy
kivy.require('1.9.0')
from kivy.uix.widget import Widget
from kivy.uix.button import Button as Bu
from kivy.uix.button import Button as Bu
from  kivy.uix.image import Image
from  kivy.uix.boxlayout import BoxLayout
from  kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from random import random
from kivy.core.image import Image as CoreImage
from kivy.uix.popup import Popup
from kivy.graphics import (Color,Ellipse,Rectangle,Line)
from PIL import ImageDraw
from kivy.uix.label import Label
import cv2
#import sys
import numpy as np
class pain(Widget):
    def __init__(self,**kwargs):
        super(pain,self).__init__(**kwargs)
        #print(dir(pain))
        self.size=(Window.size[0],Window.size[1])



        #picture = AsyncImage(source =r'D:/work_slava/map.png')
        #point_bufer=()
        pointt=tuple()
        #print(dir(Widget()))
        with open("profile.txt","r") as file:
            pointt =file.read().split('\n')

        if (len(pointt))%2!=0:
            print("error")
        else:
            print("good")
        #poi_float=float(pointt)
        a=[]
        for i in pointt:
            a.append(float(i))
        #print((a))

        with self.canvas:
            #
            #Image(source =r'D:/work_slava/map.png',size=(Window.size[0],Window.size[1]))
            Image(source =r'map.png',size=(Window.size[0],Window.size[1]))

            Color(0,1,0,1)

            self.line=Line(points=a,close=True)
            #for o in a:
                #print('o=',o)
            #self.Button(text='Clear')
            #self.expot_to_png("sdewad.png")


    #def on_touch_down(self,touch):
            #popup = Popup(title='Test popup',
            #content=Label(text='upp'),
            #size_hint =(.2,.2))
            #popup.open()
    def on_touch_down(self,touch):
            #file_load =sys.path
            #file =file_load[0]
            #print('file=',file)

            self.size=(Window.size[0],Window.size[1])
            self.export_to_png("screenshot.png")
            cat_image = cv2.imread('screenshot.png')
            contours = np.array( [ [100,450],[200, 450], [200,400]  ], dtype=np.int32  )
            low_red = (0,255,0 )
            flagg=0
            #high_red = (149,255,149)
            #only_cat = cv2.inRange(cat_image, low_red, high_red)
            #y,x = np.where(only_cat != 0)
            #print(dir(self))
            #self.expot_to_png("sde.png")
            #moments = cv2.moments(only_cat,1) # получим моменты
            color=(0,255,0)# находим кординаты цветиа
            lower_red = np.array([0,255,0]) # находим кординаты цветиа
            upper_red = np.array([0,255,0])# находим кординаты цветиа
            mask=cv2.inRange(cat_image,lower_red,upper_red)# находим кординаты цветиа
            coord=cv2.findNonZero(mask)# находим кординаты цветиа
            cv2.fillPoly(cat_image, pts =[coord], color=(0,255,0))# находим кординаты цветиа
            filename='write_2.png'
            #img = Image.open("write_2.png")
            #obj=img.load()
            #print(obj[175,429])

            cv2.imwrite(filename, cat_image)
            cat_image = cv2.imread('write_2.png')
            color=(0,255,0)
            lower_red = np.array([0,255,0])
            upper_red = np.array([0,255,0])
            mask=cv2.inRange(cat_image,lower_red,upper_red)
            coord=cv2.findNonZero(mask)
            #print('coord=',coord)
            #print('type=',type(coord))


            #px=cat_image[0,255,0]
            #print('px=',dir(cat_image))

            #cv2.imshow('cat_image', cat_image)
            coord_23=np.array([[int(touch.x),int(touch.y)]])
            """
            здесь возникает откланение .

            Я пыталься в цикло for сделать но
            он не ркботает так надо
            Но может быть дело в другом

            """
            #print('coord_23=',coord_23)
            #print('type1=',type(coord_23))

            #bool_bufer=True



            #for k in coord:
                #a=[k]
                #print('type2=',type(k))
            if np.any(coord==coord_23):
                flagg+=1
                popup = Popup(title='Test popup',
                content=Label(text='upp'),
                size_hint =(.2,.2))
                popup.open()
                if flagg ==1:
                    with self.canvas:
                         Image(source =r'write_2.png',size=(Window.size[0],Window.size[1]),opacity=0.5)





class Paintapp(App):
    def build(self):
        paren=Widget()
        self.paren=pain()
        #flagg=1
        paren.add_widget(self.paren)
        #paren.add_widget(Bu(text='Clear'))





        return pain()

    #def save(self,instance):
        #self.painter.export_to_png('ver.png')

if __name__ =='__main__':
    Paintapp().run()
