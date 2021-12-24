

import sys, os
from pathlib import Path
from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer


FLATPAGES_EXTENSION = '.md'
DEBUG=True

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

FLATPAGES_AUTO_RELOAD = DEBUG

app.config['FREEZER_DESTINATION'] = './docs/'
freezer = Freezer(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(path)
    print(f"Page title -- {page['title']}")
    return render_template('page.html', page=page)

@freezer.register_generator
def pagelist():
    for page in pages:
        # the first parameter is the endpoint single quoted
        yield url_for('page', path=page.path)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=5001)


