from peewee import Model, CharField, SqliteDatabase, PostgresqlDatabase

db = PostgresqlDatabase("postgres", host="localhost", port=5432)
