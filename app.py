from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(_name_, template_folder="templates")
socketio = SocketIO(app, cors_allowed_origins="*")

# Flask route to serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

# Handle word sent from frontend
@socketio.on('send_word')
def handle_message(word):
    print(f"Received word from frontend: {word}")
    # Emit the word to all connected clients (including Android app)
    socketio.emit('receive_word', word)

# Run Flask server with Socket.IO
if _name_ == "_main_":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
