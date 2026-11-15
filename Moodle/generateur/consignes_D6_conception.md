---
kicker: 3W Academy · Cycle Expert en informatique et SI · Bloc 3
titre: Dossier de conception d'application (D6)
soustitre: Consignes · dossier en groupe de trois et oral individuel · à rendre la veille de la semaine S9
---
Medisecure veut remplacer sa plateforme Medisecure Connect par une nouvelle version, plus sûre, plus simple à faire évoluer et intégrée au reste du SI. Vous en rédigez le dossier de conception, qui servira de référence aux équipes de développement. Le dossier se fait en groupe de trois, se rend la veille de la semaine S9 et donne lieu à un oral individuel.

## Ce qui est évalué

Ce dossier valide l'activité « Conception d'une application informatique » du bloc 3, « Concevoir et développer une application informatique ». La partie développement du bloc (C25 à C27) sera évaluée dans le dossier D7, qui réalisera une partie de ce que vous concevez ici.

| Compétence | Ce qu'elle demande | Critères du référentiel |
| --- | --- | --- |
| C21 | Concevoir une architecture applicative adaptée au SI existant, à partir des besoins fonctionnels et des exigences de sécurité, et produire des maquettes représentatives | Le diagramme d'architecture décrit précisément l'infrastructure matérielle, le réseau et le stockage, en privilégiant l'économie de ressources et la sécurité. Les maquettes des interfaces et des flux de données de chaque module sont claires. Les critères de performance, de sécurité et de conformité sont définis sous forme d'indicateurs. |
| C22 | Schématiser les processus métier en tenant compte des contraintes, de l'existant et des vulnérabilités | Trois schémas de processus métier UML sont décrits avec justesse. |
| C23 | Recommander un environnement informatique, ses interactions avec l'infrastructure et les techniques qui réduisent son impact écologique, sur des critères comparatifs | Le choix d'environnement est comparé, argumenté et cohérent avec l'architecture. |
| C24 | Justifier les patterns logiciels et les patterns de classes par les besoins du projet | Les patterns logiciels et les design patterns sont justifiés. Une stratégie de déploiement et une stratégie de maintien sont proposées et justifiées. |

## Périmètre de l'application

Vous concevez l'ensemble de la nouvelle plateforme, mais pas avec le même niveau de détail partout. Le module Rendez-vous est obligatoire ; chaque groupe choisit en plus, le premier jour de S7, l'un des deux modules A ou B.

| Module | Ce qu'il couvre | Niveau de détail attendu |
| --- | --- | --- |
| Rendez-vous | Prise de rendez-vous en ligne, au téléphone et à l'accueil, téléconsultation, agendas des praticiens de tous les centres | Conception détaillée : processus, maquettes, classes, patterns |
| A. Télésurveillance | Réception des mesures, détection et tri des alertes, console des infirmières, application patient, en tenant compte du règlement sur les dispositifs médicaux | Conception détaillée, si ce module est choisi |
| B. Dossier patient unifié | Identité (INS), rapprochement des doublons, consentements, documents, lien avec les deux DPI | Conception détaillée, si ce module est choisi |
| Facturation | Forfaits de télésurveillance, téléconsultations, lien avec FactuSanté | Place dans l'architecture et interfaces |
| Identité et accès | Authentification des patients et des soignants (dont Pro Santé Connect), droits d'accès, traçabilité | Architecture et mesures de sécurité |
| Intégrations | DPI, DMP, laboratoire, imagerie, Assurance Maladie, fabricant des appareils | Contrats d'interface et adaptateurs |

Certains sujets ont déjà été traités dans d'autres dossiers et ne sont pas à refaire ici. L'analyse d'impact RGPD (dossier D4) et le plan de reprise d'activité (dossier D3) sont repris en résumé lorsqu'ils influencent un choix de conception. Le pipeline DevSecOps sera construit dans le dossier D7, et l'architecture big data et les modèles prédictifs dans le dossier D8.

## Livrables et calendrier

Le dossier est collectif, par groupe de trois au plus, et chaque membre le présente ensuite seul à l'oral.

| Élément | Attendu |
| --- | --- |
| Dossier écrit | 20 à 25 pages hors annexes, au format PDF |
| Maquettes | Lien vers le projet Figma (ou outil équivalent) accessible en lecture, et captures dans le dossier |
| Annexes | Diagrammes en grand format, extraits de code, contrats d'interface (OpenAPI) |
| Dépôt | Sur Moodle, nommé Groupe_X_D6_Conception.pdf |
| Lancement | Semaine S7, du 22 au 26 mars 2027 : architecture, processus, maquettes |
| Suite | Semaine S8, du 12 au 16 avril 2027 : patterns, déploiement, maintien ; soutenance blanche le jeudi 15 avril |
| Rendu | La veille du premier jour de S9, à 23 h 59 (date communiquée en S8) |
| Oral individuel | Pendant la semaine S9 : 10 minutes de présentation et 10 minutes de questions |

## Plan attendu

Le dossier est la documentation de référence des futures équipes de développement : chaque choix technique y est justifié par un besoin ou une contrainte de Medisecure. Les pages indiquées sont des ordres de grandeur.

| Partie | Contenu attendu | Pages | Compétences |
| --- | --- | --- | --- |
| 1. Synthèse | En une page : l'architecture retenue, les choix structurants, ce qui change pour les utilisateurs. | 1 | C21 |
| 2. Analyse de l'existant | Les problèmes de la plateforme actuelle, à partir du dossier Medisecure : couplage par la base partagée, dette technique, sécurité, qualité du code, et leurs effets sur les soignants, les patients et l'activité. | 2 | C21 |
| 3. Processus métier | Trois diagrammes UML (activité ou séquence) : une prise de rendez-vous, un processus du module choisi, et un processus transverse au choix (téléconsultation, facturation d'un forfait, création d'un compte patient). Pour chacun : contraintes, existant, vulnérabilités et priorités. | 2 à 3 | C22 |
| 4. Architecture applicative | Une architecture hexagonale justifiée. Au moins quatre contextes métier (bounded contexts) avec leurs entités, leurs agrégats et leurs règles invariantes, et la carte de leurs relations. Le diagramme d'architecture : infrastructure, réseau, stockage, sécurité (authentification, droits d'accès, chiffrement). Les API REST (principes, versionnement, documentation OpenAPI) et les intégrations externes (HL7 FHIR, HPRIM, DICOM, SESAM-Vitale, DMP). | 4 | C21 |
| 5. Maquettes et flux de données | Au moins six écrans clés, dont trois pour les patients et trois pour les soignants, et les flux de données de chaque module. L'application des règles WCAG 2.1 niveau AA dans les maquettes : contrastes, navigation au clavier, structure, compatibilité avec les lecteurs d'écran. | 3 | C21 |
| 6. Patterns | Au moins deux patterns d'architecture logicielle et cinq design patterns, choisis parmi Abstract Factory, Builder, Adapter, Façade, Proxy, Observer, Strategy, Chain of Responsibility ou d'autres. Pour chacun : le besoin de Medisecure qu'il résout, son application, un diagramme de classes ou un extrait de code Python. Le diagramme de classes du module détaillé. | 3 à 4 | C24 |
| 7. Environnement informatique | Un comparatif argumenté des langages, frameworks, bases de données, hébergement et outillage. Les interactions entre l'infrastructure et l'application. Les mesures d'écoconception (référentiel RGESN) et une estimation de leur effet. | 2 | C23 |
| 8. Déploiement et maintien | La stratégie de déploiement : environnements, mise en production progressive, migration depuis la plateforme actuelle et reprise des données. La stratégie de maintien : corrective et évolutive, versionnement, documentation, supervision. | 2 | C24 |
| 9. Indicateurs | Au moins huit indicateurs de performance, de sécurité et de conformité, avec leur cible et leur mode de mesure. | 1 | C21 |

Le dossier Medisecure fournit le schéma de la plateforme actuelle, l'état de son code, les attentes des directions, les volumes, les exigences de disponibilité et la criticité des applications. Reprenez aussi vos dossiers D3 (architecture cible) et D4 (cahiers des charges) : la conception doit être cohérente avec eux, ou expliquer pourquoi elle s'en écarte.

## Grille d'évaluation

Le dossier écrit est noté sur 20 pour le groupe. Un choix présenté sans justification ne rapporte pas de point.

| Critère | Ce que le correcteur vérifie | Points |
| --- | --- | --- |
| Architecture (C21) | Diagramme précis de l'infrastructure, du réseau et du stockage ; sécurité et économie de ressources prises en compte ; découpage métier cohérent | 4 |
| Maquettes et flux (C21) | Écrans clairs, flux de données de chaque module, accessibilité intégrée | 3 |
| Processus métier (C22) | Trois diagrammes UML justes, avec contraintes, existant et vulnérabilités | 3 |
| Patterns (C24) | Patterns logiciels et design patterns justifiés par un besoin réel, illustrés par du code ou un diagramme | 4 |
| Environnement (C23) | Comparatif argumenté, interactions avec l'infrastructure, écoconception chiffrée | 2 |
| Déploiement et maintien (C24) | Stratégies justifiées, migration depuis l'existant réaliste | 2 |
| Indicateurs (C21) | Cibles mesurables pour la performance, la sécurité et la conformité | 1 |
| Cohérence et forme | Les parties s'accordent entre elles et avec D3 et D4 ; schémas lisibles | 1 |
| **Total** | | **20** |

Comme pour le dossier D3, l'oral individuel vérifie la maîtrise de l'ensemble du dossier et peut faire varier la note individuelle de 3 points au plus.

## Règles et conseils

Vous pouvez utiliser des outils d'IA générative dans le respect de la charte d'usage du cycle, en indiquant en annexe lesquels et pour quoi faire. Le code présenté doit être compris et expliqué à l'oral par chaque membre du groupe ; un extrait que vous ne savez pas commenter vous coûtera plus qu'il ne vous rapportera.

Partez des problèmes réels. La plateforme actuelle a été découpée en services sans que ses données le soient : quatre services partagent la même base. Votre architecture doit montrer comment chaque contexte métier possède ses données et comment les contextes communiquent. Sinon, vous reproduirez le défaut que vous êtes censés corriger.

Un pattern se justifie par un besoin, pas par sa présence dans une liste. Le Strategy convient bien aux règles de facturation qui varient selon le type d'acte, l'Adapter aux intégrations avec des systèmes que vous ne contrôlez pas, le Proxy au contrôle d'accès aux dossiers médicaux. Le Singleton, lui, n'est accepté que si vous expliquez pourquoi l'injection de dépendances ne suffit pas.

La simplicité est une qualité. Le pôle plateforme de Medisecure compte dix personnes, dont deux alternants, et n'a aucune expérience des conteneurs en production. Une architecture que cette équipe ne saurait ni construire ni exploiter n'est pas une bonne architecture, même si elle est élégante.

Pensez enfin à la migration. La plateforme actuelle sert 4 200 patients télésurveillés, 7 jours sur 7. Il n'est pas question de l'arrêter un week-end pour basculer : votre stratégie de déploiement doit dire comment l'ancienne et la nouvelle version cohabitent pendant la transition.
