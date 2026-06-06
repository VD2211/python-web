    # Let's import the Flask
    # from flask import Flask
    # import os # importing operating system module

    # app = Flask(__name__)

    # @app.route('/') # This decorator create the home route
    # def home():
    #     return '<h1>Welcome</h1>'

    # if __name__ == '__main__':
    #     # for the development we use the environ
    #     # To make it work for both production and development

    #     port = int(os.environ.get("PORT", 5000))
    #     app.run(debug=True, host='0.0.0.0', port=port)


# To run the flask application, write python app.py in the main flask application directory.

# After you run python app.py check local host 5000

# let us add additional route. Creating about route

# Let's import the flask
    # from flask import Flask
    # import os # importing operating system module

    # app = Flask(__name__)

    # @app.route('/') # this decorator create the home route

    # def home():
    #     return '<h1>Welcome</h1>'

    # @app.route('/about')
    # def about():
    #     return '<h1>About us</h1>'

    # if __name__ == '__main__':
    #     # for deployment we use the environ
    #     # to amke it work for both production and development
    #     port = int(os.environ.get("PORT", 5000))
    #     app.run(debug=True, host='0.0.0.0', port=port)

# Now, we added the about route in the above code. How about if we want to render an HTML file instead of string?
# It is possible to render HTML file using the function 'render_template'.
# Let us create a folder called templates and create home.html and about.html in the project directory.
# Let us also import the render_template function from flask.

    # from flask import Flask, render_template
    # import os # importing operating system module

    # app = Flask(__name__)

    # @app.route('/') # this decorator create the home route
    # def home():
    #     return render_template('home.html')

    # @app.route('/about')
    # def about():
    #     return render_template('about.html')

    # if __name__ == '__main__':
    #     # for deployment we use the environ
    #     # To make it work for both production and development
    #     port = int(os.environ.get("PORT", 5000))
    #     app.run(debug=True, host='0.0.0.0', port=port)


# As you can see to go to different pages or to navigate we need a navigation.
# Let's add a link to each page or let's create a layout which we use to every page

# Navigation
# <ul>
#   <li><a href="/">Home</a></li>
#   <li><a href="/about">About</a></li>
# </ul>

# Now we can navigate between the pages using the above link.
# Let us create additional page which handle from data.
# You can call it any name, I like to call it post.html

# We can inject data to the HTML files using Jinja2 template engine.

# from flask import Flask, render_template, request, redirect, url_for
# import os # importing operating system module

# app = Flask(__name__)

# @app.route('/') # this decorator create the home route
# def home():
#     techs = ['HTML', 'CSS', 'Flask', 'Python']
#     name = '30 days Of Python Programming'
#     return render_template('home.html', techs=techs, name=name, title='Home')

# @app.route('/about') 
# def about():
#     name = '30 Days Of Python Programming'
#     return render_template('about.html', name=name, title='About Us')

# @app.route('/post')
# def post():
#     name = 'Text Analyzer'
#     return render_template('post.html', name=name, title=name)

# if __name__ == '__main__':
#     # for deployment
#     # To make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)

# Creating a layout

# In the template files, there are lots of repeated codes, we can write a layout and we can remove the repetition.
# Let's create layout.html inside the templates folder.
# After we create the layout we will import every file.

# Serving Static File

# Create a static folder in your project directory.
# Inside the static folder create CSS or styles folder and create a CSS stylesheet.
# We use the url_for module to serve the static file

# Request methods, there are different request methods(GET, POST, PUT, DELETE) are the common request methods which
# allow us to do CRUD(Create, Read, Update, Delete) operation.

# In the post, route we will use GET and POST method alternative depending on the type of the request, check how it looks
# in the code below. The request method is a function to handle request methods and also to access form data. app.py

# Let's import the flask
from flask import Flask, render_template, request, redirect, url_for
import os # importing operating system module

app = Flask(__name__)
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/') # this decorator create the home route
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))
    
if __name__ == '__main__':
    # for deployment
    # to make it work for both production and deployment
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)



