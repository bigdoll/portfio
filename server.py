from flask import Flask, render_template, url_for, request, redirect
from markupsafe import escape
import csv
app = Flask(__name__)  # it means it is the __main__ file


# @app.route('/')
# def my_home():
#     return render_template('index.html')


# @app.route('/index.html')
# def index():
#     return render_template('index.html')


# def my_home():
#     return render_template('index.html')


# @app.route('/work.html')
# def my_work():
#     return render_template('work.html')


# @app.route('/works.html')
# def my_works():
#     return render_template('works.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')

@app.route('/<string:page_name>')
def html_page(page_name=None):
    return render_template(page_name, name=escape(page_name))


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            # print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)
    # return 'form submitted hooorayyy'

# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     # it tries to search inside template folder...you just need to get use to it. #"<p>Hello, Robert!</p>"
#     # grab the ecom.ico from the static folder
#     # print(url_for('static', filename='ecom.ico'))
#     return render_template('index.html', name=escape(username), post_id=escape(post_id))


# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs'


# # @app.route('/favicon.ico')
# # def blog():
# #     return 'These are my thoughts on blogs'


# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'This is my dogs'
