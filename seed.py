from app import app, db
from models import *

with app.app_context():
    print("Deleting existing tables...")
    db.session.query(user_groups).delete()
    User.query.delete()
    Group.query.delete()
    Post.query.delete()

    print("Creating user table...")
    U1=User(username="User1",email="a@yahoo.com")
    U2=User(username="User2",email="b@yahoo.com")
    U3=User(username="User3",email="c@yahoo.com")
    U4=User(username="User4",email="d@yahoo.com")
    U5=User(username="User5",email="e@yahoo.com")
    
    db.session.add_all([U1,U2,U3,U4,U5])
    print("Done creating user table...")
    db.session.commit()
    
    print("Creating posts table...")
    P1=Post(title="Post1",description="Description1",user=U1)
    P2=Post(title="Post2",description="Description2",user=U1)
    P3=Post(title="Post3",description="Description3",user=U1)
    P4=Post(title="Post4",description="Description4",user=U2)
    P5=Post(title="Post5",description="Description5",user=U1)
    P6=Post(title="Post6",description="Description6",user=U3)
    P7=Post(title="Post7",description="Description7",user=U1)
    P8=Post(title="Post8",description="Description8",user=U5)
    P9=Post(title="Post9",description="Description9",user=U4)
    P10=Post(title="Post10",description="Description10",user=U2)
       
    db.session.add_all([P1,P2,P3,P4,P5,P6,P7,P8,P9,P10])
    print("Done creating posts table...")
    db.session.commit()
    
    print("Creating groups table...")
    G1=Group(name="Group1")
    G2=Group(name="Group2")
    G3=Group(name="Group3")
    G4=Group(name="Group4")
    G5=Group(name="Group5")
    
    db.session.add_all([G1,G2,G3,G4,G5])
    print("Done creating groups table...")
    db.session.commit()
    
    # Adds users to groups
    print("Assigning user to groups...")
    U1.groups.append(G5)
    U1.groups.append(G2)
    
    # Add user to groups
    G5.users.append(U2)
    G5.users.append(U5)
    
    G4.users.append(U3)
    G4.users.append(U1)
    
    db.session.commit()
    