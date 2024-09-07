from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required to encrypt session data

# Route for the home page where the user logs in
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        # Store the username in the session
        session['username'] = username
        return redirect(url_for('dashboard'))
    return render_template('index.html')

# Route for the dashboard that displays the user-specific data
@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if 'username' in session:
        username = session['username']
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('index'))

# Route to log out and clear the session
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
