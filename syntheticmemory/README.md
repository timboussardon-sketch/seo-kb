# syntheticmemory

La couche où le système apprend **sur Tim et sa méthode** : préférences, décisions, principes, feedback sur les skills, erreurs à ne pas refaire. Durable et traçable. Brique de gouvernance de la base, vue d'ensemble dans [[moc/moc-methode-kb]].

Ne jamais l'appeler « second cerveau » ni « tim brain ». C'est `syntheticmemory`.

## Pourquoi (et pourquoi c'est sur le bon axe)

Les `ledgers/` d'`agent-synthetic` mémorisent le **travail produit** (claims, sources, prédictions). `syntheticmemory` mémorise **ce qui est vrai sur Tim et sa façon de travailler**. Le but n'est pas de rendre le système plus autonome — c'est de le rendre plus **aligné** : qu'un skill, une boucle ou Claude puisse rappeler « comment Tim veut que ce soit fait » avant d'agir, au lieu de retomber dans le corpus moyen.

C'est l'antidote concret à la dette cognitive : le système ne pense pas à la place de Tim, il retient ses positions pour ne pas les lui faire ré-énoncer à chaque fois.

## Principes

- **Append-only, traçable git.** On ajoute, on ne réécrit pas. Pour corriger, on ajoute un nouveau souvenir avec `supersedes` pointant l'ancien.
- **Pas de vector store, pas d'API.** Sous ~500 souvenirs, le rappel par recouvrement de termes suffit (même logique que `kb-semantic-search`). On rebranche un vrai vector store seulement si le rappel devient mauvais — mesuré, pas supposé.
- **Extraction par Claude, pas par script.** Aucune clé API câblée. Quand Tim donne un feedback, tranche une décision ou exprime une préférence durable, Claude (ou un futur skill) appelle `add.py`. Le script ne fait que valider et écrire.
- **Rappel déterministe.** `recall.py` scanne `store.jsonl`, score par recouvrement, retourne le top N. Reproductible.

## Schéma d'un souvenir (`store.jsonl`)

Un objet JSON par ligne :

```json
{"id":"SM-2026-06-07-001","added":"2026-06-07","type":"preference","subject":"wording","statement":"...","evidence":"...","confidence":0.95,"tags":["wording"],"supersedes":null}
```

- `type` : `preference` | `fact` | `decision` | `principle` | `skill_feedback` | `mistake`
- `subject` : domaine court (wording, voix, gouvernance, infra, strategie-seo...)
- `statement` : le souvenir, énoncé en une à trois phrases, autoportant
- `evidence` : d'où ça vient (conversation, fichier, run)
- `confidence` : 0-1
- `supersedes` : `id` d'un souvenir que celui-ci remplace, sinon `null`

## Usage

```bash
# rappeler ce que le système sait sur un sujet
./recall.py "wording marque"            # tous types
./recall.py "voix rédaction" --type preference --n 3

# ajouter un souvenir (généralement appelé par Claude après un feedback de Tim)
./add.py --type decision --subject gouvernance \
  --statement "..." --evidence "conversation 2026-06-07" \
  --confidence 0.9 --tags "gouvernance,skills"
```

## Distinction avec les autres mémoires

- `agent-synthetic/ledgers/` : faits sur le **travail** (newsletter). Append-only aussi, mais autre objet.
- `~/.claude/.../memory/` (mémoire perso de Claude) : aide-mémoire de l'assistant, hors repo. `syntheticmemory` est **dans le repo, versionné, utilisable par les skills**.
