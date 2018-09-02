from flask import Flask, render_template
import pandas as pd
import numpy as np
import os

tree_folder = os.path.join('static', 'tree')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = tree_folder


@app.route('/index')
def hello():
    df = pd.read_csv('MOCK_DATA.csv')
    head = df.head(10)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'tree.png')
    return render_template('index.html', title='Home', data=head.to_html(), user_image = full_filename)

@app.route('/data_analysis')
def data_analysis():
	x = pd.DataFrame(np.random.randn(5, 6), columns=list('ABCDEF'))
	return render_template("home.html",  data=x.to_html())



if __name__ == '__main__':
    app.run(port=1234, debug=True)