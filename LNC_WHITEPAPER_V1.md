Lanaia Coin (LNC) est un projet de cryptomonnaie décentralisée visant à offrir une réserve numérique sûre, transparente et accessible, avec une emission prévisible et une gouvernance communautaire.

Résumé exécutif

Lanaia Coin (LNC) propose une crypto-monnaie conçue pour la durabilité, la sécurité et la simplicité d'utilisation. Inspirée par les meilleures pratiques des protocoles établis, LNC met l'accent sur une émission contrôlée, une faible inflation résiduelle et des mécanismes clairs pour la participation de la communauté.

Objectifs du projet

- Fournir une réserve numérique avec une offre maximale limitée et une distribution lisible dans le temps.
- Assurer la sécurité du réseau via des mécanismes de consensus compatibles avec des mineurs et validateurs légers.
- Favoriser l'adoption grâce à des outils simples et une documentation claire.
- Mettre en place une gouvernance décentralisée pour les évolutions protocolaires.

Conception monétaire

Offre maximale

LNC a une offre cible maximale de 21,000,000 LNC. L'émission est structurée en ères d'un nombre fixe de blocs, avec une récompense par bloc initiale et des halvings successifs qui divisent la récompense par deux à chaque ère.

Paramètres principaux (V1)

- Offre cible maximale : 21,000,000 LNC
- Récompense initiale par bloc : 10 LNC
- Temps moyen par bloc : 120 secondes
- Blocs par ère (halving) : 1,050,000 (~4 ans)

Programme d'émission

La logique d'émission suit une suite d'ères. Pour chaque ère, la récompense par bloc est divisée par deux par rapport à l'ère précédente. Cette approche permet de découper l'émission en étapes prévisibles et d'atteindre progressivement l'offre maximale.

Sécurité et consensus

La spécification V1 est agnostique au mécanisme exact de consensus afin de rester flexible pour les implémentations futures. Le prototype initial et les premières implémentations peuvent utiliser un algorithme de type Proof-of-Work (PoW) ou un modèle hybride, avec des contraintes visant à limiter la centralisation et favoriser la participation de nœuds diversifiés.

Caractéristiques de conception

- Emission prévisible : Les paramètres d'émission (récompense initiale, durée d'ère) sont publics et immuables dans la spécification V1.
- Transparence : Toutes les règles d'émission et les métriques de réseau doivent être auditable via l'explorateur et les outils de monitoring.
- Simplicité : Le protocole favorise des règles faciles à comprendre pour encourager la confiance et l'adoption.

Tokenomics et distribution

V1 prévoit une distribution initiale visant à garantir un lancement sain et l'activité du réseau :

- Récompenses de minage / validation : Principal mécanisme d'attribution lors de la production de blocs.
- Réserve développement : Un pourcentage limité (à définir dans la gouvernance) peut être réservé pour financer le développement initial, la sécurité et les partenariats.
- Réserves communautaires : Fonds alloués pour l'écosystème (grants, hackathons, intégrations).

Gouvernance

La gouvernance initiale sera légère et axée sur la transparence. Les propositions d'évolution de protocole (amendements de paramètres, nouvelles fonctionnalités) devront être documentées, débattues publiquement, puis votées via un mécanisme qui sera défini par la communauté (DAO ou processus de gouvernance multi-signature dans V2).

Interopérabilité et adoption

LNC vise à être facilement intégrable aux portefeuilles existants et aux services d'échange. Les premières versions incluront des interfaces API simples, une documentation claire et des SDKs légers pour accélérer l'intégration.

Sécurité et audits

Les composants critiques (protocoles de consensus, portefeuilles, contrats) seront soumis à des audits de sécurité indépendants. Les bonnes pratiques de gestion des clés et des processus de mise à jour sécurisés seront documentées et encouragées.

Roadmap (V1 → V2)

- V1 : Spécification, prototype de simulation d'émission, dépôt initial, documentation.
- V1.1 : Implémentations de référence (nœud léger, wallet), tests d'intégration.
- V2 : Gouvernance on-chain, audits de sécurité, améliorations du consensus et optimisation des performances.

Conclusion

Lanaia Coin (LNC) se positionne comme une cryptomonnaie avec une émission claire et prévisible, orientée vers la communauté et la sécurité. La version V1 de la spécification jette les bases pour une adoption progressive, des audits rigoureux, et une gouvernance qui évoluera avec la communauté.

---

Annexe technique — paramètres utilisés dans le prototype

- BLOCS_PAR_ERE = 1_050_000
- RECOMPENSE_INITIALE = 10.0
- TEMPS_BLOC_SEC = 120

Ces paramètres sont repris dans le prototype de simulateur (prototype/lnc_miner_prototype.py) pour valider l'émission et visualiser le cumul jusqu'à l'approche de l'offre cible maximale.
