from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.score import ScoreModel


class Score(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('diff',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('score',
                        type=int,
                        required=True,
                        help="Every score needs a store_id."
                        )

    
    def get(self):
        return {'scores': list(map(lambda x: x.json(), ScoreModel.query.all()))}

    def post(self):

        data = Score.parser.parse_args()

        score = ScoreModel(**data)

        try:
            score.save_to_db()
        except:
            return {"message": "An error occurred inserting the score."}, 500

        return score.json(), 201

    def delete(self, tag):
        score = ScoreModel.find_by_tag(tag)
        if score:
            score.delete_from_db()
            return {'message': 'score deleted.'}
        return {'message': 'score not found.'}, 404