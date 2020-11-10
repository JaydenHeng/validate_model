from tflite_prediction import evaluate_tflite

model_path = 'Models/'
label_path = 'Models/'
dataset_path = 'Prediction_set/'
log_path = 'Prediction_log/'
case = "Positive/"
#evaluate_tflite('model_v12', 'prediction_set_should_match')
#evaluate_tflite('conti_model_23', 'prediction_set_should_match')

evaluate_tflite(model_path + 'model_v2', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v3', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v4', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v5', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v6', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v7', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v8', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v9', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v10', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v11', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v12', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v13', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v14', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v15', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v16', model_path + 'labels.txt', dataset_path + case, log_path + case)

case = "Negative/"

evaluate_tflite(model_path + 'model_v2', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v3', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v4', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v5', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v6', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v7', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v8', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v9', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v10', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v11', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v12', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v13', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v14', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v15', model_path + 'labels.txt', dataset_path + case, log_path + case)
evaluate_tflite(model_path + 'model_v16', model_path + 'labels.txt', dataset_path + case, log_path + case)
