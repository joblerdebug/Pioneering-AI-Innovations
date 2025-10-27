# Smart Agriculture - Crop Yield Prediction Model
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

class SmartAgriculturePredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.is_trained = False
        
    def generate_sample_data(self, n_samples=1000):
        """Generate synthetic agricultural data for demonstration"""
        np.random.seed(42)
        
        data = {
            'soil_moisture': np.random.uniform(10, 60, n_samples),
            'temperature': np.random.uniform(15, 35, n_samples),
            'humidity': np.random.uniform(30, 90, n_samples),
            'nitrogen': np.random.uniform(10, 100, n_samples),
            'phosphorus': np.random.uniform(5, 50, n_samples),
            'potassium': np.random.uniform(20, 80, n_samples),
            'ph_level': np.random.uniform(5.0, 7.5, n_samples)
        }
        
        # Simulate crop yield based on environmental factors
        data['crop_yield'] = (
            data['soil_moisture'] * 0.3 +
            data['temperature'] * 0.2 +
            data['nitrogen'] * 0.15 +
            data['phosphorus'] * 0.15 +
            data['potassium'] * 0.1 +
            data['ph_level'] * 5 +
            np.random.normal(0, 10, n_samples)
        )
        
        return pd.DataFrame(data)
    
    def train_model(self, df):
        """Train the crop yield prediction model"""
        X = df.drop('crop_yield', axis=1)
        y = df['crop_yield']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        self.model.fit(X_train, y_train)
        self.is_trained = True
        
        # Evaluate model
        y_pred = self.model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"Model Training Complete!")
        print(f"Mean Absolute Error: {mae:.2f}")
        print(f"R² Score: {r2:.4f}")
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'feature': X.columns,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("\nFeature Importance:")
        print(feature_importance)
        
        return mae, r2
    
    def predict_yield(self, sensor_data):
        """Predict crop yield based on sensor data"""
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions")
        
        prediction = self.model.predict([sensor_data])[0]
        return prediction
    
    def plot_feature_importance(self):
        """Plot feature importance"""
        if not self.is_trained:
            raise ValueError("Model must be trained first")
        
        importance = self.model.feature_importances_
        features = ['Soil Moisture', 'Temperature', 'Humidity', 
                   'Nitrogen', 'Phosphorus', 'Potassium', 'pH Level']
        
        plt.figure(figsize=(10, 6))
        plt.barh(features, importance)
        plt.xlabel('Feature Importance')
        plt.title('Crop Yield Prediction - Feature Importance')
        plt.tight_layout()
        plt.savefig('feature_importance.png')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Initialize predictor
    predictor = SmartAgriculturePredictor()
    
    # Generate and train on sample data
    df = predictor.generate_sample_data()
    mae, r2 = predictor.train_model(df)
    
    # Make a prediction
    sample_sensor_data = [35, 25, 65, 45, 25, 50, 6.5]  # Example values
    predicted_yield = predictor.predict_yield(sample_sensor_data)
    print(f"\nPredicted Crop Yield: {predicted_yield:.2f} kg/ha")
    
    # Plot feature importance
    predictor.plot_feature_importance()
