from flask import Flask

# Flask app initialize करें
app = Flask(__name__)

# 🏠 Home route
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# 📄 About route
@app.route('/about')
def about():
    return "This is the About Page."

# 👤 User route with dynamic parameter
@app.route('/user/<username>')
def show_user(username):
    return f"Hello, {username}!"

# 🔢 Route with integer parameter
@app.route('/square/<int:number>')
def square(number):
    return f"The square of {number} is {number ** 2}"

# 🧪 Custom method route
@app.route('/submit', methods=['POST'])
def submit():
    return "Form submitted!"

# 🚀 Run the app
if __name__ == '__main__':
    app.run(debug=True)
