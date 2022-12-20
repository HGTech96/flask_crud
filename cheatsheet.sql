CREATE DATABASE pets;
CREATE ROLE john WITH LOGIN PASSWORD ‘password’;
GRANT ALL PRIVILEGES ON DATABASE pets TO john;

--from flask_sqlalchemy import SQLAlchemy
--app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://john:password@localhost/pets'
--db = SQLAlchemy(app)