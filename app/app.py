<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Customer App Running"

@app.route('/health')
def health():
    return {"status":"UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Customer App Running"

@app.route('/health')
def health():
    return {"status":"UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 82c0ee0aa98f2cd0823946b1a8e0b3f1dd295783
