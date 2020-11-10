from plot import *

positive_log_path = 'Prediction_log/Positive/overall_results.xml'
negative_log_path = 'Prediction_log/Negative/overall_results.xml'

#single_plot(positive_log_path, 'Positive')
comparison_plot(positive_log_path, negative_log_path, 'Postive', 'Negative')
