from PyQt4 import QtCore,QtGui
from ui_about import *

import icons_rc

# This file is part of qphotosort
# qphotosort: photo (JPEG) manager 
#
# Copyright (c) 2006, 2008
#      Carles Pina i Estany <carles@pina.cat>
#
# qphotosort is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# qdacco is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class About(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)

		self.ui=Ui_about()
		self.ui.setupUi(self)

