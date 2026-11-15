# FICHE 22 | Les vulnérabilités des infrastructures de données | 7

@qcm
Q: Supposons que Kestrel Track et une application interne de reporting partagent la même base PostgreSQL, avec un seul compte technique qui lit, modifie et supprime toutes les tables. Un attaquant compromet l'application de reporting, peu protégée. Que permet d'anticiper la famille « droits trop larges » ?
- Seules les tables du reporting sont atteintes, car chaque application garde son périmètre
+ Toutes les données de la base, y compris celles des destinataires
- Seule la disponibilité de Kestrel Track est menacée par la compromission
- Aucune conséquence, tant que la base reste chiffrée sur le disque du serveur
E: Des applications qui partagent une base partagent souvent son compte : compromettre la moins protégée donne accès à toutes les données, en lecture comme en modification. Le chiffrement du disque ne protège pas contre un accès applicatif légitime en apparence.

Q: Un e-commerçant chiffre sa base de production. Chaque nuit, un script exporte les commandes en CSV vers un serveur de fichiers pour l'équipe marketing, qui les garde sans limite de durée. Quelle affirmation est juste ?
- Le chiffrement de la base protège aussi l'export, puisqu'il en provient
- L'export n'est pas un bien support, car ce n'est pas une application
- Le risque principal porte sur la disponibilité des commandes exportées
+ L'export est un bien support aussi sensible que la base
E: L'export hérite de la sensibilité des données qu'il porte et échappe souvent au chiffrement de la production : il est sans doute moins protégé que la base, et doit figurer dans la matrice des flux.

Q: Un auditeur découvre, grâce à un moteur qui indexe les services exposés, la base de données d'une mutuelle accessible sur Internet sans mot de passe. Quelle famille de vulnérabilités et quelle vue de la cartographie sont concernées ?
+ Stockage mal configuré ; vue des infrastructures logiques
- Injection ; inventaire applicatif
- Dette de dépendances ; inventaire applicatif et état du support
- Fuite par export ; matrice des flux, rubrique des flux manuels
E: Une base ouverte sur Internet sans mot de passe relève de la mauvaise configuration du stockage ; l'exposition et les zones se lisent sur la vue des infrastructures logiques.

Q: Supposons qu'une application interne de Kestrel insère directement dans ses requêtes à la base le texte saisi dans un champ de recherche. Quelle vulnérabilité et quels critères de sécurité sont en jeu ?
- Données en clair ; confidentialité
- Absence de journalisation ; traçabilité
+ Injection ; intégrité et confidentialité
- Droits trop larges ; disponibilité
E: Une saisie insérée sans contrôle dans une requête permet à un attaquant de la modifier pour lire ou altérer des données.

# FICHE 23 | Attaques contre les systèmes d'IA et IA fantôme | 7

@qcm
Q: Une équipe data télécharge sur une plateforme publique un modèle préentraîné de lecture d'adresses, dans un format de fichier qui peut exécuter du code au chargement. Quelle attaque faut-il redouter en priorité ?
- Une inversion de modèle sur les adresses déjà lues
- Une injection de prompt directe par un utilisateur
+ Une attaque par la chaîne d'approvisionnement
- Une évasion par des étiquettes d'adresse modifiées
E: Un modèle piégé devient un logiciel malveillant au moment de son chargement ; c'est la chaîne d'approvisionnement des modèles, en phase de développement, qui est visée.

Q: Un concurrent interroge des dizaines de milliers de fois l'API publique d'un modèle de tarification d'une mutuelle pour en reconstituer une copie. Qu'est-ce qui est atteint en premier ?
+ La confidentialité du modèle, volé par extraction
- L'intégrité des décisions du modèle
- La disponibilité des données d'entraînement
- La traçabilité des échanges avec les adhérents
E: L'extraction de modèle revient à voler un actif par interrogation massive d'une API exposée.

Q: Un hôpital publie un modèle de détection d'une maladie rare. Un chercheur montre qu'on peut déduire, à partir des réponses du modèle, qu'une personne figurait dans le jeu d'entraînement. Pourquoi est-ce grave en santé ?
- Parce que cela dégrade la précision du modèle pour les autres patients
- Parce que le modèle peut alors être copié à moindre coût par un concurrent
- Parce que cela permet à un attaquant d'empêcher le déclenchement d'une alerte
+ Parce que savoir qu'un patient figure dans la cohorte révèle son diagnostic
E: L'inférence d'appartenance atteint la confidentialité des données d'entraînement ; en santé, l'appartenance à une cohorte de malades est en elle-même une donnée de santé.

Q: Une mutuelle prévoit d'ouvrir en 2027 un assistant d'IA pour ses adhérents. Dans l'analyse de risques de son SI actuel, un analyste bâtit sur cet assistant son seul scénario opérationnel « data ou IA ». Que lui dire ?
- C'est le bon choix, car un projet d'IA concentre les risques les plus récents du SI
+ Le projet est un facteur aggravant ; le scénario part d'un bien support existant
- Il doit attendre l'ouverture de l'assistant pour mener toute l'analyse de risques
- Le scénario est recevable s'il cite une catégorie du Top 10 de l'OWASP
E: L'atelier 4 analyse le SI tel qu'il est : le scénario s'appuie sur un bien support existant (base partagée, export, usage d'IA fantôme), et le projet d'IA s'y cite comme facteur aggravant.

# FICHE 24 | OWASP, MITRE ATLAS, ANSSI : du vocabulaire au scénario | 7

@qcm
Q: Un assistant interne d'un transporteur peut, en plus de répondre aux clients, modifier l'adresse de livraison d'un colis. Un audit montre qu'une injection de prompt pourrait détourner des colis. Quelle catégorie du Top 10 de l'OWASP 2026 décrit ce qui aggrave les conséquences de l'injection ?
- Consommation non bornée
- Informations erronées (mésinformation)
- Faiblesses des vecteurs et des plongements
+ Autonomie excessive
E: Chaque droit d'agir accordé au modèle élargit les conséquences d'une injection ; c'est l'autonomie excessive, troisième en 2026 selon les sources consultées par le cours.

Q: Un développeur place le mot de passe d'une base de données dans les consignes système d'un chatbot, en supposant que l'utilisateur ne les verra jamais. Quel risque du Top 10 de l'OWASP 2026 prend-il ?
- Empoisonnement des données et du modèle
+ Exposition du contexte caché
- Traitement inapproprié des sorties
- Chaîne d'approvisionnement
E: Tout ce que le modèle voit sans que l'utilisateur le voie peut être révélé ; on n'y place jamais un secret.

Q: Dans son scénario opérationnel, un apprenant écrit : « l'attaquant applique une technique d'ATLAS parmi les 56 recensées ». Quel reproche lui faire ?
- Aucun, car ATLAS fixe une fois pour toutes le nombre de ses techniques
- D'utiliser ATLAS, qui ne décrit que des attaques théoriques, jamais observées
+ De citer un décompte qui varie au lieu de nommer tactique et technique
- D'utiliser ATLAS, qui ne s'applique qu'aux grands modèles de langage
E: ATLAS est mis à jour plusieurs fois par an et documente aussi des cas réels ; on nomme la tactique et la technique d'après la matrice en ligne, et on rattache l'étape à un bien support.

Q: Une collectivité veut déployer un assistant d'IA générative alors que ses comptes administrateurs n'ont pas d'authentification multifacteur. Quel message du cadre de l'ENISA de 2023 s'applique ?
+ Les fondamentaux de la cybersécurité passent avant les pratiques propres à l'IA
- Les mesures propres à l'IA remplacent l'hygiène classique dès qu'un modèle est déployé
- La sécurité de l'IA relève uniquement de la CNIL
- Le cadre exclut le secteur public de son champ
E: Le Multilayer Framework organise les pratiques en trois couches : fondamentaux de la cybersécurité, pratiques propres à l'IA, pratiques sectorielles.

# FICHE 25 | PCA, PRA et bilan d'impact sur l'activité | 8

@qcm
Q: Supposons que, chez Kestrel, si RoutePro ne répond pas à 5 h, les chefs de quai affectent les colis à la main à partir des listes de tournées imprimées la veille. Comment qualifier ce dispositif ?
+ Un mode dégradé, qui relève de la continuité
- Un plan de reprise d'activité, car RoutePro est arrêté
- Un retour à la normale
- Une mesure de l'atelier 5 sans lien avec la continuité
E: Continuer avec des moyens réduits pendant l'arrêt, c'est le mode dégradé ; le PRA, lui, organise le redémarrage de RoutePro.

Q: Un DSI explique : « Notre PCA, c'est la réplication de nos serveurs sur un second site. » Que manque-t-il à cette vision ?
- Rien, si le second site est à plus de cent kilomètres
- Une analyse de risques, car la réplication relève du BIA
+ Les locaux, les personnes, les fournisseurs et la communication
- Un contrat d'assurance qui couvre la perte des serveurs
E: Le PCA dépasse largement l'informatique ; la réplication n'est qu'un moyen technique de son volet informatique.

Q: Dans la partie 4 d'un dossier sur Kestrel, un apprenant écrit : « Une réplication de RoutePro vers un second site réglerait l'écart de +118 heures. » Que lui dire ?
- C'est attendu : la partie 4 doit proposer une solution par application
+ Le D2 s'arrête au constat ; le choix d'une solution relève du D3
- La phrase est acceptable si le coût de la réplication est chiffré
- La phrase doit être déplacée dans la synthèse destinée à la direction
E: Un état des lieux qui propose déjà une solution oriente la décision avant que les options aient été comparées ; il décrit l'écart et ce qu'il signifie pour l'activité.

Q: Une responsable de la continuité demande à chaque direction combien de temps elle peut se passer de son outil. Toutes répondent « pas du tout ». Que faire pour obtenir une réponse utile ?
- Retenir ces réponses et fixer partout une DMIA nulle
- Imposer à chaque direction la DMIA proposée par la DSI
- Lister d'abord les menaces les plus probables pour chaque outil
+ Poser la question par un scénario daté, à plusieurs horizons
E: Posée sans scénario ni prix, la question fait imaginer le pire. « Si l'outil s'arrête un mardi à 4 h, que se passe-t-il à 5 h, à 8 h, le lendemain ? » fait apparaître le tolérable ; le BIA part des activités, pas des menaces.

# FICHE 26 | DMIA, PDMA, MTPD et classes de criticité | 8

@qcm
Q: Chez Kestrel, TeleFleet a une DMIA de 24 heures. La paie, qui dépend des temps de conduite issus de TeleFleet, a une DMIA de 5 jours, et l'on suppose qu'elle reste au-dessus de 72 heures même en fin de mois. Que donne la règle d'héritage ?
- TeleFleet descend en classe 4, comme la paie qui en dépend
- La paie monte en classe 2, comme TeleFleet dont elle dépend
+ TeleFleet reste en classe 2, car la paie est de classe inférieure
- Les deux applications passent en classe 3, par moyenne des deux
E: Une application dont dépend une application d'une classe supérieure hérite de cette classe ; l'héritage ne joue que dans ce sens, et la paie (classe 4) est ici de classe inférieure.

Q: Le directeur des prestations d'une mutuelle déclare : « Si le traitement des remboursements s'arrête plus de dix jours, nous perdons nos grands contrats collectifs. » De quelle notion relève ce seuil ?
- De la PDMA
- De la DMIA
- D'une classe de criticité
+ De la MTPD
E: Au-delà de ce seuil, les impacts menacent les contrats essentiels : c'est la durée maximale tolérable de perturbation, qui porte sur l'activité ; la DMIA se fixe en deçà.

Q: Une application exige une PDMA de 1 heure. Sa base est sauvegardée chaque nuit sur un serveur du même local, et une copie part chaque semaine hors site. En cas de destruction du local, quelle perte de données faut-il retenir dans le pire cas ?
+ 168 heures
- 1 heure
- 24 heures
- Aucune, grâce à la copie hors site
E: Seule la copie hebdomadaire survit au sinistre : la perte peut atteindre 7 jours, soit 168 heures.

Q: Pour classer les applications de Medisecure, un apprenant se fonde tantôt sur la DMIA, tantôt sur la gravité, selon ce qui lui paraît le plus parlant pour chaque application. Quel reproche lui faire ?
- Aucun : choisir pour chaque application le critère le plus parlant rend le classement plus juste
+ La règle doit être écrite avant d'être appliquée, la même pour toutes
- Il aurait dû se limiter à la PDMA, seule mesure objective
- Il aurait dû retenir au moins sept classes de criticité
E: Plusieurs règles sont possibles, y compris une règle qui croise deux critères ; l'essentiel est de l'écrire et de l'appliquer à toutes les applications.

# FICHE 27 | Capacité actuelle de reprise, dépendances et écarts | 8

@qcm
Q: Chez Kestrel, le Portail EDI exige une DMIA de 4 heures. Il est hébergé chez le prestataire, dont l'engagement de reprise n'est pas documenté. Que porter dans la colonne de l'écart ?
- 0 h, car un prestataire tient ses engagements contractuels
+ « Non estimable : contrat à lire », un manque qui est un constat
- +4 h, par prudence, faute d'information sur le prestataire
- Rien : un service externe sort de la grille d'impact
E: Quand une information manque, on écrit « non estimable » et on dit laquelle ; ce manque sera porté au diagnostic.

Q: L'éditeur de StockFlow garantirait, dans un contrat fictif, 99,8 % de disponibilité annuelle. La direction des opérations demande une DMIA de 4 heures. Que conclure ?
+ Rien n'est garanti : le taux ne fixe aucune durée de rétablissement
- Le besoin est tenu, car 99,8 % correspond à moins de 4 heures d'arrêt par an
- Le besoin est tenu si la maintenance est programmée la nuit
- L'écart est de +13,5 heures
E: Sur 8 760 heures, 99,8 % autorisent environ 17,5 heures d'arrêt cumulé, qui peuvent tomber en une fois ; il faut chercher dans le contrat une durée maximale de rétablissement.

Q: Une DSI affiche « 99 % de sauvegardes réussies ce trimestre » pour prouver sa capacité de reprise. Qu'est-ce qui manque ?
- Le taux du trimestre précédent, pour montrer la tendance
- Une note de maturité CMMI du domaine
- La validation du directeur général
+ Un test de restauration réussi et daté
E: Un taux de sauvegardes réussies ne dit rien de la capacité à restaurer, ni de la durée nécessaire : seul un test le prouve.

Q: Chez Kestrel, la direction des opérations demande 8 heures pour KDriver et Kestrel Track. On constate qu'un arrêt de Kestrel Track à 4 h prive les chauffeurs de leur tournée pour toute la matinée. Quel motif de discussion est en jeu ?
- L'incohérence entre deux demandes de la même direction
- Le coût probable, sans commune mesure avec l'impact évité
+ Une dépendance cachée
- Le dépassement de la MTPD de l'activité de livraison
E: KDriver ne reçoit ses tournées que par Kestrel Track ; la direction n'avait pas vu que l'arrêt de l'une prive les chauffeurs de l'autre au moment du départ : c'est une dépendance cachée, que la cartographie révèle.

# FICHE 28 | Le PESTEL du SI | 9

@qcm
Q: Dans un PESTEL du SI de Kestrel, un apprenant écrit : « Hausse du prix du gazole (économique) ; effet sur le SI : hausse des coûts de Kestrel. » Quelle correction apporter ?
- Classer le facteur en « environnemental », car il touche aux carburants
- Supprimer le facteur, qui ne concerne pas l'informatique
- Ajouter le montant exact de la hausse en euros
+ Écrire ce que le facteur exige des données et des applications
E: Par exemple : la direction voudra réduire les kilomètres à vide, ce qui exige des données de tournées fiables et un outil d'optimisation. Le facteur devient un facteur pour le SI quand on écrit cette conséquence.

Q: La fin du support étendu de SQL Server 2016, base de RoutePro, est fixée par Microsoft au 14 juillet 2026. Comment traiter ce point dans le dossier de Kestrel ?
- Tout en section 5.1, car c'est une décision d'éditeur
- Tout en section 5.2, car RoutePro fait partie du parc
+ L'annonce de l'éditeur en 5.1, la version installée en 5.2
- Ni l'un ni l'autre : c'est une solution pour le D3
E: La décision de l'éditeur est un facteur externe, la version installée un fait interne ; mélanger les deux est une erreur fréquente, et le SWOT les placera dans deux cases différentes.

Q: Un apprenant classe le règlement européen sur l'espace européen des données de santé (EHDS), publié en mars 2025 et applicable par étapes de 2027 à 2035, dans la dimension « politique ». Que lui dire ?
+ Il relève du légal : texte adopté, avec des dates d'application
- C'est juste, car ses obligations ne s'appliquent pas encore à ce jour
- Il relève du technologique, car il porte sur des données
- Il n'a pas sa place dans le PESTEL, car il est européen
E: On classe en « légal » ce qui est en vigueur ou adopté avec une date d'application ; le « politique » réunit orientations, programmes et textes en discussion.

Q: Une PME a trouvé deux facteurs environnementaux et aucun facteur politique. Son analyste propose d'écrire un facteur politique vague pour remplir la case. Qu'en penser ?
- C'est la bonne démarche, puisque chaque case du tableau doit être remplie
+ Il faut chercher un facteur politique réel, sourcé, avec son effet
- Il suffit d'écrire « aucun facteur politique » dans la case
- On peut déplacer un facteur environnemental en « politique »
E: La grille sert à n'oublier aucune famille ; le D2 demande un facteur sourcé par dimension, avec son effet écrit sur le SI, pas un remplissage.

# FICHE 29 | Cinq forces, facteurs clés de succès et évaluation des impacts | 9

@qcm
Q: Chez Kestrel, la grande distribution pèse 60 % du chiffre d'affaires et applique des pénalités en cas de retard. Quelle exigence sur le SI ce pouvoir des clients fait-il naître ?
+ Un EDI disponible et des preuves de livraison horodatées
- Un site web plus attractif pour les particuliers
- Une baisse des prix des prestations, financée par le SI
- Une application mobile réservée aux acheteurs de la grande distribution
E: Un client puissant impose ses formats, ses délais et ses engagements ; le SI doit les tenir et prouver le service rendu, en cas de litige sur une pénalité.

Q: Un apprenant présente comme « analyse des cinq forces » le tableau des concurrents de Medisecure, avec leur nombre de centres. Qu'est-ce qui manque ?
- Le chiffre d'affaires et la part de marché de chaque concurrent
- Une sixième force consacrée à l'État
- La date de création de chaque concurrent
+ Des constats qui relient la pression concurrentielle au SI
E: Une liste de concurrents est un fait ; l'élément E16 attend au moins deux constats qui relient la pression concurrentielle à une exigence sur le SI.

Q: Un programme public finance l'interopérabilité, mais conditionne ses versements à des indicateurs qu'une organisation n'atteint pas aujourd'hui. Comment classer ce facteur ?
- En opportunité, puisqu'il apporte un financement
+ Le dédoubler, ou retenir la face dominante justifiée par un fait
- En menace, puisque les indicateurs ne sont pas atteints aujourd'hui
- L'écarter, puisqu'un facteur ne peut pas avoir deux faces
E: Un facteur à deux faces se dédouble en une opportunité et une menace, ou garde sa face dominante ; le classement se justifie par un fait de l'organisation.

Q: Dans le transport de colis, dire au client où est son colis est un facteur clé de succès. Un transporteur constate que son suivi n'est mis à jour qu'une fois par jour. Comment traiter ce constat ?
- Comme une menace externe, à placer dans la section 5.1
- Comme une opportunité, puisque les concurrents font mieux
+ Comme une faiblesse probablement majeure du diagnostic interne
- Comme un point secondaire, faute de plainte des clients
E: Un facteur clé de succès que le SI ne soutient pas est souvent une faiblesse majeure ; les facteurs clés de succès font le pont entre l'analyse externe et le diagnostic interne.

# FICHE 30 | Diagnostic, domaines et échelles de maturité | 10

@qcm
Q: Chez Kestrel, les sauvegardes sont faites sur un NAS de la salle serveur, chaque nuit selon l'hypothèse H1, avec une copie hebdomadaire sur disque externe conservée au siège ; aucun test de restauration n'est documenté. Quelle note est défendable sur l'échelle à cinq niveaux ?
- 3, car une copie sur disque externe existe hors de la salle
- 4, car les sauvegardes ont lieu chaque nuit
+ 2, car les pratiques existent sans isolement ni test documenté
- 5, car deux supports de sauvegarde coexistent au siège
E: Le niveau 3 exige une politique écrite, une copie hors site et un test ; la copie reste au siège, donc pas hors site, et aucun test n'est documenté.

Q: Un apprenant écrit : « Domaine applications : noté 2,5. » sans autre phrase. Quel est le principal reproche ?
- L'usage d'une demi-note, que l'échelle du cours interdit
+ L'absence des faits qui prouvent les critères du niveau
- L'absence d'une note sur 20, plus lisible pour la direction
- L'absence du modèle officiel de COBIT 2019
E: Règle de preuve : chaque note est suivie de « noté N parce que… ». Une demi-note se tolère si elle est expliquée.

Q: Chez un e-commerçant, chaque évolution du site coûte deux fois plus cher qu'il y a trois ans, car le code, écrit dans l'urgence, n'a jamais été restructuré. Ce symptôme relève surtout :
- De l'obsolescence technique
- D'un défaut de gouvernance
- D'un manque de budget
+ De la dette technique
E: La dette technique produit des intérêts : chaque évolution coûte plus cher que si le code avait été bien conçu. L'obsolescence technique, elle, se date par la fin de support d'un composant.

Q: Lequel de ces énoncés du diagnostic de Kestrel compare un indicateur à une référence ?
+ « RoutePro arrêté 9 heures en 2024, pour 2 heures tolérées »
- « Kestrel dispose de deux serveurs de virtualisation au siège »
- « La disponibilité de RoutePro est bonne selon les utilisateurs »
- « Le budget SI de 2026 s'élève à 1,3 M€ »
E: Un indicateur n'a de sens que comparé à une référence ; ici, le besoin exprimé par les métiers, soit un écart de 7 heures.

# FICHE 31 | Hiérarchiser forces et faiblesses, construire le SWOT | 10

@qcm
Q: Dans le SWOT de Kestrel, quel croisement désigne le point le plus critique ?
- L'équipe de développement face à l'attente de suivi en temps réel
+ Les pénalités de la grande distribution face à F1 (SAL-01)
- L'opportunité liée à ISO 14001 face à la faiblesse F5, sans gouvernance
- La menace NIS2 face à la force que représente le canal EDI majoritaire
E: Une menace qui frappe directement une faiblesse désigne un point critique ; ici, F1 (RoutePro et toute l'infrastructure du siège reposent sur la seule salle SAL-01, sans site de secours ni restauration testée, score 9) est exposée aux pénalités de retard.

Q: Une faiblesse est notée impact 2 et urgence 1. L'éditeur du composant concerné annonce sa fin de support dans huit mois. Que devient son score ?
- 2, car une annonce ne change aucune note
- 4, car l'urgence passe à 2
+ 6, car l'urgence passe à 3
- 9, car l'impact et l'urgence passent à 3
E: Une échéance de moins d'un an donne une urgence de 3 ; l'impact, lui, ne change pas : 2 × 3 = 6.

Q: Un apprenant liste comme force de Kestrel « aucune fuite de données connue ». Quel est le défaut ?
+ Une force est une ressource, pas l'absence d'une faiblesse
- Le fait n'est pas sourcé, mais c'est bien une force de Kestrel
- C'est une opportunité externe, pas une force interne
- C'est une menace, puisqu'une fuite pourrait survenir demain
E: Une force se prouve par un fait positif sur lequel la stratégie peut s'appuyer : compétence, application appréciée, actif de données, contrat favorable.

Q: À quoi le D2 demande-t-il de relier les cinq faiblesses les mieux classées ?
- À une solution chiffrée qui sera détaillée dans le D3
- À un concurrent du marché qui maîtrise mieux ce point
- À une note de maturité supérieure à 3 dans leur domaine
+ À un risque ou à un écart, et à un objectif du plan 2030
E: C'est la condition c de l'élément E18 : un risque de la partie 3 ou un écart de la partie 4, et un objectif du plan 2030.

# FICHE 32 | Enjeux, synthèse pour une direction et restitution orale | 10

@qcm
Q: Quelle phrase convient à la synthèse d'une page destinée au comité de direction de Kestrel ?
- « Le TMS on-premise présente un SPOF critique pour l'exploitation »
- « Le niveau CMMI global du SI est estimé à 1,8 sur 5 »
- « Voir le schéma de l'annexe C pour le détail des dépendances de RoutePro »
+ « Une panne du logiciel des tournées a coûté 38 000 € de pénalités »
E: La synthèse remplace le nom d'un composant par sa fonction, donne les conséquences métier, n'utilise aucun sigle non expliqué et ne renvoie à aucun schéma.

Q: Un apprenant formule l'enjeu : « Choisir entre un site de secours et une reprise dans le cloud pour RoutePro. » Que lui reprocher ?
+ L'arbitrage ferme d'autres options et l'enjeu n'a pas d'échéance
- Rien : un arbitrage entre deux solutions est une forme acceptable
- Seulement l'absence d'échéance, la forme étant correcte
- Il faudrait remplacer « choisir » par « migrer vers le cloud »
E: « Choisir entre… et… » n'est acceptable que si toutes les options restent ouvertes ; un enjeu porte aussi une échéance justifiée et se relie à une faiblesse ou à un risque.

Q: Pendant la restitution, la directrice médicale de Medisecure demande ce que signifierait l'arrêt d'un logiciel critique. Quel angle choisir pour répondre ?
- Le délai de restauration du logiciel
- Le coût du support étendu de l'éditeur
+ La sécurité des patients et la continuité des soins
- Le score CVSS des vulnérabilités du logiciel
E: On parle à chaque membre du comité dans sa langue : la directrice médicale raisonne en sécurité des patients.

Q: Un apprenant propose douze enjeux dans sa section 5.4 pour ne rien oublier. Quel conseil lui donner ?
- Les garder tous, puisque le D2 demande au moins dix enjeux distincts
+ Les regrouper : au-delà de sept, la direction ne les retient plus
- N'en garder que trois, pour être lisible par la direction
- Les répartir entre la synthèse et la partie 6 du dossier
E: Cinq enjeux au moins sont demandés ; au-delà de sept, il faut regrouper.
