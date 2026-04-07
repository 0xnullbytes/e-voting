from flask import Blueprint, request, jsonify
from app import db
from models import Electeur, Vote, Candidat
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)


@main.route('/electeurs', methods=['POST'])
def create_electeur():
    data = request.json

    electeur = Electeur(
        nom=data['nom'],
        email=data['email'],
        mot_de_passe=generate_password_hash(data['mot_de_passe'])
    )

    db.session.add(electeur)
    db.session.commit()

    return jsonify({"id": electeur.id})


@main.route('/voter', methods=['POST'])
def voter():
    data = request.json

    vote = Vote(
        electeur_id=data['electeur_id'],
        candidat_id=data['candidat_id']
    )

    db.session.add(vote)
    db.session.commit()

    return jsonify({"message": "Vote enregistré"})


@main.route('/votes', methods=['GET'])
def list_votes():
    votes = Vote.query.all()
    return jsonify([
        {
            "id": v.id,
            "electeur": v.electeur.nom,
            "candidat": v.candidat.nom,
        }
        for v in votes
    ])


@main.route('/candidats', methods=['POST'])
def create_candidat():
    data = request.json
    candidat = Candidat(nom=data['nom'])
    db.session.add(candidat)
    db.session.commit()
    return jsonify({"id": candidat.id, "nom": candidat.nom}), 201


@main.route('/candidats', methods=['GET'])
def list_candidats():
    candidats = Candidat.query.all()
    return jsonify([
        {"id": c.id, "nom": c.nom}
        for c in candidats
    ])
