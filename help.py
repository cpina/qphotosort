
from PyQt4 import QtCore,QtGui
from ui_help import *

import icons_rc

# This file is part of qphotosort
# qphotosort is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# any later version.
# 
# qphotosort is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with qphotosort; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# 
# Carles Pina i Estany <carles@pina.cat>, 2006 


class Help(QtGui.QDialog):
	def __init__(self,action):
		QtGui.QDialog.__init__(self)

		self.ui=Ui_help()
		self.ui.setupUi(self)

		title="Help"

		if action=="merge":
			title_frame="Merge"
			text="Combines photos from different directories to one destination. The new name is based on date+time, making it easy to sort chronogically. It can copy the photos or just link the photos from the destination folder to the source directories. The destination names are based on Exif data and time (avoiding to overwrite photos) and the photo suffix.<P><U>Directory:</U> List of directories. Double click in directory field to search a directory<BR> <U>Photo suffix:</U> Suffix to add after date+time.<BR> <U>Time Offset:</U>Seconds to add in Exif time. Accept only integers, positive or negatives."
			height=350

		if action=="resize":
			title_frame="Resize"
			text="Change the size of the photographies without changing the proportion. The results are saved in a new folder, if you want to add a prefix write in prefix field."
			height=200

		if action=="renumerate":
			title_frame="Renumerate"
			text="Orders the files from a directory alphabetically and copies them to destination directory using the format \"newbasename-number\""
			height=200

		if action=="rotate":
			title_frame="Rotate"
			text="Rotates all the photographs from a directory, using the Exif information. Also changes Exif information to be coherent."
			height=200
		
		if action=="time":
			title_frame="Time"
			text="You can select a photo, see what Exif time has and write the real time. In the offset field you will have the difference that should be added to the photo to have the correct time. Usefull when some people don't have the correct time their camera.<P>When you have the \"Offset\", in \"Merge directories\" tab select in which fields from 3th column you want to insert the offset and press \"Export\""
			height=300

		self.setWindowTitle(title)
		self.ui.text.setText(text)
		self.ui.frame.setTitle(title_frame)

	        self.resize(QtCore.QSize(QtCore.QRect(0,0,400,height).size()).expandedTo(self.minimumSizeHint()))
		self.setMinimumSize(QtCore.QSize(400,height))
		self.setMaximumSize(QtCore.QSize(400,height))


