from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_URL = 'https://openrouter.ai/api/v1/chat/completions'
API_KEY = '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'
MODEL = 'qwen/qwen3-coder:free'

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    if request.method == 'POST':
        user_input = request.form['user_input']
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            response_text = result['choices'][0]['message']['content']
        else:
            response_text = f"Xatolik: {response.status_code}"
    return render_template('index.html', response=response_text)

if __name__ == '__main__':
    app.run(debug=True)
