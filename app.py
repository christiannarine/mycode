from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/screenshots/<filename>')
def get_screenshot(filename):
    screenshot_path = os.path.join('screenshots', filename)
    return send_file(screenshot_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

Christians-MacBook-Pro:~ christiannarine$ 
