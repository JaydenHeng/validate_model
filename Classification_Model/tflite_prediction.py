import tensorflow as tf
import numpy as np
import glob
import argparse
import pathlib
from os import path
from matplotlib import pyplot as plt
from PIL import Image
from image_processing import rotate_image
from xml_fun import create_xml

def output_to_csv(filename, model_name, data):
	# Open file in append mode
    with open(filename, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow([model_name, data])


def execute_tflite(image_array, interpreter, input_index, output_index):
	input_image = np.array(image_array, dtype=np.float32)

	interpreter.set_tensor(input_index, input_image)
	interpreter.invoke()

	output_data = interpreter.get_tensor(output_index)
	results = np.squeeze(output_data)

	top_k = results.argsort()[-6:][::-1] #Return sorted index

	return top_k, results

def use_multi_angle_evaluation(image, top_k, results, interpreter, input_index, output_index):

	if(top_k[0] == 0 and results[top_k[0]] < 0.95): #If top element is conti_band and precision < 95%
		image_data = np.array([rotate_image(image,90)])
		top_k_rot90, results_rot90 = execute_tflite(image_data, interpreter, input_index, output_index)

		if(top_k_rot90[0] == 0 and results_rot90[top_k_rot90[0]] >= 0.95):
			top_k = top_k_rot90
			results = results_rot90

		if(top_k_rot90[0] == 0 and results_rot90[top_k_rot90[0]] < 0.95): #If top element is conti_band and precision < 90%
			image_data = np.array([rotate_image(image,180)])
			top_k_rot180, results_rot180 = execute_tflite(image_data, interpreter, input_index, output_index)

			if(top_k_rot180[0] == 0 and results_rot180[top_k_rot180[0]] >= 0.95):
				top_k = top_k_rot180
				results = results_rot180

			if(top_k_rot180[0] == 0 and results_rot180[top_k_rot180[0]] < 0.95): #If top element is conti_band and precision < 90%
				image_data = np.array([rotate_image(image,270)])
				top_k_rot270, results_rot270 = execute_tflite(image_data, interpreter, input_index, output_index)

				if(top_k_rot270[0] == 0 and results_rot270[top_k_rot270[0]] >= 0.95):
					top_k = top_k_rot270
					results = results_rot270

	return top_k, results


def evaluate_tflite(model_path, label_path, dataset_path, log_path):
	interpreter = tf.lite.Interpreter(model_path + '.tflite')
	interpreter.allocate_tensors()

	input_details = interpreter.get_input_details()
	output_details = interpreter.get_output_details()

	label = np.array(open(label_path).read().splitlines())

	results = []
	final_results = []
	match_results = []
	
	match_count = match_95_count = match_95_96_count = match_96_97_count = match_97_98_count = match_98_99_count = match_99_count = 0

	for idx, filename in enumerate(glob.glob(dataset_path + '*.jpg')):
		final_results.append([filename.split('/')[-1],[]])
		image = Image.open(filename)
		image_data = np.array([np.asarray(image)])
		top_k, results = execute_tflite(image_data, interpreter, input_details[0]['index'], output_details[0]['index'])
		#top_k, results = use_multi_angle_evaluation(image, top_k, results, interpreter, input_details[0]['index'], output_details[0]['index'])

		print("---------------" + filename.split('/')[-1] + "---------------")
		for idy, i in enumerate(top_k):
			if idy == 0 and i == 0:
				match_count += 1
				match_results.append(results[i])
				if(results[i] >= 0.95):
					match_95_count += 1

				if(results[i] >= 0.95 and results[i] < 0.96):
					match_95_96_count += 1
				elif(results[i] >= 0.96 and results[i] < 0.97):
					match_96_97_count += 1
				elif(results[i] >= 0.97 and results[i] < 0.98):
					match_97_98_count += 1
				elif(results[i] >= 0.98 and results[i] < 0.99):
					match_98_99_count += 1
				elif(results[i] >= 0.99):
					match_99_count += 1

			final_results[idx][1].append([label[i],results[i]])
			print('{:08.6f}:{}'.format(float(results[i]), label[i]))

	# if(path.exists('prediction_log') == False):
	# 	pathlib.Path('prediction_log').mkdir(parents=True, exist_ok=True)

	with open(log_path + 'results_' + model_path.split('/')[-1] + '.txt', 'w') as filehandle:
		filehandle.writelines("%s\n" % result for result in final_results)
		filehandle.writelines("\n%s%s%s%s\n" % ('Total match case(s): ',match_count,'/', idx + 1))
		filehandle.writelines("%s%s%s%s\n" % ('Total match case(s) with similarity >= 95%: ',match_95_count,'/',match_count))
		filehandle.writelines("%s%s%s%s\n" % ('Total match case(s) with similarity within 95~96% range: ',match_95_96_count,'/',match_95_count))
		filehandle.writelines("%s%s%s%s\n" % ('Total match case(s) with similarity within 96~97% range: ',match_96_97_count,'/',match_95_count))
		filehandle.writelines("%s%s%s%s\n" % ('Total match case(s) with similarity within 97~98% range: ',match_97_98_count,'/',match_95_count))
		filehandle.writelines("%s%s%s%s\n" % ('Total match case(s) with similarity within 98~99% range: ',match_98_99_count,'/',match_95_count))
		filehandle.writelines("%s%s%s%s\n" % ('Total match case(s) with similarity >= 99%: ',match_99_count,'/',match_95_count))
		if(match_results.__len__() > 0):
			filehandle.writelines("%s%s\n" % ('25th Percentile: ', np.percentile(np.asarray(match_results), 25)))
			filehandle.writelines("%s%s\n" % ('50th Percentile: ', np.percentile(np.asarray(match_results), 50)))
			filehandle.writelines("%s%s\n" % ('75th Percentile: ', np.percentile(np.asarray(match_results), 75)))
		else:
			filehandle.writelines("%s\n" % ('25th Percentile: Unknown'))
			filehandle.writelines("%s\n" % ('50th Percentile: Unknown'))
			filehandle.writelines("%s\n" % ('75th Percentile: Unknown'))

	# percentage = np.arange(0,101,1)
	# percentile = np.linspace(0,100,6001)
	# ax = plt.gca()
	# lines = [
	# 	('linear', None),
	# 	('higher', '--'),
	# 	('lower', '--'),
	# 	('nearest', '--'),
	# 	('midpoint', '--')
	# ]

	# for interpolation, style in lines:
	# 	ax.plot(
	# 		percentile, np.percentile(percentage, percentile, interpolation=interpolation),
	# 		label=interpolation, linestyle=style)
	# ax.set(
	# 	title="xxxx",
	# 	xlabel='Percentile',
	# 	ylabel='Percentage')
	# ax.legend()
	# plt.show()
	create_xml(log_path + 'overall_results.xml', model_path.split('/')[-1], match_count)

