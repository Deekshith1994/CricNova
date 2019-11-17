from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():

    #Hard coded data, gotta link it to DB instead.
    posts = [
        {
            'id': '01',
            'title': 'SRH vs RCB',
            'subtitle': 'Warner ton helps SRH stay on top',
            'author': 'Deekshith',
            'date_posted': '12/04/2020',
            'content': 'Warner ton helps SRH stay on top'
        },
        {
            'id': '02',
            'title': 'KKR vs DC',
            'subtitle':  'Russel injured again',
            'author': 'Saith',
            'date_posted': '11/04/2020',
            'content': 'Russel injured again'
        },
        {
            'id': '03',
            'title': 'MI vd CSK',
            'subtitle': 'Age not just a number?',
            'author': 'Prithvi',
            'date_posted': '10/04/2020',
            'content': 'Age not just a number?'
        },
        {
            'id': '04',
            'title': 'DC vs KKR',
            'subtitle': 'Glimpse of Pant we want',
            'author': 'Himanshu',
            'date_posted': '09/04/2020',
            'content': 'Glimpse of Pant we want'
        },
        {
            'id': '05',
            'title': 'KXIP vs RR',
            'subtitle': 'Gayle fails again',
            'author': 'Anirudh',
            'date_posted': '8/04/2020',
            'content': 'Gayle fails again'
        }
    ]
    posts = posts
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    post = {
            'id': '05',
            'title': 'Match',
            'subtitle': 'Match Number',
            'author': 'Deekshith',
            'date_posted': '8/04/2020',
            'content': "Here we write the content of the match"
        }

    return render_template('post.html', post=post)


@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
