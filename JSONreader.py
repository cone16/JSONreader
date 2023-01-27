from console import hud_alert

import json
import ui
import dialogs


class JSONreader():
	
	def __init__(self):
		self.removeable_chars = '"{}[],'
		print('passed init...')
			
	def openJSON(self, JSONdoc):
		# try ro open the file. if something 
		# went wrong, catch the error and don't 
		# shut the whole app
		
		# clean the textview if not, the new 
		# file will written right under the 
		# previous one
		v['textview1'].text = ''
		try:
			with open(JSONdoc, 'r') as file:
				for line in file:
					for char in self.removeable_chars:
						line = line.replace(char, '')
					json.loads(json.dumps(line))
					v['textview1'].text += line				
		except (json.JSONDecodeError) as err:
			hud_alert(err)
			v['textview1'].text = ''


def buttonClicked(sender):
	# Get the tapped sender(in this case
	# button!)'s title or name
	button_title = sender.title
	button_name = sender.name
	print('sender is now: ', button_title)
		
	# If the tapped button title the right
	# one, run method readJSON or whatever
	# you like.
	if button_name == 'open':
		print(button_name, ' was been tabbed!')
		JSONdoc = dialogs.pick_document(types=['public.json'])
		v['textfield1'].text = JSONdoc
		JSONreader().openJSON(JSONdoc)
	if button_name == 'exit':
		v.close()
		quit()
		

# Start configuration for the App
if __name__ == '__main__':
	v = ui.load_view()
	
	# Check the screensize and get one for
	# the right device
	if min(ui.get_screen_size()) >= 768:
		# iPad
		v.frame = (0, 0, 360, 400)
		v.present('sheet')
	else:
		# iPhone
		v.present(orientations=['portrait'])
		# v.present('sheet')
