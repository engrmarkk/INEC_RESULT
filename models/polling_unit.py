from extensions import db

"""
 `uniqueid` int(11) NOT NULL AUTO_INCREMENT,
  `polling_unit_id` int(11) NOT NULL,
  `ward_id` int(11) NOT NULL,
  `lga_id` int(11) NOT NULL,
  `uniquewardid` int(11) DEFAULT NULL,
  `polling_unit_number` varchar(50) DEFAULT NULL,
  `polling_unit_name` varchar(50) DEFAULT NULL,
  `polling_unit_description` text,
  `lat` varchar(255) DEFAULT NULL,
  `long` varchar(255) DEFAULT NULL,
  `entered_by_user` varchar(50) DEFAULT NULL,
  `date_entered` datetime DEFAULT NULL,
  `user_ip_address` varchar(50) DEFAULT NULL,
"""


class PollingUnit(db.Model):
    __tablename__ = 'polling_unit'
    uniqueid = db.Column(db.Integer, primary_key=True)
    polling_unit_id = db.Column(db.Integer)
    ward_id = db.Column(db.Integer)
    lga_id = db.Column(db.Integer)
    uniquewardid = db.Column(db.Integer)
    polling_unit_number = db.Column(db.String(50))
    polling_unit_name = db.Column(db.String(50))
    polling_unit_description = db.Column(db.Text)
    lat = db.Column(db.String(255))
    long = db.Column(db.String(255))
    entered_by_user = db.Column(db.String(50))
    date_entered = db.Column(db.String(50))
    user_ip_address = db.Column(db.String(50))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"PollingUnit('{self.uniqueid}', '{self.polling_unit_id}', '{self.ward_id}', " \
               f"'{self.lga_id}', '{self.uniquewardid}', " \
               f"'{self.polling_unit_number}', '{self.polling_unit_name}', '{self.polling_unit_description}', " \
               f"'{self.lat}', '{self.long}', '{self.entered_by_user}', '{self.date_entered}', '{self.user_ip_address}')"
