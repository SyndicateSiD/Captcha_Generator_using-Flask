from flask import Flask, render_template, request, jsonify, send_file
from random import randint
from captcha.image import ImageCaptcha
from io import BytesIO
import os

app = Flask(__name__)

# Initialize the ImageCaptcha object
image = ImageCaptcha(width=200, height=100, fonts=[
    'C:/Users/KIIT/Documents/Subjects/Computer/Python/Captcha_Gen/fonts/ChelseaMarketsr.ttf',
    'C:/Users/KIIT/Documents/Subjects/Computer/Python/Captcha_Gen/fonts/DejaVuSanssr.ttf'
])

# Global variable to store the captcha text
captcha_text = ""

def generate_captcha():
    global captcha_text
    random_number = str(randint(100000, 999999))
    captcha_text = random_number
    data = image.generate(random_number)
    image.write(random_number, 'static/out.png')
    return captcha_text

@app.route('/')
def index():
    random_number = generate_captcha()
    return render_template('index.html', captcha=random_number)

@app.route('/verify', methods=['POST'])
def verify():
    global captcha_text
    
    captcha_in = request.json.get('captcha', '').strip()
    
    if captcha_in == captcha_text:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})
    

@app.route('/refresh', methods=['GET'])
def refresh():
    random_number = generate_captcha()
    return send_file('static/out.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
