from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class Container(GridLayout):

	text_input_widget = ObjectProperty()
	label_widget = ObjectProperty()

	def change_text(self):
		self.label_widget.text = \
			self.text_input_widget.text.upper()
		self.text_input_widget.text = ''	

class NewApp(App):
	def build(self):
		return Container()


def main():
	NewApp().run()

if __name__ == "__main__":
	main()

