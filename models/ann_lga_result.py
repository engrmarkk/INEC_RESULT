from extensions import db

"""
(`result_id`, `lga_name`, `party_abbreviation`, `party_score`, 
`entered_by_user`, `date_entered`, `user_ip_address`)
"""


class AnnLgaResult(db.Model):
    __tablename__ = 'announced_lga_results'
    result_id = db.Column(db.Integer, primary_key=True)
    lga_name = db.Column(db.String(50))
    party_abbreviation = db.Column(db.String(50))
    party_score = db.Column(db.Integer)
    entered_by_user = db.Column(db.String(50))
    date_entered = db.Column(db.String(50))
    user_ip_address = db.Column(db.String(50))


    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"AnnLgaResult('{self.result_id}', '{self.lga_name}', '{self.party_abbreviation}', " \
               f"'{self.party_score}', '{self.entered_by_user}', " \
               f"'{self.date_entered}', '{self.user_ip_address}')"
