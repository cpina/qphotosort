#!/usr/bin/python

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

import re
import os
import stat
import time
import glob
import shutil
import EXIF
import getopt,sys
import datetime

import os
class mergeFiles:
	"Interface to merge directory files using Exif date"

	def __init__(self,file,dest_directory,suffix,offset,symb_links,file_pattern_="%Y-%m-%d_%H:%M:%S"):
	        self.file_pattern = file_pattern_

		#File documentation: http://www.daniweb.com/code/snippet218.html
		fileStats=os.stat(file)

		dest = self.get_date(file,offset)

		(dirName,fileName) = os.path.split(file)
		(fileBaseName,fileExtension) = os.path.splitext(fileName)
	
		destination = dest_directory+'/'+dest+suffix+'.jpg'
		destination = self.next_name(destination)

		if symb_links == 1:
			origen=os.path.dirname(file)
			cami = relatiu(os.path.normpath(dest_directory),origen)
			#print "symlink("+cami+"/"+os.path.basename(file)+","+destination+")"
			os.symlink(cami+"/"+os.path.basename(file),destination)
		else:
			#print "copy("+file+","+destination+")"
			shutil.copy(file,destination)

	def next_name(self,destination):
		if os.path.exists(destination):
			#TODO: str(destination) would be better before?
			#It is a class 'class 'PyQt4.QtCore.QString',
			#os.path.split is not handling correctly but
			#os.path.exists yes (depends of Qt version?
			#before 2008-August Debian stable was working fine...
			(dirName,fileName) = os.path.split(str(destination))
			(fileBaseName,fileExtension) = os.path.splitext(fileName)
		
			#fitxerPatro = re.compile('(\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2})_(\d+)(\..*)')
			#primer = fitxerPatro.match(fileName)

			destination=dirName+'/'+fileBaseName+"_"+".jpg"
                        destination=self.next_name(destination)

                        # Note: next code it was for the first release,
                        # where I was adding a number after the photo, 
                        # but user couldn't choose the file pattern format
			#if primer:
				#num = primer.group(2)
				#print "num",num
				#num2 = int(num)+1
				##next name by date
				#return(self.next_name(dirName+'/'+primer.group(1)+"_"+str(num2)+".jpg"))
			#else:
				#fitxerPatro = re.compile('(.*)_(\d+)(\..*)')
				#primer = fitxerPatro.match(fileName)
				#if primer:
					#num=primer.group(2)
					#num2=int(num)+1
					##no date, but we will not overwrite
					#return (self.next_name(dirName+'/'+primer.group(1)+"_"+str(num2)+".jpg"))
				##new _ name...
				#return(self.next_name(dirName+'/'+fileBaseName+"_1.jpg"))
		return destination

	def get_date(self,foto,offset):
		#http://home.cfl.rr.com/genecash/digital_camera/EXIF.py
		f=open(foto,'rb')
		try:
			tags=EXIF.process_file(f, details=False, stop_tag='DateTimeOriginal')
		except:
			(dirName,fileName) = os.path.split(foto)
			(fileBaseName,fileExtension) = os.path.splitext(fileName)
			ret = fileBaseName
			return ret

		f = re.compile('(\d{4}):(\d{2}):(\d{2}) (\d{2}):(\d{2}):(\d{2})')
		j = str(tags['EXIF DateTimeOriginal'])
		dades = f.match(j)
		data = datetime.datetime(int(dades.group(1)),int(dades.group(2)),int(dades.group(3)),int(dades.group(4)),int(dades.group(5)),int(dades.group(6)))
		data = data+datetime.timedelta(0,offset)
		#ret = data.strftime("%Y-%m-%d_%H:%M:%S")
		ret = data.strftime(self.file_pattern)
		return ret


class resizeFiles:
	"Resize files of a directory using convert"
	
	def __init__(self,file,size,destination,newPrefix):
		(dirName,fileName) = os.path.split(file)
		(fileBaseName,fileExtension) = os.path.splitext(fileName)
		
		c = os.system("convert -resize "+size+" \""+file+"\" \""+destination+"/"+newPrefix+fileName+"\"")
		if c != 0:
			raise ExceptionFile
			

class rotateFiles:
	"Rotate files of a directory using convert"
	
	def __init__(self,file,destination,newPrefix):
		(dirName,fileName) = os.path.split(file)
		(fileBaseName,fileExtension) = os.path.splitext(fileName)
	

		orient = get_orientation(file)
		if orient == 90 or orient == 270:
			temp = destination+"/"+fileName+".tmp"
			os.system("jpegtran -copy all -rotate "+str(orient)+" -outfile "+temp+" "+file)
			os.system("exif -t 'Orientation' --ifd=0 --set-value=1 -o "+destination+"/"+newPrefix+fileName+" "+temp)
			os.remove(temp)
		else:
			shutil.copy(file,destination+"/"+newPrefix+fileName)

class renameFiles:
	"Rename files, moving from one directory to other directory"
	def __init__(self):
		self.num=1

	def move(self,file,destination,newname):
		(dirName,fileName) = os.path.split(file)
		(fileBaseName,fileExtension) = os.path.splitext(fileName)

		numfile = "%03d" % self.num
		shutil.copy(file,destination+"/"+newname+numfile+fileExtension)
		self.num = self.num+1
		
def deleteDirectory(directory):
	for f in glob.glob(directory+'/*.[jJ][pP][gG]'):
		os.remove(f)
	
	os.rmdir(directory)


def get_date2(foto):
	#http://home.cfl.rr.com/genecash/digital_camera/EXIF.py
	f=open(foto,'rb')
	try:
		tags=EXIF.process_file(f,details=False, stop_tag='DateTimeOriginal')
	except:
		(dirName,fileName) = os.path.split(foto)
		(fileBaseName,fileExtension) = os.path.splitext(fileName)
		ret = fileBaseName
		return ret

	f = re.compile('(\d{4}):(\d{2}):(\d{2}) (\d{2}):(\d{2}):(\d{2})')
	j = str(tags['EXIF DateTimeOriginal'])
	dades = f.match(j)
	data = datetime.datetime(int(dades.group(1)),int(dades.group(2)),int(dades.group(3)),int(dades.group(4)),int(dades.group(5)),int(dades.group(6)))
	return data


def get_orientation(foto):
	#http://home.cfl.rr.com/genecash/digital_camera/EXIF.py
	f=open(foto,'rb')
	try:
		tags=EXIF.process_file(f,details=False, stop_tag='Image Orientation')
	except:
		return 0
	
	j = str(tags['Image Orientation'])
	a=re.compile(" CW")


	if re.compile(" CW").search(j,1):
		return 90
	
	if re.compile(" CCW").search(j,1):
		return 270

	return 0

from itertools import izip

def relatiu(orig,desti):
        o = orig.split('/')[1:]
        d = desti.split('/')[1:]
        n=0
        for n, (i, j) in enumerate(izip(o, d)) :
                if i != j :
                        break
                if n + 1 == len(o) :
                        n += 1
        return '../' * (len(o) - n) + '/'.join(d[n:])

def Usage():
	print "You need to execute one action:"
	print "   --merge  --source1=directory1 --source2=directory2 --destination=directory"
	print "   --resize --size=400x400 --source=directory1 --destination=directory"
	print "   --rename --source=directory1 --destination=directory --newname=YY"
	print "   --rotate --source=directory --destination=directory"

#-----------------------------
def main():
	if len(sys.argv)==1:
		Usage()
		sys.exit(3)
	
	try:
		opts,args=getopt.getopt(sys.argv[1:],"",["about","merge","resize","rename","rotate","source=","source1=","source2=","destination=","size=","newprefix=","newname="])
	
	except getopt.GetoptError:
		Usage()
		sys.exit(2)


	merge=False
	resize=False
	rename=False
	rotate=False
	about=False
	newname=""
	newprefix=""

	for o,a in opts:
		if o == "--about":
			about = True

		if o == "--merge":
			merge = True

		if o == "--source":
			source = a 
		
		if o == "--source1":
			source1 = a
	
		if o == "--source2":
			source2 = a

		if o == "--destination":
			destination = a

		if o == "--resize":
			resize = True
	
		if o == "--size":
			size = a

		if o == "--newprefix":
			newprefix = a

		if o == "--newname":
			newname = a

		if o == "--rename":
			rename = True

		if o == "--rotate":
			rotate = True

	if about:
		print ""
		print "Photosort allows to merge photos from several directories based on Exif\ndate/time. Also has options to resize, renumerate or rotate the photos"
		print ""
		print "It is possible to use photosort in command line\n, but is recommended to use qphotosort -graphic version"
		print ""
		print "Carles Pina i Estany, 2006"
		print "License: 2.0 or later"
		exit

	if merge and len(source1)>0 and len(source2)>0 and len(destination)>0:
		if len(sys.argv) != 5:
			Usage()
			sys.exit(2)

		for f in glob.glob(source1+'/*.[jJ][pP][gG]'):
			c = mergeFiles(f,destination,"",0,0)
	
		for f in glob.glob(source2+'/*.[jJ][pP][gG]'):
			c = mergeFiles(f,destination,"",0,0)
		
	if resize and len(source)>0:
		for f in glob.glob(source+'/*'):
			r = resizeFiles(f,size,destination,newprefix)

	if rename and len(destination)>0:
		r = renameFiles()
		
		for f in glob.glob(source+'/*'):
			r.move(f,destination,newname)

	if rotate and len(destination)>0:
		for f in glob.glob(source+'/*'):
			r = rotateFiles(f,destination,newprefix)

def mf(a,b):
	c = mergeFiles(a,b)

if __name__ == "__main__":
	print "photosort 1 Beta, GPL version 2.0 or later"
	main()

#Examples of usage:
#Merge fotos1 and fotos2, destination is /tmp/test
#./photosort.py --merge --source1=/mnt/dades/fotos2 --source2=/mnt/dades/fotos1 --destination=/tmp/test/

#Resize the photos of one directory (photos will keep the proportion)
#./photosort.py --resize --size 400x400  --source=/mnt/dades/fotos1/ --destination=/tmp/

#Rename the photos (renumerate)
#./photosort.py --rename --source=/mnt/dades/fotos1 --destination=/tmp/test --newname=YY

#Rotate the photos
#./photosort.py --rotate --source=/mnt/dades/fotos1/ --destination=/tmp
