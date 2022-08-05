from skimage import io, filters
import numpy as np

path = "C:\\grmn\\prj\\avtn\\git\\dev\\gide_repos\\GIDE_SGX530_ON_GI275\\src\\sln\\nonvol\\emmc0_bk6\\utf_results\\act\\opengl_s023.bmp"
path_y_flip = "C:\\grmn\\prj\\avtn\\git\\dev\\gide_repos\\GIDE_SGX530_ON_GI275\\src\\sln\\nonvol\\emmc0_bk6\\utf_results\\act\\opengl_s023_y_flip.bmp"
image = io.imread(path)
(n_R, n_C, n_E) = image.shape
image_y_flip = np.empty((n_R, n_C, n_E), dtype='uint8')
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
