from extensions import db

"""
  `state_id` int(11) NOT NULL,
  `state_name` varchar(50) NOT NULL,
"""


class State(db.Model):
    __tablename__ = 'state'
    state_id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(50))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"State('{self.state_id}', '{self.state_name}')"
