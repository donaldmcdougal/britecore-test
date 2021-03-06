from database import DBSession, Client, ProductArea

class Seed():
    def createSeedData(self):
        session = DBSession()

        if len(session.query(Client).all()) == 0:
            clientA = Client(name='Client A')
            clientB = Client(name='Client B')
            clientC = Client(name='Client C')
            session.add_all([clientA, clientB, clientC])
            session.flush()
            session.commit()

        if len(session.query(ProductArea).all()) == 0:
            policies1 = ProductArea(name='Policies')
            policies2 = ProductArea(name='Billing')
            policies3 = ProductArea(name='Claims')
            policies4 = ProductArea(name='Reports')
            session.add_all([policies1, policies2, policies3, policies4])
            session.flush()
            session.commit()
