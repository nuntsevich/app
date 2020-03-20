# python main.py -m screen:droid2,portrait,scale=.75

# from kivy.app import App
# from kivy.uix.button import Button 
# from kivy.uix.gridlayout import GridLayout
# from kivy.properties import ObjectProperty

# class Container(GridLayout):

# 	text_input_widget = ObjectProperty()
# 	label_widget = ObjectProperty()

# 	def change_text(self):
# 		self.label_widget.text = \
# 			self.text_input_widget.text.upper()
# 		self.text_input_widget.text = ''	

# class NewApp(App):
# 	def build(self):
# 		return Container()


# def main():
# 	NewApp().run()

# if __name__ == "__main__":
# 	main()


from kivy.app import App
from kivy.uix.button import Button 

class NewApp(App):
	def build(self):
		return Button(text='Hello world')

NewApp().run()

# <ItemLabel@Label>:
#     font_size: '25sp'


# <Container>
#     rows: 3
#     padding: 50

#     text_input_widget: text_input
#     label_widget: label

#     TextInput:
#         id: text_input
#         size_hint: 1, 0.4
#         multiline: False
#         font_size: 40

#     Label:
#         id: label
#         text: 'Some text'
#         font_size: 40

#     FloatLayout:
#         Button:
#             size_hint: 0.5, 0.4
#             pos_hint: { 'center_x': 0.5, 'y': 0.1 }
#             text: 'Hello'
#             font_size: 40 

#             on_release:
#                 root.change_text()
