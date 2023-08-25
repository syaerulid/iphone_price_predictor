from flask import Flask, request, jsonify, render_template
from model import model  # Make sure the model is properly imported

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('iphone_frontend.html', result="")

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form[f'feature{i}']) for i in range(1, 7)]
    
    # Make predictions using the loaded regression model
    prediction = model.predict([features])[0]
    
    return render_template('iphone_frontend.html', result=f"The predicted output is Rp: {prediction:.2f}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
