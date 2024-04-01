from flask import Flask, request
import os

app = Flask(__name__)

flag_file = ""
for file in os.listdir('/'):
    if file.startswith('flag'):
        flag_file = f"/{file}"
        break

f = open(flag_file, "r")
flag = f.read()


@app.route('/')
def index():
    html = """
    <h1>Flag where</h1>
    <div class="tenor-gif-embed" data-postid="15808900" data-share-method="host" data-aspect-ratio="1" data-width="25%"><a href="https://tenor.com/view/huh-what-where-why-how-gif-15808900">Huh What GIF</a>from <a href="https://tenor.com/search/huh-gifs">Huh GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
    """
    return html

@app.route('/oopsie')
def read_file():
    file_name = request.args.get('file_name')
    f = open(file_name, 'r')
    content = f.read()
    return content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
