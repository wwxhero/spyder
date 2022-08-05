from skimage import io, filters
import numpy as np
import os
from pathlib import Path

delimeter = '\\'
file_type = '.bmp'
path_dir = "C:\\grmn\\prj\\avtn\\git\\dev\\gide_repos\\GIDE_SGX530_ON_GI275\\src\\sln\\nonvol\\emmc0_bk6\\utf_results\\act"
path_dir_y_flip = path_dir + delimeter + "y_flip"
Path(path_dir_y_flip).mkdir(parents=True, exist_ok=True)

def ls_dir(path, filter):
	files = []
	for filename in os.scandir(path):
		if filename.is_file():
			(name, ext) = os.path.splitext(filename.name)
			files.append(name)
	return files

# get the list of files matching pattern *.jpg
files = ls_dir(path_dir, filter='*'+file_type)

for file in files:
	path = path_dir + delimeter + file + file_type
	path_y_flip = path_dir_y_flip + delimeter + file + file_type
	#print("src:" + path)
	#print("dst:" + path_y_flip)
	image = io.imread(path)
	(n_R, n_C, n_E) = image.shape
	image_y_flip = np.empty((n_R, n_C, n_E), dtype='uint8') #revise the hardcode data type
	# for all i_r, i_r':
	#		(i_r + i_r' = n_R-1) -> image(i_r, _, _) = image(i_r', _, _)
	for i_r in range(0, n_R):
		i_r_prime = n_R-1-i_r
		image_y_flip[i_r_prime] = image[i_r]
	# io.imshow(image)
	# io.show()
	# io.imshow(image_y_flip)
	# io.show()
	io.imsave(path_y_flip, image_y_flip)


