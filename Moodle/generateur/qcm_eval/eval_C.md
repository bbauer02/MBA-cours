# FICHE 21 | Radar technologique et matrice impact × maturité | 5

@qcm
Q: Le radar de Thoughtworks classe une technologie dans l'anneau « Adopter ». À la DSI de Medisecure, personne ne la maîtrise et aucun projet ne l'a encore utilisée. Où la placer sur le radar de Medisecure ?
- Adopter, puisque Thoughtworks la recommande déjà
- Suspendre, puisque l'équipe ne sait pas l'utiliser
+ Évaluer, pour comprendre d'abord ce qu'elle apporterait
- Préparer, pour la surveiller de près
E: Le radar d'une organisation dépend de ses compétences, de son budget et de ses règles : sans compétence interne, on commence par explorer. « Préparer » est une zone de la matrice impact × maturité, pas un anneau du radar.

Q: Une start-up présente le prototype d'une IA qui trierait les alertes de télésurveillance. Aucun client ne l'utilise encore. Pour Medisecure, dont les infirmières jugent 85 % des alertes inutiles, l'impact serait fort. Quelle conduite adopter ?
+ Préparer : surveiller de près et suivre les prochains résultats
- Agir : instruire tout de suite une recommandation
- Ignorer pour l'instant, faute de client de référence
- Opportunité ponctuelle : l'utiliser si l'occasion se présente
E: Impact fort et maturité faible (un simple prototype) placent l'information dans « Préparer ». « Agir » suppose une solution éprouvée ou un texte applicable.

Q: Un éditeur publie une version stable de son outil de visioconférence, qui améliore un peu le partage d'écran. Aucun projet de Medisecure n'en dépend. Que faire de cette information ?
- La placer dans « Agir » et lancer un projet dédié
- La placer dans « Préparer » et la surveiller de près
+ L'utiliser si l'occasion se présente, sans projet dédié
- La supprimer de la base, puisqu'elle ne sert à rien
E: Maturité forte et impact faible : c'est une opportunité ponctuelle. On ne lui consacre pas de projet, mais on ne l'efface pas pour autant.

Q: En 2025, une technologie à fort impact pour Medisecure n'existe qu'en prototype. En 2026, plusieurs centres de santé comparables l'utilisent avec succès en production. Comment évolue sa place dans la matrice impact × maturité ?
- Elle reste dans « Préparer », car l'impact n'a pas changé
- Elle passe de « Ignorer pour l'instant » à « Agir »
+ Elle passe de « Préparer » à « Agir »
- Elle passe d'« Agir » à « Opportunité ponctuelle »
E: L'impact reste fort, mais la maturité devient forte : la technologie se déplace de « Préparer » vers « Agir », où l'on étudie une recommandation.

# FICHE 22 | Évaluer l'impact environnemental | 5

@qcm
Q: La DSI compare deux offres de visioconférence pour les 14 centres. La première impose un boîtier neuf dans chaque salle, la seconde fonctionne avec les écrans déjà en place. Les deux consomment autant d'électricité. Laquelle a la plus faible empreinte ?
- La première, car un matériel neuf consomme moins qu'un ancien
- Les deux à égalité, car leur consommation électrique est identique
+ La seconde, car elle évite de fabriquer 14 boîtiers neufs
- La première, car un boîtier dédié allège le réseau des centres
E: Raisonner en cycle de vie, c'est compter la fabrication, l'usage et la fin de vie ; fabriquer un équipement pèse souvent plus lourd que l'utiliser. À consommation égale, l'offre qui évite du matériel neuf a la plus faible empreinte.

Q: Medisecure envisage de déplacer les applications de la salle serveur du siège vers un hébergeur cloud. Pour noter l'impact environnemental de ce projet, à quoi faut-il le comparer ?
- À un centre de données idéal, alimenté uniquement en énergie renouvelable
- À la part moyenne du numérique dans l'empreinte carbone française
+ À la situation actuelle, avec les équipements déjà en place
- À l'offre la plus sobre proposée par un hébergeur concurrent
E: La méthode du cours compare toujours à la situation actuelle, et non à une situation idéale ou à une moyenne nationale.

Q: Un éditeur annonce que la nouvelle version de son DPI « consommera moins de ressources », sans donner aucun chiffre. Elle s'installe sur les postes actuels des centres. Avec le barème du cours, quelle note environnementale retenir ?
- 3, car l'éditeur annonce une baisse des ressources
+ 2, car la baisse annoncée n'est ni chiffrée ni vérifiée
- 1, car toute nouvelle version alourdit l'empreinte
- 0, car un DPI traite un grand volume de données
E: Le barème réserve la note 3 à une réduction mesurable de l'empreinte. Une baisse annoncée sans chiffre, sans nouvel équipement, reste neutre ou incertaine (note 2), et l'hypothèse retenue s'écrit à côté de la note.

Q: Un projet de Medisecure impose l'achat de deux serveurs neufs, hébergés chez un prestataire certifié HDS, pour entraîner un modèle d'IA. Aucun équipement n'est retiré. Avec le barème du cours, quelle note environnementale retenir ?
- 2, car l'hébergeur est certifié HDS
- 3, car l'IA permettra peut-être d'autres économies
+ 0, car le projet dégrade nettement l'empreinte
- 2, car seule la consommation électrique compte
E: Le barème donne 0 pour une dégradation nette : nouveaux équipements, calcul intensif. La certification HDS porte sur la sécurité des données de santé, pas sur l'empreinte, et la note s'accompagne de l'hypothèse retenue.

# FICHE 23 | La fiche de veille et la base de connaissances | 5 et 8

@qcm
Q: Le RSSI dépose sur Teams le lien d'un blog qui annonce une faille dans Keycloak 15. Le veilleur n'a encore trouvé ni l'avis de l'éditeur ni la fiche CVE. Quel statut donner à la fiche ?
- Vérifiée, car le RSSI est une personne fiable
- Diffusée, car l'information circule déjà sur Teams
+ À confirmer, faute de source primaire trouvée
- Archivée, en attendant l'avis de l'éditeur
E: Une fiche reste « à confirmer » tant que la source primaire n'est pas trouvée. La fiabilité du correspondant ne remplace pas la source primaire.

Q: Dans le résumé d'une fiche de veille, un apprenant écrit : « Cette décision de la CNIL est inquiétante et Medisecure devrait réagir vite. » Que faut-il en penser ?
+ Ce jugement relève de l'analyse ; le résumé reste factuel
- C'est correct : le résumé doit donner l'avis du veilleur
- Cette phrase doit devenir le titre de la fiche
- Il faut la supprimer : une fiche ne donne jamais d'avis
E: Le résumé tient en trois à cinq phrases factuelles. Ce que l'information change pour Medisecure va dans la rubrique « analyse pour l'organisation », qui fait la différence avec une revue de presse.

Q: Medisecure utilise déjà Microsoft 365. Son chargé de veille veut ranger les fiches dans un outil de prise de notes qu'il est seul à utiliser. Quel conseil lui donner ?
- Garder son outil, s'il le maîtrise mieux que les autres
- Choisir l'outil du marché qui offre le plus de fonctions
+ Préférer une liste SharePoint ou un canal Teams de Medisecure
- Enregistrer les fiches dans un dossier de son ordinateur
E: L'outil compte moins que la structure : mieux vaut un outil que l'organisation utilise déjà. Un outil que personne d'autre n'utilise fait disparaître la base avec son créateur.

Q: Un apprenant a noté 15 informations. Les cinq premières de sa grille portent toutes sur la cybersécurité. Comment choisir ses trois fiches de veille pour le dossier D1 ?
- Trois fiches en cybersécurité, puisque ce sont les trois mieux notées
- Une fiche par axe sur trois axes différents, quelle que soit la note
- Les trois informations les plus récentes, quel que soit leur axe
+ Deux en cybersécurité, la troisième sur la mieux notée d'un autre axe
E: Les fiches viennent du premier tiers de la grille et couvrent au moins deux axes. Si ce tiers ne couvre qu'un axe, la troisième fiche porte sur l'information la mieux notée d'un autre axe, avec une phrase de justification.

# FICHE 24 | Lire un texte réglementaire en veilleur | 6

@qcm
Q: Une directive européenne impose de nouvelles obligations, mais la loi française de transposition n'est pas encore votée. Une entreprise veut savoir ce qui lui sera exactement demandé. Que doit suivre le veilleur ?
- Rien : la directive s'applique déjà directement en France
+ Le projet de loi national, puis ses décrets d'application
- Uniquement EUR-Lex, car la directive fixe tous les détails
- Uniquement la presse spécialisée, plus rapide que les sites officiels
E: Une directive doit être transposée par des textes nationaux ; tant que ce n'est pas fait, on ne sait pas exactement ce qui sera demandé. On suit donc le projet de loi, puis les décrets qui le complètent.

Q: Un règlement européen est entré en vigueur le mois dernier ; ses obligations ne s'appliqueront que deux ans après cette date. Un consultant affirme à Medisecure qu'elle doit être en conformité dès aujourd'hui. Qu'en penser ?
- Il a raison : un texte en vigueur est déjà exigible
- Il a raison, car un règlement s'applique sans transposition
- Il a tort, car un règlement doit d'abord être transposé
+ Il a tort, car les obligations ne s'appliquent que dans deux ans
E: L'entrée en vigueur fait exister le texte ; les obligations ne deviennent exigibles qu'à la date d'application, ici deux ans plus tard. Un règlement n'a pas besoin de transposition, mais cela ne change pas sa date d'application.

Q: Les centres de Medisecure sont tous situés en France. Pour le Data Act, le veilleur doit-il attendre une loi française avant de considérer le texte comme applicable ?
+ Non, c'est un règlement : il s'applique directement dans toute l'UE
- Oui, car c'est une directive, comme NIS2
- Oui, tant que Légifrance n'en a pas publié la traduction
- Non, car le Data Act ne vise que les États, pas les entreprises
E: Le Data Act est un règlement : il s'applique directement, sans transposition. Le veilleur suit son calendrier et ses textes d'application.

Q: Un apprenant écrit dans son dossier : « L'AI Act impose des obligations aux systèmes à haut risque. » Selon la méthode du cours, que manque-t-il à cette phrase ?
- La date d'entrée en vigueur du règlement, le 1er août 2024
- Le lien vers un article de presse qui résume le texte
+ La date d'application de l'obligation, avec son article
- La date de transposition de l'AI Act dans le droit français
E: Il faut citer la date d'application de l'obligation dont on parle, avec l'article qui la fixe : l'entrée en vigueur ne suffit pas, car les règles sur le haut risque s'appliquent plus tard. L'AI Act est un règlement : il n'est pas transposé.

# FICHE 25 | Données personnelles et données de santé | 6

@qcm
Q: Un laboratoire de recherche demande à Medisecure un fichier des patients télésurveillés, sans les noms, mais avec le sexe, le code postal, la date de la dernière hospitalisation et le traitement suivi. Que vaut ce fichier au regard du RGPD ?
- Il est anonyme, puisque les noms des patients ont été retirés
- Il échappe au RGPD si le laboratoire est situé en France
+ Il reste soumis au RGPD, car il n'est pas anonyme
- Il devient anonyme si chaque nom est remplacé par un code
E: Croisées, ces informations permettent souvent de retrouver un patient : le fichier n'est pas anonyme et le RGPD s'applique. Remplacer le nom par un code donne des données pseudonymisées, qui restent des données personnelles.

Q: Lors de l'incident de mars 2025, Medisecure a découvert le chiffrement le 12 mars à 7 h 45. La violation présentait un risque pour les patients. Jusqu'à quand fallait-il prévenir la CNIL ?
- Le 13 mars à 7 h 45
+ Le 15 mars à 7 h 45
- Le 12 avril, soit un mois après
- Aucun délai : le signalement au CERT Santé suffisait
E: Le RGPD impose de prévenir la CNIL au plus tard 72 heures après la découverte. Medisecure l'a fait le 17 mars, trop tard ; le signalement au CERT Santé ne remplace pas la notification à la CNIL.

Q: La salle serveur du siège est exploitée par Medisecure Services SAS. Elle stocke les dossiers des patients des centres, gérés par l'association Medisecure Santé. Pourquoi cette situation pose-t-elle une question de certification HDS ?
+ La société héberge des données de santé pour un tiers, l'association
- La salle serveur se trouve hors de l'Espace économique européen
- Toute salle serveur qui stocke des dossiers doit être certifiée ISO/IEC 27001
- L'association n'a pas désigné de délégué à la protection des données
E: La certification HDS est exigée de quiconque héberge des données de santé pour le compte d'un tiers. Ici, la société et l'association sont deux entités juridiques distinctes.

Q: Le directeur des opérations veut lancer un modèle d'IA qui exploite les dossiers des patients pour prédire les rendez-vous non honorés. Le DPO estime que ce traitement peut créer un risque élevé. Quand conduire l'analyse d'impact (AIPD) ?
- Dans les 72 heures qui suivent la mise en production
- Seulement si la CNIL en fait la demande
- Après un premier incident sur ces données
+ Avant de lancer le traitement
E: L'AIPD est une étude obligatoire, menée avant le lancement d'un traitement qui présente un risque élevé pour les personnes. Le délai de 72 heures concerne la notification d'une violation.

# FICHE 26 | IA et dispositifs médicaux | 6

@qcm
Q: Medisecure étudie une IA qui classerait les alertes de télésurveillance pour signaler aux infirmières les patients à appeler en priorité. Le logiciel est qualifié de dispositif médical de classe IIb. Quelle conséquence pour l'AI Act ?
- Elle relève du MDR seul, donc échappe à l'AI Act
+ Elle est en principe un système d'IA à haut risque
- Elle n'est soumise qu'à une obligation de transparence
- Elle devient à haut risque seulement si elle traite des données de santé
E: Un logiciel d'IA qui est un dispositif médical de classe IIa ou supérieure, donc évalué par un organisme extérieur, est en principe à haut risque au sens de l'AI Act. Le MDR figure à l'annexe I de l'AI Act : être un dispositif médical ne fait pas échapper à l'AI Act.

Q: Un éditeur développe un outil d'IA qui prédit les rendez-vous non honorés et le vend à Medisecure, qui l'utilise dans ses 14 centres. Quels sont les rôles de chacun dans l'AI Act ?
- L'éditeur est déployeur, Medisecure est fournisseur
- Les deux sont fournisseurs, car ils sont liés par un contrat
+ L'éditeur est fournisseur, Medisecure est déployeur
- Les deux sont déployeurs, car l'outil sert aux patients
E: Le fournisseur développe le système et le met sur le marché ; le déployeur l'utilise dans son activité. Leurs obligations sont différentes.

Q: La DRH de Medisecure envisage une IA qui trie les candidatures des infirmières. Ce logiciel n'est pas un dispositif médical. Pourquoi peut-il quand même relever du haut risque de l'AI Act ?
- Il traite des données de santé des candidates
+ Son usage, l'emploi, fait partie des usages sensibles de l'annexe III
- Medisecure soigne des patients, donc tous ses outils d'IA sont visés
- Tout système d'IA est à haut risque dès l'entrée en vigueur du texte
E: Un système peut être à haut risque par le produit qu'il équipe (annexe I, dont les dispositifs médicaux) ou par son usage (annexe III : emploi, éducation, accès aux services essentiels). Le secteur de la santé ne rend pas à lui seul un outil à haut risque.

Q: Parmi ces outils envisagés par Medisecure, lequel a une finalité médicale qui peut en faire un dispositif médical ?
+ Un outil qui propose une dose d'insuline à partir des mesures de glucose
- Un outil qui synchronise les plannings des médecins et les agendas
- Un outil qui produit le fichier mensuel des forfaits de télésurveillance
- Un outil qui envoie aux patients des rappels de rendez-vous par SMS
E: Un logiciel est un dispositif médical si son fabricant lui donne une finalité médicale : diagnostiquer, surveiller, prévenir ou traiter une maladie. Proposer une dose d'insuline contribue au traitement.

# FICHE 27 | Cybersécurité et données : NIS2, CRA, Data Act | 6

@qcm
Q: Une entité soumise à NIS2 détecte un incident important le lundi à 10 h. Quel calendrier de signalement respecte la directive ?
- Notification avant mardi 10 h, alerte avant jeudi 10 h, rapport final sous un mois
- Un seul rapport complet, envoyé avant jeudi 10 h
+ Alerte avant mardi 10 h, notification avant jeudi 10 h, rapport final sous un mois
- Alerte avant jeudi 10 h, rapport final avant le lundi suivant
E: NIS2 prévoit une alerte précoce sous 24 heures, une notification sous 72 heures, puis un rapport final sous un mois.

Q: Medisecure dépend de la plateforme du fabricant pour récupérer les mesures des balances et tensiomètres connectés de ses patients. Quel texte européen organise l'accès aux données produites par ces appareils et leur partage avec un tiers ?
- Le Cyber Resilience Act
- La directive NIS2
- L'AI Act
+ Le Data Act
E: Le Data Act donne aux utilisateurs de produits connectés un droit d'accès aux données que ces produits génèrent, et un droit de les partager avec un tiers, ce qui peut réduire la dépendance de Medisecure au fabricant. Le CRA porte sur la sécurité des produits, NIS2 sur la cybersécurité des organisations.

Q: En octobre 2026, le fabricant des boîtiers télématiques des camions de Kestrel apprend qu'une faille de son micrologiciel est activement exploitée. Quel texte l'oblige à la signaler ?
- Le Data Act, car les boîtiers produisent des données
+ Le Cyber Resilience Act, qui vise les produits numériques
- NIS2, dès sa transposition dans chaque pays de l'Union
- Le RGPD, car les boîtiers géolocalisent les chauffeurs
E: Depuis le 11 septembre 2026, le CRA oblige les fabricants de produits numériques à signaler les failles activement exploitées. Le Data Act porte sur l'accès aux données, pas sur leur sécurité.

Q: Un collègue affirme : « La transposition de NIS2 était due le 17 octobre 2024, donc la loi française s'applique déjà à Medisecure. » Que doit faire le veilleur ?
- L'approuver, puisque la date limite fixée pour la transposition est dépassée
+ Vérifier où en est la loi à l'Assemblée nationale et dater ce contrôle
- Le contredire, car NIS2 ne vise pas du tout le secteur de la santé
- Le contredire, car NIS2 est un règlement qui s'applique sans loi nationale
E: Une date limite dépassée ne crée pas la loi nationale. À la date du cours, la loi « Résilience » était en attente : on suit le dossier législatif sur le site de l'Assemblée nationale et on date chaque vérification.

# FICHE 28 | Diffuser au bon lecteur | 8

@qcm
Q: Une campagne d'hameçonnage vise les centres de santé. Dès aujourd'hui, les secrétaires de Medisecure doivent transférer au support tout courriel suspect. Quel livrable leur adresser ?
- La note de synthèse d'une page, avec les options et leur coût
- La fiche technique, avec les indicateurs de compromission
+ Un flash de quelques lignes, sans sigle, sur cette seule consigne
- La prochaine newsletter mensuelle, avec les autres actualités
E: Le flash sert à faire appliquer une consigne par les équipes. Une alerte urgente ne peut pas attendre la newsletter, et la note comme la fiche technique visent d'autres lecteurs.

Q: Une faille touche Keycloak 15, utilisé par Medisecure Connect. Qu'attend surtout le tech lead de la plateforme dans la fiche technique ?
+ Les versions touchées, l'identifiant CVE, le correctif et les tests à faire
- Les options possibles, leurs coûts et la décision à prendre par la direction
- Une consigne de trois lignes, sans sigle, pour les équipes d'accueil
- Une sélection commentée des actualités du mois, classées par axe
E: La fiche technique sert à faire agir : versions exactes, identifiants des vulnérabilités, procédure et tests. Le tech lead doit pouvoir créer un ticket sans recherche complémentaire.

Q: Pour son flash destiné aux secrétaires, un apprenant reprend le premier paragraphe de sa note au DSI : contexte réglementaire, deux options chiffrées, décision attendue. Quel défaut le correcteur relèvera-t-il ?
- Le flash est trop court pour être pris au sérieux par les équipes
+ Le texte demande une décision au lieu de donner une consigne
- Le flash aurait dû être validé d'abord par le tech lead
- Le flash ne doit jamais mentionner un texte réglementaire
E: Chaque format part de ce que le lecteur doit faire après lecture : la note fait décider la direction, le flash fait appliquer une seule consigne aux équipes. Un flash peut citer un texte, à condition de rester clair et sans sigle inexpliqué.

Q: Une note de veille contient une matrice où seule la couleur rouge signale les sujets urgents, et un graphique dont le texte alternatif est « Graphique ». Quelle correction faut-il faire ?
- Choisir un rouge plus vif et agrandir le graphique pour mieux le voir
- Écrire « urgent » à côté du rouge et garder « Graphique » comme texte alternatif
- Ajouter une légende des couleurs et un titre plus long au graphique
+ Écrire « urgent » à côté du rouge et dire ce que montre le graphique
E: L'information ne doit jamais passer par la couleur seule, et le texte alternatif dit ce qu'il faut retenir de l'image : « Graphique » ne dit rien. Une légende des couleurs laisse l'urgence portée par la seule couleur.

# FICHE 29 | Faire vivre et mesurer la veille | 8

@qcm
Q: Le CERT-FR publie une alerte critique le lundi à 9 h. Le tech lead de Medisecure reçoit la fiche technique le mardi à 15 h. Quel indicateur cela renseigne-t-il, et avec quelle valeur ?
- Le délai d'alerte : 6 heures
- Les décisions alimentées : une décision
+ Le délai d'alerte : 30 heures
- Le taux de lecture : 100 %
E: Le délai d'alerte mesure le temps écoulé entre la publication d'une information et sa diffusion au destinataire : de lundi 9 h à mardi 15 h, 30 heures.

Q: Medisecure est une organisation fictive. Pour son dossier, quel indicateur un apprenant peut-il réellement chiffrer à partir de sa propre veille pendant l'intersession ?
- Le délai entre un bulletin du CERT-FR et la lecture de la fiche par le tech lead
- Le nombre de décisions de la direction alimentées par sa veille
+ Le délai entre la publication d'une information et sa fiche
- Le nombre de signalements reçus de ses correspondants chez Medisecure
E: Les indicateurs qui supposent des destinataires ou des correspondants réels chez Medisecure sont déclarés « non mesuré ». Le délai entre la publication et la fiche ne dépend que du travail de l'apprenant.

Q: Ce trimestre, le DPO a signalé trois informations au veilleur. L'une a permis de lancer l'analyse d'impact de MediSuivi. Que doit faire le veilleur pour entretenir ce réseau ?
- Lui demander de remplir une fiche complète à chaque signalement
- Lui envoyer chaque mois la liste à jour des axes de veille
- Remercier tous les correspondants par un même courriel type
+ Lui dire que son signalement a servi et le citer dans la newsletter
E: Animer un réseau, c'est rendre la contribution facile et visible : dire à chacun à quoi son signalement a servi. Exiger une fiche complète décourage la participation, et un courriel type ne dit à personne à quoi il a servi.

Q: En six mois, les signalements reçus des correspondants passent de 4 à 20 par mois, mais la plupart sont hors des axes de veille. Que peut-on en conclure ?
- La veille est devenue cinq fois plus utile pour la direction
- Le taux de lecture des livrables a lui aussi été multiplié par cinq
+ Le réseau est plus actif, mais ce volume ne prouve pas l'utilité
- Il faut cesser de suivre cet indicateur, qui ne sert à rien
E: Les contributions du réseau mesurent sa vitalité ; le volume ne dit rien de la pertinence. L'utilité réelle se juge aux décisions alimentées.

# FICHE 30 | Une recommandation exploitable | 9

@qcm
Q: Lequel de ces énoncés est une recommandation exploitable pour Medisecure ?
- Moderniser la télésurveillance grâce à l'intelligence artificielle
+ Tester 4 mois un tri IA des alertes des insuffisants cardiaques
- Sensibiliser la direction aux opportunités de l'IA en santé
- Suivre de près l'AI Act et ses évolutions réglementaires en santé
E: Une recommandation exploitable nomme une action, un périmètre et une durée, et répond à un problème du cas : 85 % d'alertes jugées sans suite. Les autres énoncés sont des intentions ou des alertes.

Q: Un apprenant doit présenter au moins trois recommandations innovantes. Laquelle peut compter comme innovante pour Medisecure ?
- Généraliser l'authentification multifacteur à tous les soignants
- Sensibiliser tous les soignants aux risques de l'IA générative
- Isoler les sauvegardes et écrire un plan de reprise d'activité
+ Prédire les rendez-vous non honorés par un modèle d'IA
E: Une solution innovante est absente du SI de Medisecure, et sa nouveauté et sa maturité sont établies par la veille. L'authentification multifacteur, la sensibilisation, même quand elle porte sur l'IA, les sauvegardes isolées et le plan de reprise sont des mesures de base.

Q: Pour une recommandation de rappels intelligents des rendez-vous au centre de Saint-Denis, quel indicateur de succès est valable ?
- Rendez-vous non honorés à Saint-Denis : descendre sous 8 %
- Nombre de SMS de rappel envoyés aux patients chaque mois
+ Rendez-vous non honorés à Saint-Denis : de 11,2 % à 8 % en six mois
- Patients plus satisfaits et équipes d'accueil moins sollicitées
E: Un indicateur de succès a un point de départ, une cible et une échéance. Viser « sous 8 % » sans valeur de départ ni date ne permet pas de juger la réussite, et le nombre de SMS envoyés mesure l'activité, pas le résultat.

Q: Un apprenant propose de renégocier le contrat de la plateforme de réservation. L'idée lui vient d'une discussion, et aucune information de sa veille ne s'y rapporte. Que lui manque-t-il pour la retenir dans le dossier ?
+ Une information de veille dont la recommandation découle
- Un caractère innovant, exigé pour chaque recommandation
- Un texte réglementaire qui rende la renégociation obligatoire
- L'accord préalable de la direction de Medisecure
E: Chaque recommandation doit découler d'une information de veille. Elle n'a pas besoin d'être innovante : au moins trois sur cinq doivent l'être, pas toutes.

# FICHE 31 | Chiffrer et prioriser | 9

@qcm
Q: Le dossier Medisecure fixe le coût d'un développeur interne confirmé à 68 k€ par an, charges comprises. Avec une hypothèse de 200 jours travaillés par an, combien coûtent 20 jours de son travail ?
- Environ 340 €
- Environ 3,4 k€
+ Environ 6,8 k€
- Environ 13,6 k€
E: 68 000 € ÷ 200 jours = 340 € par jour ; 20 jours × 340 € = 6 800 €, soit environ 6,8 k€. L'hypothèse des 200 jours s'écrit dans le chiffrage.

Q: Le passage de 9 centres à un nouveau DPI comprend la reprise des données (15 à 25 k€ par base, une seule fois) et un abonnement de 23 k€ par centre et par an. Comment classer ces dépenses ?
- Reprise : fonctionnement ; abonnement : investissement
+ Reprise : investissement ; abonnement : fonctionnement
- Les deux sont des investissements, car liés au même projet
- Les deux sont du fonctionnement, car payés à des prestataires
E: L'investissement est une dépense ponctuelle de mise en place ; le fonctionnement revient chaque année. Chez Medisecure, le budget de fonctionnement SI ne peut pas augmenter de plus de 10 % par an.

Q: Un projet occuperait deux développeurs pendant 18 mois pour refaire l'apparence du site WordPress, sans lien avec un objectif du plan Medisecure 2030. Où le placer dans la matrice valeur × effort ?
- Gains rapides : à lancer en premier
- Projets structurants : à planifier
+ À écarter ou à reformuler
- Compléments : si l'occasion se présente
E: Valeur faible et effort fort : le projet est à écarter ou à reformuler. Un projet structurant suppose une valeur forte.

Q: Un assistant d'IA ferait gagner 30 minutes par jour à chaque secrétaire médicale. Le directeur financier veut compter ce gain comme une économie dans le chiffrage. Que lui répondre ?
- Le compter en entier si les secrétaires utilisent l'outil chaque jour
+ Le compter si le temps libéré sert ailleurs ou évite d'embaucher
- Le compter à moitié seulement, pour rester prudent sur le gain réel
- Le compter dès la première année si l'outil est déjà prêt à l'emploi
E: Un gain de temps n'est une économie que si le temps libéré est réellement employé autrement ou évite un recrutement, et cette hypothèse s'écrit. Réduire le gain de moitié au hasard ne remplace pas une hypothèse justifiée.

# FICHE 32 | L'IA générative au service de la veille | 7 et 10

@qcm
Q: Un apprenant fait résumer par un assistant d'IA une ligne directrice de la Commission européenne publiée en anglais. Que demande la charte d'usage de la formation ?
- Rien de particulier : cet usage est autorisé sans aucune condition
- Citer l'assistant comme source du résumé, avec la date de la question
+ Relire le document sur les points utilisés et citer ce document
- Renoncer : faire résumer un document public par une IA est interdit
E: Résumer un document public est autorisé sous conditions : relire le document et citer celui-ci, jamais l'IA. Citer une IA comme source est interdit.

Q: Le pare-feu de Medisecure relève 1 500 connexions par semaine vers des assistants d'IA gratuits, utilisés par des secrétaires pour rédiger des courriers. Le DSI propose de bloquer ces sites et de clore le sujet. Que lui répondre ?
- Bloquer suffit, car le risque de ces outils est surtout technique
+ Bloquer ne suffit pas : il faut aussi proposer un outil approuvé
- Ne rien bloquer, car un courrier ne contient pas de données de santé
- Autoriser ces outils si les secrétaires utilisent un compte personnel
E: C'est de l'IA fantôme : les données saisies sortent du contrôle de Medisecure, sans contrat ni hébergement HDS. Interdire ne suffit pas, car l'usage répond à un besoin réel de gain de temps : il faut proposer un outil approuvé, que la veille aide à choisir.

Q: Un assistant d'IA affirme qu'une obligation figure à « l'article 12 bis » d'un règlement et donne un lien. En l'ouvrant, le veilleur ne trouve aucun article de ce numéro. Que faire de l'affirmation ?
- La garder comme vérifiée, puisque l'IA a donné un lien
- La citer en précisant « selon l'assistant d'IA »
+ La rejeter, car la source donnée ne la confirme pas
- Demander à un autre assistant de la confirmer
E: Si la source proposée n'existe pas ou ne dit pas la même chose, l'affirmation est rejetée. Une IA peut inventer une référence de façon très convaincante : c'est une hallucination.

Q: Dans son entreprise d'alternance, un apprenant veut coller dans un assistant public la liste des versions logicielles de ses serveurs, pour repérer celles hors support. Que prévoit la charte ?
- C'est autorisé, car ces données ne sont pas personnelles
- C'est autorisé si l'historique des conversations est désactivé
- C'est autorisé s'il déclare ensuite cet usage en annexe G
+ Ce n'est permis que dans un outil approuvé par l'employeur
E: Les informations techniques internes (architecture, versions, journaux) décrivent les faiblesses d'une organisation. La charte les interdit dans un outil public et ne les admet que dans un outil approuvé par l'employeur.

# FICHE 33 | L'intersession et le contrôle | 11

@qcm
Q: Au contrôle, l'axe « numérique responsable » d'un apprenant est tiré au sort. Son dispositif n'a rien produit de nouveau sur cet axe depuis le début de la période 2. Que doit-il faire ?
- Présenter une information de l'axe déjà utilisée dans son dossier
+ Montrer son suivi, puis l'information la plus récente de l'axe
- Demander au formateur de tirer au sort un autre axe de veille
- Présenter à la place une information d'un axe non tiré
E: Pour un axe à suivi lent, on montre les flux, les requêtes et le journal, puis l'information la plus récente. Le premier élément est alors noté au plus à la moitié ; une information déjà présente dans le dossier vaut zéro sur cet élément.

Q: Au contrôle, un apprenant ne retrouve rien dans son dispositif et trouve une information récente avec un moteur de recherche pendant les 30 minutes. Quelle conséquence ?
- Aucune, si l'information est récente et absente du dossier
- La veille flash entière est notée zéro
+ Le premier élément noté n'obtient qu'une partie des points
- Le contrôle est reporté pour cet apprenant
E: L'information doit être trouvée dans le dispositif. Trouvée par une recherche pendant le contrôle, elle ne rapporte qu'une partie des points du premier élément ; les autres éléments sont notés normalement.

Q: À la fin de la période 1, un apprenant n'a tenu qu'une séance de veille et n'a aucune capture de son agrégateur. Il prévoit quatre séances en période 2 pour compenser. Est-ce suffisant ?
+ Non, ces exigences se vérifient période par période
- Oui, si le total atteint au moins six séances sur l'intersession
- Oui, s'il rédige deux lignes de journal de plus en période 2
- Non, il doit recommencer toute l'intersession à zéro
E: Deux séances datées et une capture de chaque outil sont exigées dans chacune des trois périodes. Ce qui manque en période 1 ne se rattrape pas : des points sont perdus définitivement.

Q: Pendant une veille flash, un apprenant présente une alerte du CERT Santé sur une faille de VPN. Quelle action proposée répond le mieux au barème du contrôle ?
- Demander aux équipes d'être vigilantes sur le VPN dans les jours à venir
- Signaler la faille au RSSI lors du prochain comité de sécurité
+ Demander au RSSI de corriger le VPN des prestataires sous 48 heures
- Demander au tech lead de la plateforme de corriger le VPN sous 48 heures
E: Le barème attend une action précise, bornée dans le temps et adressée à la bonne fonction. Le tech lead développe et exploite Medisecure Connect, pas le VPN : c'est le RSSI qu'il faut saisir. « Être vigilant » ou « au prochain comité » ne fixent ni action précise ni échéance claire.
