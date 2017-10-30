#!/usr/bin/env python3
# -*- coding: cp1252 -*-
"""       turtle-example-suite:

             global_clock.py

Modified version of "Enhanced clock-program" in Turtle to show date and teme in different time zones. 
Python 3.x on windows. Need to have Turtle in your libraries. Resizing window brings the times in centre! 
Edit and use timezones of your choice! 
  ------------------------------------
   Press STOP to exit the program!
  ------------------------------------
"""
from turtle import *
from datetime import datetime

from datetime import datetime
from pytz import timezone

import pytz

def coverted_time(Time_Zone):
    localFormat =    "%Y-%m-%d %H:%M"
    timezoneformat = "%Y-%m-%d %H:%M"

    Time_Now=datetime.now()
    Time_Now_RemoteTimeZone=Time_Now.astimezone(pytz.timezone(Time_Zone))
    Time_Now_Formated = Time_Now_RemoteTimeZone.strftime(timezoneformat)
    Time_Now_RemoteTimeZone=Time_Now.astimezone(pytz.timezone(Time_Zone))
    return Time_Now_RemoteTimeZone.strftime(timezoneformat) + "   " + Time_Zone

    

def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def hand(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)

def make_hand_shape(name, laenge, spitze):
    reset()
    jump(-laenge*0.15)
    begin_poly()
    hand(laenge, spitze)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)

def clockface(radius):
    reset()
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global second_hand, minute_hand, hour_hand, writer
    writer = Turtle()
    #writer.mode("logo")
    writer.ht()
    writer.pu()
    writer.bk(5)
    

def wochentag(t):
    wochentag = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return wochentag[t.weekday()]

def datum(z):
    monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    j = z.year
    m = monat[z.month - 1]
    t = z.day
    return "%s %d %d" % (m, t, j)

def tick():

    try:
        tracer(False)  # Terminator can occur here
        writer.clear()
        writer.home()
        #writer.left(180)
        #writer.back(370)
        #writer.left(90)
        #writer.back(400)     
        writer.forward(100)    
        writer.left(90)
        writer.forward(200)
        writer.left(90)
        #writer.forward(465)
        #writer.back (300)     
        #writer.write(wochentag(t),
                   #  align="left", font=("Courier", 14, "bold"))
        # writer.right(90)
        #writer.forward(90)
        #writer.write("Sydney",
                     #align="left", font=("Courier", 14, "bold"))
        writer.write(coverted_time('Australia/Sydney'),
                    align="left", font=("Courier", 14, "bold"))  
        writer.forward(40)
        writer.write(coverted_time('UTC'),
                    align="left", font=("Courier", 14, "bold"))  
        writer.forward(40)
        writer.write(coverted_time('Asia/Singapore'),
                    align="left", font=("Courier", 14, "bold"))
        writer.forward(20)
        writer.write(coverted_time('Asia/Tokyo'),
                    align="left", font=("Courier", 14, "bold"))
        writer.forward(20)
        writer.write(coverted_time('Asia/Kolkata'),
                    align="left", font=("Courier", 14, "bold"))
        writer.forward(20)
        writer.write(coverted_time('Asia/Tehran'),
                    align="left", font=("Courier", 14, "bold"))        
        writer.forward(20)
        writer.write(coverted_time('Europe/Paris'),
                    align="left", font=("Courier", 14, "bold"))        
       

        writer.forward(20)
        writer.write(coverted_time('US/Eastern'),
                    align="left", font=("Courier", 14, "bold"))
        # writer.left(90)
        writer.forward(20)
        writer.write(coverted_time('US/Mountain'),
                    align="left", font=("Courier", 14, "bold"))
        writer.forward(20)
        writer.write(coverted_time('US/Pacific'),
                    align="left", font=("Courier", 14, "bold"))

        writer.forward(20)
     
        #writer.write(datum(t),
                     #align="left", font=("Courier", 14, "bold"))
        #writer.back(185)

        
        tracer(True)
        tracer(True)
        ontimer(tick, 6000)
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "EVENTLOOP"

if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()
