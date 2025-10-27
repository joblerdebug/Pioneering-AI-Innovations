# Convert Keras model to TensorFlow Lite
import tensorflow as tf
import numpy as np

def convert_to_tflite():
    # Load the trained model
    model = tf.keras.models.load_model('recyclable_model.h5')
    
    # Convert to TensorFlow Lite
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    
    # Apply optimization for smaller size and faster execution
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    
    # Convert the model
    tflite_model = converter.convert()
    
    # Save the TensorFlow Lite model
    with open('recyclable_model.tflite', 'wb') as f:
        f.write(tflite_model)
    
    print("Model converted to TensorFlow Lite successfully!")
    print(f"Model size: {len(tflite_model)} bytes")

def test_tflite_model():
    # Load TFLite model and allocate tensors
    interpreter = tf.lite.Interpreter(model_path='recyclable_model.tflite')
    interpreter.allocate_tensors()
    
    # Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    print("Input details:", input_details)
    print("Output details:", output_details)
    
    # Test with sample data
    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    
    interpreter.invoke()
    
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print(f"Output predictions: {output_data}")
    
    return interpreter

if __name__ == "__main__":
    convert_to_tflite()
    test_tflite_model()
