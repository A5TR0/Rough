import os
import pandas as pd



class Directory:

	def __init__(self, directory_tree):
		self.directory_tree = directory_tree


	def split(self): # returns a dict containing all the file paths in the given folder/directory tree
		file_paths = {}

		for root, dirs, files in os.walk(self.directory_tree, onerror=True):
			for file in files:
				if file != '.DS_Store': # if the file is not titled ".DS_Store"...
					file_path = os.path.join(root, file) # creates the file path
					file_paths[str(file)] = Original_File(file_path) # creates an Original File object for each file path

		return file_paths



class Original_File(object):

	def __init__(self, file_path):
		self.df = pd.read_csv(file_path) # the original file
		self.name = file_path # path to get to the file


	def data_count(self, col_keyword, func):
		match_columns = {}
		for column in self.df:
			if col_keyword.upper() in column.upper():
				fail = 0
				track = {}
				conditions = []
				for element in self.df[column]:
					try:
						if func(element) in track:
							track[func(element)] += 1
						else:
							track[func(element)] = 1
							conditions.append(str(func))
					except:
						fail += 1
				
				conditions.append('fail')
				#import ipdb;ipdb.set_trace()

				keys = list(track.keys())
				map(str, keys)
				#map(lambda k: str(k), keys)
				keys.append('fail')

				track['fail'] = fail
				entire_track = [conditions, keys]


				match_columns[column] = track
		# FIXME this uses the entire_track variable from the last matching column , why??
		compressed = list(zip(*entire_track))
		import ipdb; ipdb.set_trace()
		print(match_columns)
		index = pd.MultiIndex.from_tuples(compressed, names=['condition', 'event'])
		data_counted = pd.DataFrame(match_columns, index=index).fillna(0)
		#data_counted.sort_index(inplace=True)
		return data_counted

	def change_index(self, column):
		self.df.set_index([column], inplace=True)


	def change_column(self, column):
		print(original)



class Parsed_File:

	def __init__(self, result_of_original):
		self.parsed = result_of_original


	def remove_columns(self, columns):
		print(parsed)


	def remove_rows(self, rows):
		print(parsed)



class Filtered_File:

	def __init__(self, result_of_parsed):
		self.filtered = result_of_parsed


	def store_in(self, directory):
		print(filtered)



directory = Directory('/Users/Taro/autodidact_data_science/gentrification_in_sf/acquire')

subfolder = directory.split()
#sub_keys = list(subfolder.keys())

#for key in range(len(sub_keys)):
#for key, value in subfolder.items():
print(subfolder['Map_SF_Pipeline_2015_Q1.csv'].data_count('date', len))
	#print('-------------------------------------------')
















