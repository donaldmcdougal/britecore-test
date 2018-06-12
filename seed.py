from database import session, Client, ProductArea

clientA = Client(name='Client A')
clientB = Client(name='Client B')
clientC = Client(name='Client C')
session.add_all([clientA, clientB, clientC])
session.flush()
policies1 = ProductArea(name='Policies')
policies2 = ProductArea(name='Billing')
policies3 = ProductArea(name='Claims')
policies4 = ProductArea(name='Reports')
session.add_all([policies1, policies2, policies3, policies4])
session.commit()
