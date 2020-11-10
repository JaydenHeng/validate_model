import matplotlib.pyplot as plt
import numpy as np
from xml_fun import read_xml

def single_plot(log_path, plot_label):
	#Prepare data
	model_name, match_value = read_xml(log_path)

	# Plot the data
	plt.plot(model_name, match_value, label=plot_label)
	plt.xticks(rotation='vertical') # Rotate x-axis ticks vertically
	plt.xlabel('Model name') # Define x-label
	plt.ylabel('Number of match cases') # Define y-label
	plt.gcf().subplots_adjust(bottom=0.15) # Prevent x-axis label from cropped away
	plt.legend() # Add a legend
	plt.show() # Show the plot

def comparison_plot(log_path_1, log_path_2, plot_label_1, plot_label_2):
	model_name_1, match_value_1 = read_xml(log_path_1)
	model_name_2, match_value_2 = read_xml(log_path_2)

	# Plot the data
	plt.plot(model_name_1, match_value_1, label=plot_label_1)
	plt.plot(model_name_2, match_value_2, label=plot_label_2)
	plt.xticks(rotation='vertical') # Rotate x-axis ticks vertically
	plt.xlabel('Model name') # Define x-label
	plt.ylabel('Number of match cases') # Define y-label
	plt.gcf().subplots_adjust(bottom=0.15) # Prevent x-axis label from cropped away
	plt.legend() # Add a legend
	plt.show() # Show the plot
