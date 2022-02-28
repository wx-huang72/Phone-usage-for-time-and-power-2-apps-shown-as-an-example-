#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install plotly')


# In[3]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Phone:
    
    def __init__(self):
        self.power = int( input("What is the batter level now (in integer): ") )
        self.using_messenger_time = 0
        self.using_youtube_time = 0
        self.messenger_using_power = 0
        self.youtube_using_power = 0
        self.left_power = self.power

        
    def check_battery_level(self):
        if self.left_power <= 30:
            print("Warning!!!Low Battery Level!!!Charge as soon as possible!!")
    
    
    def messenger(self):
        if_using_messenger = input("Did you use the messenger today?(Y/N) ")
        if if_using_messenger.lower() == "y":
            self.using_messenger_time = int(input("How long have you used it today?(in hour)"))
            
        self.messenger_using_power = 5*self.using_messenger_time
        self.left_power = self.left_power - self.messenger_using_power
        print("You still have {}% left!".format(self.left_power))
        
            
    def youtube(self):
        if_using_youtube = input("Did you use the youtube today?(Y/N) ")
        if if_using_youtube.lower() == "y":
            self.using_youtube_time = int(input("How long have you used it today ? (in hour)"))
        
        self.youtube_using_power = 15*self.using_youtube_time
        self.left_power = self.left_power - self.youtube_using_power
        print("You still have {}% left!".format(self.left_power))
            

    def charging(self):
        if_charging = input("Did you charge your phone today?(Y/N) ")
        if if_charging.lower() == "y":
            in_minute_or_hour = input("Which unit do you think can better describe your charging time, minute or hour?")
            if in_minute_or_hour.lower() == "hour":
                self.charging_time_in_hour = int(input("How many hours have you charged for today?(only integer allowed)"))
                self.charged_power_in_hour = 48*self.charging_time_in_hour
                self.left_power = self.left_power + self.charged_power_in_hour
            
            else:
                self.charging_time_in_minute = int(input("How many minutes have you charged for today?(only integer allowed)"))
                self.charged_power_in_minute = 0.8*self.charging_time_in_minute
                self.left_power = self.left_power + self.charged_power_in_minute
            
            
    def stop_charging(self):    
        if self.left_power > 100:
            self.left_power = 100
            print("Congrates!You have {}% left!".format(self.left_power))
        elif self.left_power <= 30:
            print("Only {}% left!!Please keep charging!!".format(self.left_power))        
        else:
            self.left_power    
            print("Congrates!You have {}% left!".format(self.left_power))
        
        
    def plotting(self):
        labels = ["using_messenger_time", "using_youtube_time", "other"]
        
        color_set_1 = ['rgb(100,149,237)', 'rgb(30,144,255)', 'rgb(65,105,225)']
        color_set_2 = ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)']
        
        fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]]) 

        fig.add_trace(go.Pie(labels=labels, values=[self.using_messenger_time,self.using_youtube_time,(8-self.using_messenger_time-self.using_youtube_time)], 
                             name="Software duration distribution",marker_colors=color_set_1),1,1)
        fig.add_trace(go.Pie(labels=labels, values=[self.messenger_using_power,self.youtube_using_power,self.left_power], 
                             name="Software power using",marker_colors=color_set_2),1, 2)

        fig.update_traces(hole=.4, hoverinfo="label+percent+name")                                      

        fig.update_layout(
            title_text="Phone usage in a day (8 hours)",

            annotations=[dict(text='time', x=0.20, y=0.5, font_size=20, showarrow=False),             
                         dict(text='power', x=0.83, y=0.5, font_size=20, showarrow=False)])
        fig.show()     
            
            
            

my_phone = Phone()
my_phone.check_battery_level()
my_phone.messenger()
my_phone.check_battery_level()
my_phone.youtube()
my_phone.check_battery_level()
my_phone.charging()
my_phone.check_battery_level()
my_phone.stop_charging()
my_phone.plotting()

