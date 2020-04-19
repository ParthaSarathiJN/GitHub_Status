from bs4 import BeautifulSoup
import requests
import pprint


URL = 'https://www.githubstatus.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

componentNames = soup.find_all('span', class_='name')
#print(componentNames)

componentStatus = soup.find_all('span', class_='component-status')
#print(componentStatus)

componentsNameList = []
componentStatusList = []
removeList = []


def typesFunc(componentNames):
	count = 0

	for names in componentNames:
		componentsNameList.append(names.text.strip())

	for names in componentsNameList:
		if 'Other' in names or 'Visit' in names:
			removeList.append(count)
			componentsNameList.remove(names)
		count += 1

	return componentsNameList, removeList

typesFunc(componentNames)
#print(componentsNameList)
#print(removeList)


def conditionsFunc(componentStatus, removeList):
	count = 0
	for status in componentStatus:
		componentStatusList.append(status.text.strip())

	for status in componentStatusList:
		if count in removeList:
			componentStatusList.remove(status)
		count+= 1

	return componentStatusList

conditionsFunc(componentStatus, removeList)
#print(componentStatusList)


result = dict(zip(componentsNameList, componentStatusList))

#print(result)



import os
from os import path
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty

Window.size = (600, 333)
Window.clearcolor = (0.035, 0.168, 0.203, 0.4)


class ConnectPage(GridLayout):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.cols = 2

		#import GithubStatus

		compName = componentsNameList
		compStatus = componentStatusList

		self.add_widget(Label(text=compName[0], font_size=25, font_name='calibri'))
		if compStatus[0] == 'Operational': 
			self.comp0 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.050, 0.772, 0.129, 1]))
		else: self.comp0 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.772, 0.050, 0.066, 1]))
		self.add_widget(self.comp0)

		self.add_widget(Label(text=compName[1], font_size=25, font_name='calibri'))
		if compStatus[1] == 'Operational': 
			self.comp1 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.050, 0.772, 0.129, 1]))
		else: self.comp1 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.772, 0.050, 0.066, 1]))
		self.add_widget(self.comp1)

		self.add_widget(Label(text=compName[2], font_size=25, font_name='calibri'))
		if compStatus[2] == 'Operational': 
			self.comp2 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.050, 0.772, 0.129, 1]))
		else: self.comp2 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.772, 0.050, 0.066, 1]))
		self.add_widget(self.comp2)

		self.add_widget(Label(text=compName[3], font_size=25, font_name='calibri'))
		if compStatus[3] == 'Operational': 
			self.comp3 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.050, 0.772, 0.129, 1]))
		else: self.comp3 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.772, 0.050, 0.066, 1]))
		self.add_widget(self.comp3)

		self.add_widget(Label(text=compName[4], font_size=25, font_name='calibri'))
		if compStatus[4] == 'Operational': 
			self.comp4 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.050, 0.772, 0.129, 1]))
		else: self.comp4 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.772, 0.050, 0.066, 1]))
		self.add_widget(self.comp4)

		self.add_widget(Label(text=compName[5], font_size=25, font_name='calibri'))
		if compStatus[5] == 'Operational': 
			self.comp5 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.050, 0.772, 0.129, 1]))
		else: self.comp5 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.772, 0.050, 0.066, 1]))
		self.add_widget(self.comp5)

		self.add_widget(Label(text=compName[6], font_size=25, font_name='calibri'))
		if compStatus[6] == 'Operational': 
			self.comp6 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.050, 0.772, 0.129, 1]))
		else: self.comp6 = (Label(text=compStatus[0], font_size=25, font_name='calibri', color=[0.772, 0.050, 0.066, 1]))
		self.add_widget(self.comp6)



class Github_StatusApp(App):
	def build(self):
		return ConnectPage()


if __name__ == "__main__":
	Github_StatusApp().run()
