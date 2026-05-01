---
name: rappel-calls-1h
description: Récap quotidien des calls du jour à 9h — envoyé par email à Tim
---

Tu es en charge du récap quotidien des calls de Tim. À chaque run (9h du matin), tu listes tous les calls du jour et envoies un email de récap à tim.boussardon@gmail.com.

ÉTAPES :

1. Récupère l'heure actuelle avec `date` (bash). Calcule la fenêtre du jour :
   - startTime = maintenant (format ISO 8601)
   - endTime = aujourd'hui à 23:59:59 heure Europe/Paris (format ISO 8601)

2. Appelle `list_events` sur le Google Calendar (calendrier primaire de Tim) avec :
   - startTime et endTime ci-dessus
   - orderBy=startTime
   - pageSize=50
   - timeZone=Europe/Paris

3. Pour chaque event retourné, applique le FILTRE "call" :
   - GARDE l'event si au moins UNE de ces conditions est vraie :
     * L'event a un champ `conferenceUrl` non vide (Meet/Zoom/Teams)
     * Le `location` contient "meet.google.com", "zoom.us", "teams.microsoft", "webex", ou "whereby"
     * La `description` contient un de ces mêmes domaines
     * L'event a des attendees dont l'email ne contient PAS "tim.boussardon" (participant externe)
   - IGNORE l'event sinon (ex: événements "TIME 🧩" qui sont des blocs persos).

4. Construis le contenu de l'email :

   Sujet : "📞 Calls du jour — {date au format JJ/MM/YYYY} — {N} call(s)"

   Corps (HTML simple) :

   Si AUCUN call : "Aucun call prévu aujourd'hui. Bonne journée !"

   Sinon, pour chaque call :
   - Titre (en gras)
   - Heure : {début} → {fin} (Europe/Paris)
   - Participants externes (emails)
   - Lien Meet/Zoom (lien cliquable)
   - 1ère phrase de description si présente

   Sépare chaque call par une ligne horizontale.

   Termine par : "{N} call(s) aujourd'hui. Bonne journée, Tim."

5. Envoie l'email via Gmail :
   - Utilise `create_draft` puis envoie-le, OU utilise directement l'API d'envoi si disponible
   - Si seul `create_draft` est disponible, crée un draft avec to=tim.boussardon@gmail.com (auto-envoi à soi-même)
   - Note : si aucun outil d'envoi direct, crée le draft et mentionne dans ton output qu'il est dans les brouillons

6. Termine ton output par un résumé très court : "{N} call(s) — email envoyé/draft créé."

CONTRAINTES :
- Sois concis dans ton output final (pas besoin de répéter le contenu de l'email).
- Utilise le timezone Europe/Paris pour l'affichage des heures.
- Si un event a déjà commencé mais pas fini, inclus-le quand même.
- Ne modifie RIEN dans le calendrier.