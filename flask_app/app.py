from flask import Flask, request, jsonify, render_template
from model import get_ai_response
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_message = data.get('message')
    model = data.get('model')

    if not user_message or not model:
        return jsonify({"error": "Missing user message or model selection"}), 400

    system_prompt = "You are an AI assistant helping with customer inquiries. Provide a helpful and concise response."
    start_time = time.time()

    print("user_message", user_message)
    print("model", model)
    
    try:
        if model == "gemma":
            response = get_ai_response(system_prompt, user_message)
        else:
            return jsonify({"error": "Invalid model selection"}), 400
        print(response)
        response['duration'] = time.time() - start_time
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)