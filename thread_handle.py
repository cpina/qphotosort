import sys
import time
import glob
import photosort

from PyQt4 import QtCore,QtGui
from main import *

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
# Carles Pina i Estany <carles@pina.cat>, 2006, 2008


class MergeThread(QtCore.QThread):
	def __init__(self, name, *args):
		self.name=name
		apply(QtCore.QThread.__init__, (self, ) + args)

	def setinfo(self,s,dest,suffix_,offset_,symb_links_,file_pattern_):
		self.a=s
		self.destination=dest
		self.suffix = suffix_
		self.offset = offset_
		self.symb_links = symb_links_
		self.file_pattern = str(file_pattern_)

	def setcomm(self,ppal):
		self.gui= ppal #ppal == main

	def run(self):
		#buttonok = False
		sendInformation(3,"",self.gui)
		total = 0

		for i in self.a:
			total = total + len(glob.glob(i+'/*.[jJ][pP][gG]'))
		
		#progress.totalsteps = total
		sendInformation(4,total,self.gui)
		
		count = 0
		index = 0
		for i in self.a:
			for f in glob.glob(i+'/*.[jJ][pP][gG]'):
				if len(str(self.offset[index]))>0:
					offset = int(self.offset[index])
				else:
					offset = 0
				try:
    					c = photosort.mergeFiles(f,self.destination,self.suffix[index],offset,self.symb_links,self.file_pattern)
				except:
					print "Mal",RuntimeError,TypeError,NameError
					sendInformation(0,RuntimeError,self.gui)
					return True
					
				count = count+1
				sendInformation(1,count,self.gui)
			index=index+1

		sendInformation(2,"",self.gui)

class ResizeThread(QtCore.QThread):
	def __init__(self, name, *args):
		self.name=name
		apply(QtCore.QThread.__init__, (self, ) + args)

	def setinfo(self,source,size,prefix,destination):
		self.source=source
		self.newsize=size
		self.newprefix=prefix
		self.destination=destination

	def setcomm(self,ppal):
		self.gui = ppal

	def run(self):
		sendInformation(3,"",self.gui)
		
		total = len(glob.glob(self.source+'/*.[jJ][pP][gG]'))
		i = 0

		sendInformation(4,total,self.gui)

		for f in glob.glob(self.source+'/*.[jJ][pP][gG]'):
			try:
    				c = photosort.resizeFiles(f,self.newsize,self.destination,self.newprefix)
			except:
				sendInformation(0,"",self.gui)
				return True

			i = i+1
			#update progressbar
			sendInformation(1,i,self.gui)
		
		sendInformation(2,"",self.gui)

class RenumerateThread(QtCore.QThread):
	def __init__(self, name, *args):
		self.name=name
		apply(QtCore.QThread.__init__, (self, ) + args)

	def setinfo(self,s1,s2,s3):
		self.source = s1
		self.newbasename = s2
		self.newdestination = s3

	def setcomm(self,ppal):
		self.gui = ppal

	def run(self):
		sendInformation(3,"",self.gui)
		total = len(glob.glob(self.source+'/*.[jJ][pP][gG]'))
		i = 0

		sendInformation(4,total,self.gui)

                r = photosort.renameFiles()

                for f in glob.glob(self.source+'/*.[jJ][pP][gG]'):
			try:
                        	r.move(f,self.newdestination,self.newbasename)
			except:
				sendInformation(0,"",self.gui)
				return True
			i=i+1
			sendInformation(70001,i,self.gui)
		
		sendInformation(2,"",self.gui)


class RotateThread(QtCore.QThread):
	def __init__(self, name, *args):
		self.name=name
		apply(QtCore.QThread.__init__, (self, ) + args)

	def setinfo(self,source,prefix,destination):
		self.source=source
		self.newprefix=prefix
		self.destination=destination

	def setcomm(self,ppal):
		self.gui = ppal

	def run(self):
		sendInformation(3,"",self.gui)
		
		total = len(glob.glob(self.source+'/*.[jJ][pP][gG]'))
		i = 0

		sendInformation(4,total,self.gui)

		for f in glob.glob(self.source+'/*.[jJ][pP][gG]'):
			try:
    				c = photosort.rotateFiles(f,self.destination,self.newprefix)
			except:
				#DialogBox
				sendInformation(0,"",self.gui)
				return True
			i = i+1
			#update progressbar
			sendInformation(1,i,self.gui)
		
		sendInformation(2,"",self.gui)

class LoadImage(QtCore.QThread):
	def __init__(self, name, *args):
		self.name=name
		apply(QtCore.QThread.__init__, (self, ) + args)

	def setinfo(self,file):
		self.file=file

	def setcomm(self,ppal):
		self.gui= ppal #ppal == main

	def run(self):
		#To add again:
		#image = QPixmap(190,170)
		#image.load(self.file)
		#sendInformation(10,image,self.gui)
		
		date = photosort.get_date2(self.file)
		sendInformation(11,date,self.gui)


#gui: main widget
#id: message number
#s: message contents

class MyEvent(QtCore.QEvent):
	def setData(self,data):
		self.data=data

	def getData(self):
		return self.data

def sendInformation(id,s,gui):
	number=MyEvent.Type(MyEvent.User+id)
	event=MyEvent(number)
	event.setData(s)
	#QtGui.QApplication.sendEvent(gui,event)
	QtGui.QApplication.postEvent(gui,event)

