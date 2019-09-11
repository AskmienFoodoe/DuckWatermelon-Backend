from db import db


class ScoreModel(db.Model):
    __tablename__ = 'items'

    tag = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    diff = db.Column(db.String(32))
    score = db.Column(db.Integer)


    def __init__(self, name, diff, score):
        self.name = name
        self.diff = diff
        self.score = score

    def json(self):
        return {'tag': self.tag, 'name': self.name, 'diff': self.diff, 'score': self.score}

    @classmethod
    def find_by_tag(cls, tag):
        return cls.query.filter_by(tag=tag).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
