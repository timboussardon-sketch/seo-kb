#!/usr/bin/env python3
"""
Lexique des modificateurs d'intention (corpus 1 Qadence) — assemblage.

Séparation stricte des responsabilités :
  - les FAMILLES et l'appartenance d'un modificateur à une famille sont
    CURÉES À LA MAIN ci-dessous, contre la doctrine du vault
    (skills seo-mots-cles-decisionnels §modificateurs et seo-modeles-pseo §catégories).
  - la FRÉQUENCE et l'INTENTION OBSERVÉE viennent uniquement de
    qadence/grounding/modificateurs.json (13 344 requêtes Google Suggest FR
    sur 23 verticales + 1 986 mots-clés déjà classés).

Rien n'est inventé. Un modificateur sans mesure sort avec
`mesure: null` et devra porter la position doctrinale, pas un faux chiffre.

Seuil d'honnêteté : une intention observée n'est publiée que si elle repose
sur au moins MIN_N mots-clés classés. En dessous, l'échantillon ne dit rien.

Sortie : qadence/grounding/lexique.json
"""

import json
import os

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUNDING = os.path.join(VAULT, "qadence", "grounding", "modificateurs.json")
OUT = os.path.join(VAULT, "qadence", "grounding", "lexique.json")

MIN_N = 15      # en dessous, l'échantillon ne dit rien
MIN_PART = 60   # une dominante à 40 % n'est pas une dominante, c'est une répartition plate

# --- Curation à la main. Doctrine, pas data. ---------------------------------
# Chaque famille dit ce que le modificateur RÉVÈLE de la personne qui tape.
FAMILLES = {
    "achat-direct": {
        "libelle": "Achat direct",
        "signal": "La personne a choisi de payer. Elle cherche le montant ou le moyen de passer commande.",
        "etage": "Do",
        "modificateurs": [
            "prix", "tarif", "tarifs", "coût", "cout", "combien", "combien ça coûte",
            "devis", "acheter", "commander", "souscrire", "abonnement", "prendre",
            "pas cher", "moins cher", "gratuit", "gratuite", "free", "essai",
            "essai gratuit", "démo", "demo", "offre", "promo", "réduction",
        ],
    },
    "comparaison": {
        "libelle": "Comparaison",
        "signal": "La personne a une liste courte. Elle arbitre entre des options déjà identifiées.",
        "etage": "Do",
        "modificateurs": [
            "vs", "versus", "comparatif", "comparaison", "comparer", "meilleur",
            "meilleurs", "meilleure", "top", "alternative", "alternatives",
            "lequel choisir", "quel choisir", "différence", "difference", "ou",
            "classement", "concurrent",
        ],
    },
    "evaluation": {
        "libelle": "Évaluation et réassurance",
        "signal": "La personne veut être rassurée avant d'engager. Elle cherche l'expérience des autres.",
        "etage": "Do",
        "modificateurs": [
            "avis", "test", "tests", "retour", "retour d'expérience", "fiable",
            "arnaque", "review", "reviews", "témoignage", "note", "sérieux",
            "vaut le coup", "ça marche",
        ],
    },
    "usage": {
        "libelle": "Mise en œuvre",
        "signal": "La personne a décidé de faire elle-même. Elle cherche le mode opératoire.",
        "etage": "Know",
        "modificateurs": [
            "comment", "comment faire", "tutoriel", "tuto", "guide", "étapes",
            "etapes", "exemple", "exemples", "modèle", "modele", "template",
            "checklist", "méthode", "methode", "faire", "créer", "creer",
            "mettre en place", "utiliser", "configurer",
        ],
    },
    "definition": {
        "libelle": "Définition",
        "signal": "La personne découvre le sujet. Elle ne connaît pas encore le vocabulaire.",
        "etage": "Know-Simple",
        "modificateurs": [
            "définition", "definition", "def", "c'est quoi", "qu'est-ce que",
            "signification", "meaning", "what is", "que es", "principe",
            "explication", "expliqué", "vulgarisé",
        ],
    },
    "format": {
        "libelle": "Format attendu",
        "signal": "La personne veut un objet à emporter, pas une page à lire.",
        "etage": "Know",
        "modificateurs": [
            "pdf", "excel", "word", "vidéo", "video", "youtube", "image",
            "schéma", "schema", "liste", "download", "télécharger", "telecharger",
            "infographie", "powerpoint", "ppt",
        ],
    },
    "profil": {
        "libelle": "Profil de la personne",
        "signal": "La personne se reconnaît dans un segment. Elle écarte tout ce qui ne lui parle pas.",
        "etage": "Know",
        "modificateurs": [
            "pour", "débutant", "debutant", "pme", "tpe", "e-commerce", "ecommerce",
            "b2b", "b2c", "freelance", "indépendant", "independant", "étudiant",
            "etudiant", "association", "artisan", "startup", "grand compte",
        ],
    },
    "geographie": {
        "libelle": "Ancrage géographique",
        "signal": "La personne veut un interlocuteur joignable, ou une règle qui s'applique chez elle.",
        "etage": "Do",
        "modificateurs": [
            "paris", "lyon", "marseille", "bordeaux", "lille", "toulouse",
            "nantes", "nice", "strasbourg", "montpellier", "france", "belgique",
            "suisse", "maroc", "tunisie", "canada", "près de moi", "pres de moi",
            "local", "autour de moi",
        ],
    },
    "prestataire": {
        "libelle": "Recherche de prestataire",
        "signal": "La personne a renoncé à faire elle-même. Elle cherche quelqu'un à qui confier le travail.",
        "etage": "Do",
        "modificateurs": [
            "agence", "agency", "consultant", "freelance", "expert", "cabinet",
            "prestataire", "spécialiste", "specialiste", "specialist",
            "accompagnement", "prestation", "service", "services",
        ],
    },
    "emploi-formation": {
        "libelle": "Emploi et formation",
        "signal": "La personne veut EXERCER le métier, pas l'acheter. Piège classique du trafic qui ne convertit jamais.",
        "etage": "hors-cible",
        "modificateurs": [
            "emploi", "job", "jobs", "salaire", "recrutement", "offre d'emploi",
            "formation", "certification", "certificat", "école", "ecole",
            "master", "cours", "course", "métier", "metier", "devenir",
            "alternance", "stage", "diplôme", "diplome", "reconversion",
        ],
    },
    "temporel": {
        "libelle": "Fraîcheur",
        "signal": "La personne se méfie de l'information périmée. Elle veut l'état actuel.",
        "etage": "Know",
        "modificateurs": [
            "2025", "2026", "nouveau", "nouvelle", "dernier", "dernière",
            "mise à jour", "actualité", "récent", "recent", "aujourd'hui",
        ],
    },
    "outil": {
        "libelle": "Recherche d'outil",
        "signal": "La personne cherche un logiciel qui fait le travail, pas un prestataire.",
        "etage": "Do",
        "modificateurs": [
            "outil", "outils", "logiciel", "plateforme", "platform", "application",
            "app", "tools", "tool", "software", "saas", "générateur", "generateur",
            "calculateur", "simulateur",
        ],
    },
    "probleme": {
        "libelle": "Dépannage",
        "signal": "Quelque chose est cassé. La personne cherche à réparer, pas à comprendre.",
        "etage": "Know",
        "modificateurs": [
            "erreur", "problème", "probleme", "ne fonctionne pas", "ne marche pas",
            "pourquoi", "résoudre", "resoudre", "corriger", "réparer", "reparer",
            "bug", "panne", "bloqué", "bloque",
        ],
    },
}


def slugify(s):
    table = str.maketrans("àâäéèêëîïôöùûüç", "aaaeeeeiioouuuc")
    s = s.lower().translate(table)
    return "".join(c if c.isalnum() else "-" for c in s).strip("-").replace("--", "-")


def main():
    with open(GROUNDING, encoding="utf-8") as f:
        g = json.load(f)
    mesures = {m["token"]: m for m in g["modificateurs"]}

    fiches = []
    ecartes = []
    for fam_slug, fam in FAMILLES.items():
        for mod in fam["modificateurs"]:
            m = mesures.get(mod)
            mesure = None
            if m:
                dist = m.get("intention_mesuree") or {}
                total = sum(dist.values())
                mesure = {
                    "occurrences_suggest": m["occurrences"],
                    "verticales": m["verticales"],
                    "exemples_reels": m["exemples"],
                    "intention_observee": None,
                    "echantillon_intention": total,
                }
                if total >= MIN_N:
                    dominante = max(dist, key=dist.get)
                    part = round(100 * dist[dominante] / total)
                    if part >= MIN_PART:
                        mesure["intention_observee"] = {
                            "dominante": dominante,
                            "part": part,
                            "distribution": dist,
                        }
            # RÈGLE DURE : pas de mesure, pas de fiche. Un modificateur qu'on n'a
            # pas observé dans de la donnée réelle ne se publie pas, même si la
            # doctrine sait quoi en dire. Les écartés sont tracés dans
            # `ecartes_faute_de_donnee` pour savoir quoi grounder plus tard.
            if not mesure:
                ecartes.append({"modificateur": mod, "famille": fam_slug})
                continue
            fiches.append(
                {
                    "slug": slugify(mod),
                    "modificateur": mod,
                    "famille": fam_slug,
                    "famille_libelle": fam["libelle"],
                    "signal": fam["signal"],
                    "etage_doctrine": fam["etage"],
                    "mesure": mesure,
                }
            )

    intentions_ok = sum(1 for f in fiches if f["mesure"]["intention_observee"])
    familles_retenues = sorted({f["famille"] for f in fiches})

    payload = {
        "corpus": "Lexique des modificateurs d'intention",
        "regle": "Une fiche n'existe que si le modificateur a été observé dans "
                 "de la donnée réelle. Aucune fréquence, aucune intention n'est "
                 "estimée. L'intention n'est publiée qu'au-delà de "
                 f"{MIN_N} mots-clés classés.",
        "familles": {
            k: {kk: vv for kk, vv in v.items() if kk != "modificateurs"}
            for k, v in FAMILLES.items()
            if k in familles_retenues
        },
        "seuil_intention_publiable": MIN_N,
        "total_fiches": len(fiches),
        "fiches_avec_intention_publiable": intentions_ok,
        "ecartes_faute_de_donnee": ecartes,
        "source_mesures": g["sources"],
        "fiches": fiches,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"fiches publiables (mesurées) : {len(fiches)}")
    print(f"dont intention publiable     : {intentions_ok}")
    print(f"écartées faute de donnée     : {len(ecartes)}")
    print(f"familles retenues            : {len(familles_retenues)}/{len(FAMILLES)}")
    print(f"écrit                        : {OUT}")


if __name__ == "__main__":
    main()
