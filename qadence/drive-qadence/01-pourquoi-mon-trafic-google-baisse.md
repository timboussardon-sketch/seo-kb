---
type: contenu
format: brief-hn
projet: qadence
statut: brief
requete_cible: pourquoi mon trafic Google baisse
intention: Know → Do
capacite_qadence: cron content-decay + audit_gsc
schema: Article
created: 2026-07-13
sources_vault: [[weight-decay]], [[fraicheur-contenu]], [[retrieval-collapse]], [[test-substitution-llm]], [[tabou-visibilite]]
---

# Pourquoi mon trafic Google baisse

Un trafic organique qui baisse a trois causes structurelles aujourd'hui : le contenu a vieilli et Google favorise le récent, la page est devenue substituable par un moteur génératif, ou elle est rétrogradée dans un pool web pollué par l'IA. La bonne mesure n'est pas le trafic total, ce sont les leads perdus.

## Le contenu a vieilli et Google favorise le récent
- Les architectures modernes sont conçues pour oublier l'ancien au profit du récent et du surprenant, ce qui pénalise structurellement les contenus statiques sur le long terme [[weight-decay]]
- Le biais de récence est observé dans le top 10 : les résultats classés sont plus récents de 1 à 5 ans [[weight-decay]]
- À contenu équivalent, une page datée de moins de 3 mois est citée environ 3 fois plus qu'une page ancienne [[fraicheur-contenu]]

## La page est devenue substituable par ChatGPT
- Si un LLM peut produire 80 % de la réponse, l'utilisateur n'a plus aucune raison de cliquer et le trafic s'effondre [[test-substitution-llm]]
- Les pages-commodité (FAQ génériques, guides sans donnée propre) perdent leur trafic dès qu'un moteur génératif répond à leur place [[test-substitution-llm]]

## La page est rétrogradée dans un pool web pollué
- À 67 % de pollution du pool web, plus de 80 % des réponses IA sont contaminées, ce qui redistribue les positions [[retrieval-collapse]]
- Les fermes d'articles IA sont détectées et rétrogradées : le Core Update de mars 2026 a coûté 40 à 80 % de trafic aux sites industrialisés sans supervision [[retrieval-collapse]]
- Les signaux d'humanité vérifiable et la data propriétaire échappent à cet effondrement du retrieval [[retrieval-collapse]]

## Mesurer la baisse en leads, pas en trafic
- Une chute de trafic informationnel n'est pas une chute de leads : ce qui compte, ce sont les mots-clés business, le CPC et les demandes générées [[tabou-visibilite]]
- Montrer la data plutôt que parler de positions perdues oriente la décision vers les pages qui convertissent [[tabou-visibilite]]

## Lancer le diagnostic avec Qadence
- Le cron content-decay compare les 28 derniers jours à la période précédente sur ta Search Console réelle et remonte les URL en recul de clics, sans chiffre inventé : donnée absente = signalée
- L'audit_gsc croise chaque URL en baisse avec son intention pour distinguer un contenu à rafraîchir d'une page substituable à abandonner
→ CTA : qadence.io/app
