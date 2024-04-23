from flask import Flask
from sqlalchemy import select

from alch_app.db import session
from alch_app.models import User 


app = Flask(__name__)


@app.route('/')
def index():
    # CREATE
    # news_user = User(username = 'superuser', email = 'superuser@example.com')
    # session.add(news_user)
    # session.commit()

    # READ
    user1 = session.get(User, 1)
    # print(user1)
    
    user2 = session.execute( select(User).filter_by( username='user2' ) ).scalar_one()
    # print(user2)
    
    users = session.execute( select(User).order_by( User.username ) ).scalars()
    for elem in users:
        pass # print(elem)

    
    # UPDATE
    user = session.execute( select(User).filter_by( username='user2' ) ).scalar_one()
    # user.email = 'user2@yandex.ru'
    # session.commit()

    # DELETE
    user = session.execute( select(User).filter_by( username='user2' ) ).scalar_one()
    session.delete(user)
    session.commit()


    return 'SQLAlchemy works'


if __name__ == '__main__':
    app.run(debug=True)
