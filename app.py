# from flask import Flask, render_template
# from flask_minify import Minify

# app = Flask(__name__)

# # Enable minification
# Minify(app=app, html=True, js=True, cssless=True)
#test


from flask import Flask, render_template, request

app = Flask(__name__)

@app.context_processor
def inject_styles():
    is_homepage = request.path == '/'
    # You can add more context variables as needed
    return dict(is_homepage=is_homepage)

@app.route('/')
def home():
    return render_template('index.html', is_index=True)

@app.route('/locations')
def locations():
    return render_template('locations.html', is_index=False)

@app.route('/menu')
def menu():
    return render_template('menu.html', is_index=False)

@app.route('/contact')
def contact():
    return render_template('contact.html', is_index=False)

@app.route('/about')
def about():
    return render_template('about.html', is_index=False)


if __name__ == '__main__':
    app.run(debug=True)


i




