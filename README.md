# E-Voting API

Mini application de vote électronique construite avec Flask et MySQL.

## Installation
```bash
pip install -r requirements.txt
flask db upgrade
flask run
```

## Endpoints

| Méthode | Route | Description |
|---|---|---|
| POST | /electeurs | Créer un électeur |
| POST | /candidats | Créer un candidat |
| GET | /candidats | Lister les candidats |
| POST | /vote | Voter |
| GET | /votes | Lister les votes |

## Exemples

**Créer un électeur**
```json
POST /electeurs
{ "nom": "Ali", "email": "ali@test.com", "mot_de_passe": "1234" }
```

**Créer un candidat**
```json
POST /candidats
{ "nom": "Candidate A" }
```

**Voter**
```json
POST /vote
{ "electeur_id": 1, "candidat_id": 1 }
```
