from flask import flask

app = Flask(__name__)

# TODO: Need to deal with passing the lot currently selected in and out of the various routes, maybe use a session?

@app.route('/', methods=['GET', 'POST'])
def index():
# This should return the index page, from which a lot can be selected and loaded into the session cookie
    if request.method='POST':
        # Load the lot id into the session
        return redirect('/')

    else:
        return render_template('index.html')


@app.route('/new_lot', methods=['GET', 'POST'])
def new_lot():
    if request.method='POST':
    # If here by POST (form submittal), enter the form data and redirect to a current_lot page with the new lot details
        return redirect('/current_lot')

    else:
    # If here by GET (start new batch button), present the blank form for starting a new batch
        return render_template('new_lot.html')


@app.route('/finished_lot', methods=['GET', 'POST'])
def finished_lot():
    if request.method='POST':
    # If arriving via POST, input the data and redirect via GET
        return redirect('/finished_lot')


    else:
    # If arriving via GET, just show the dashboard with the form
        return render_template('finished_lot.html')



@app.route('/current_lot', methods=['GET', 'POST'])
def current_lot():
    if request.method='POST':
    # If arriving via POST, input the info from the submitted form and come back via GET
        return redirect('/current_lot')


    else:
    # If arriving via GET, render the page
        return render_template('current_lot.html')

    