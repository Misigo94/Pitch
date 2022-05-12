export SECRET_KEY= 'Password'
export SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://user1:Password@localhost:5432/user1db'

# python3.9 manage.py migrate
# python3.9 manage.py shell
python3.9 manage.py server

