import os
from xml.etree import ElementTree as ET

def prepare_data(root, model_name, match_case):
	result = ET.SubElement(root, 'result')
	model = ET.SubElement(result, 'model')
	match = ET.SubElement(result, 'match')
	model.text = model_name
	match.text = str(match_case)

def create_xml(file_name, model_name, match_case):
	if os.path.exists(file_name):
		tree = ET.parse(file_name)
		root = tree.getroot()
		prepare_data(root, model_name, match_case)
		tree.write(open(file_name, 'wb'))
	else:
		root = ET.Element('root')
		prepare_data(root, model_name, match_case)
		data = ET.tostring(root)
		file = open(file_name, "wb")
		file.write(data)

def grab_data(root):
	model_names = []
	match_cases = []

	for item in root.findall('result'):
		model_names.append(item.find('model').text)
		match_cases.append(int(item.find('match').text))

	return model_names, match_cases
	

def read_xml(file_name):
	tree = ET.parse(file_name)
	root = tree.getroot()

	return grab_data(root)



	