from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Membership(base):
    __tablename__ = "Membership"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address_1st = Column(String)
    address_2nd = Column(String)
    address_postcode = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Progammer table
ada_lovelace = Membership(
    first_name="Ada",
    last_name="Lovelace",
    address_1st="44 Burnthwaite Rd",
    address_2nd="Fulham, London",
    address_postcode="SW6 5BE"
)

chris_carabine = Membership(
    first_name="Chris",
    last_name="Carabine",
    address_1st="Flat 1, 67 Wellesley Rd",
    address_2nd="Twickenham",
    address_postcode="TW2 5RZ"
)

# add each instance of our programmers to our session
#session.add(ada_lovelace)
#session.add(chris_carabine)

#updATING
#membership = session.query(Membership).filter_by(id=1).first()
#membership.first_name = "poppy"

# commit our session to the database
#session.commit()



# query the database to find all Programmers
memberships = session.query(Membership)
for membership in memberships:
    print(
        membership.id,
        membership.first_name + " " + membership.last_name,
        membership.address_1st,
        membership.address_2nd,
        membership.address_postcode,
        sep=" * "
    )
