from text_to_speech.exception import TTSException
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from text_to_speech.components.get_accent import get_accent_tld, get_accent_message
import sys
import os
from text_to_speech.components.textTospeech import TTSapplication

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    try: 
        accent_list = get_accent_message()
        return render_template('index.html', accent_list=accent_list)
    except Exception as e:
        raise TTSException(e, sys)

@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predict():
    try:
        if request.method == 'POST':
            # Validate request data
            if not request.json:
                return {"error": "No JSON data provided"}, 400
            
            if 'data' not in request.json or 'accent' not in request.json:
                return {"error": "Missing 'data' or 'accent' in request"}, 400
                
            data = request.json['data']
            accent_input = request.json['accent']
            
            if not data or not accent_input:
                return {"error": "Empty 'data' or 'accent' provided"}, 400
                
            accent = get_accent_tld(accent_input)
            if not accent:
                return {"error": f"Invalid accent: {accent_input}"}, 400
                
            print(f"Processing TTS for accent: {accent}")
            result = TTSapplication().text2speech(data, accent)
            return {"data": result.decode("utf-8")}
        else:
            # Handle GET requests
            return {"message": "Use POST method with JSON data containing 'data' and 'accent' fields"}, 200
    except Exception as e:
        print(f"Error in predict route: {str(e)}")
        return {"error": "Internal server error occurred"}, 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)