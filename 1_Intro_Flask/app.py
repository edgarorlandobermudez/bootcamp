from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    username = "Invitado"
    return render_template('index.html', username=username)

@app.route('/about')
def about():
    return 'Sobre nosotros'

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('profile.html', username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

if __name__ == '__main__':
    app.run(debug=True)
