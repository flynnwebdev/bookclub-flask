import psycopg2
from psycopg2.extras import NamedTupleCursor

conn = psycopg2.connect(dbname="database_lesson_development",
                        user="postgres", password="postgres", cursor_factory=NamedTupleCursor)

cur = conn.cursor()
