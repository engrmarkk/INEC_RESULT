from extensions import db

"""
result_id` int(11) NOT NULL AUTO_INCREMENT,
  `state_name` varchar(50) NOT NULL,
  `party_abbreviation` char(4) NOT NULL,
  `party_score` int(11) NOT NULL,
  `entered_by_user` varchar(50) NOT NULL,
  `date_entered` datetime NOT NULL,
  `user_ip_address` varchar(50) NOT NULL,
  PRIMARY KEY (`result_id`)
"""


class AnnStateResult(db.Model):
    __tablename__ = 'announced_state_results'
    result_id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(50))
    party_abbreviation = db.Column(db.String(50))
    party_score = db.Column(db.Integer)
    entered_by_user = db.Column(db.String(50))
    date_entered = db.Column(db.String(50))
    user_ip_address = db.Column(db.String(50))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"AnnStateResult('{self.result_id}', '{self.state_name}', '{self.party_abbreviation}', " \
               f"'{self.party_score}', '{self.entered_by_user}', " \
               f"'{self.date_entered}', '{self.user_ip_address}')"
