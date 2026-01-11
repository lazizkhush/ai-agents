from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg://postgres:xref14max@localhost:5432/ai_agents")


create_table_script = """
create table users(
    id integer primary key,
    username text,
    password text
);

create table history(
    id integer primary key,
    user_id int,
    user_message_id int,
    message text,
    role text -- user, model
);
"""

with engine.begin() as conn:
    conn.execute(text(create_table_script))




