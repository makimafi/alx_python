from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alx_flask_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Route for adding and retrieving users
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        try:
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash("User added successfully!")
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding user: {str(e)}")

    return render_template('add_user.html')

# Route for displaying all users
@app.route('/users')
def show_users():
    try:
        users = User.query.all()
        return render_template('users.html', users=users)
    except Exception as e:
        flash(f"Error retrieving users: {str(e)}")
        return redirect('/add_user')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
