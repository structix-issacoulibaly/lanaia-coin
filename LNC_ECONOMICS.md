# LNC Economics (V1)

Ce document présente les paramètres économiques initiaux (tokenomics) pour Lanaia Coin (LNC) — version V1. Les chiffres et pourcentages listés ici sont des propositions initiales et pourront être ajustés par la gouvernance.

Résumé de l'offre

- Offre cible maximale : 21,000,000 LNC
- Récompense initiale par bloc : 10 LNC
- Blocs par ère (halving) : 1,050,000 (~4 ans)
- Temps moyen par bloc : 120 secondes

Allocation initiale (proposition)

- Récompenses de minage / validation : 85% de l'émission totale (distribution par blocs au fil des ères)
- Réserve développement : 5% (utilisée pour financer le développement initial, audits, infra)
- Réserves communautaires : 7% (grants, partenariats, programmes d'incitation)
- Airdrop / lancement : 3% (pour bootstrap de l'écosystème, promotions et early adopters)

Remarques sur l'allocation

- Les pourcentages ci-dessus sont comptés sur l'offre maximale et peuvent être lockés/vested selon des calendriers pour prévenir la vente massive initiale.
- La réserve développement sera sujette à des conditions de déblocage (vesting) et idéalement gérée par un mécanisme multisig ou une structure DAO transparente.

Vesting et déblocage

- Réserve développement (5%) : vesting linéaire sur 3 ans après le bloc de genèse avec un cliff de 6 mois.
- Réserves communautaires (7%) : libération progressive via propositions et approbations communautaires.
- Airdrop (3%) : distribution planifiée aux early adopters et contributeurs identifiés selon une liste vérifiable.

Inflation résiduelle et modèle d'émission

- Le modèle d'émission suit des halvings programmés — la récompense par bloc est divisée par deux à chaque nouvelle ère (tous les 1,050,000 blocs).
- La somme cumulée des émissions tend vers l'offre cible maximale (21,000,000 LNC). Les émissions ultérieures deviennent négligeables après plusieurs halvings.

Mécanismes anti-spam et frais

- Les frais de transaction ne sont pas couverts en détail dans V1 mais devront être définis dans les implémentations ultérieures (V1.1/V2) pour éviter les abus et couvrir les frais d'infrastructure.

 Gouvernance des paramètres économiques

- Les paramètres critiques (allocation, vesting, émissions réservées) peuvent être modifiés via un processus de gouvernance transparent qui sera défini et mis en place dans V2 (DAO ou multisig + vote communautaire).

Risques et considérations

- Concentration des réserves : garder une faible part réservée aux entités centralisées et appliquer des politiques de vesting.
- Ajustements futurs : la communauté doit conserver la capacité d'adapter certains paramètres si des problèmes majeurs apparaissent (p. ex. sécurité, exploitations inattendues, demandes de marché).

Annexe — paramètres repris dans le prototype

- BLOCS_PAR_ERE = 1_050_000
- RECOMPENSE_INITIALE = 10.0
- TEMPS_BLOC_SEC = 120

---

Note : Ce document est une base pour discussion et vote communautaire. Les montants finaux et la gouvernance doivent être décidés publiquement avant toute distribution significative.