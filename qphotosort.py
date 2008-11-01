#!/usr/bin/python

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
# along with Foobar; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# 
# Carles Pina i Estany <carles@pina.cat>, 2006, 2008


import sys
import shutil 
import os

from PyQt4 import QtCore, QtGui
from main import *

import icons_rc
import i18n_rc

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QDialog.__init__(self)

		self.setfocus={0:False,1:False,2:False,3:False,4:False}

		self.firstTime=True;
		self.clickToWrite=self.tr("Double click to select a directory")

		qlocal=QtCore.QLocale()
		locale=qlocal.name().split("_")[0]

		translator = QtCore.QTranslator()
		translator.load(":/i18n/i18n_"+str(locale)+".qm")
		QtGui.qApp.installTranslator(translator)

		self.merge_rows=10

		self.createMenus()

                #set up the interface
                self.ui = Ui_Form()
                self.ui.setupUi(self)

		#self.connect(self.ui.resize_source_button,QtCore.SIGNAL("clicked()"),self.on_resize_source_button_clicked)

		self.installEventFilter(self)

		self.checkExternal()

		
		self.model = QtGui.QStandardItemModel(self.merge_rows,3,self)
		self.model.setHeaderData(0,QtCore.Qt.Horizontal, QtCore.QVariant(self.tr("Directory")))
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, QtCore.QVariant(self.tr("Photo Suffix")))
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, QtCore.QVariant(self.tr("Time Offset")))
		self.setRowCol(0,0,self.clickToWrite)
		#self.ui.merge_sources.setToolTip(QtGui.QApplication.translate("MainWindow", "test", None, QtGui.QApplication.UnicodeUTF8))

		#self.selectionModel = QtGui.QItemSelectionModel(self.model)
		#self.ui.merge_sources.setSelectionModel(self.selectionModel)
	
		#Insert Data:
		#self.model.setData(self.model.index(0,0,QtCore.QModelIndex()),QtCore.QVariant("hola"))
		#self.model.setData(self.model.index(0,1,QtCore.QModelIndex()),QtCore.QVariant("adeu"))
		#self.model.setData(self.model.index(0,2,QtCore.QModelIndex()),QtCore.QVariant("adeu"))

		#Access data:
		#print self.model.data(self.model.index(0,0,QtCore.QModelIndex()),QtCore.Qt.DisplayRole).toString()
		
		#Insert model to widget

		self.ui.merge_sources.setModel(self.model)
		#width=self.ui.merge_sources.width()
		#print width
		width=489

		self.ui.merge_sources.setColumnWidth(0,width-252)
		#self.model.setData(self.model.index(1,0,QtCore.QModelIndex()),QtCore.QVariant("test"))
		#QtGui.QMessageBox.warning(self,self.tr("Backup"),self.tr("This is the first version. It is strongly recommended to have a backup of your photos before work with qphotosort. Please, backup your photos!"),QtGui.QMessageBox.Ok,QtGui.QMessageBox.NoButton)

	def checkExternal(self):
		self.enable={}
		self.enable[0]=True
		self.enable[1]=True
		self.enable[2]=True
		self.enable[3]=True
		self.enable[4]=True

		convert=os.system("convert > /dev/null 2> /dev/null")
		if convert!=0:
			#resize not working
			QtGui.QMessageBox.warning(self,self.tr("Error"),self.tr("convert not found in your PATH. You will not be able to use resize feature. Solution: install imagemagick package"),QtGui.QMessageBox.Ok,QtGui.QMessageBox.NoButton)
			self.enable[1]=False

		jpegtran=os.system("jpegtran --help > /dev/null 2> /dev/null")
		if jpegtran!=256:
			#rotate not working
			QtGui.QMessageBox.warning(self,self.tr("Error"),self.tr("jpegtran not found in your PATH. You will not be able to use rotate feature. Solution: install libjpeg-progs package"),QtGui.QMessageBox.Ok,QtGui.QMessageBox.NoButton)
			self.enable[3]=False

		exif=os.system("exif > /dev/null 2> /dev/null")
		if exif!=256:
			#rotate not working
			QtGui.QMessageBox.warning(self,self.tr("Error"),self.tr("exif not found in your PATH. You will not be able to use rotate feature. Solution: install exif package"),QtGui.QMessageBox.Ok,QtGui.QMessageBox.NoButton)
			self.enable[3]=False
	
	def on_merge_sources_doubleClicked(self,index):
		if index.column()==0:
			current=self.getRowCol(index.row(),0)
			directori=QtGui.QFileDialog.getExistingDirectory(self,self.tr("Select a directory"),current)
			if (directori!=""):
				self.model.setData(self.model.index(index.row(),0,QtCore.QModelIndex()),QtCore.QVariant(directori))
	
	def on_merge_sources_clicked(self,index):
		if self.firstTime==True:
			self.setRowCol(0,0,"")
			self.firstTime=False


	@QtCore.pyqtSignature("int")
	def on_tabWidget_currentChanged(self,index):
		#self.ui.process.setEnabled(self.enable[index])
		if (self.setfocus[index]==False):
			if index==0:
				self.ui.merge_sources.setFocus()
			if index==1:
				self.ui.resize_source.setFocus()
			if index==2:
				self.ui.renumerate_source.setFocus()
			if index==3:
				self.ui.rotate_source.setFocus()
			if index==4:
				self.ui.time_photo_time.setFocus()
			
			self.setfocus[index]=True

	@QtCore.pyqtSignature("")
	def on_time_select_clicked(self):
		photo=QtGui.QFileDialog.getOpenFileName(self,self.tr("Select a photo"))
		if len(str(photo))>0:
			#cursor=QCursor(3)
			import thread_handle
            		self.thread_image = thread_handle.LoadImage("loadimage")
                	self.thread_image.setinfo(str(photo))
                	self.thread_image.setcomm(self)
                	self.thread_image.start()


	def calcular_offset(self):
		d1 = self.ui.time_photo_time.dateTime()
		d2 = self.ui.time_real_time.dateTime()

		self.ui.time_offset.setText(str(d1.secsTo(d2)))

	def on_time_photo_time_dateTimeChanged(self):
		self.calcular_offset()

	def on_time_real_time_dateTimeChanged(self):
		self.calcular_offset()


	def setRowCol(self,row,col,data):
		self.model.setData(self.model.index(row,col,QtCore.QModelIndex()),QtCore.QVariant(data))
	
	def getRowCol(self,row,col):
		return (str(self.model.data(self.model.index(row,col,QtCore.QModelIndex()),QtCore.Qt.DisplayRole).toString()))

	@QtCore.pyqtSignature("")
	def on_time_export_clicked(self):
		row=0

		selecteds = self.ui.merge_sources.selectedIndexes()
		export_time = str(self.ui.time_offset.text())

		for i in selecteds:
			if i.column()==2:
				self.model.setData(i,QtCore.QVariant(export_time))

	@QtCore.pyqtSignature("")
	def on_resize_source_button_clicked(self):
		self.ask_directory(self.ui.resize_source)
	
	@QtCore.pyqtSignature("")
	def on_merge_destination_button_clicked(self):
		self.ask_directory(self.ui.merge_destination)

	@QtCore.pyqtSignature("")
	def on_resize_destination_button_clicked(self):
		self.ask_directory(self.ui.resize_destination)

	@QtCore.pyqtSignature("")
	def on_renumerate_source_button_clicked(self):
		self.ask_directory(self.ui.renumerate_source)

	@QtCore.pyqtSignature("")
	def on_renumerate_select_destination_button_clicked(self):
		self.ask_directory(self.ui.renumerate_destination)

	@QtCore.pyqtSignature("")
	def on_rotate_source_button_clicked(self):
		self.ask_directory(self.ui.rotate_source)

	@QtCore.pyqtSignature("")
	def on_rotate_destination_button_clicked(self):
		self.ask_directory(self.ui.rotate_destination)

	def ask_directory(self,object):
		directori=QtGui.QFileDialog.getExistingDirectory(self,self.tr("Select a directory"))
		object.setText(directori)

	def continue_overwriting(self):
		answer=QtGui.QMessageBox.warning(self,self.tr("Confirmation"),self.tr("Source and destination directory are the same and new prefix is empty. If you continue, you will loose source photos. Do you want to continue?"),QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
		return (answer==QtGui.QMessageBox.Yes)

	@QtCore.pyqtSignature("")
	def on_process_clicked(self):
		import thread_handle

		tab=self.ui.tabWidget.currentIndex()

		if tab==0:
			directories=[]
			suffixes=[]
			offsets=[]

			for row in xrange(0,self.merge_rows):
				directory = self.getRowCol(row,0)
				if (directory != "" and directory != self.clickToWrite):
					directories.append(self.getRowCol(row,0))
					suffix=self.getRowCol(row,1)
					suffix=QtCore.QString(suffix)
					suffix=suffix.remove('/')
					suffixes.append(suffix)
					
					offset=self.getRowCol(row,2)
					try: 
						offset=int(offset)
					except:
						offset=0

					offsets.append(offset)

			self.thread1=thread_handle.MergeThread("thread1")
			self.thread1.setinfo(directories,str(self.ui.merge_destination.text()),suffixes,offsets,self.ui.merge_link.isChecked(),self.ui.file_pattern.text())
			self.thread1.setcomm(self)
			self.thread1.start()

		if tab==1:
			qsource=self.ui.resize_source.text().remove(QtCore.QRegExp("/$"))
			qdestination=self.ui.resize_destination.text().remove(QtCore.QRegExp("/$"))
			qprefix=self.ui.resize_newprefix.text().remove("/")

			if (qsource==qdestination and qprefix==""):
				if (self.continue_overwriting()==False):
					return

			self.thread1=thread_handle.ResizeThread("thread1")

			size_ok = str(self.ui.resize_x.text())+"x"+str(self.ui.resize_y.text())
			self.thread1.setinfo(str(qsource),size_ok,str(qprefix),str(qdestination))

			self.thread1.setcomm(self)
			self.thread1.start()

		if tab==2:
                	self.thread1=thread_handle.RenumerateThread("thread1")
             	   	self.thread1.setinfo(str(self.ui.renumerate_source.text()),str(self.ui.renumerate_basename.text()),str(self.ui.renumerate_destination.text()))
     	           	self.thread1.setcomm(self)
                	self.thread1.start()

		if tab==3:
			qsource=self.ui.rotate_source.text().remove(QtCore.QRegExp("/$"))
			qdestination=self.ui.rotate_destination.text().remove(QtCore.QRegExp("/$"))
			qprefix=self.ui.rotate_newprefix.text().remove("/")

			if (qsource==qdestination and qprefix==""):
				if (self.continue_overwriting()==False):
					return

	                self.thread1=thread_handle.RotateThread("thread1")
	                self.thread1.setinfo(str(qsource),str(qprefix),str(qdestination))
	                self.thread1.setcomm(self)
	                self.thread1.start()

		if tab==4:
			calcular_offset()


	def eventFilter(self,object,event):
		#TODO: save in a variable the message number and compare event.type with this variable!
		if (event.type() == QtCore.QEvent.Type(QtCore.QEvent.User+0)):
			QtGui.QMessageBox.warning(self,self.tr("Error"),self.tr("Error reading/writing files or other problems. Check permission of destination directory, not overwrite files, space. You can also execute from console and check the error message"),QtGui.QMessageBox.Ok,QtGui.QMessageBox.NoButton)
			self.ui.progressBar.setRange(0,100)
			self.ui.progressBar.setValue(0);
			self.ui.process.setEnabled(True)
			return True

		if (event.type() == QtCore.QEvent.Type(QtCore.QEvent.User+1)):
			self.ui.progressBar.setValue(int(event.getData()))
			return True

		if (event.type() == QtCore.QEvent.Type(QtCore.QEvent.User+2)):
			self.ui.process.setEnabled(True)
			#self.ui.progressBar.setProgress(0)
			#self.ui.progressBar.setEnabled(False)
			self.ui.progressBar.setRange(0,100)
			self.ui.progressBar.setValue(0)
			QtGui.QMessageBox.information(self,self.tr("Information"),self.tr("Done!"),QtGui.QMessageBox.Ok,QtGui.QMessageBox.NoButton)
			return True

		if (event.type() == QtCore.QEvent.Type(QtCore.QEvent.User+3)):
			self.ui.process.setEnabled(False)
			return True

		if (event.type() == QtCore.QEvent.Type(QtCore.QEvent.User+4)):
			self.ui.progressBar.setRange(0,int(event.getData()))
			return True

		if (event.type() == QtCore.QEvent.Type(QtCore.QEvent.User+10)):
			#In previous version
			self.image.setPixmap(a0.data())
			return True

		if (event.type() == QtCore.QEvent.Type(QtCore.QEvent.User+11)):
			date = event.getData()
			t = QtCore.QTime(date.hour,date.minute,date.second)
			d = QtCore.QDate(date.year,date.month,date.day)
			dt = QtCore.QDateTime(d,t)

			self.ui.time_photo_time.setDateTime(dt)
			self.ui.time_real_time.setDateTime(dt)

		return QtGui.QWidget.eventFilter(self,object,event);

	def createMenus(self):
		self.aboutQphotosort = QtGui.QAction(self.tr("&About qphotosort"),self)
		self.aboutQphotosort.setIcon(QtGui.QIcon(":/icons/help.png"))
		self.connect(self.aboutQphotosort,QtCore.SIGNAL("triggered()"),self.about)

		self.helpMenu = self.menuBar().addMenu(self.tr("&Help"))
		self.helpMenu.addAction(self.aboutQphotosort)
		

	#HELP BUTTONS
	@QtCore.pyqtSignature("")
	def on_merge_help_clicked(self):
		import help
		dialog=help.Help("merge")
		dialog.exec_()


	@QtCore.pyqtSignature("")
	def on_resize_help_clicked(self):
		import help
		dialog=help.Help("resize")
		dialog.exec_()


	@QtCore.pyqtSignature("")
	def on_renumerate_help_clicked(self):
		import help
		dialog=help.Help("renumerate")
		dialog.exec_()

	@QtCore.pyqtSignature("")
	def on_rotate_help_clicked(self):
		import help
		dialog=help.Help("rotate")
		dialog.exec_()


	@QtCore.pyqtSignature("")
	def on_time_help_clicked(self):
		import help
		dialog=help.Help("time")
		dialog.exec_()

	def about(self):
		import about
		dialog=about.About()
		dialog.exec_()

	#DELETE BUTTONS
	@QtCore.pyqtSignature("")
	def on_resize_delete_source_clicked(self):
		self.delete_directory(self.ui.resize_source)

	@QtCore.pyqtSignature("")
	def on_resize_delete_destination_clicked(self):
		self.delete_directory(self.ui.resize_destination)

	@QtCore.pyqtSignature("")
	def on_renumerate_delete_source_clicked(self):
		self.delete_directory(self.ui.renumerate_source)

	@QtCore.pyqtSignature("")
	def on_renumerate_delete_destination_clicked(self):
		self.delete_directory(self.ui.renumerate_destination)

	@QtCore.pyqtSignature("")
	def on_rotate_delete_source_clicked(self):
		self.delete_directory(self.ui.rotate_source)

	@QtCore.pyqtSignature("")
	def on_rotate_delete_destination_clicked(self):
		self.delete_directory(self.ui.rotate_destination)

	@QtCore.pyqtSignature("")
	def on_merge_delete_destination_clicked(self):
		self.delete_directory(self.ui.merge_destination)

	@QtCore.pyqtSignature("")
	def on_merge_delete_sources_clicked(self):
		row=0

		howmany=self.howMany()
		if howmany==0:
			QtGui.QMessageBox.warning(self,self.tr("Information"),self.tr("There isn't any directory"),QtGui.QMessageBox.Yes,QtGui.QMessageBox.NoButton)
			return
			

		answer=QtGui.QMessageBox.warning(self,self.tr("Confirmation"),self.tr("Are you sure that you want to delete ALL listed directories?"),QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
		if answer==QtGui.QMessageBox.No:
			return
			
		answer=QtGui.QMessageBox.warning(self,self.tr("Confirmation"),self.tr("Are you sure that you are sure to delete ALL listed directories?"),QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
		if answer==QtGui.QMessageBox.No:
			return

		while row<self.merge_rows:
			if str(self.getRowCol(row,0))!="":
				try:
					shutil.rmtree(str(self.getRowCol(row,0)))
					self.setRowCol(row,0,"")
				except:
					QtGui.QMessageBox.warning(self,self.tr("Error"),self.tr("Error deleting "+self.getRowCol(row,0)+" directory. Check permissions, etc."),QtGui.QMessageBox.Ok,QtGui.QMessageBox.NoButton)
			row=row+1


	def delete_directory(self,qline):
		directory=qline.text()
		if (directory==""):
			QtGui.QMessageBox.warning(self,self.tr("Error"),self.tr("You have not selected any directory"))
			return

		answer=QtGui.QMessageBox.warning(self,self.tr("Confirmation"),self.tr("Are you sure that you want to delete ")+directory+self.tr(" directory?") ,QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
		if answer==QtGui.QMessageBox.Yes:
			try:
				shutil.rmtree(str(directory))
				qline.setText("")
			except:
				QtGui.QMessageBox.warning(self,self.tr("Error"),self.tr("Error deleting directory. Check permissions, etc."),QtGui.QMessageBox.Ok,QtGui.QMessageBox.NoButton)
		
	def howMany(self):
		row=0
		ret=0

		while (row<self.merge_rows):
			if self.getRowCol(row,0)!="":
				ret=ret+1
			
			row=row+1

		return ret

if __name__ == "__main__":
        app=QtGui.QApplication(sys.argv)
        window=MainWindow()
        window.show()
        sys.exit(app.exec_())

