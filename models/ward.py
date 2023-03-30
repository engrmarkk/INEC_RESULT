from extensions import db

"""
 `uniqueid` int(11) NOT NULL AUTO_INCREMENT,
  `ward_id` int(11) NOT NULL,
  `ward_name` varchar(50) NOT NULL,
  `lga_id` int(11) NOT NULL,
  `ward_description` text,
  `entered_by_user` varchar(50) NOT NULL,
  `date_entered` datetime NOT NULL,
  `user_ip_address` varchar(50) NOT NULL
"""


class Ward(db.Model):
    __tablename__ = 'ward'
    uniqueid = db.Column(db.Integer, primary_key=True)
    ward_id = db.Column(db.Integer)
    ward_name = db.Column(db.String(50))
    lga_id = db.Column(db.Integer)
    ward_description = db.Column(db.Text)
    entered_by_user = db.Column(db.String(50))
    date_entered = db.Column(db.String(50))
    user_ip_address = db.Column(db.String(50))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Ward('{self.uniqueid}', '{self.ward_id}', '{self.ward_name}', " \
               f"'{self.lga_id}', '{self.ward_description}', " \
               f"'{self.entered_by_user}', '{self.date_entered}', '{self.user_ip_address}')"
