"""
Task 2: Edge AI Prototype
Team Member: Edge AI Specialist
This script creates a lightweight image classification model, converts it to TensorFlow Lite, and simulates inference for recyclable item recognition.
"""
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models

# 1. Create simple CNN model
model = models.Sequential([
    layers.Conv2D(16, (3,3), activation='relu', input_shape=(64, 64, 3)),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(32, activation='relu'),
    layers.Dense(3, activation='softmax')  # 3 classes: paper, plastic, glass
])

# 2. Convert to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model
with open('recyclable_model.tflite', 'wb') as f:
    f.write(tflite_model)

# 3. Test inference (simulated)
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

# Mock input
def test_inference():
    input_data = np.random.rand(1,64,64,3).astype(np.float32)
    interpreter.set_tensor(interpreter.get_input_details()[0]['index'], input_data)
    interpreter.invoke()
    output = interpreter.get_tensor(interpreter.get_output_details()[0]['index'])
    print(f"Predicted class probabilities: {output}")

if __name__ == "__main__":
    test_inference() 