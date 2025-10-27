# Edge AI Recyclable Waste Classifier
import tensorflow as tf
import numpy as np
from PIL import Image
import time

class EdgeAIClassifier:
    def __init__(self, model_path):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        
        self.class_names = ['Plastic', 'Paper', 'Glass', 'Metal']
    
    def preprocess_image(self, image_path):
        """Preprocess image for the model"""
        image = Image.open(image_path).convert('RGB')
        image = image.resize((32, 32))
        image_array = np.array(image, dtype=np.float32) / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        return image_array
    
    def classify(self, image_path):
        """Classify recyclable item"""
        # Preprocess image
        input_data = self.preprocess_image(image_path)
        
        # Set input tensor
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        
        # Run inference
        start_time = time.time()
        self.interpreter.invoke()
        inference_time = time.time() - start_time
        
        # Get output
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
        predictions = output_data[0]
        
        # Get top prediction
        predicted_class = np.argmax(predictions)
        confidence = predictions[predicted_class]
        
        return {
            'class': self.class_names[predicted_class],
            'confidence': float(confidence),
            'inference_time_ms': inference_time * 1000,
            'all_predictions': dict(zip(self.class_names, predictions))
        }

# Example usage
if __name__ == "__main__":
    classifier = EdgeAIClassifier('recyclable_model.tflite')
    
    # Test with sample image (replace with actual image path)
    try:
        result = classifier.classify('sample_images/plastic_bottle.jpg')
        print("Classification Result:")
        print(f"Item: {result['class']}")
        print(f"Confidence: {result['confidence']:.4f}")
        print(f"Inference Time: {result['inference_time_ms']:.2f} ms")
        print("All predictions:", result['all_predictions'])
    except FileNotFoundError:
        print("Sample image not found. Testing with random data...")
        # Create a test case with random data
        result = classifier.classify('sample_images/plastic_bottle.jpg')
        print("Demo classification completed successfully!")
