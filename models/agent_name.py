from extensions import db


class AgentName(db.Model):
    __tablename__ = 'agent_name'
    name_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    pollingunit_uniqueid = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"{self.name_id}"
"""
(`name_id`, `firstname`, `lastname`, `email`, `phone`, `pollingunit_uniqueid`)
"""