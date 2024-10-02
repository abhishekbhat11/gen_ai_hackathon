from flask import Flask, request, jsonify, render_template
from langchain_google_genai import ChatGoogleGenerativeAI
# from pyngrok import ngrok
import markdown

app = Flask(__name__)

# Initialize Gemini API
gemini = ChatGoogleGenerativeAI(model="gemini-pro", api_key='AIzaSyAX0b5iyfnfPdXn8TYl9_9bizjcdK7PsPo')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    messages = [("user", user_message)]
    response = gemini.invoke(messages)
    
    # Convert markdown response to HTML
    html_response = markdown.markdown(response.content)
    
    return jsonify({'response': html_response})

if __name__ == '__main__':
    # public_url = ngrok.connect(5000)
    # print(f' * Public URL: {public_url}')
    app.run(debug=True)