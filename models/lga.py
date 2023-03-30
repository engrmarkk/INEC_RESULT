from extensions import db

"""
 `uniqueid` int(11) NOT NULL AUTO_INCREMENT,
  `lga_id` int(11) NOT NULL,
  `lga_name` varchar(50) NOT NULL,
  `state_id` int(50) NOT NULL,
  `lga_description` text,
  `entered_by_user` varchar(50) NOT NULL,
  `date_entered` datetime NOT NULL,
  `user_ip_address` varchar(50) NOT NULL,
"""


class Lga(db.Model):
    __tablename__ = 'lga'
    uniqueid = db.Column(db.Integer, primary_key=True)
    lga_id = db.Column(db.Integer)
    lga_name = db.Column(db.String(50))
    state_id = db.Column(db.Integer)
    lga_description = db.Column(db.Text)
    entered_by_user = db.Column(db.String(50))
    date_entered = db.Column(db.String(50))
    user_ip_address = db.Column(db.String(50))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Lga('{self.uniqueid}', '{self.lga_id}', '{self.lga_name}', " \
               f"'{self.state_id}', '{self.lga_description}', " \
               f"'{self.entered_by_user}', '{self.date_entered}', '{self.user_ip_address}')"
