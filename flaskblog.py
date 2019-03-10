from flask import Flask, render_template
app = Flask(__name__)

posts = [{
    'author': 'Leslie Alldridge',
    'title': 'Blog 1',
    'content': 'content is here',
    'date_posted': 'April 20, 2019'
}, {
    'author': 'Leslie Alldridge',
    'title': 'Blog 2',
    'content': 'content is here2',
    'date_posted': 'April 22, 2019'
}]


@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
