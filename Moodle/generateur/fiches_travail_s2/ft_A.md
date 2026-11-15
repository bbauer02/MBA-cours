# FT 01 | L'organisation vue comme un système | 1

@situation
Vous êtes stagiaire à la DSI de Kestrel Logistique en mars 2026. Hélène Garnier, directrice des SI, prépare un déplacement à l'agence de Clermont-Ferrand, le plus petit des trois sites. Elle vous demande de décrire l'agence avec le vocabulaire de la gestion : ses ressources, son fonctionnement en sous-systèmes et la manière dont l'information y circule, pour repérer où elle circule mal.

@capacites
Repérer la finalité et les ressources d'une organisation
Décrire un circuit physique à partir d'un entretien
Calculer une moyenne et un écart relatif
Appliquer le modèle systémique de Le Moigne
Distinguer donnée, information et connaissance
Caractériser une structure et une configuration de Mintzberg
Argumenter à partir d'une grille d'analyse

@duree 60 minutes

@annexe 1 | « Je découvre les tournées le matin » | Source fictive : compte rendu d'entretien avec le responsable de l'agence de Clermont-Ferrand, DSI, mars 2026
La navette de nuit arrive de Saint-Priest vers 3 h 30 avec les colis à livrer dans la journée. Les agents de quai la déchargent, scannent chaque colis, puis le trient par tournée. Une seconde navette repart le soir vers Saint-Priest avec les colis enlevés chez les clients auvergnats.

Les tournées ont été construites la veille au soir par les planificateurs de Saint-Priest. « Je les découvre le matin. Si un chauffeur est absent, je refais l'affectation au téléphone avec le chef de quai. » Vers 6 h, les chauffeurs partent avec leur terminal KDriver ; les preuves de livraison remontent dans Kestrel Track sans intervention.

Quand un colis arrive abîmé, le chef de quai le note à la main dans un cahier ; une assistante d'exploitation prévient ensuite le client par téléphone. « Chaque lundi, je reçois de Saint-Priest un tableau Excel des retards de la semaine passée. Je n'ai pas d'accès direct aux chiffres. Je décide des renforts en intérimaires le jeudi, pour la semaine suivante, à l'expérience : je sais que le lundi est notre jour le plus chargé, parce que les magasins de la grande distribution se réapprovisionnent après le week-end. »

Les tarifs des clients auvergnats sont négociés au siège par la direction commerciale ; le commercial de l'agence lui transmet les demandes. L'agence rend compte chaque semaine, en visioconférence, au directeur des opérations, Sébastien Morin.

@annexe 2 | L'agence de Clermont-Ferrand en bref | Source fictive : fiche d'identité interne de l'agence, direction des opérations, janvier 2026
| Élément | Valeur |
| --- | --- |
| Effectif | 35 salariés : 1 responsable de l'agence, 1 chef de quai, 11 agents de quai, 18 chauffeurs, 2 assistantes d'exploitation, 1 commercial, 1 technicien d'atelier |
| Tournées | 24 par jour, dont 6 confiées à des sous-traitants du dernier kilomètre |
| Rattachement | Directeur des opérations ; le commercial dépend de la directrice commerciale, Léa Fontaine |
| Liaison avec le siège | Tunnel VPN sur fibre, 100 Mbit/s, sans lien de secours |
| Outils utilisés | KDriver, scanners de quai reliés à StockFlow, Kestrel Track en consultation, Microsoft 365 ; cahier de quai sur papier |

@annexe 3 | Colis traités par l'agence, semaine type de février 2026 | Source fictive : relevé des scans de quai, direction des opérations
@graphique barres colis par jour
Lundi : 1520
Mardi : 1310
Mercredi : 1260
Jeudi : 1290
Vendredi : 1220

@annexe 4 | Le circuit physique d'un colis à l'agence | Source fictive : schéma de travail de la DSI, mars 2026, à compléter à partir de l'annexe 1
@schema
Arrivée :: Navette de nuit depuis Saint-Priest -> [[Déchargement et scan de chaque colis]] -> [[Tri par tournée]]
... -> Départ des chauffeurs vers 6 h -> [[Livraison et preuve de livraison dans KDriver]]
Retour :: Enlèvements chez les clients auvergnats -> [[Navette du soir vers Saint-Priest]]

@question 1 | Identifier | Annexes 1 et 2
Indiquez la finalité de l'agence au sein de Kestrel, puis donnez pour chacune des cinq catégories de ressources du cours un exemple propre à l'agence. Si les annexes ne décrivent aucune ressource propre à l'agence dans une catégorie, dites-le et expliquez pourquoi.
@tableau
| Élément | Ce que l'on observe à l'agence de Clermont-Ferrand |
| --- | --- |
| Finalité | |
| Ressource humaine | |
| Ressource financière | |
| Ressource matérielle | |
| Ressource immatérielle | |
| Ressource informationnelle | |

@question 2 | Identifier | Annexes 1 et 4
Complétez le schéma de l'annexe 4 à partir de l'entretien.

@question 3 | Calculer | Annexes 2 et 3
Calculez le nombre moyen de colis traités par jour pendant la semaine type, puis l'écart du lundi à cette moyenne, en colis et en pourcentage. Calculez enfin la part de l'agence dans les 9 000 colis quotidiens de Kestrel et comparez-la à sa part dans l'effectif total de 300 salariés.
@lignes 6

@question 4 | Mobiliser | Annexes 1, 2 et 4
Appliquez à l'agence le modèle systémique de Le Moigne : pour chaque sous-système, citez ses éléments à l'agence et une information qu'il émet ou reçoit.
@tableau
| Sous-système | Éléments à l'agence | Information émise ou reçue |
| --- | --- | --- |
| Système de pilotage | | |
| Système d'information | | |
| Système opérant | | |

@question 5 | Analyser | Annexes 1 et 3
Qualifiez chacun des éléments suivants de donnée, d'information ou de connaissance, et justifiez.
@tableau
| Élément tiré des annexes | Nature | Justification |
| --- | --- | --- |
| Le scan d'un colis sur le quai | | |
| Le tableau Excel des retards de la semaine passée | | |
| « Le lundi est notre jour le plus chargé » | | |

@question 6 | Analyser | Annexes 1 et 2
L'agence de Clermont-Ferrand est-elle une division au sens des structures du cours ? Caractérisez la structure de Kestrel telle qu'on la voit depuis l'agence, puis indiquez de quelle configuration de Mintzberg relève le travail du quai.
@lignes 6

@question 7 | Argumenter | Toutes les annexes
En vous appuyant sur le modèle de Le Moigne, montrez dans un paragraphe argumenté que les échanges d'information entre le pilotage et le système opérant de l'agence présentent des faiblesses. Vous ne proposerez pas de solution technique.
@lignes 10

@retiens
Selon Le Moigne, une organisation se décompose en trois sous-systèmes : le système [[opérant]], qui transforme des entrées en sorties, le système de [[pilotage]], qui décide et contrôle, et le système d'[[information]], qui relie les deux. Une organisation mobilise cinq catégories de ressources ; la ressource [[informationnelle]] comprend les données, les documents et les connaissances partagées. Une [[donnée]] est un fait brut ; mise en contexte, elle devient une information ; interprétée et reliée à l'expérience, elle devient une [[connaissance]]. Une connaissance écrite nulle part repose sur les personnes qui la détiennent : leur départ est une perte qu'aucune [[sauvegarde]] ne compense.

@corrige 1
| Élément | Ce que l'on observe à l'agence de Clermont-Ferrand |
| --- | --- |
| Finalité | Livrer à temps les colis de sa zone et collecter les enlèvements des clients auvergnats ; elle concourt à la finalité de Kestrel, entreprise privée : vendre un service de transport avec profit |
| Ressource humaine | 35 salariés, dont 18 chauffeurs et 11 agents de quai ; savoir-faire du tri |
| Ressource financière | Aucune ressource propre décrite : l'agence dépend du budget de Kestrel SAS et, au-delà, de Vidal Participations |
| Ressource matérielle | Quai, navettes, terminaux KDriver, scanners, lien VPN de 100 Mbit/s |
| Ressource immatérielle | Relations avec les clients auvergnats, savoir-faire collectif de l'équipe, connaissance du terrain |
| Ressource informationnelle | Tournées, scans, preuves de livraison, cahier de quai, tableau des retards |

L'agence n'est pas une organisation autonome : sa finalité est un sous-objectif de celle de Kestrel. Notion mobilisée : chapitre 1, « L'organisation : finalités, ressources, structure ». Accepter tout exemple juste et sourcé ; la ligne « financière » est la plus délicate, la réponse attendue est l'absence de ressource propre.

@corrige 2
Le schéma complété se lit ainsi : navette de nuit, déchargement et scan de chaque colis, tri par tournée, départ des chauffeurs vers 6 h, livraison et preuve de livraison dans KDriver ; en retour, les enlèvements chez les clients auvergnats repartent par la navette du soir vers Saint-Priest. C'est le flux physique du système opérant : les entrées (colis reçus) sont transformées en sorties (colis livrés). L'enseignant peut faire remarquer que le scan et la preuve de livraison sont aussi des points de collecte d'information : chaque geste physique produit une donnée (chapitre 1, « Fonctions et rôles du SI »).

@corrige 3
Moyenne : (1 520 + 1 310 + 1 260 + 1 290 + 1 220) / 5 = 6 600 / 5 = 1 320 colis par jour.

Écart du lundi : 1 520 − 1 320 = + 200 colis, soit 200 / 1 320 = + 15,2 % au-dessus de la moyenne.

Part de l'agence dans les colis : 1 320 / 9 000 = 14,7 %. Part dans l'effectif : 35 / 300 = 11,7 %. L'agence traite donc une part des colis supérieure à sa part des salariés (environ 37,7 colis par salarié et par jour, contre 9 000 / 300 = 30 pour Kestrel). Le pic du lundi confirme par les chiffres ce que le responsable sait par expérience (annexe 1). Le calcul n'autorise pas à conclure sur la productivité : une partie des tournées est sous-traitée et les métiers diffèrent selon les sites.

@corrige 4
| Sous-système | Éléments à l'agence | Information émise ou reçue |
| --- | --- | --- |
| Système de pilotage | Responsable de l'agence, chef de quai ; au-dessus, Sébastien Morin et les planificateurs de Saint-Priest | Reçoit le tableau des retards ; émet les décisions de renfort et les réaffectations de tournées |
| Système d'information | KDriver, StockFlow et ses scanners, Kestrel Track, Microsoft 365, mais aussi le cahier de quai, le téléphone et les procédures | Mémorise les scans et les preuves de livraison ; transmet les tournées ; diffuse le tableau des retards |
| Système opérant | Agents de quai, chauffeurs, sous-traitants, navettes | Émet des scans, des preuves de livraison, des signalements de colis abîmés ; reçoit les tournées affectées |

Notion : chapitre 1, « L'approche systémique de Le Moigne ». Point d'attention : le cahier de quai et le téléphone font partie du système d'information, même s'ils ne sont pas informatiques.

@corrige 5
| Élément tiré des annexes | Nature | Justification |
| --- | --- | --- |
| Le scan d'un colis sur le quai | Donnée | Fait brut enregistré (un code, une heure, un lieu), sans interprétation |
| Le tableau Excel des retards de la semaine passée | Information | Données mises en contexte et transmises à un destinataire, à qui elles ont un sens |
| « Le lundi est notre jour le plus chargé » | Connaissance | Interprétation reliée à l'expérience, qui permet d'agir (décider des renforts) ; elle n'est écrite nulle part |

Notion : chapitre 1, « Donnée, information, connaissance ». L'annexe 3 confirme la connaissance par des données : c'est l'intérêt d'un SI qui mémorise.

@corrige 6
L'agence n'est pas une division. Une division possède ses propres fonctions et une autonomie sur un marché ou une région ; or l'agence ne négocie pas ses tarifs (direction commerciale), ne construit pas ses tournées (planificateurs du siège) et rend compte au directeur des opérations. Son commercial dépend même d'une autre direction que le reste de l'équipe. Kestrel a donc une structure fonctionnelle, à laquelle les sites ajoutent une dimension géographique. Le recours à des sous-traitants pour 6 tournées sur 24 ajoute un trait de structure en réseau. Le travail du quai (scanner, trier, charger selon des gestes standardisés) relève de la bureaucratie mécaniste de Mintzberg, coordonnée par la standardisation des procédés. Notion : chapitre 1, « Les structures et les configurations de Mintzberg ».

@corrige 7
Éléments attendus. L'information montante arrive tard et sous une forme pauvre : le pilotage de l'agence reçoit les retards une fois par semaine, dans un tableau Excel, sans accès direct aux chiffres ; il décide donc des renforts « à l'expérience », sur une connaissance tacite. Une partie de l'information opérationnelle n'est pas mémorisée de façon exploitable : les colis arrivés abîmés sont notés dans un cahier papier, puis signalés au client par téléphone ; ce cahier ne permet ni partage ni statistique. L'information descendante arrive sans concertation : les tournées sont construites au siège la veille et découvertes le matin ; les réaffectations faites au téléphone ne laissent pas de trace écrite dans les annexes. Enfin, une seule liaison sans secours relie l'agence au siège (annexe 2). Le modèle montre que le système opérant fonctionne, mais que le pilotage local décide en partie à l'aveugle.

Barème indicatif sur 5 points : 1 point pour l'usage correct des trois sous-systèmes ; 1 point par faiblesse justifiée par une annexe (trois attendues) ; 1 point pour la qualité de la rédaction et l'absence de solution technique imposée.

# FT 02 | Chaîne de valeur et processus | 1

@situation
En avril 2026, Léa Fontaine, directrice commerciale, se plaint qu'il faille « près de trois semaines » pour faire démarrer un nouveau client e-commerçant. Alternant à la DSI, vous êtes chargé par Hélène Garnier de décrire ce processus, de le situer dans la chaîne de valeur de Kestrel et de repérer les passages de relais où l'information se perd.

@capacites
Caractériser un processus : déclencheur, résultat, acteurs
Calculer un délai de bout en bout et un taux de transformation
Situer des activités dans la chaîne de valeur de Porter
Classer des processus en pilotage, réalisation et support
Repérer les passages de relais et argumenter

@duree 60 minutes

@annexe 1 | Comment arrive un nouvel e-commerçant | Source fictive : courriel de Léa Fontaine à Hélène Garnier, avril 2026
Hélène, voici comment se passe aujourd'hui l'arrivée d'un nouveau client e-commerçant. La demande arrive par le formulaire du site web, sous forme de courriel, dans la boîte de l'assistante commerciale. Elle la transmet à un commercial, qui rappelle le prospect, calcule le prix dans un tableur à partir de la grille tarifaire, puis met le devis en forme dans un traitement de texte. Le contrat signé revient par courrier ou en pièce jointe ; je le contresigne.

L'assistante commerciale envoie alors à la comptabilité une fiche client (raison sociale, adresse de facturation, coordonnées bancaires) pour créer le client dans l'ERP finance. En parallèle, elle demande par courriel à la DSI d'ouvrir un compte sur le portail B2B de Kestrel Track ; le technicien support y ressaisit les coordonnées du client. L'exploitation enregistre enfin le premier ordre d'enlèvement dans RoutePro.

Comme ces e-commerçants n'utilisent pas l'EDI, leurs ordres arrivent ensuite chaque jour par courriel, dans un fichier tableur, et une assistante d'exploitation les saisit dans RoutePro. Au premier trimestre, un prospect a signé chez un concurrent pendant ce délai de démarrage.

@annexe 2 | Délais moyens du démarrage d'un e-commerçant | Source fictive : relevé de la direction commerciale sur les 12 derniers clients signés, mars 2026
| Étape | Acteur | Support ou outil | Délai moyen (jours ouvrés) |
| --- | --- | --- | --- |
| 1. Recevoir et transmettre la demande | Assistante commerciale | Site web, messagerie | 1 |
| 2. Établir et envoyer le devis | Commercial | Tableur, traitement de texte | 3 |
| 3. Obtenir le contrat signé | Prospect, directrice commerciale | Papier ou PDF | 6 |
| 4. Créer le client dans l'ERP finance | Comptabilité | ERP finance | 2 |
| 5. Ouvrir le compte du portail B2B (en parallèle de l'étape 4) | Technicien support de la DSI | Kestrel Track | 3 |
| 6. Enregistrer le premier ordre d'enlèvement (après les étapes 4 et 5) | Assistante d'exploitation | RoutePro | 2 |

@annexe 3 | Demandes de devis d'e-commerçants reçues par le site web en 2025 | Source fictive : direction commerciale ; 27 contrats signés sur l'année
@graphique barres demandes
1er trimestre : 38
2e trimestre : 45
3e trimestre : 41
4e trimestre : 56

@annexe 4 | Le processus « Faire démarrer un nouvel e-commerçant » | Source fictive : schéma de travail de la DSI, avril 2026, à compléter
@schema
[[Déclencheur : une demande de devis arrive par le site web]] -> Vendre : devis et contrat signé -> [[Créer le client : ERP finance et portail B2B]]
... -> Enregistrer le premier ordre dans RoutePro -> [[Résultat : premier colis enlevé chez le client]]

@question 1 | Identifier | Annexes 1, 2 et 4
Complétez le schéma de l'annexe 4 : l'événement déclencheur, l'activité manquante et le résultat du processus.

@question 2 | Identifier | Annexes 1 et 2
Pour qui ce processus crée-t-il de la valeur ? Combien de services traverse-t-il ? À quelle famille de processus appartient-il ? Expliquez pourquoi on parle ici d'un processus et non d'une fonction.
@lignes 5

@question 3 | Calculer | Annexes 2 et 3
Calculez la durée du processus en additionnant toutes les étapes, puis sa durée réelle en tenant compte des étapes menées en parallèle. Calculez la part de cette durée réelle qui dépend du prospect et celle qui dépend de Kestrel. Calculez enfin le taux de transformation des demandes de devis en contrats en 2025.
@lignes 7

@question 4 | Mobiliser | Annexe 1 et cours
Situez chaque activité dans la chaîne de valeur de Porter.
@tableau
| Activité de Kestrel | Activité de la chaîne de valeur | Principale ou de soutien |
| --- | --- | --- |
| Rappeler le prospect et établir le devis | | |
| Enregistrer l'ordre d'enlèvement dans RoutePro | | |
| Créer le client dans l'ERP finance et le facturer | | |
| Ouvrir le compte du client sur le portail B2B | | |
| Recruter une assistante d'exploitation supplémentaire | | |
| Choisir un sous-traitant pour livrer les colis du nouveau client | | |

@question 5 | Mobiliser | Annexe 1 et cours
Classez les processus suivants de Kestrel dans leur famille et justifiez en quelques mots.
@tableau
| Processus | Famille | Justification |
| --- | --- | --- |
| Faire démarrer un nouvel e-commerçant | | |
| Traiter une réclamation pour colis endommagé | | |
| Préparer les indicateurs du comité de direction mensuel | | |
| Créer et supprimer les comptes des utilisateurs | | |
| Choisir les secteurs à prospecter en 2027 | | |

@question 6 | Analyser | Annexes 1 et 2
Repérez trois passages de relais du processus où l'information change de support ou est ressaisie. Pour chacun, dites quelle information circule et quel risque il fait courir.
@lignes 7

@question 7 | Argumenter | Toutes les annexes
Dans une note de dix lignes à Léa Fontaine, montrez que ce processus freine l'objectif de « Cap 2029 » de porter la part e-commerce à 40 % du chiffre d'affaires, et expliquez ce que l'analyse par processus apporte par rapport à la lecture de l'organigramme.
@lignes 10

@retiens
La chaîne de valeur de Porter distingue les activités [[principales]], qui créent, vendent et servent le produit, et les activités de [[soutien]], qui les rendent possibles ; la différence entre la valeur créée et le coût des activités forme la [[marge]]. Un [[processus]] est un enchaînement d'activités qui transforme des éléments d'entrée en résultats ayant de la valeur pour un [[client]], interne ou externe. Il traverse souvent plusieurs [[services]], ce qui le distingue d'une fonction. On distingue les processus de pilotage, de [[réalisation]] et de [[support]]. Chaque passage de relais est un endroit où une donnée peut être [[ressaisie]], perdue ou retardée.

@corrige 1
Déclencheur : une demande de devis arrive par le formulaire du site web. Activité manquante : créer le client, dans l'ERP finance et sur le portail B2B de Kestrel Track. Résultat : le premier colis est enlevé chez le nouveau client. Un processus se décrit de l'événement déclencheur au résultat, sans suivre l'organigramme (chapitre 1, « Les processus : pilotage, réalisation, support », et chapitre 4, « Dessiner vue par vue »).

@corrige 2
Le processus crée de la valeur pour un client externe, l'e-commerçant, qui peut commencer à expédier. Il traverse quatre services internes, la direction commerciale (assistante, commercial, directrice), la comptabilité, la DSI et l'exploitation, et fait intervenir un acteur externe, le prospect. C'est un processus de réalisation, puisqu'il produit directement la valeur pour le client. On parle de processus et non de fonction parce que l'enchaînement traverse plusieurs services et a un début et une fin identifiables ; une fonction, comme la comptabilité, regroupe des personnes par métier. Notion : chapitre 1, « Les processus : pilotage, réalisation, support ».

@corrige 3
Durée en additionnant toutes les étapes : 1 + 3 + 6 + 2 + 3 + 2 = 17 jours ouvrés.

Durée réelle : les étapes 4 et 5 se déroulent en parallèle ; on retient la plus longue, 3 jours. 1 + 3 + 6 + 3 + 2 = 15 jours ouvrés, soit trois semaines : les « près de trois semaines » de Léa Fontaine sont confirmés.

Part du prospect (étape 3) : 6 / 15 = 40 %. Part de Kestrel : 9 / 15 = 60 %. L'essentiel du délai dépend donc de Kestrel.

Demandes de devis en 2025 : 38 + 45 + 41 + 56 = 180. Taux de transformation : 27 / 180 = 15 %. Ce taux, rapproché du prospect perdu, suggère que le délai coûte des clients ; l'annexe ne permet pas de le prouver.

@corrige 4
| Activité de Kestrel | Activité de la chaîne de valeur | Principale ou de soutien |
| --- | --- | --- |
| Rappeler le prospect et établir le devis | Commercialisation et vente | Principale |
| Enregistrer l'ordre d'enlèvement dans RoutePro | Logistique d'entrée | Principale |
| Créer le client dans l'ERP finance et le facturer | Infrastructure de l'entreprise (finance, comptabilité) | Soutien |
| Ouvrir le compte du client sur le portail B2B | Développement technologique (la DSI paramètre l'outil) ; le portail lui-même sert l'activité « services » | Soutien |
| Recruter une assistante d'exploitation supplémentaire | Gestion des ressources humaines | Soutien |
| Choisir un sous-traitant pour livrer les colis du nouveau client | Approvisionnements | Soutien |

Notion : chapitre 1, « La chaîne de valeur de Porter ». La ligne du portail B2B se discute ; on accepte « services » si l'élève distingue l'usage de l'outil (principale) et son administration par la DSI (soutien).

@corrige 5
| Processus | Famille | Justification |
| --- | --- | --- |
| Faire démarrer un nouvel e-commerçant | Réalisation | Produit directement la valeur pour un client externe |
| Traiter une réclamation pour colis endommagé | Réalisation | Fait partie du service rendu au client |
| Préparer les indicateurs du comité de direction mensuel | Pilotage | Sert à contrôler les résultats et à décider |
| Créer et supprimer les comptes des utilisateurs | Support | Fournit une ressource (l'accès au SI) aux autres processus |
| Choisir les secteurs à prospecter en 2027 | Pilotage | Fixe une orientation |

Notion : chapitre 1, « Les processus : pilotage, réalisation, support ».

@corrige 6
Trois passages de relais sont attendus parmi les suivants. Du site web à l'assistante commerciale, puis au commercial : la demande circule par courriel ; elle peut rester sans suite si personne n'en assure le suivi. De l'assistante commerciale à la comptabilité et à la DSI : les coordonnées du client passent par une fiche puis par un courriel, et sont saisies deux fois, dans l'ERP finance et dans le portail B2B ; risque d'incohérence entre les deux applications et délai de 2 à 3 jours. Du client à l'exploitation : les ordres quotidiens arrivent dans un fichier tableur par courriel et sont saisis à la main dans RoutePro ; risque d'erreur de saisie et charge qui croîtra avec le nombre d'e-commerçants. On peut ajouter le contrat papier, qui oblige à une numérisation et ne laisse pas de trace partagée. Pour aller plus loin, avec le vocabulaire du chapitre 4 : la saisie des ordres dans RoutePro est un flux manuel ; les coordonnées du client saisies dans deux applications de fonctions différentes relèvent d'un défaut de donnée de référence, non d'une redondance.

@corrige 7
Éléments attendus. L'objectif « Cap 2029 » suppose de signer et de faire démarrer beaucoup de petits clients ; or chaque démarrage prend 15 jours ouvrés, dont 60 % du fait de Kestrel (question 3), et au moins un prospect est parti pendant ce délai. Le processus repose sur des ressaisies (coordonnées du client dans deux applications, ordres quotidiens saisis à la main dans RoutePro) : sa charge augmente avec chaque nouveau client, alors que l'objectif est précisément d'en augmenter le nombre. Le taux de transformation de 15 % montre une marge de progrès. L'organigramme montre quatre services séparés, chacun efficace dans son périmètre ; seule la vue par processus révèle les attentes entre eux et les ressaisies, car un processus traverse les services. La note peut dire ce que l'objectif exige du SI (recevoir des ordres sans ressaisie, créer un client une seule fois) sans choisir d'outil.

Barème indicatif sur 5 points : 2 points pour le lien chiffré avec l'objectif, 1 point pour les ressaisies identifiées, 1 point pour l'apport de la vue processus, 1 point pour la forme de la note.

# FT 03 | Système d'information, système informatique et familles d'applications | 1

@situation
En mai 2026, Isabelle Roux, directrice administrative et financière, à qui la DSI est rattachée, prépare une présentation du SI de Kestrel pour le conseil de Vidal Participations. Stagiaire à la DSI, vous relisez sa note. Vous venez aussi de passer une demi-journée à la cellule service client du siège. Hélène Garnier vous demande de montrer ce que la note oublie.

@capacites
Repérer une définition implicite du SI
Distinguer SI et système informatique
Analyser les fonctions et les rôles du SI
Calculer des parts et un temps de travail
Classer des besoins dans les familles d'applications
Argumenter une réponse à un dirigeant

@duree 60 minutes

@annexe 1 | Ce que la DAF veut présenter au conseil | Source fictive : extrait d'une note d'Isabelle Roux, mai 2026
Le système d'information de Kestrel, c'est d'abord douze applications, deux serveurs de virtualisation dans la salle du siège et un budget de 1,3 M€. Il est entre les mains de la DSI, qui compte dix personnes. Le reste, par exemple la façon dont le service client traite les réclamations, relève de l'organisation des services et non du SI. Je propose donc de présenter au conseil l'inventaire des applications et des serveurs : c'est une vision complète de notre SI.

@annexe 2 | Une demi-journée à la cellule service client | Source fictive : compte rendu d'observation d'un stagiaire de la DSI, mai 2026
La cellule service client du siège compte quatre conseillères, dont une responsable. Elle reçoit en moyenne 180 appels par jour de clients et de destinataires. Pour chaque appel, la conseillère cherche le colis dans Kestrel Track à partir du numéro de suivi. Si le statut ne suffit pas, elle appelle le chauffeur sur son téléphone professionnel.

Les réclamations pour colis endommagé de Saint-Priest et de Moirans suivent un circuit propre. Le chef de quai les signale sur une fiche papier. La conseillère recopie la fiche dans un classeur « Litiges 2026 » partagé sur Microsoft 365, puis y colle la photo prise par le chauffeur dans KDriver. Si un dédommagement est accordé, elle envoie un courriel à la comptabilité, qui crée un avoir dans l'ERP finance. Aucune procédure n'est écrite : la règle « rappeler le client sous 48 heures » se transmet oralement. Le classeur « Litiges 2026 » ne figure pas dans l'inventaire de la DSI.

Une fois par mois, la responsable compte à la main les litiges par client et envoie le total à Léa Fontaine, qui s'en sert dans ses négociations commerciales. « Quand une conseillère est absente, on perd le fil de ses dossiers », regrette-t-elle.

@annexe 3 | Motifs des appels reçus par la cellule service client | Source fictive : comptage des conseillères, moyenne journalière d'avril 2026
@graphique barres appels par jour
Où est mon colis : 92
Reprogrammer : 38
Colis endommagé : 24
Litige facture : 11
Autres motifs : 15

@annexe 4 | Besoins recensés par la DSI auprès des directions | Source fictive : liste de travail de la DSI, mai 2026, sans choix d'outil
| Besoin | Besoin exprimé | Direction demandeuse |
| --- | --- | --- |
| A | Suivre dans un même outil les prospects, les devis et les réclamations de chaque client | Commerciale |
| B | Rassembler les données de RoutePro, de KDriver et de TeleFleet pour produire les indicateurs de « Cap 2029 » | Direction générale |
| C | Calculer automatiquement les tournées qui minimisent les kilomètres à vide | Opérations |
| D | Gérer les plannings, les absences et les temps de travail des chauffeurs, en lien avec la paie | Ressources humaines |
| E | Gérer les commandes et les factures des sous-traitants du dernier kilomètre | Administrative et financière |

@question 1 | Identifier | Annexe 1
Quelle définition du système d'information Isabelle Roux utilise-t-elle implicitement ? Relevez la phrase qui le montre.
@lignes 4

@question 2 | Mobiliser | Annexes 1 et 2
À partir de la définition de Reix, donnez pour chaque composante du SI un exemple observé à la cellule service client, puis indiquez s'il fait partie du système informatique.
@tableau
| Composante du SI (Reix) | Exemple à la cellule service client | Dans le système informatique ? |
| --- | --- | --- |
| Matériels | | |
| Logiciels | | |
| Personnel | | |
| Données | | |
| Procédures | | |

@question 3 | Analyser | Annexe 2
Décrivez comment chacune des quatre fonctions du SI est assurée pour une réclamation de colis endommagé, et relevez une faiblesse pour chacune.
@tableau
| Fonction | Comment elle est assurée | Faiblesse observée |
| --- | --- | --- |
| Collecter | | |
| Mémoriser | | |
| Traiter | | |
| Diffuser | | |

@question 4 | Calculer | Annexes 2 et 3
Calculez la part des appels « Où est mon colis ? » dans le total, puis le nombre moyen d'appels par conseillère et par jour. Si la moitié de ces appels était évitée et qu'un appel dure en moyenne 4 minutes, quel temps de travail serait libéré chaque jour ?
@lignes 5

@question 5 | Analyser | Annexes 2 et 3
Illustrez par un exemple de la cellule chacun des trois rôles du SI (opérationnel, aide à la décision, coordination). Lequel est le plus mal assuré ? Justifiez.
@lignes 6

@question 6 | Mobiliser | Annexe 4
Rattachez chaque besoin à une famille d'applications du cours, avec son sigle quand il existe.
@tableau
| Besoin | Famille d'applications | Justification |
| --- | --- | --- |
| A | | |
| B | | |
| C | | |
| D | | |
| E | | |

@question 7 | Argumenter | Toutes les annexes
Rédigez la réponse d'Hélène Garnier à Isabelle Roux : expliquez pourquoi l'inventaire des applications et des serveurs ne donne pas une vision complète du SI, et ce qu'une cartographie devra montrer en plus.
@lignes 10

@retiens
Selon Reix, le système d'information est un ensemble [[organisé]] de ressources : matériels, logiciels, [[personnel]], données et [[procédures]]. Le système [[informatique]] n'en est qu'une partie : il regroupe les moyens techniques qui traitent [[automatiquement]] l'information. Le SI remplit quatre fonctions : collecter, [[mémoriser]], traiter et diffuser. Il joue un rôle opérationnel, un rôle d'aide à la [[décision]] et un rôle de [[coordination]]. Les applications se classent en grandes familles : ERP, CRM, SCM, décisionnel, applications [[métier]].

@corrige 1
Isabelle Roux confond le SI et le système informatique : elle le réduit aux moyens techniques (applications, serveurs) et au budget, et le confie à la seule DSI. La phrase décisive est : « Le reste, par exemple la façon dont le service client traite les réclamations, relève de l'organisation des services et non du SI. » Elle exclut ainsi les personnes et les procédures, que la définition de Reix inclut. Notion : chapitre 1, « SI et système informatique ».

@corrige 2
| Composante du SI (Reix) | Exemple à la cellule service client | Dans le système informatique ? |
| --- | --- | --- |
| Matériels | Postes des conseillères, terminaux KDriver, téléphones professionnels des chauffeurs | Oui pour les postes et les terminaux ; le téléphone, qui sert ici à un échange oral sans traitement automatique, se discute |
| Logiciels | Kestrel Track, KDriver, Microsoft 365, ERP finance | Oui |
| Personnel | Quatre conseillères, chef de quai, chauffeurs, comptabilité | Non |
| Données | Numéros de suivi, statuts, photos, classeur « Litiges 2026 », fiches papier | En partie : les fiches papier et le comptage manuel n'y sont pas |
| Procédures | Circuit des réclamations, règle orale du rappel sous 48 heures, comptage mensuel | Non |

Notion : chapitre 1, « Le système d'information : définition » et « SI et système informatique ».

@corrige 3
| Fonction | Comment elle est assurée | Faiblesse observée |
| --- | --- | --- |
| Collecter | Fiche papier du chef de quai, photo prise dans KDriver | Support papier, à recopier |
| Mémoriser | Classeur « Litiges 2026 » sur Microsoft 365 | Fichier hors inventaire, sans règle de tenue ; les dossiers en cours d'une absente sont perdus de vue |
| Traiter | Décision de dédommagement, avoir créé dans l'ERP finance, comptage mensuel par client | Comptage à la main, une fois par mois |
| Diffuser | Courriel à la comptabilité, total mensuel envoyé à Léa Fontaine | Diffusion par courriel, tardive, sans trace structurée |

Notion : chapitre 1, « Fonctions et rôles du SI ».

@corrige 4
Part des appels « Où est mon colis ? » : 92 / 180 = 51,1 %. Plus d'un appel sur deux porte sur une information que Kestrel Track contient déjà, puisque KDriver y synchronise les statuts toutes les 2 minutes.

Appels par conseillère : 180 / 4 = 45 appels par jour.

Temps libéré : 92 / 2 = 46 appels évités ; 46 × 4 = 184 minutes, soit 3 h 04 par jour, environ 0,4 équivalent temps plein sur une journée de 7 heures. Le calcul est une estimation : l'annexe ne dit pas pourquoi les destinataires appellent au lieu de consulter le suivi.

@corrige 5
Rôle opérationnel : la conseillère consulte Kestrel Track pour répondre à un appel. Rôle de coordination : le courriel à la comptabilité, qui relie le service client et la finance, et la photo du chauffeur, qui relie le terrain et le service client. Rôle d'aide à la décision : le total mensuel des litiges par client transmis à Léa Fontaine pour ses négociations. Ce dernier rôle est le plus mal assuré : l'information est produite à la main, une fois par mois, à partir d'un classeur hors inventaire, alors qu'elle sert une décision commerciale. La coordination est aussi fragile, puisqu'elle repose sur des courriels et une règle orale. Notion : chapitre 1, « Fonctions et rôles du SI ».

@corrige 6
| Besoin | Famille d'applications | Justification |
| --- | --- | --- |
| A | Gestion de la relation client (CRM) | Prospects, devis, réclamations : c'est le contenu type d'un CRM |
| B | Décisionnel (BI) | Rassembler des données de plusieurs applications pour produire des indicateurs |
| C | Gestion de la chaîne logistique (SCM), outil de transport (TMS) ; aussi application métier | Optimisation des tournées, fonction d'un TMS |
| D | Progiciel de gestion intégré (ERP), module de paie et de temps, ou application spécialisée en ressources humaines | Le cours range la paie parmi les fonctions possibles d'un ERP |
| E | Progiciel de gestion intégré (ERP), module achats | Achats et factures fournisseurs |

Notion : chapitre 1, « Les grandes familles d'applications ». Le cours rappelle qu'une application peut relever de deux familles : accepter un double classement s'il est justifié et tenu.

@corrige 7
Éléments attendus. Selon Reix, le SI comprend aussi le personnel, les procédures et les données traitées à la main : la cellule service client en fait partie. L'inventaire proposé ne montrerait ni la fiche papier, ni la règle orale des 48 heures, ni le classeur « Litiges 2026 », absent de l'inventaire de la DSI, ni la dépendance aux conseillères. Or ces éléments portent des données personnelles de destinataires et une information utilisée dans les négociations commerciales. Une cartographie devra montrer les flux manuels (fiche papier recopiée et photo de KDriver collée dans le classeur, courriel vers la comptabilité pour l'avoir), les usages hors inventaire et la fragilité de la couverture des fonctions. Aujourd'hui, le traitement des réclamations ne repose sur aucune application de l'inventaire de la DSI : c'est un trou. Une fois le classeur inscrit à l'annexe A comme usage hors inventaire, il ne sera plus un trou mais une application à couverture fragile, à signaler comme telle (chapitre 3, « Les quatre niveaux du référentiel et la vue fonctionnelle »). La réponse reste courtoise et factuelle.

Barème indicatif sur 5 points : 1 point pour la définition de Reix, 2 points pour trois éléments oubliés tirés de l'annexe 2, 1 point pour ce que la cartographie doit montrer, 1 point pour le ton adapté à une directrice.

# FT 04 | Lire une stratégie : niveaux, objectifs SMART, stratégies génériques | 1

@situation
En février 2026, Paul Vidal prépare avec l'actionnaire la revue annuelle du plan « Cap 2029 ». Hélène Garnier doit dire au comité de direction ce que la stratégie exige du SI. Alternant à la DSI, vous êtes chargé de lire trois documents et d'en tirer une analyse structurée.

@capacites
Distinguer les niveaux de stratégie
Retrouver les éléments de la définition de Chandler
Tester des objectifs avec la grille SMART
Calculer une croissance et un taux annuel moyen
Identifier des stratégies génériques
Relier stratégie et exigences envers le SI

@duree 60 minutes

@annexe 1 | Les attentes de l'actionnaire | Source fictive : extrait d'une lettre du président de Vidal Participations à Paul Vidal, janvier 2026
Le conseil de Vidal Participations a confirmé sa décision de conserver Kestrel Logistique et de ne pas entrer dans d'autres métiers logistiques, comme le transport sous température dirigée. Il attend de sa filiale qu'elle reste le transporteur de référence de la livraison rapide en Auvergne-Rhône-Alpes.

Le conseil fixe deux attentes pour 2029 : un chiffre d'affaires d'au moins 48 M€ et une marge opérationnelle de 5 %, contre 3,1 % en 2025. Il accepte d'apporter des fonds pour des investissements, à condition que chacun soit relié à un objectif de « Cap 2029 » et chiffré. La grande distribution reste le socle de l'activité, mais la croissance doit venir du e-commerce.

@annexe 2 | Objectifs 2026 des directions | Source fictive : feuille de route 2026 du comité de direction, janvier 2026
| Direction | Objectif 2026, tel qu'il est écrit |
| --- | --- |
| Opérations | « Améliorer la ponctualité des livraisons. » |
| Opérations | « Former 100 % des chauffeurs salariés à l'écoconduite avant le 30 septembre 2026. » |
| Commerciale | « Signer 30 nouveaux clients e-commerçants en 2026. » |
| Administrative et financière | « Ramener le délai moyen de paiement des clients de 58 à 50 jours au 31 décembre 2026. » |
| Systèmes d'information | « Moderniser le SI. » |

@annexe 3 | Livraison régionale : trois modèles face à face | Source fictive : article du « Courrier du Transport », février 2026
En Auvergne-Rhône-Alpes, la livraison de colis voit s'affronter trois modèles. Le groupe national Hexapole Messagerie dessert toute la France à J+2 depuis de grands centres de tri automatisés. Il affiche les prix les plus bas du marché pour les gros volumes et ne personnalise presque rien.

À l'autre bout, la jeune société lyonnaise Lumivélo livre en vélo cargo, en moins de deux heures, dans le centre de Lyon. Ses clients, des commerçants et des marques haut de gamme, acceptent de payer environ deux fois le prix d'une livraison classique. Elle ne sort pas de la métropole.

Entre les deux, les transporteurs régionaux comme Kestrel Logistique misent sur la livraison à J+1 dans toute la région et sur l'information du destinataire. « Notre force, c'est la proximité et le suivi en ligne », explique Léa Fontaine, directrice commerciale. Un consultant du secteur nuance : « Les régionaux doivent choisir. Soit ils tiennent leur promesse de service et la font payer, soit ils s'alignent sur les prix des nationaux, avec des marges déjà parmi les plus faibles du secteur. »

@annexe 4 | Part du e-commerce dans le chiffre d'affaires de Kestrel | Source fictive : direction administrative et financière, comptes annuels
@graphique lignes % du chiffre d'affaires
2021 : 20
2022 : 22
2023 : 25
2024 : 28
2025 : 30

@question 1 | Identifier | Annexes 1 et 2
Situez chaque décision ou objectif à son niveau de stratégie et indiquez qui le fixe.
@tableau
| Décision ou objectif | Niveau de stratégie | Qui le fixe |
| --- | --- | --- |
| Ne pas entrer dans le transport sous température dirigée | | |
| Rester le transporteur de référence de la livraison rapide dans la région | | |
| Faire venir la croissance du e-commerce | | |
| Signer 30 nouveaux clients e-commerçants en 2026 | | |
| Moderniser le SI | | |

@question 2 | Mobiliser | Annexe 1
Retrouvez dans la lettre les trois éléments de la définition de la stratégie de Chandler. Lequel est le moins précis ?
@lignes 5

@question 3 | Mobiliser | Annexe 2
Testez quatre objectifs avec la grille SMART et proposez une reformulation de ceux qui ne passent pas le test. Vous fixerez une valeur cible plausible en le signalant.
@tableau
| Objectif | Critères satisfaits | Critères manquants | Reformulation proposée |
| --- | --- | --- | --- |
| Améliorer la ponctualité des livraisons | | | |
| Former 100 % des chauffeurs à l'écoconduite avant le 30 septembre 2026 | | | |
| Ramener le délai de paiement de 58 à 50 jours au 31 décembre 2026 | | | |
| Moderniser le SI | | | |

@question 4 | Calculer | Annexes 1 et 4
Calculez le chiffre d'affaires e-commerce de 2025 (42 M€ au total), puis celui de 2029 si la part atteint 40 % d'un chiffre d'affaires de 48 M€. Calculez la hausse en valeur et en pourcentage, puis le taux de croissance annuel moyen nécessaire de 2025 à 2029. Prolongez enfin la tendance de 2021 à 2025 : l'objectif de 40 % est-il cohérent avec elle ?
@lignes 8

@question 5 | Analyser | Annexe 3
Identifiez la stratégie générique de chacun des trois acteurs.
@tableau
| Acteur | Cible | Source de l'avantage | Stratégie générique |
| --- | --- | --- | --- |
| Hexapole Messagerie | | | |
| Lumivélo | | | |
| Kestrel Logistique | | | |

@question 6 | Analyser | Annexes 1 et 3
Expliquez le risque que le consultant décrit, en utilisant l'expression de Porter qui le désigne. Montrez que les attentes de l'actionnaire rendent ce risque concret pour Kestrel.
@lignes 6

@question 7 | Argumenter | Toutes les annexes
Pour Hélène Garnier, montrez ce que deux attentes de la stratégie (part e-commerce à 40 % et marge opérationnelle de 5 %) exigent du système d'information. Expliquez ensuite pourquoi « Moderniser le SI » ne constitue pas une stratégie SI.
@lignes 10

@retiens
Selon [[Chandler]], la stratégie est la détermination des buts à long terme, l'adoption des actions à mener et l'allocation des [[ressources]] nécessaires. Elle se décide à trois niveaux : le [[groupe]], le domaine d'activité et le niveau [[fonctionnel]], auquel appartient la stratégie SI. Un objectif utile est SMART : spécifique, [[mesurable]], atteignable, pertinent et [[temporellement]] défini. Porter distingue trois stratégies génériques : la domination par les [[coûts]], la [[différenciation]] sur tout le marché et la [[focalisation]] sur un segment restreint ; l'entreprise qui ne choisit pas risque d'être « coincée au milieu ».

@corrige 1
| Décision ou objectif | Niveau de stratégie | Qui le fixe |
| --- | --- | --- |
| Ne pas entrer dans le transport sous température dirigée | Groupe | Conseil de Vidal Participations |
| Rester le transporteur de référence de la livraison rapide dans la région | Domaine d'activité (comment gagner dans ce métier), orienté par le groupe | Conseil, puis direction générale de Kestrel |
| Faire venir la croissance du e-commerce | Domaine d'activité | Conseil et direction générale de Kestrel |
| Signer 30 nouveaux clients e-commerçants en 2026 | Fonctionnel | Direction commerciale |
| Moderniser le SI | Fonctionnel | DSI |

Notion : chapitre 1, « La stratégie : définition et niveaux ». La deuxième ligne se discute : la lettre l'énonce, mais c'est une manière de gagner dans un métier, donc un choix de domaine d'activité.

@corrige 2
La destination : rester le transporteur de référence de la livraison rapide dans la région, avec 48 M€ de chiffre d'affaires et 5 % de marge en 2029. Les moyens : des fonds de l'actionnaire, sous condition que chaque investissement soit relié à un objectif et chiffré. Le chemin : faire venir la croissance du e-commerce. Le chemin est l'élément le moins précis : la lettre ne dit pas par quelles actions Kestrel passera de 3,1 % à 5 % de marge. Notion : chapitre 1, définition de la stratégie de Chandler (1962).

@corrige 3
| Objectif | Critères satisfaits | Critères manquants | Reformulation proposée |
| --- | --- | --- | --- |
| Améliorer la ponctualité des livraisons | Pertinent (J+1 de « Cap 2029 ») ; daté par défaut (feuille de route 2026) | Spécifique (quelle ponctualité ?), mesurable (ni indicateur ni valeur de départ) ; atteignabilité invérifiable | « Livrer à l'heure annoncée X % des colis au 31 décembre 2026 », X à fixer après mesure de la valeur de départ |
| Former 100 % des chauffeurs à l'écoconduite avant le 30 septembre 2026 | S, M, T ; pertinent (kilomètres à vide, ISO 14001) | Atteignable à vérifier (140 chauffeurs, budget de formation) | Satisfaisant ; préciser le responsable et le budget |
| Ramener le délai de paiement de 58 à 50 jours au 31 décembre 2026 | S, M avec valeur de départ, T ; pertinent (trésorerie, marge) | Atteignabilité à justifier | Satisfaisant |
| Moderniser le SI | Daté par défaut seulement (feuille de route 2026) | Spécifique, mesurable, atteignable (invérifiable), pertinent (aucun lien avec un objectif de « Cap 2029 ») ; échéance propre absente | Exemple : « Remplacer d'ici juin 2027 les composants hors support des applications exposées aux clients » ; la cible est illustrative |

Notion : chapitre 1, « Des objectifs SMART ». Selon la règle du cours, l'horizon de la feuille de route vaut échéance par défaut (fin 2026), plus faible qu'une date propre ; accepter « échéance manquante » si l'élève le justifie ainsi. Accepter d'autres reformulations si elles sont mesurables, datées et signalées comme proposées.

@corrige 4
E-commerce 2025 : 30 % × 42 = 12,6 M€.

E-commerce 2029 : 40 % × 48 = 19,2 M€.

Hausse : 19,2 − 12,6 = 6,6 M€, soit 6,6 / 12,6 = + 52,4 %.

Taux annuel moyen sur quatre ans : (19,2 / 12,6)^(1/4) − 1 = 1,524^(0,25) − 1 ≈ 0,111, soit environ 11,1 % par an.

Tendance : de 20 % en 2021 à 30 % en 2025, la part gagne 10 points en 4 ans, soit 2,5 points par an. Prolongée, elle donne 30 + 4 × 2,5 = 40 % en 2029 : l'objectif est cohérent avec la tendance, à condition que celle-ci se maintienne, ce que rien ne garantit. Remarque utile : les autres clients passeraient de 42 − 12,6 = 29,4 M€ à 48 − 19,2 = 28,8 M€, en légère baisse, alors que l'actionnaire présente la grande distribution comme le socle.

@corrige 5
| Acteur | Cible | Source de l'avantage | Stratégie générique |
| --- | --- | --- | --- |
| Hexapole Messagerie | Tout le marché national | Coûts les plus bas, gros volumes, automatisation | Domination par les coûts |
| Lumivélo | Un segment : le centre de Lyon, clients haut de gamme | Rapidité (moins de deux heures), prix double accepté | Focalisation par la différenciation |
| Kestrel Logistique | Un segment géographique : la région | J+1 sur toute la région, suivi en ligne, proximité | Focalisation par la différenciation |

Notion : chapitre 1, « Avantage concurrentiel et stratégies génériques de Porter ».

@corrige 6
Le consultant décrit la position « coincée au milieu » (« stuck in the middle ») : une entreprise qui n'offre ni le prix le plus bas ni une différence que le client paie. Kestrel est exposée : sa marge de 3,1 % est faible, et l'actionnaire exige 5 % en 2029, soit 2,4 M€ de résultat sur 48 M€ contre 1,3 M€ en 2025 (3,1 % × 42). Si elle baisse ses prix pour suivre Hexapole, elle s'éloigne de cet objectif ; si elle reste différenciée, elle doit faire payer son service et donc le rendre visible et fiable. L'élève doit conclure qu'un choix est nécessaire, ou que les deux voies doivent être conciliées explicitement.

@corrige 7
Éléments attendus. La part e-commerce à 40 % exige du SI de gérer beaucoup de petits clients sans charge proportionnelle : recevoir leurs ordres sans ressaisie, les facturer automatiquement, leur offrir un suivi en ligne fiable, puisque l'information du destinataire est l'argument de différenciation (annexe 3). La marge de 5 % exige de réduire les coûts d'exploitation : mesurer et optimiser les tournées, supprimer les ressaisies, produire des indicateurs de coût par tournée ou par client. Le SI est donc tiré dans deux directions, rendre le service visible et réduire les coûts (chapitre 1). « Moderniser le SI » n'est pas une stratégie SI : ce n'est pas un objectif SMART, il n'est relié à aucun objectif de « Cap 2029 », alors que l'actionnaire l'exige pour tout investissement, et il ne fixe ni cible, ni projets, ni moyens. Une stratégie SI découle de la stratégie de l'entreprise et se formalise dans un schéma directeur (chapitre 2, « Pourquoi une stratégie SI »).

Barème indicatif sur 5 points : 2 points pour les exigences liées à chaque attente, 2 points pour la critique de « Moderniser le SI » appuyée sur SMART et sur la lettre, 1 point pour la clarté.

# FT 05 | La place du SI et l'alignement stratégique | 2

@situation
En juillet 2026, Paul Vidal envisage de rattacher la DSI à la direction générale et de créer une instance dédiée au SI. Avant d'en parler au comité de direction, il demande à Hélène Garnier une note sur la place du SI chez Kestrel et sur la manière de choisir les projets. Vous êtes son alternant et préparez les éléments de cette note.

@capacites
Distinguer SI support et SI levier
Calculer la structure d'un budget SI et un dépassement
Appliquer la grille de McFarlan à des demandes de projets
Identifier les perspectives d'alignement de Henderson et Venkatraman
Analyser un dispositif de gouvernance
Discuter les limites d'un modèle
Argumenter une recommandation à un dirigeant

@duree 75 minutes

@annexe 1 | « J'ai changé d'avis sur l'informatique » | Source fictive : propos de Paul Vidal recueillis par Hélène Garnier, juillet 2026
« Pendant longtemps, j'ai vu l'informatique comme une charge à contenir. C'est pour cela que la DSI est rattachée à la DAF : on regarde d'abord le budget. Les projets passent en comité de direction mensuel, quand il reste du temps.

Le renouvellement du contrat de notre premier client de la grande distribution m'a fait changer d'avis. En juin, il a renouvelé pour trois ans, à une condition : recevoir d'ici mars 2027 les statuts de livraison en temps réel, par une API branchée sur son propre système. Sans Kestrel Track, nous n'aurions même pas pu discuter.

Hélène me propose d'aller plus loin : offrir aux e-commerçants une page de suivi à leurs couleurs, que nos concurrents régionaux n'ont pas, et en faire un argument de vente. Sébastien attend toujours le module d'optimisation de RoutePro pour les kilomètres à vide. Romain me rappelle chaque mois que Kestrel Track tourne sur une version de Django qui n'est plus maintenue.

Je n'ai que 260 k€ de projets cette année. Je veux comprendre comment choisir, et qui doit choisir. »

@annexe 2 | Budget SI 2026 par poste | Source fictive : direction administrative et financière ; total de 1 300 k€
@graphique barres k€
Personnel DSI : 560
SaaS et licences : 310
Maintenance des progiciels : 120
Matériel, réseau : 50
Projets : 260

@annexe 3 | Demandes de projets SI en attente de décision | Source fictive : registre des demandes tenu par la DSI, juin 2026
| N° | Demande | Demandeur | Application concernée | Coût estimé | Objectif de « Cap 2029 » invoqué |
| --- | --- | --- | --- | --- | --- |
| D1 | Module d'optimisation des tournées | Sébastien Morin | APP-01 RoutePro | 95 k€ | Réduire de 20 % les kilomètres à vide |
| D2 | Migration vers une version maintenue de Django | Hélène Garnier | APP-03 Kestrel Track | 70 k€ | Aucun ; sécurité |
| D3 | Outil de gestion de la relation client | Léa Fontaine | Nouvelle application | 38 k€ | Part e-commerce à 40 % |
| D4 | Authentification multifacteur pour tous les salariés | Romain Chevalier | APP-10 Microsoft 365, SEC-01 Passerelle VPN | 18 k€ | Aucun ; sécurité |
| D5 | Interface entre TeleFleet et la paie | Nicolas Perrin | APP-05 TeleFleet et APP-08 Paie | 25 k€ | Aucun |
| D8 | API de statuts en temps réel pour le premier client de la grande distribution | Léa Fontaine | APP-03 Kestrel Track | 70 k€ | Aucun ; condition du renouvellement du contrat |

Le comité de mai a renvoyé à 2027 les demandes D6 (liens 4G de secours) et D7 (scanners), sans examiner la grille de cotation de la DSI. D4, confiée en février à la DSI « sans coût supplémentaire », a été chiffrée en avril.

@annexe 4 | Le circuit actuel d'une demande de projet SI | Source fictive : schéma de la DSI, juin 2026
@schema
Demande par courriel ou à l'oral -> DSI : Hélène Garnier -> DAF : Isabelle Roux
... -> Comité de direction mensuel -> Décision au cas par cas
... -> Projet décidé -> Suivi : aucun tableau de bord -> Bilan : non prévu

@question 1 | Identifier | Annexe 1
Relevez dans les propos de Paul Vidal ce qui relève d'une vision du SI comme support, puis ce qui montre un SI levier.
@lignes 5

@question 2 | Calculer | Annexes 2 et 3
Calculez la part du budget consacrée au fonctionnement et celle du personnel dans le fonctionnement. Calculez le total des demandes, le dépassement de l'enveloppe de projets en k€ et en pourcentage, puis la part de l'enveloppe qu'absorberaient les trois demandes portant sur Kestrel Track et RoutePro.
@lignes 7

@question 3 | Mobiliser | Annexes 1 et 3, cours
Le chapitre 2 a placé les applications de Kestrel dans la grille de McFarlan. Pour chaque demande, indiquez la position de l'application concernée, puis le fait nouveau des annexes qui confirme ou fait évoluer cette position (pour l'outil à créer, justifiez sa position par les annexes). Dites enfin ce qu'il faut gérer en priorité.
@tableau
| Demandes | Application | Position et fait nouveau des annexes | Priorité de gestion |
| --- | --- | --- | --- |
| D2 et D8 | Kestrel Track | | |
| D1 | RoutePro | | |
| D3 | Outil de relation client (à créer) | | |
| D4 | Microsoft 365 | | |
| D5 | TeleFleet et Paie | | |

@question 4 | Mobiliser | Annexes 1 et 3
Associez chaque projet à une perspective du modèle d'alignement de Henderson et Venkatraman.
@tableau
| Projet | Domaine moteur | Perspective | Justification |
| --- | --- | --- | --- |
| Page de suivi aux couleurs des e-commerçants | | | |
| Module d'optimisation des tournées | | | |
| Outil de gestion de la relation client | | | |
| Migration de Django et authentification multifacteur | | | |

@question 5 | Analyser | Annexes 1 et 4
Confrontez le circuit de l'annexe 4 au cycle de gouvernance de la norme ISO/IEC 38500 (évaluer, diriger, surveiller). Quelle étape est la plus défaillante ?
@lignes 6

@question 6 | Analyser | Annexe 1
Le modèle de Henderson et Venkatraman suppose une stratégie explicite et un réglage rationnel. Montrez, à partir des propos de Paul Vidal, une limite de ce modèle dans le cas de Kestrel.
@lignes 5

@question 7 | Argumenter | Toutes les annexes
Rédigez la partie de la note qui répond à la question de Paul Vidal : « comment choisir, et qui doit choisir ». Vous proposerez des critères d'arbitrage écrits et une instance, en justifiant par les annexes et par le cours.
@lignes 10

@retiens
Le SI [[support]] accompagne la stratégie au moindre coût ; le SI [[levier]] rend possible une stratégie nouvelle. La grille de [[McFarlan]] croise l'impact actuel et l'impact futur du SI pour distinguer quatre positions : support, production, avenir et stratégique. Le modèle de Henderson et Venkatraman relie quatre domaines par la cohérence stratégique et l'[[intégration fonctionnelle]] ; il décrit quatre [[perspectives]]. La [[gouvernance]] du SI fixe les orientations, arbitre et contrôle ; selon l'ISO/IEC 38500, la direction doit évaluer, [[diriger]] et [[surveiller]].

@corrige 1
Vision support : « l'informatique comme une charge à contenir », la DSI rattachée à la DAF « car on regarde d'abord le budget », les projets examinés « quand il reste du temps ». Vision levier : le contrat du premier client renouvelé grâce aux capacités de Kestrel Track (« sans Kestrel Track, nous n'aurions même pas pu discuter ») ; la page de suivi aux couleurs des e-commerçants, argument de vente que les concurrents régionaux n'ont pas. Le SI devient une partie de l'offre elle-même. Notion : chapitre 2, « Pourquoi une stratégie SI ».

@corrige 2
Fonctionnement : 1 300 − 260 = 1 040 k€, soit 1 040 / 1 300 = 80 % du budget. Personnel dans le fonctionnement : 560 / 1 040 = 53,8 % (43,1 % du budget total).

Total des demandes : 95 + 70 + 38 + 18 + 25 + 70 = 316 k€. Dépassement : 316 − 260 = 56 k€, soit 56 / 260 = 21,5 % de l'enveloppe.

Demandes D1, D2 et D8 : 95 + 70 + 70 = 235 k€, soit 235 / 260 = 90,4 % de l'enveloppe. Les deux seules demandes sur Kestrel Track (140 k€) en absorbent déjà 53,8 %. Tout ne peut pas être fait en 2026 : il faut des critères pour choisir.

@corrige 3
| Demandes | Application | Position et fait nouveau des annexes | Priorité de gestion |
| --- | --- | --- | --- |
| D2 et D8 | Kestrel Track | Stratégique, position renforcée : l'impact actuel devient contractuel (renouvellement du premier client conditionné à une API d'ici mars 2027) ; l'impact futur s'élargit (page de suivi aux couleurs des e-commerçants) | Fiabilité et évolution à la fois ; la migration de Django conditionne l'API |
| D1 | RoutePro | Stratégique, confirmée : Sébastien Morin attend toujours le module pour les kilomètres à vide (impact futur) ; l'impact actuel fort vient du cours (panne de 2024) | Fiabilité et évolution |
| D3 | Outil de relation client (à créer) | Avenir : impact actuel nul, puisqu'il n'existe pas ; impact futur fort, car Léa Fontaine l'invoque pour la part e-commerce à 40 % | Investir, expérimenter |
| D4 | Microsoft 365 | Support, inchangée : la demande n'invoque aucun objectif de « Cap 2029 » ; elle touche toutefois la sécurité de tous les salariés et de la passerelle VPN | Coût maîtrisé ; mesure de sécurité peu coûteuse (18 k€) |
| D5 | TeleFleet et Paie | TeleFleet : avenir ; Paie : support, confirmée par l'absence d'objectif invoqué (annexe 3) | Interface utile, non urgente au regard de la stratégie |

Notion : chapitre 2, « La grille stratégique de McFarlan ». La simple reprise des positions du chapitre 2 ne suffit pas : la colonne centrale doit citer un fait des annexes ; la ligne D5 se discute.

@corrige 4
| Projet | Domaine moteur | Perspective | Justification |
| --- | --- | --- | --- |
| Page de suivi aux couleurs des e-commerçants | Stratégie des TI | Potentiel concurrentiel | Une capacité technique existante ouvre un nouvel argument commercial, puis change l'offre |
| Module d'optimisation des tournées | Stratégie de l'entreprise | Transformation technologique | L'objectif des kilomètres à vide impose de choisir une technologie, puis d'adapter l'infrastructure SI |
| Outil de gestion de la relation client | Stratégie de l'entreprise | Exécution de la stratégie | L'objectif e-commerce change l'organisation commerciale, que le SI outille ensuite |
| Migration de Django et authentification multifacteur | Stratégie des TI | Niveau de service | La DSI fixe des exigences de sécurité et de fiabilité, adapte l'infrastructure et sert les métiers |

Notion : chapitre 2, « L'alignement stratégique : le modèle de Henderson et Venkatraman ». L'API du premier client relèverait de la transformation technologique ; d'autres associations sont acceptables si le domaine moteur est bien justifié.

@corrige 5
Évaluer : aucune évaluation commune n'existe ; les demandes arrivent par courriel ou à l'oral et ne sont pas comparées selon des critères écrits. Diriger : une décision est prise, mais au cas par cas, en comité de direction, « quand il reste du temps » ; la direction ne fixe ni priorités ni politique. Surveiller : c'est l'étape la plus défaillante, puisque aucun tableau de bord ne suit les projets décidés et qu'aucun bilan n'est prévu. Le rattachement à la DAF et l'absence d'instance dédiée sont cohérents avec ces manques. Notion : chapitre 2, « La gouvernance du SI » et « Les acteurs et les instances de la gouvernance ». Accepter « évaluer » comme réponse si elle est bien argumentée.

@corrige 6
Le modèle suppose une stratégie explicite, formalisée et stable. Chez Kestrel, le rôle du SI a été découvert par un événement (le renouvellement du contrat) et non par une démarche ; les projets naissent de demandes individuelles portées par chaque directeur. L'alignement résulte donc de négociations et d'opportunités, comme l'a souligné Ciborra (1997), plutôt que d'un réglage rationnel. Une autre limite acceptée : le modèle ne dit pas comment arbitrer entre plusieurs perspectives quand l'enveloppe est limitée. Notion : chapitre 2, limites du modèle de Henderson et Venkatraman.

@corrige 7
Éléments attendus. Le constat : 316 k€ de demandes pour 260 k€ (question 2), un circuit sans évaluation ni suivi (question 5), des applications stratégiques fragiles (question 3). Des critères écrits, appliqués à toutes les demandes : lien avec un objectif de « Cap 2029 », exigé par l'actionnaire ; obligation contractuelle ou réglementaire, comme la condition du premier client pour mars 2027 ; risque de sécurité ou de continuité ; coût et délai chiffrés ; position de l'application dans la grille de McFarlan. Une instance : un comité SI, ou un point SI à date fixe en comité de direction, présidé par le directeur général, avec la DSI et les directeurs métiers, qui recense les demandes, les classe et suit les projets décidés avec un tableau de bord. Le rattachement de la DSI à la direction générale peut être proposé comme cohérent avec un SI levier, en signalant que la décision relève du dirigeant. Les critères doivent montrer que la migration de Django n'est pas un simple confort : l'API du premier client repose sur une application dont la base technique n'est plus maintenue.

Barème indicatif sur 6 points : 1 point pour le constat chiffré, 2 points pour au moins quatre critères écrits et justifiés, 2 points pour l'instance et le suivi, 1 point pour l'argumentation appuyée sur le cours (McFarlan, ISO/IEC 38500, support ou levier).
