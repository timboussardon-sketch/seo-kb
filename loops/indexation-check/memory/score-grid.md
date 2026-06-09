# Grille de qualite (gate) - indexation-check

Un run ne "passe" que s'il coche ces criteres. Sinon : ne pas publier, logguer en mistakes.

- [ ] Chaque claim a >= 2 sources independantes dont 1 primaire (sinon marquer fragile).
- [ ] Aucun chiffre/date invente (placeholder [A SOURCER] sinon).
- [ ] Anti-IA-writing respecte ([[ton-de-voix-tim]]).
- [ ] Au moins 1 prediction datee posee (resolve_by J+30 ou J+90) si le run produit du contenu mesurable.
- [ ] validate.sh passe (JSONL + capture_mode).
