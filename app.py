from flask import Flask, render_template, request
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

try:
    model = load_model('models/assembly_classifier_model_1.h5')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

try:
    encoder_classes = np.load('encoders/encoder_classes.npy', allow_pickle=True)
    encoder = LabelEncoder()
    encoder.classes_ = encoder_classes
except Exception as e:
    print(f"Error loading encoder: {e}")
    encoder = None

snippet_labels = [
    "ari_snippet", "if_ari_snippet", "for_ari_snippet", "if_if_ari_snippet",
    "if_for_ari_snippet", "for_if_ari_snippet", "for_for_ari_snippet"
]

def predictor(new_code):
    """Predicts the snippet type based on input tokens."""
    if encoder is None or model is None:
        return "Model/Encoder Error", -1

    known_tokens = [token for token in new_code if token in encoder.classes_]
    if not known_tokens:
        return "Unknown Token Error", -1

    try:
        encoded_new_code = encoder.transform(known_tokens).tolist()
        max_length = 16
        padded_new_code = pad_sequences([encoded_new_code], padding='post', maxlen=max_length)
        predicted_snippet = model.predict(padded_new_code)
        predicted_class = np.argmax(predicted_snippet)
        return snippet_labels[predicted_class], predicted_class
    except Exception as e:
        print(f"Prediction Error: {e}")
        return "Prediction Error", -1

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_label = None
    predicted_class = None

    if request.method == 'POST':
        new_code = request.form['code_snippet'].split(',')
        predicted_label, predicted_class = predictor(new_code)

    return render_template('index.html', predicted_label=predicted_label, predicted_class=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
