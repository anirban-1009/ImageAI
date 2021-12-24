from imageai.Classification import ImageClassification
import os

execution_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "resnet50_imagenet_tf.2.0.h5"))
prediction.loadModel()

predicitions, probabilities = prediction.classifyImage(os.path.join(execution_path, "1.jpg"), result_count=5)
for eachPrediction, eachProbability in zip(predicitions, probabilities):
    print(eachPrediction, " : ", eachProbability)