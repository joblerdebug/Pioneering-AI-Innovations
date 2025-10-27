# Data Flow Diagram Generator for Smart Agriculture System
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_data_flow_diagram():
    fig, ax = plt.subplots(1, 1, figsize=(15, 8))
    
    # Colors
    sensor_color = '#4CAF50'  # Green
    gateway_color = '#2196F3'  # Blue
    cloud_color = '#FF9800'    # Orange
    ai_color = '#9C27B0'       # Purple
    user_color = '#F44336'     # Red
    
    # Positions
    positions = {
        'sensors': [(2, 6), (2, 5), (2, 4), (2, 3)],
        'gateway': (5, 4.5),
        'edge_ai': (8, 4.5),
        'cloud': (11, 6),
        'ai_model': (11, 3),
        'farmer': (14, 4.5)
    }
    
    # Create elements
    # Sensors
    sensor_names = ['Soil Moisture', 'Temperature', 'NPK Sensor', 'Camera']
    for i, (x, y) in enumerate(positions['sensors']):
        ax.add_patch(patches.Rectangle((x, y), 1.5, 0.8, 
                                     facecolor=sensor_color, 
                                     edgecolor='black',
                                     alpha=0.7))
        ax.text(x + 0.75, y + 0.4, sensor_names[i], 
               ha='center', va='center', fontweight='bold')
    
    # Gateway
    ax.add_patch(patches.Rectangle(positions['gateway'], 2, 1.5,
                                 facecolor=gateway_color,
                                 edgecolor='black',
                                 alpha=0.7))
    ax.text(positions['gateway'][0] + 1, positions['gateway'][1] + 0.75,
           'IoT Gateway', ha='center', va='center', fontweight='bold')
    
    # Edge AI
    ax.add_patch(patches.Rectangle(positions['edge_ai'], 2, 1.5,
                                 facecolor=ai_color,
                                 edgecolor='black',
                                 alpha=0.7))
    ax.text(positions['edge_ai'][0] + 1, positions['edge_ai'][1] + 0.75,
           'Edge AI\n(Immediate Control)', ha='center', va='center', 
           fontweight='bold', fontsize=9)
    
    # Cloud
    ax.add_patch(patches.Rectangle(positions['cloud'], 2, 1.5,
                                 facecolor=cloud_color,
                                 edgecolor='black',
                                 alpha=0.7))
    ax.text(positions['cloud'][0] + 1, positions['cloud'][1] + 0.75,
           'Cloud Platform', ha='center', va='center', fontweight='bold')
    
    # AI Model
    ax.add_patch(patches.Rectangle(positions['ai_model'], 2, 1.5,
                                 facecolor=ai_color,
                                 edgecolor='black',
                                 alpha=0.7))
    ax.text(positions['ai_model'][0] + 1, positions['ai_model'][1] + 0.75,
           'LSTM Model\n(Yield Prediction)', ha='center', va='center', 
           fontweight='bold', fontsize=9)
    
    # Farmer
    ax.add_patch(patches.Rectangle(positions['farmer'], 2, 1.5,
                                 facecolor=user_color,
                                 edgecolor='black',
                                 alpha=0.7))
    ax.text(positions['farmer'][0] + 1, positions['farmer'][1] + 0.75,
           'Farmer\nDashboard', ha='center', va='center', fontweight='bold')
    
    # Draw arrows
    arrows = [
        # Sensors to Gateway
        ((3.5, 6.4), (5, 5.5), 'Sensor Data'),
        ((3.5, 5.4), (5, 5.2), ''),
        ((3.5, 4.4), (5, 4.9), ''),
        ((3.5, 3.4), (5, 4.6), ''),
        
        # Gateway to Edge AI
        ((7, 5.25), (8, 5.25), 'Processed Data'),
        
        # Edge AI to Cloud
        ((10, 5.25), (11, 6.5), 'Aggregated Data'),
        
        # Cloud to AI Model
        ((11, 4.5), (11, 4.5), 'Stored Data'),
        
        # AI Model to Farmer
        ((13, 3.75), (14, 4.5), 'Predictions & Insights'),
        
        # Farmer to Gateway (control signals)
        ((14, 3.75), (7, 3.75), 'Control Commands', 'red')
    ]
    
    for start, end, label, color in arrows:
        color = color if color else 'blue'
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color=color, lw=2))
        if label:
            mid_x = (start[0] + end[0]) / 2
            mid_y = (start[1] + end[1]) / 2
            ax.text(mid_x, mid_y, label, ha='center', va='center', 
                   fontsize=8, bbox=dict(boxstyle="round,pad=0.3", 
                                       facecolor='white', alpha=0.8))
    
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Smart Agriculture System - Data Flow Diagram', 
                fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('smart_agriculture_data_flow.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    create_data_flow_diagram()
