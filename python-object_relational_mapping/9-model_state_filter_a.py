#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import func

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn_str = (
        f"mysql+mysqldb://{username}:"
        f"{password}@localhost:3306/"
        f"{database}"
    )
    engine = create_engine(conn_str, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states_with_a = (
        session.query(State)
        .filter(State.name.ilike('%a%'))
        .order_by(State.id)
        .all()
    )

    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()
