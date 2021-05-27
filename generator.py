"""
A Chinese word dataset generator

@author Hao-Ying Cheng

@description create the chinese datasets that's image format.
			 An entry point.
			 Reference by:
			 	Python 生成漢字字型檔文字, 以及轉換為文字圖片,
			 	https://www.itread01.com/content/1548359660.html

@Date 2021-05-27	

"""
 
# import modules
import os
import pygame

def read_files(filepath) -> list:
	"""
	read the files which contains chinese in text format.

	Args:
		filepath:
			file path for reading
	Returns:
		chinese dataset that's list type
	"""
	dataset = []
	with open(filepath, 'r') as f:
		words = f.readlines()
		# remove '\n' 
		for word in words:
			dataset.append(word.replace('\n', ""))
	return dataset


def encoding(dataset, encoding='utf-8') -> list:
	"""
	encode the chinese text

	Args:
		dataset:
			list of chinese text
		encoding:
			set encoded format
	Returns:
		Encoded chinese text that's list type
	"""
	return [data.encode(encoding) for data in dataset]

def generate_dataset(chi_dataset, IsDecoded=True, decoding='utf-8', text_format='wqy-zenhei.ttc', size=128):
	"""
	generate chinese in image format

	Args:
		chi_dataset:
			list of chinese text
		decoded:
			@default True 
			whether chinese text is decoded or not
			In other words, it is unicode or others (e.g., utf-8, ASCII)
		text_format:
			@default 'wqy-zenhei.ttc'
			select text format you want
		size:
			@default 128
			set the size of output images (e.g., 128x128) 
	"""
	# the directory of chinese images
	chinese_dir = "chinese";
	# if no chinese directory, create it
	if not os.path.exists(chinese_dir):
		os.mkdir(chinese_dir)
	
	# whether chinese is decoded or not
	pygame.init()
	if decoded:
		# output the chinese text image
		for chi in chi_dataset:
			# set chinese text format
			font = pygame.font.Font(text_format, size)
			text = font.render(chi, True, (0, 0, 0), (255, 255, 255))
			# save images
			pygame.image.save(text, os.path.join(chinese_dir, chi+".png"))
	else:
		# decode and output the chinese text image
		for unichi in chi_dataset:
			# decode encoded chinese (e.g., encoded by utf-8)
			word = unichi.decode(decoding)
			# set chinese text format
			font = pygame.font.Font(text_format, size)
			text = font.render(word, True, (0, 0, 0), (255, 255, 255))
			# save images
			pygame.image.save(text, os.path.join(chinese_dir, word+".png"))




# entry point
if __name__ == '__main__':
	# read the chinese dataset in text format
	chi_datas = read_files('./training_data_dic.txt')
	# simulate the encoded chinese dataset
	encoded_chi = encoding(chi_datas)
	#
	generate_dataset(chi_datas)
	#generate_dataset(encoded_chi, False)