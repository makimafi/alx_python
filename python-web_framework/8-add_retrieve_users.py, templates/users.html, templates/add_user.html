from flask import Flask, render_template, request, flash
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)

# Database setup
engine = create_engine('sqlite:///alx_flask_db.db')
Base.metadata.create_all(engine)

# Flask route for adding a new user
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        try:
            new_user = User(name=name, email=email)
            session = sessionmaker(bind=engine)()
            session.add(new_user)
            session.commit()
            flash('User added successfully!')
        except Exception as e:
            session.rollback()
            flash(f'Error: {str(e)}')
        finally:
            session.close()

    return render_template('add_user.html')

# Flask route for displaying all users
@app.route('/users')
def display_users():
    session = sessionmaker(bind=engine)()
    users = session.query(User).all()
    session.close()
    return render_template('8-users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
