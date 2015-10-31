import pandas as pd
import numpy as np
import os

class Directory(object):
	def __init__(self, directory_tree):
		self.directory_tree = directory_tree
		self.load_files_as_df()

	def load_files_as_df(self):
		file_paths = {}

		for root, dirs, files in os.walk(self.directory_tree, onerror=True):
			for file in files:
				if file != '.DS_Store': # if the file is not titled ".DS_Store"...
					file_path = os.path.join(root, file) # creates the file path
					file_paths[str(file)] = File(file_path) # creates a File object for each file path
		self.files = pd.DataFrame.from_dict(file_paths, orient='index') # a DataFrame using file_paths
		self.files.columns = ['File']
		self.expand_files_df()

	def expand_files_df(self):
		paths = []
		formats = []
		for file_object in self.files['File']:
			paths.append(file_object.path)
			formats.append(file_object.format)

		new_data = list(zip(paths,formats))
		extension = pd.DataFrame(new_data, index=self.files.index, columns=['.path', '.format'])
		self.files = pd.concat([self.files, extension], axis=1)


	def apply(self, macro_columns, micro_columns, macro_rows, micro_rows, func):

		print(self.files.columns[0])



class File(object):
	def __init__(self, path):
		self.path = path
		self.format = self.find_format()


	def find_format(self):
		char_num = -1
		ext = ""
		while self.path[char_num] != '.':
			char_num -= 1
		ext = self.path[char_num:]
		return ext



#class All(object):



#class Data_Frame(object):













