# Import necessary modules
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Update a User
@app.route('/update_user/<int:user_id>', methods=['GET','POST'])
def update_user(user_id):
    user = User.query.get(user_id)

    if user is None:
        flash("User not found!")
        return redirect('/')

    if request.method == 'POST':
        # Extract the updated name and email from the form data
        updated_name = request.form['name']
        updated_email = request.form['email']

        # Validate the data: ensure both fields are provided
        if not updated_name or not updated_email:
            flash("Both name and email are required.")
            return redirect(request.url)

        # Use the given user_id to identify and update the corresponding user in the User table
        user.name = updated_name
        user.email = updated_email

        try:
            # Save the changes to the database
            db.session.commit()
            flash("User updated successfully!")
            return redirect('/')
        except Exception as e:
            # Handle potential database errors
            db.session.rollback()
            flash(f"Error updating user: {str(e)}")
            return redirect(request.url)

    # For GET requests, render the update_user.html template
    return render_template('update_user.html', user=user)

# Delete a User
@app.route('/delete_user/<int:user_id>', methods=['GET','POST'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if user is None:
        flash("User not found!")
        return redirect('/')

    if request.method == 'POST':
        try:
            # Remove the user from the User table
            db.session.delete(user)
            db.session.commit()
            flash("User deleted successfully!")
            return redirect('/')
        except Exception as e:
            # Handle potential database errors
            db.session.rollback()
            flash(f"Error deleting user: {str(e)}")
            return redirect(request.url)

    # For GET requests, render the delete_user.html template
    return render_template('delete_user.html', user=user)

# Run the Flask application
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
