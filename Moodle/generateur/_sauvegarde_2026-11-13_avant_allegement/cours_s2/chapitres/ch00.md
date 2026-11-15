## 0. Introduction

> [!OBJECTIFS] Ce que vous saurez faire à la fin de ce chapitre
> Vous saurez expliquer à quoi sert ce cours et ce que le dossier D2 évalue. Vous connaîtrez la compétence visée, le déroulé de la semaine S2, la progression conseillée jusqu'au dépôt et la restitution orale. Vous saurez enfin comment travailler ce support, ses encadrés et ses études de documents, pour produire seul votre dossier pendant l'intersession.

### À quoi sert ce cours

Avant de décider où aller, une direction doit savoir d'où elle part. Le directeur général de Medisecure a demandé un schéma directeur, c'est-à-dire un plan qui fixe pour plusieurs années la cible du système d'information, les projets et leur ordre. Personne ne peut l'écrire sérieusement aujourd'hui. Le RSSI le dit sans détour : « Je n'ai ni cartographie ni journaux. Si nous sommes attaqués demain, je ne saurai pas ce qui a été touché. »

Ce cours vous apprend à produire l'état des lieux qui manque. Il commence par les notions de base, car on ne cartographie bien que ce que l'on comprend : ce qu'est une organisation, un système d'information, une stratégie. Il vous donne ensuite trois méthodes. La cartographie décrit le SI tel qu'il est, du métier jusqu'aux serveurs. L'analyse de risques dit ce qui peut mal tourner, avec quelle gravité et quelle vraisemblance. Le diagnostic critique juge l'ensemble, distingue les forces des faiblesses et formule les questions que le schéma directeur devra trancher.

Le cours s'appuie, comme en S1, sur deux organisations fictives. Kestrel Logistique, transporteur régional de 300 salariés en Auvergne-Rhône-Alpes, sert aux exemples travaillés : chaque méthode y est appliquée de bout en bout, de sa cartographie à son diagnostic. Medisecure, réseau de 14 centres de santé, reste le cas fil rouge : les exercices et votre dossier D2 portent sur elle. Les exercices ne sont jamais corrigés dans le cours, car le dossier est le vôtre.

### La compétence visée

Le dossier D2 valide la quatrième compétence du bloc 1 du titre RNCP 40573, « Définir une stratégie de systèmes d'information ». Avec le dossier D1, il forme la première mise en situation professionnelle de ce bloc. Le tableau suivant résume ce que la compétence exige concrètement de vous.

| Critère du référentiel | Ce que le correcteur attend de vous | Éléments de la grille |
| --- | --- | --- |
| La cartographie du SI est complète, avec l'inventaire des quatre niveaux (métier, fonctionnel, applicatif, infrastructure) | Sept vues construites avec un outil, cohérentes entre elles, appuyées sur des inventaires complets (applications, flux, infrastructure) et un modèle de cartographie explicite | E1 à E8 |
| Une méthode d'analyse de risques est appliquée | Les cinq ateliers d'EBIOS Risk Manager (ou les étapes équivalentes d'ISO/IEC 27005:2022) menés sur les biens supports de votre cartographie, puis les besoins de continuité confrontés à la capacité réelle de Medisecure | E9 à E15 |
| Le diagnostic du SI est détaillé, avec ses forces et ses faiblesses | Un diagnostic de l'environnement et des huit domaines internes, des forces et des faiblesses prouvées et hiérarchisées, des enjeux formulés pour la direction | E16 à E19 |

Ces trois parties s'enchaînent, et c'est leur enchaînement qui fait la valeur du dossier. La cartographie fournit les biens supports de l'analyse de risques. L'analyse de risques et l'analyse d'impact fournissent les preuves du diagnostic. Le diagnostic, enfin, fournit au dossier D3 ses points de départ. Un risque qui porte sur un serveur absent de votre cartographie, ou une faiblesse qui ne s'appuie sur aucun fait, rompt cette chaîne et coûte des points.

[[FIGURE:c00-chaine-d1-d2-d3|De la veille au schéma directeur : la place du dossier D2|Un schéma horizontal en trois blocs reliés par des flèches de gauche à droite. Bloc 1 « D1 · Veille (S1) » avec en dessous « ce qui change autour de Medisecure ». Bloc 2, plus grand et mis en valeur, « D2 · Cartographie, risques, diagnostic (S2) » découpé verticalement en trois sous-blocs empilés reliés par de petites flèches descendantes : « Cartographie : le SI tel qu'il est », « Risques et continuité : ce qui peut mal tourner », « Diagnostic : forces, faiblesses, enjeux ». Bloc 3 « D3 · Stratégie SI et architecture (S3) » avec en dessous « où aller, dans quel ordre, avec quel budget ». Une flèche en pointillés part du bloc 1 vers le sous-bloc « Diagnostic » avec l'étiquette « environnement externe, réglementation ». Sous l'ensemble, une bande « Compétences : C1 à C3 » sous le bloc 1, « C4 » sous le bloc 2, « C5 à C9 » sous le bloc 3.]]

### Le déroulé de la semaine S2

La semaine S2 compte cinq jours, du Jour 1 au Jour 5. Comme en S1, la théorie occupe le matin et les ateliers sur Medisecure l'après-midi. La semaine lance le dossier et vous donne les méthodes ; le travail de fond se fait ensuite, en autonomie, pendant l'intersession : deux semaines en entreprise et les trois week-ends qui les encadrent.

| Jour | Temps fort | Ce que vous devez produire |
| --- | --- | --- |
| Jour 1 | Le matin, contrôle du dossier D1 et élection des délégués. L'après-midi, lancement du dossier D2 et notions de base (chapitres 0 et 1) | Une première lecture de Medisecure : structures, processus, chaîne de valeur, plan 2030 traduit en vision, mission et objectifs |
| Jour 2 | Stratégie SI, gouvernance et urbanisation (chapitre 2), puis cartographie (chapitres 3 et 4) | L'outil de cartographie installé, le modèle de cartographie, les vues de l'écosystème, métier et applicative commencées, l'inventaire applicatif et la matrice des flux ouverts (exercice du chapitre 4) |
| Jour 3 | Sécurité et risque (chapitre 5), puis ateliers 1 et 2 d'EBIOS Risk Manager (chapitre 6) | Les échelles de gravité et de vraisemblance, les valeurs métier et leurs biens supports, les événements redoutés, les couples source de risque et objectif visé |
| Jour 4 | Vulnérabilités des infrastructures data et IA (chapitre 7), ateliers 3 à 5 (chapitre 6), analyse d'impact sur l'activité (chapitre 8) | Un premier scénario opérationnel, les vues des infrastructures commencées (fin de l'exercice du chapitre 4), la grille d'impact des onze lignes du tableau de continuité ouverte |
| Jour 5 | Environnement et diagnostic critique (chapitres 9 et 10), QCM de l'UE2, pitch d'étape, planning de l'intersession (chapitre 11) | Le PESTEL et le diagnostic de deux domaines commencés, votre pitch de 5 minutes et votre planning des deux périodes de l'intersession |

Le pitch du Jour 5 est un point d'étape, non noté. En cinq minutes, vous montrez votre outil de cartographie avec au moins trois vues commencées, vos échelles de gravité et de vraisemblance, et vos valeurs métier. Vous recevez un retour oral. Le QCM du Jour 5, lui, est noté au titre du contrôle continu de l'UE2 : il porte sur les notions des chapitres 1 à 10. Le contenu exact de chaque atelier peut être ajusté par l'équipe pédagogique : le planning publié sur Moodle fait foi.

> [!ATTENTION] Une cartographie ne se dessine pas au dernier moment
> La cartographie est la base de tout le reste : l'analyse de risques nomme ses biens supports, l'analyse d'impact suit ses dépendances, le diagnostic cite ses constats. Si vos vues ne sont pas commencées dans un outil à la fin du Jour 2, vous rédigerez l'analyse de risques sur des objets qui n'existent pas encore, puis vous devrez tout renommer. Choisissez votre outil dès le Jour 2, même imparfaitement, et construisez le modèle avant de dessiner.

### Le dossier D2 et son calendrier

Le dossier D2 est individuel. Vous pouvez comparer des outils et des notations avec vos pairs, mais vos schémas, votre analyse de risques et votre diagnostic sont personnels. Le dossier compte 20 à 25 pages, synthèse comprise, hors annexes. Vous déposez deux fichiers sur Moodle : le dossier en un seul PDF, annexes comprises, et le fichier source de votre cartographie. Huit annexes, de A à H, contiennent les inventaires et les tableaux qui prouvent ce que vous affirmez, comme le résume le tableau suivant.

| Annexe | Contenu |
| --- | --- |
| A. Inventaire applicatif | Les 18 applications du parc et au moins un usage hors inventaire, avec au moins dix attributs chacun en plus du nom, dont les quatre attributs de sécurité |
| B. Matrice des flux | Au moins 15 flux, renseignés sur sept champs |
| C. Matrice processus × applications | Les applications utilisées par chaque processus de la vue métier |
| D. Inventaire de l'infrastructure | Sites, salles, serveurs, stockage, sauvegardes, liens, équipements de sécurité, postes |
| E. Tableaux de l'analyse de risques | Les tableaux complets des cinq ateliers |
| F. Grille d'analyse d'impact | Les besoins de continuité, ligne par ligne du tableau des métiers, avec les applications que couvre chaque ligne |
| G. Preuves de la cartographie | Une capture de l'outil pour chaque vue, avec le nom du fichier, et la liste des objets, exportée de l'outil ou tenue à part |
| H. Hypothèses, sources et usage de l'IA | Les hypothèses numérotées, les sources extérieures, les usages de l'IA générative |

Après la semaine S2 vient l'intersession, en entreprise : deux semaines de travail encadrées par trois week-ends, que le chapitre 11 découpe en deux périodes. Le dossier se dépose ensuite sur Moodle. Après le dépôt, lors de la restitution orale, vous présentez votre état des lieux en 8 minutes à un comité de direction simulé, puis vous répondez à 4 minutes de questions. Cette restitution est notée à part, au titre du contrôle continu de l'UE2. Les modalités figurent dans les consignes du dossier D2 publiées sur Moodle.

Le tableau suivant relie chaque chapitre du cours aux parties du dossier et aux éléments E1 à E20 de la grille d'évaluation. Servez-vous-en pour savoir quoi relire quand vous rédigez une partie.

| Chapitre du cours | Parties du dossier D2 | Éléments de la grille concernés |
| --- | --- | --- |
| 1. Organisation, système d'information, stratégie | 1.1 ; vocabulaire de tout le dossier | E20 (présence de 1.1) ; bases de E2 c (structures juridiques), E3 a (classement des processus) et E18 c (plan 2030) |
| 2. Du SI à la stratégie SI | 1.1, 2.1, 2.4 ; domaine « gouvernance du SI » de 5.2 | E1 c (vues et quatre niveaux) ; E4 (vue fonctionnelle) ; E17 |
| 3. Cartographier le SI | 1.2, 2.1, 2.2 ; notions communes à toutes les vues | E1 (périmètre, modèle, outil) ; E2 (écosystème) |
| 4. Construire et faire vivre la cartographie | 2.3 à 2.8 ; annexes A, B, C, D et G | E3 à E8 ; E1 (annexe G et fichier source) |
| 5. Sécurité et risque | 3.1 ; socle de 3.2 | E9 (méthode et échelles) ; E10 c (socle) |
| 6. Analyser les risques avec EBIOS Risk Manager | 3.2 à 3.6 ; annexe E | E10 à E14 |
| 7. Les vulnérabilités des infrastructures data et IA | 3.5 ; 2.5 et annexes A et B ; domaines « données » et « sécurité » de 5.2 | E13 (scénario sur les données ou l'IA) ; E5 ; E17 |
| 8. Analyse d'impact sur l'activité et besoins de continuité | Partie 4 ; annexe F | E15 |
| 9. Analyser l'environnement du SI | 5.1 | E16 |
| 10. Le diagnostic critique du SI | 5.2 à 5.4 ; synthèse ; partie 6 | E17 à E19 ; E20 (présence de la synthèse et de la partie 6) |
| 11. Passer à l'autonomie | Organisation de l'intersession ; restitution orale | Tous, par l'auto-évaluation |
| 12. Annexes | Gabarits des annexes A à H | E1, E5, E9 à E19 |

> [!DOSSIER] Lire la grille avant d'écrire
> Chacun des 20 éléments de la grille vaut un point et se décompose en trois conditions vérifiables. Trois conditions remplies donnent 1 point, deux donnent 0,5 point, une ou aucune donne 0. Une condition est remplie ou ne l'est pas, jamais à moitié. Lisez donc les descripteurs des consignes avant d'écrire chaque partie. Prenez aussi l'habitude de citer la section du dossier de présentation entre parenthèses après chaque fait : le correcteur en vérifie cinq au hasard, et beaucoup de conditions portent sur des « faits sourcés ».

### Comment utiliser ce cours

Le cours se lit dans l'ordre, car chaque méthode s'appuie sur la précédente : on comprend l'organisation avant de cartographier son SI, on cartographie avant d'analyser les risques, on analyse avant de juger. Chaque chapitre de méthode s'ouvre sur ses objectifs et comprend au moins un exercice et une étude de document. Comptez environ une heure de lecture attentive par chapitre de méthode, et deux pour le chapitre 6.

Les encadrés ont chacun un rôle. OBJECTIFS annonce ce que vous saurez faire. DÉFINITION donne, en quelques phrases, le sens exact d'une notion clé : c'est votre rappel de cours, à connaître pour le QCM et à employer correctement dans le dossier. EXEMPLE montre la méthode appliquée à Kestrel Logistique : lisez-le comme un modèle de raisonnement, pas comme un texte à recopier, car Medisecure n'a ni les mêmes métiers ni les mêmes risques. MÉTHODE donne une démarche pas à pas. ATTENTION signale un piège fréquent. DOSSIER indique la section du D2 et l'élément de la grille concernés. EXERCICE vous fait appliquer la méthode à Medisecure, avec une durée indicative et un livrable.

L'encadré ÉTUDE DE DOCUMENT est nouveau par rapport à la S1. Il vous propose un texte à analyser : un article de presse ou un entretien fictifs, un cas réel résumé à partir de sources vérifiées, ou un court extrait d'un guide officiel. Des questions de réflexion l'accompagnent. Elles vont de la compréhension du texte à sa critique, puis à son application à Medisecure ou à votre entreprise d'alternance. Ces études servent de support aux discussions en séance. Préparez-les par écrit en quelques lignes : elles entraînent au raisonnement attendu dans le diagnostic et à l'oral de restitution.

Faites les exercices au moment où vous les rencontrez. Leurs livrables sont les briques de votre dossier : une vue bâclée au Jour 2 se paie pendant toute l'intersession. Gardez-les dans un même dossier de travail, daté, et ne conservez pas votre fichier de cartographie sur un service en ligne accessible sans contrôle d'accès, comme le demandent les consignes.

La semaine S2 est chargée, et tous les exercices n'ont pas le même poids. Le tableau suivant distingue les exercices indispensables, dont le livrable entre directement dans le dossier D2, et les exercices facultatifs, utiles pour s'entraîner ou pour nourrir une partie. Si le temps manque, faites d'abord les premiers.

Les exercices indispensables représentent près de 40 heures de travail, bien plus que les après-midi d'atelier de la semaine. Vous ne les finirez donc pas tous en S2 : la dernière colonne indique ce qui se fait en séance et ce qui se termine pendant l'intersession. Le planning du chapitre 11 tient compte de ce report.

| Chapitre | Exercice | Statut | Usage dans le dossier D2 | Durée indicative | En séance, puis en intersession |
| --- | --- | --- | --- | --- | --- |
| 1 | Situer Medisecure : structure, chaîne de valeur, stratégie | Indispensable | Section 1.1 et première carte des processus | 2 h 30 | Jour 1 ; repris en fin de période 1 pour la section 1.1 |
| 2 | McFarlan et gouvernance chez Medisecure | Facultatif | Peut nourrir le domaine « gouvernance du SI » de 5.2 | 2 h 30 | En autonomie, si le temps le permet |
| 3 | Le modèle de cartographie et la vue de l'écosystème de Medisecure | Indispensable | Sections 2.1 et 2.2 | 3 heures | Jour 2 ; achevé en période 1 |
| 4 | L'inventaire applicatif, la matrice des flux et la vue applicative de Medisecure, puis la vue physique | Indispensable | Sections 2.5 et 2.6 (vue physique), annexes A et B | 4 heures, puis 2 heures | Jour 2 (annexes A et B, vue applicative), Jour 4 (vue physique) ; achevé en période 1 |
| 5 | Les échelles de Medisecure et cinq écarts au socle | Indispensable | Sections 3.1 et 3.2 | 2 h 30 | Jour 3 |
| 6 | Ateliers 1 à 5 sur Medisecure | Indispensable | Sections 3.2 à 3.6, annexe E | 14 heures au total | Ateliers 1 et 2 au Jour 3, ateliers 3 à 5 commencés au Jour 4 ; achevés en période 2 |
| 7 | Repérer les vulnérabilités data et IA de Medisecure et construire un scénario | Indispensable | Section 3.5 | 2 h 30 | Commencé au Jour 4 ; achevé en période 2 |
| 8 | La grille d'impact de Medisecure | Indispensable | Partie 4, annexe F | 2 h 30 | Grille ouverte au Jour 4 ; achevée en période 2 |
| 9 | Le PESTEL du SI de Medisecure et les cinq forces | Indispensable | Section 5.1 | 2 h 30 | Commencé au Jour 5 ; achevé en période 2 |
| 10 | Diagnostiquer deux domaines de Medisecure et formuler des enjeux | Indispensable | Sections 5.2 à 5.4 | 3 heures | Commencé au Jour 5 ; achevé en période 2 |
| 11 | Faire le point à mi-parcours | Facultatif | Auto-évaluation, non remise | 45 minutes | Au milieu de l'intersession, après le gel des noms |

Pendant l'intersession, vous serez seul face au cas. Le chapitre 11 vous propose un planning et une check-list d'auto-évaluation alignée sur la grille. Avant de poser une question, relisez la consigne du dossier et le dossier de présentation de Medisecure : la plupart des réponses s'y trouvent. En cas de divergence entre ce cours et les consignes du dossier D2, les consignes font foi. Enfin, toute information datée citée dans ce cours, version d'une norme ou état d'un texte, a été vérifiée à la date de rédaction ; certaines évoluent vite, et vous devez en vérifier l'état actuel. Quand le cours signale un point incertain, vérifiez-le : vous mettez ainsi en pratique la veille de la S1.
