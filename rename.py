import os, string

location = "/home/hypuh/Documents/The Wire Season 1"
for root, dirs, files in os.walk(location):
	total = 0
	for filename in files:
		if '.mkv' in filename or '.srt' in filename:
			currentFile = []
			currentFile.append(filename)
			strcurfile = str(currentFile)
			ss = strcurfile.translate({ord(c): None for c in string.whitespace}).split()
			s = ','
			s = s.join(ss)
			titles = s[15:]
			if '[' in filename:
				epnum = filename.split()
				epsplit = epnum[2].split('x')
				season = str(epsplit[0])
				episode = str(epsplit[1])
				title = str(epnum[3])
				newseason = season.translate({ord('['): None})
				newepisode = episode.translate({ord(']'): None})
				newtitle = titles.translate({ord(']'): None})
				newname = 'The Wire ' + 's' + '0' + newseason + 'e' + newepisode + ' ' + newtitle
				path = os.path.join(location, filename)
				os.rename(filename, newname)
				continue
		else:
			path = os.path.join(location, filename) 
			os.remove(path)
			total += 1
			print("File Deleted:   " + filename)
			continue


				# Directory 
				#directory = "The Wire Season 01" 
				# Parent Directory path 
				#parent_dir = os.getcwd()
				# Path 
				#path = os.path.join(parent_dir, directory) 
				# Create the directory 
				#os.mkdir(path) 
				#print("Directory '% s' created" % directory) 
				#os.rename(location, filename)

print("Total of: " + str(total) + " files deleted")
