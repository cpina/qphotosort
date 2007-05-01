TEMPLATE	= app
LANGUAGE	= C++

CONFIG	+= qt warn_on release

FORMS	= form1.ui \
	merge_help_d.ui \
	resize_help_d.ui \
	rename_help.ui \
	about.ui \
	main.ui

IMAGES	= images/button_ok.png \
	images/fileopen.png

unix {
  UI_DIR = .ui
  MOC_DIR = .moc
  OBJECTS_DIR = .obj
}

