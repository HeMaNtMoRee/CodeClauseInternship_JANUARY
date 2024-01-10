from flask import Flask, render_template, request, redirect
import hashlib

app = Flask(__name__)

url_mapping = {}


def generate_short_url(url):
    hash_object = hashlib.md5(url.encode())
    return hash_object.hexdigest()[:8]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form.get('original_url')

    if original_url:
        short_code = generate_short_url(original_url)
        url_mapping[short_code] = original_url
        short_url = request.url_root + short_code
        return render_template('index.html', short_url=short_url)

    return redirect('/')


@app.route('/<short_code>')
def redirect_to_original(short_code):
    original_url = url_mapping.get(short_code)
    if original_url:
        return redirect(original_url)
    else:
        return 'Short URL not found', 404


if __name__ == '__main__':
    app.run(debug=True)
