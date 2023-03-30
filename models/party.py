from extensions import db

"""
 `id` int(11) NOT NULL AUTO_INCREMENT,
  `partyid` varchar(11) NOT NULL,
  `partyname` varchar(11) NOT NULL,
"""


class Party(db.Model):
    __tablename__ = 'party'
    id = db.Column(db.Integer, primary_key=True)
    partyid = db.Column(db.String(11))
    partyname = db.Column(db.String(11))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Party('{self.id}', '{self.partyid}', '{self.partyname}')"
