# FICHE 11 | Les types de sources | 3

@qcm
Q: Le RSSI de Medisecure lit sur un blog spécialisé qu'une faille touche Keycloak 15. Pour citer cette information dans une fiche de veille, quel document doit-il retrouver ?
- Un second blog qui annonce la même faille
- L'article de presse qui a inspiré le blog
+ L'avis de sécurité publié par le projet Keycloak
- La synthèse produite par un outil de recherche par IA
E: Le projet qui produit le logiciel est la source primaire de la faille : c'est le dernier maillon de la chaîne, celui qu'on cite. Un second blog reste une source secondaire et ne prouve rien de plus.

Q: Lors d'un salon, un éditeur annonce oralement au DSI de Medisecure la fin prochaine de l'un de ses produits. Comment classer cette source ?
+ Primaire et informelle
- Secondaire et formelle
- Primaire et formelle
- Secondaire et informelle
E: L'éditeur produit l'information sur son propre produit, donc la source est primaire ; une annonce orale dans un salon passe par un canal peu contrôlé, donc informelle. Les deux distinctions sont indépendantes.

Q: Dans sa cartographie, un apprenant écrit : « EUR-Lex est gratuit, donc moins fiable qu'une base juridique payante. » Que faut-il lui répondre ?
- Il a raison, une base payante est mieux contrôlée
- Il a tort, une source gratuite est toujours primaire
+ Il a tort, EUR-Lex publie lui-même le droit de l'Union
- Il a raison, EUR-Lex n'est qu'une source secondaire
E: Le coût et la fiabilité sont indépendants. EUR-Lex est gratuit, mais c'est une source primaire, puisqu'il publie le droit de l'Union européenne ; une source gratuite n'est pas primaire pour autant.

Q: Le blog de l'éditeur de MediDossier publie les notes de version de MediDossier v8 et un résumé d'une nouvelle recommandation de la CNIL. Comment classer ce blog ?
- Primaire pour les deux contenus, car l'éditeur est identifié
- Secondaire pour les deux contenus, car c'est un blog
+ Primaire pour les notes de version, secondaire pour la CNIL
- Secondaire pour les notes de version, primaire pour la CNIL
E: Une source est primaire pour ce qu'elle produit elle-même et secondaire pour ce qu'elle rapporte. Le résumé d'une recommandation de la CNIL reprend une information produite ailleurs.

# FICHE 12 | Les grandes sources institutionnelles | 3

@qcm
Q: Medisecure se demande quelles obligations s'appliquent à la salle serveur de son siège au regard du référentiel HDS. Quel organisme consulter en priorité ?
- La Haute Autorité de santé
+ L'Agence du numérique en santé
- L'ENISA, agence de l'Union européenne
- La CNIL, autorité des données personnelles
E: L'Agence du numérique en santé publie les référentiels du numérique en santé, dont le référentiel HDS. La HAS publie des recommandations de bonne pratique, pas ce référentiel.

Q: Le dossier Medisecure demande si l'application MediSuivi est un dispositif médical. Quelle source institutionnelle ajouter à la cartographie pour suivre la surveillance de ces dispositifs ?
- L'Agence du numérique en santé
- La CNIL
- Le CERT Santé
+ L'ANSM
E: L'ANSM surveille les dispositifs médicaux, y compris les logiciels. L'ANS publie les référentiels du numérique en santé, la CNIL contrôle le RGPD et le CERT Santé diffuse les alertes de sécurité du secteur.

Q: Chez Kestrel, le flux RSS d'une autorité, configuré il y a deux ans dans l'agrégateur, ne remonte plus rien depuis un mois, alors que son site publie toujours. Que faut-il vérifier d'abord ?
+ Que l'adresse du flux est toujours celle du site actuel
- Que l'autorité est toujours compétente sur le sujet
- Que la cote de fiabilité de l'autorité n'a pas changé
- Que l'export OPML de l'agrégateur fonctionne encore
E: Les adresses des institutions changent, comme l'a fait celle du CERT-FR. Un flux configuré sur une ancienne adresse peut cesser de fonctionner sans prévenir, même si le site continue de publier.

Q: Dans une note pour Medisecure, un apprenant écrit que la CNIL impose une règle précise de sécurité pour les dossiers patients. Sa seule référence est une fiche pratique de la CNIL. Que doit lui reprocher le correcteur ?
- La CNIL n'est pas compétente sur la sécurité des dossiers
- Une fiche pratique de la CNIL est une source secondaire
+ Une fiche pratique n'a pas la valeur juridique d'une délibération
- La fiche pratique aurait dû être recoupée par un blog spécialisé
E: Une autorité publie aussi des contenus de vulgarisation : une fiche pratique de la CNIL reste une source primaire, mais elle n'a pas la valeur juridique d'une délibération. Il faut toujours noter le type de document avant d'en tirer une obligation.

# FICHE 13 | Noter la fiabilité d'une source | 3

@qcm
Q: Un livre blanc sur les rançongiciels en santé, publié par un éditeur qui vend une solution de sécurité, obtient : autorité 1, origine 2, actualité 2, vérifiabilité 1, objectivité 0. Quelle cote, et quel usage ?
- B : utilisable, à confirmer avant toute décision
+ C : il sert à repérer, jamais cité seul
- D : il est écarté du dispositif
- A : il suffit seul, car l'éditeur a produit l'étude
E: Le total fait 6 sur 10, soit la cote C : la source sert à repérer un sujet, puis on cherche une source primaire indépendante. Elle n'atteint pas les 7 points de la cote B.

Q: La page de cycle de vie publiée par l'éditeur de MediDossier ne porte aucune date et n'a visiblement pas été modifiée depuis longtemps. Quel critère de la grille perd des points ?
- L'autorité
- L'origine
+ L'actualité
- L'objectivité
E: Le critère d'actualité demande si la source est datée et tenue à jour. L'éditeur reste compétent et producteur de l'information : l'autorité et l'origine ne sont pas en cause.

Q: Le flux des avis du CERT-FR obtient 10 sur 10, mais la plupart des avis portent sur des produits absents du parc de Medisecure. Que fait le veilleur ?
- Il baisse sa note pour tenir compte des avis hors sujet
+ Il garde la cote A et trie les avis au filtrage
- Il le cote C, car il faut recouper chaque avis publié
- Il le retire du dispositif, car il produit trop de bruit
E: La pertinence n'est pas dans la grille de fiabilité : une source peut être très fiable et souvent hors sujet. Le tri par axe et par inventaire se fait au filtrage.

Q: Après avoir noté ses sources, un apprenant abaisse le seuil de la cote B pour que son blog préféré y entre. Que lui reprochera le correcteur ?
- Les seuils du cours ne peuvent jamais être modifiés
- Un blog ne peut pas dépasser la cote C
+ Sa grille doit être fixée avant d'être appliquée
- La cote B est réservée aux sources primaires
E: Le correcteur attend une grille annoncée avant d'être appliquée, avec une note justifiée pour chaque source. Adapter la grille est permis, mais pas après coup pour obtenir un résultat voulu.

# FICHE 14 | Normes et référentiels : toujours avec la version | 3

@qcm
Q: Imaginons que Medisecure soit un jour certifiée ISO/IEC 27001. Le directeur général en conclut que la question NIS2 est réglée. Que lui répondre ?
- Il a raison, la certification vaut conformité à NIS2
- Il a raison si la certification porte sur l'édition 2022
+ La norme aide à prouver la conformité, sans remplacer la loi
- Il faudrait plutôt viser l'ISO/IEC 42001 pour NIS2
E: Une norme volontaire aide à démontrer qu'on respecte une obligation légale, mais elle ne la remplace pas. NIS2 est un texte obligatoire qu'il faut analyser en tant que tel.

Q: Le dossier D1 doit indiquer le référentiel d'accessibilité visé pour l'application MediSuivi. Quelle formulation convient ?
+ Respecter le RGAA 4.1.2
- Respecter le RGAA dans sa dernière version
- Respecter la norme française d'accessibilité
- Respecter le RGAA 5
E: Un référentiel se cite avec sa version, sinon on ne sait pas quels critères s'appliquent. Le RGAA 5 est seulement annoncé : la version de référence à la date du cours est la 4.1.2.

Q: Dans son dossier D1, un apprenant cite le RGESN de 2024 comme référence pour l'écoconception du portail patient de Medisecure. Supposons qu'une nouvelle version du RGESN soit publiée l'an prochain. Que faut-il faire ?
- Rien, la conformité à la version de 2024 reste acquise
+ Comparer les deux versions pour repérer les travaux nouveaux
- Mettre à jour l'année dans le dossier, sans autre analyse
- Attendre un an avant d'étudier la nouvelle version
E: Un référentiel se cite avec sa version, car une nouvelle version peut imposer des travaux de mise en conformité. Changer l'année sans analyser les écarts ne dit pas ce qu'il reste à faire.

Q: Pour héberger les données de MediSuivi, un prestataire non certifié HDS met en avant sa certification ISO/IEC 27001:2022. Le DSI de Medisecure peut-il le retenir ?
- Oui, l'ISO/IEC 27001 couvre déjà la sécurité de l'hébergement
- Oui, car une norme est en général volontaire
+ Non, la loi impose la certification HDS à cet hébergeur
- Non, une certification ISO n'a aucune valeur pour un hébergeur
E: Certains référentiels sont rendus obligatoires par un texte : la loi impose la certification HDS aux hébergeurs de données de santé. Une certification ISO/IEC 27001 garde sa valeur pour prouver la sécurité, mais elle ne remplace pas cette obligation.

# FICHE 15 | Le circuit de collecte et ses outils | 4

@qcm
Q: Kestrel surveille la page de la CNIL sur la géolocalisation avec un outil qui signale chaque modification. À quel étage du circuit de collecte cet outil appartient-il ?
- Aux sources
+ Aux capteurs
- Au point d'entrée unique
- Au stockage et au partage
E: La surveillance de pages détecte les nouveautés : c'est un capteur. La CNIL est la source, et l'agrégateur reste le point d'entrée unique.

Q: Une IA de recherche fournit à un apprenant une réponse sur NIS2, accompagnée de trois liens. Que doit-il citer dans sa fiche de veille ?
- La réponse de l'IA, puisqu'elle donne ses liens
- L'outil d'IA, présenté comme source secondaire
- Les trois liens, tels que l'IA les a fournis
+ Le document d'origine, après l'avoir ouvert et lu
E: Une IA de recherche n'est pas une source : elle peut citer un lien qui ne dit pas ce qu'elle affirme. On ouvre chaque lien, on vérifie, puis on cite le document d'origine.

Q: Pour Medisecure, deux agrégateurs gratuits sont comparés : un service en ligne géré par une société américaine et FreshRSS, installé sur un serveur de Medisecure. Les mots-clés suivis révèlent des projets confidentiels. Quel critère doit décider du choix ?
+ Le lieu d'hébergement
- Le coût de l'outil
- Le partage avec l'équipe
- La pérennité de l'outil
E: Les deux outils sont gratuits ; ce qui les distingue ici, c'est le lieu où sont stockés les mots-clés et les flux. Des mots-clés peuvent révéler un projet confidentiel.

Q: Le DSI de Medisecure reçoit ses newsletters dans sa messagerie de travail, au milieu du courrier, et ne les lit presque jamais. Quelle solution respecte le principe du circuit de collecte ?
- Les transférer chaque semaine dans OneNote sans les trier
+ Les faire entrer dans l'agrégateur, avec les autres flux
- Les remplacer par une recherche mensuelle dans un moteur
- Les lire chaque vendredi dans la messagerie, à heure fixe
E: Le principe est de tout rassembler dans un point d'entrée unique, puis de trier avant de lire. Stocker sans trier revient à déplacer le problème.

# FICHE 16 | Construire une bonne alerte | 4

@qcm
Q: Une alerte doit suivre les failles de Keycloak, désignées par les mots vulnérabilité ou faille, sans remonter d'offres d'emploi. Quelle requête convient ?
- Keycloak vulnérabilité faille emploi
- "Keycloak vulnérabilité faille emploi"
+ "Keycloak" vulnérabilité OR faille -emploi
- "Keycloak" -vulnérabilité OR -faille emploi
E: Les guillemets fixent le nom exact, OR ajoute le synonyme et le signe moins exclut le mot qui produit du bruit. Mettre toute la phrase entre guillemets ne trouverait presque rien.

Q: Un apprenant crée pour Medisecure une alerte sur les mots cybersécurité santé et reçoit 300 résultats par semaine. Quelle est son erreur de départ ?
+ Il est parti d'un thème au lieu d'une question
- Il a choisi de recevoir les résultats par flux RSS
- Il n'a pas attendu deux semaines avant de juger l'alerte
- Il a utilisé des mots en français plutôt qu'en anglais
E: La méthode commence par une question précise du plan de veille ; un thème large produit des centaines de résultats inutiles. La livraison en RSS est au contraire conseillée.

Q: Après deux semaines, une alerte a remonté 30 résultats, dont 13 inutiles. Que prévoit la méthode du cours ?
- La supprimer, car 13 résultats inutiles sont trop nombreux
- La reformuler, car il y a des résultats inutiles
- L'élargir avec des mots-clés plus généraux
+ La conserver, car moins de la moitié sont inutiles
E: On reformule ou on supprime une alerte seulement si plus de la moitié de ses résultats sont inutiles. Ici, 13 sur 30 reste sous la moitié.

Q: La requête "Node.js" "fin de support" ne trouve pas les pages en anglais, qui écrivent "end of life". Quelle modification les ajoute ?
- Ajouter -"end of life" à la requête
- Ajouter "end of life" à la suite, sans autre signe
- Retirer les guillemets autour de Node.js
+ Ajouter OR "end of life" après "fin de support"
E: OR ajoute un synonyme : la page peut contenir l'une ou l'autre expression. Sans OR, les deux expressions sont exigées ensemble, et le signe moins exclurait les pages en anglais.

# FICHE 17 | Vulnérabilités et fins de support | 4

@qcm
Q: Le RSSI de Medisecure reçoit deux alertes sur des composants du parc : une faille notée 9,6 sur un serveur interne non exposé, et une faille notée 7,5, inscrite au catalogue KEV, sur Keycloak 15 exposé à Internet. Laquelle traiter en premier ?
- La faille à 9,6, car son score est le plus élevé
+ La faille à 7,5 sur Keycloak 15
- Les deux en même temps, car elles touchent le parc
- Aucune avant de connaître leur score EPSS
E: Un score CVSS élevé dit « grave dans l'absolu », pas « dangereux pour nous ». Une faille inscrite au catalogue KEV est déjà exploitée par des attaquants, et elle touche ici un composant exposé à Internet : c'est elle qui presse.

Q: Une faille touche PostgreSQL 13. Elle n'est pas encore exploitée, et le RSSI veut savoir si elle risque de l'être dans le mois. Quel indicateur consulter ?
- Le score CVSS
- Le catalogue KEV
+ Le score EPSS
- L'identifiant CVE
E: L'EPSS estime la probabilité qu'une faille soit exploitée dans les 30 prochains jours. Le CVSS mesure la gravité technique et le KEV recense les failles déjà exploitées.

Q: Pour une note au comité de direction, endoflife.date et un article de presse donnent deux dates différentes de fin de support pour Django 2.2. Quelle date retenir ?
- Celle d'endoflife.date, site spécialisé dans ces dates
+ Celle publiée par le projet Django lui-même
- La plus proche des deux, par prudence
- Celle de la publication la plus récente
E: Le projet qui maintient le logiciel est la source primaire de sa fin de support ; endoflife.date et la presse ne font que la reprendre. Choisir la date la plus proche ne dit pas laquelle est juste.

Q: Le suivi des vulnérabilités de Medisecure est abonné à Django et à Angular, mais pas à SQL Server 2014. Une faille critique touche SQL Server 2014. Que se passe-t-il ?
- L'outil alerte quand même, car la faille est critique
- L'outil ajoute seul le produit à la liste suivie
+ Aucune alerte n'arrive, car le produit n'est pas suivi
- L'alerte arrive grâce au score EPSS de la faille
E: Un outil de suivi ne surveille que les produits qu'on lui indique. D'où l'importance d'un inventaire complet des composants et de leurs versions.

# FICHE 18 | Filtrer et vérifier | 5

@qcm
Q: Le veilleur de Medisecure lit un article passionnant sur un nouveau processeur pour smartphones haut de gamme. Aucun axe du plan de veille ne porte sur ce sujet. Que fait-il ?
+ Il l'écarte dès le filtrage, sans le vérifier
- Il le vérifie d'abord pour s'assurer qu'il est exact
- Il le classe dans une catégorie « divers »
- Il le note avec la grille d'impact
E: Le filtrage vient en premier : une information qui ne sert aucun axe est écartée. Il est inutile de vérifier ou de noter une information hors sujet.

Q: Un chercheur découvre une faille le 2 mars. Le CERT-FR publie son avis le 9 mars. Le veilleur le lit le 11 mars. Quelle est la date de publication de l'information ?
- Le 2 mars
- Le 11 mars
+ Le 9 mars
- Le jour où le correctif sera installé
E: Le 2 mars est la date de l'événement, le 9 mars celle de la publication de l'avis. Le 11 mars est seulement la date de collecte par le veilleur.

Q: Un éditeur annonce que son logiciel réduit de 40 % les alertes inutiles de télésurveillance. Avant d'utiliser ce chiffre dans une recommandation pour Medisecure, que faut-il obtenir ?
- Un second communiqué du même éditeur
+ Une source indépendante de l'éditeur qui le confirme
- Deux articles de presse qui reprennent le communiqué
- Rien de plus, l'éditeur est la source primaire
E: Un éditeur qui vante son produit n'est pas neutre, et deux articles qui reprennent son communiqué ne font qu'une source. Une performance annoncée se recoupe avec une source indépendante.

Q: Le veilleur de Medisecure range ses fiches dans des dossiers « CERT-FR », « CNIL » et « ANS ». Six mois plus tard, il ne retrouve pas tout ce qui concerne la télésurveillance. Que faut-il changer ?
- Ajouter un dossier par mois de collecte
+ Ranger d'abord les fiches par axe du plan de veille
- Laisser chaque fiche porter des mots-clés libres
- Créer un dossier pour chaque nouvelle source suivie
E: Le premier niveau de la taxonomie reprend les axes du plan de veille : un même sujet, comme la télésurveillance, se retrouve au même endroit quelle que soit la source. Un rangement par source disperse le sujet.

# FICHE 19 | Signaux faibles, signaux forts | 5

@qcm
Q: Lors d'un webinaire, un intervenant d'une autorité de santé évoque, sans plus de détails ni de date, une possible obligation de tracer les accès aux données de télésurveillance. Comment traiter cette information ?
- Comme un signal fort : lancer le projet sans attendre
+ Comme un signal faible : ouvrir une fiche et surveiller
- Comme une information hors sujet : l'écarter
- Comme une information confirmée, car elle vient d'une autorité
E: L'indice est isolé, oral et sans échéance : c'est un signal faible, à documenter et à surveiller. Le statut de l'intervenant ne suffit pas à confirmer un texte qui n'existe pas encore.

Q: Un projet de texte européen sur les logiciels de dossier patient était suivi comme signal faible. Il vient d'être publié au Journal officiel, avec ses dates d'application. Que devient-il ?
- Un signal faible, car son sujet n'a pas changé
- Une information à archiver, car déjà connue
+ Un signal fort, qui demande de décider et planifier
- Un signal faible, tant que la presse n'en a pas parlé
E: Le texte est désormais confirmé et son échéance connue : il passe de signal faible à signal fort. Le sujet est le même, c'est le niveau de certitude qui a changé.

Q: En deux mois, le veilleur relève une start-up qui annonce un tri des alertes par IA, un appel à projets régional sur la télésurveillance et un billet d'un cardiologue sur la fatigue des alertes. Comment qualifier cet ensemble ?
- Un signal fort, car trois indices vont dans le même sens
+ Des signaux faibles, à relier et à surveiller ensemble
- Du bruit, car aucune de ces sources n'est institutionnelle
- Trois signaux faibles sans rapport, à traiter séparément
E: Aucun de ces indices n'est confirmé ni assorti d'une échéance : ce sont encore des signaux faibles. Comme ils vont dans le même sens, on les relie dans une fiche commune et on les relit pour voir s'ils se renforcent ; leur nombre ne remplace pas la confirmation.

Q: Une faille sur la console de télésurveillance n'est évoquée que par un message anonyme sur un forum. Un collègue affirme : « Vu l'enjeu, c'est un signal fort. » Qu'en penser ?
+ C'est un signal faible, car rien n'est encore confirmé
- C'est un signal fort, car il touche un actif critique
- Ce n'est pas un signal, car le message est anonyme
- C'est un signal faible, car le sujet est secondaire
E: La différence tient au niveau de certitude, pas à l'importance du sujet. Un sujet grave reste un signal faible tant que l'information n'est pas confirmée.

# FICHE 20 | La grille d'impact | 5

@qcm
Q: Une information est notée : impact 2, maturité 2, gains 2, risques 2, environnement 2, effort 1. Que prévoient les seuils du cours ?
- La diffuser vite et étudier une recommandation
+ La garder pour la prochaine revue de veille
- L'archiver sans la diffuser
- La sortir du périmètre de la veille
E: Le total fait 11 sur 18, entre 8 et 13 : l'information est gardée pour la prochaine revue. Il faudrait 14 ou plus pour la diffuser vite.

Q: Une innovation sur les batteries obtient 13 sur 18, mais 0 en impact pour Medisecure. Que fait le veilleur ?
- Il la garde pour la prochaine revue, vu son total de 13
- Il la diffuse, car son total est proche du seuil de 14
- Il double le poids de l'impact et recalcule le total
+ Il l'écarte, car elle ne touche pas Medisecure
E: Une note de 0 en impact signifie que l'information ne touche aucun actif, projet ou obligation : elle n'aurait pas dû passer le filtrage et sort du périmètre, quel que soit son total.

Q: Remplacer MediDossier v8 par un nouveau DPI demandera plus d'un an de travaux. Quelle note donner au critère « effort de mise en œuvre » ?
- 3, car le projet est très lourd
+ 0, car le critère est noté à l'envers
- 3, car le projet est indispensable
- 1, car ce critère se note de 1 à 3
E: Une note haute signifie un effort faible : un projet de plus de six mois reçoit 0. Ainsi, plus le total est haut, plus l'information mérite attention.

Q: Un apprenant a daté l'adoption de sa grille, noté dix informations, puis décidé de modifier son barème. Que doit-il faire ?
- Rien de plus, puisque la grille lui appartient
- Supprimer les dix notes attribuées avec l'ancien barème
- Revenir obligatoirement à la grille du cours
+ Dater la modification dans son journal
E: La grille peut évoluer, mais toute modification se date dans le journal de veille, comme son adoption. Le correcteur peut ainsi suivre les règles appliquées à chaque note.
