from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple route for testing
@app.route('/')
def home():
    return "AI Chatbot Demo is running!"

# Mock endpoint simulating Instagram DM webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    user = data.get("user", "Unknown User")
    message = data.get("message", "")
    
    # Simple AI-like response logic
    if "hello" in message.lower():
        reply = f"Hi {user}! How can I help you today?"
    elif "book" in message.lower():
        reply = f"Got it {user}, let's schedule your call! Please provide your email."
    else:
        reply = f"Thanks {user}, I received your message: '{message}'"
    
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
