# FICHE 11 | Collecter et conduire les entretiens | 4

@qcm
Q: Le chef de projet applicatif de Kestrel prépare un entretien avec un planificateur. Que doit-il envoyer à l'avance pour obtenir le plus d'informations ?
- La liste complète des applications de Kestrel
+ L'objet de l'entretien et le schéma provisoire du processus
- Un questionnaire fermé à remplir avant la rencontre
- Le compte rendu qu'il compte rédiger ensuite
E: L'interlocuteur corrige plus volontiers un schéma qu'il ne décrit son travail à partir de rien ; le questionnaire fermé fait manquer les usages réels.

Q: Deux agents du service comptable d'une collectivité affirment que l'export vers la trésorerie est automatique. Comment rendre cette information plus solide ?
- Interroger un troisième agent du même service
- La tenir pour établie, deux sources concordent
- La remplacer par l'avis du directeur des SI
+ La confronter aux journaux de l'interface
E: Une information confirmée par deux sources de nature différente, ici une personne et un outil, vaut plus qu'une information répétée par deux personnes du même service.

Q: Le contrat d'hébergement d'une application annonce deux zones ; la console de l'hébergeur n'en montre qu'une. Que faire dans la cartographie ?
+ Poser l'écart en question et citer chaque source
- Retenir le contrat, document signé et daté
- Retenir la console et effacer la mention du contrat
- Indiquer une ou deux zones selon les vues
E: Un document décrit l'organisation voulue, l'outil l'état réel à une date ; l'écart se pose en question et ne se corrige pas en silence.

Q: Dans le dossier D2, un apprenant regrette de n'avoir pu interroger personne chez Medisecure. Où le D2 lui permet-il de valoriser ce manque ?
- Nulle part : le dossier doit paraître complet
- Dans l'annexe A, par une colonne « à vérifier »
+ Dans la partie 6, en disant ce qu'il faudrait vérifier
- Dans la synthèse d'une page, en avertissement
E: La conclusion demande précisément ce qui resterait à vérifier par des entretiens ou des outils de collecte, auxquels l'apprenant n'a pas accès.

# FICHE 12 | Inventaires, matrice des flux et matrice processus × applications | 4

@qcm
Q: Dans la matrice des flux de Kestrel, que faut-il écrire dans le champ « données » du flux FLX-06 du site web vers la messagerie ?
- Courriel du site web vers la messagerie
- Données commerciales, sensibilité moyenne
+ Demandes de devis : nom, société, besoin
- Flux commercial, au fil de l'eau
E: Le champ dit précisément ce qui transite, comme FLX-06 dans l'exemple de Kestrel ; « données commerciales » reste trop vague, « courriel » est le format et « au fil de l'eau » la fréquence.

Q: Une application d'une mutuelle est maintenue par son éditeur mais tourne sur une base de données dont le support a pris fin. Comment renseigner l'état du support ?
+ « Hors support », en nommant le composant concerné
- « Maintenu par l'éditeur », sans autre mention
- « Fin de support annoncée », sans préciser de date
- « Non documenté », faute de source sur la base
E: L'état du support porte sur l'application et sur ses composants : comme pour RoutePro sur SQL Server 2016, on retient « hors support » en nommant le composant, même si l'éditeur maintient l'application ; la fin de support a déjà eu lieu, elle n'est plus « annoncée ».

Q: Un service de Kestrel utilise un outil gratuit de partage de fichiers que la DSI n'a jamais validé. Que fait-on dans l'inventaire applicatif ?
- Ne pas l'inscrire, pour ne pas l'approuver
- L'inscrire avec la mention « interdit »
- Le signaler seulement sur la vue de l'écosystème
+ L'inscrire comme usage hors inventaire
E: On le décrit avec les mêmes attributs et on signale les inconnues ; inventorier un usage hors inventaire rend un risque visible, ce n'est pas l'approuver.

Q: La matrice CRUD d'un e-commerçant montre que la fiche client est créée à la fois dans le CRM et dans le logiciel de facturation. Qu'annonce ce constat ?
- Un flux manuel à ajouter à la matrice des flux
+ Des doublons et des incohérences entre les deux
- Un point unique de défaillance sur la fiche client
- Une application orpheline à retirer de l'inventaire
E: Une même information créée dans deux applications annonce doublons et incohérences : c'est un défaut de donnée de référence, à signaler dans les constats, et non une redondance, qui suppose deux applications assurant la même fonction.

# FICHE 13 | Points uniques de défaillance, zones de confiance, outils et maintien à jour | 4

@qcm
Q: Chez Kestrel, le NAS de sauvegarde est installé dans la même salle que les serveurs qu'il protège. Que montre ce constat ?
- Le NAS est sous-dimensionné pour les douze machines
- Les sauvegardes sont trop fréquentes pour le NAS
- Le NAS doit être virtualisé avec les serveurs
+ Un sinistre de la salle détruirait serveurs et copies
E: La salle est le point unique de défaillance ; le NAS n'en est pas un, car sa panne n'arrête rien, mais rangé dans la même pièce il constitue un défaut d'isolement des sauvegardes : un incendie ou un rançongiciel détruirait à la fois les serveurs et leurs copies.

Q: Une PME a un réseau plat : postes, serveurs et accès des prestataires sont dans le même réseau. Que doit montrer la vue de l'administration ?
- Une seule zone de confiance, puisqu'il n'y a qu'un réseau
+ Des populations de confiance inégale sur un même réseau
- Aucune zone : la notion ne s'applique pas ici
- Seulement la frontière avec Internet
E: Une zone de confiance n'est pas forcément un réseau séparé ; le réseau plat est précisément le constat à montrer.

Q: Un apprenant dessine ses vues dans draw.io et renomme « ERP » en « ERP finance » sur la vue applicative. Quel risque court-il pour l'élément E8 ?
- Que draw.io refuse le renommage d'une forme
- Que le correcteur ne puisse pas ouvrir le fichier
+ Que l'objet garde l'ancien nom dans les autres vues
- Aucun : draw.io propage le nom dans toutes les vues
E: draw.io, accepté pour le D2, n'a pas de modèle commun : chaque forme se renomme à la main, d'où l'intérêt d'une liste des objets, car E8 exige le même nom partout.

Q: Kestrel ouvre un nouvel accès VPN pour un prestataire de maintenance des quais. Que prévoit son processus de maintien à jour ?
+ Mettre à jour la cartographie sans attendre la revue
- Attendre la revue annuelle de la vue métier
- Rien : un prestataire n'est pas un objet cartographié
- Enregistrer une nouvelle version sur le serveur du siège
E: L'arrivée d'un prestataire avec un accès est un déclencheur ; et la cartographie ne se stocke pas sur le SI qu'elle décrit.

# FICHE 14 | Les critères de sécurité DICT | 5

@qcm
Q: Chez Kestrel, un litige oppose un client et un chauffeur sur l'heure d'une livraison. Quel critère de KDriver est principalement sollicité ?
- La disponibilité
- La confidentialité
+ La traçabilité
- Aucun : litige commercial
E: Il faut prouver qui a fait quoi et quand : photo, signature et horodatage de la preuve de livraison ; l'intégrité de la preuve est aussi en jeu, comme dans l'événement redouté ER6.

Q: La directrice commerciale de Kestrel déclare que les tarifs négociés avec la grande distribution ne doivent en aucun cas être vus par un concurrent. Qu'a-t-elle exprimé ?
+ Un besoin de confidentialité fort sur les tarifs
- Un besoin d'intégrité fort sur les tarifs
- Une mesure de chiffrement des tarifs à déployer
- Un besoin de traçabilité des consultations
E: « Qui ne doit en aucun cas les voir ? » est la question du critère de confidentialité ; le métier exprime un besoin, pas une mesure.

Q: Un éditeur de logiciel RH chiffre ses bases et considère que son besoin de confidentialité est « couvert ». Quelle erreur commet-il ?
- Il confond confidentialité et intégrité
- Il croit que le chiffrement protège la disponibilité
- Aucune : le chiffrement exprime le besoin
+ Il prend une mesure pour un besoin
E: Le besoin exprime le niveau de protection exigé, demandé au métier ; le chiffrement est une mesure qui y répond plus ou moins.

Q: Les noms, adresses et téléphones des destinataires de Kestrel ont un besoin de confidentialité élevé. Pourquoi ?
- Parce qu'ils sont stockés dans le cloud
+ Parce que leur fuite atteindrait les personnes
- Parce qu'ils sont indispensables à la livraison
- Parce qu'ils changent à chaque livraison
E: Le niveau du besoin se justifie par les conséquences d'une divulgation : atteinte aux personnes et notification à la CNIL.

# FICHE 15 | Menace, vulnérabilité, impact, risque et options de traitement | 5

@qcm
Q: En septembre 2025, Kestrel a déjoué de justesse une fraude au virement par usurpation d'un fournisseur. Quelle est la vulnérabilité ?
- L'escroc qui usurpe l'identité du fournisseur
+ Aucune procédure de contre-appel n'est écrite
- La perte financière évitée de justesse
- Le service comptable qui traite les virements
E: La menace est l'escroc ; la vulnérabilité est la faiblesse qu'il exploite, ici l'absence de contre-appel avant un changement de coordonnées bancaires (hypothèse H17 du registre de Kestrel).

Q: Supposons que Kestrel supprime l'accès VPN des chauffeurs, prévu pour déclarer des frais. Quelle option de traitement aurait-elle choisie ?
- Réduire
- Transférer
- Accepter
+ Éviter
E: On renonce à l'élément qui crée le risque ; l'option peut priver le métier d'un service utile.

Q: Chez Kestrel, après les mesures, un risque résiduel est estimé moyen. Qui peut l'accepter selon le seuil fixé par la direction ?
- Le responsable de l'infrastructure, seul
- Personne : un risque moyen doit être traité
+ Le comité de direction, avec un motif écrit
- Le prestataire qui a déployé la mesure
E: Chez Kestrel, un risque faible peut être accepté par le responsable de l'infrastructure, un risque moyen par le comité de direction avec un motif écrit ; un risque élevé ou critique doit être traité.

Q: Une société de transport juge qu'une panne disque « ne peut pas être évitée, puisqu'un disque finit toujours par lâcher ». Sur quoi peut-elle encore agir ?
+ Sur la vulnérabilité et sur l'impact
- Sur la menace, en changeant de marque de disques
- Sur rien : il ne reste qu'à accepter le risque
- Sur la vraisemblance seulement, par la supervision
E: On ne supprime pas la menace, mais on traite la vulnérabilité (stockage redondant) ou on réduit l'impact (procédure dégradée), comme le montre la décomposition de la panne de novembre 2024 chez Kestrel.

# FICHE 16 | Les normes ISO 27001, 27002, 27005 et le socle de sécurité | 5

@qcm
Q: Une PME de logistique veut répondre aux questions de sécurité des appels d'offres sans viser de certificat. Que lui conseiller ?
+ Adopter la démarche d'ISO/IEC 27001
- Se certifier ISO/IEC 27002, plus simple
- Se certifier ISO/IEC 27005, plus courte
- Attendre que NIS2 lui impose une norme
E: Adopter la démarche sans viser le certificat est une option fréquente et raisonnable ; seule ISO/IEC 27001 est certifiable des trois.

Q: Chez Kestrel, le guide d'hygiène de l'ANSSI demande une authentification forte pour les accès sensibles ; Microsoft 365 l'impose aux cadres seulement. Quel état d'application retenir ?
- Appliqué
+ Partiellement appliqué
- Non appliqué
- Sans objet
E: La mesure existe mais ne couvre pas tous les accès sensibles.

Q: Dans un dossier, un apprenant écrit : « NIS2 est en vigueur en France depuis le 17 octobre 2024 ». Que corriger ?
- Rien : c'est la date d'entrée en vigueur
- La date : la loi a été promulguée en 2025
- Le nom : il s'agit de la directive NIS1
+ Cette date était la limite de transposition
E: La transposition est en retard : la loi française n'était pas promulguée à la date du cours, et son état se vérifie sur Légifrance avant d'être écrit.

Q: Dans ISO/IEC 27005:2022, à quel moment fixe-t-on le critère d'acceptation des risques ?
- Après le traitement, au vu des risques résiduels
- Pendant l'évaluation, risque par risque
+ À l'établissement du contexte
- Lors de la surveillance et de la revue
E: Le critère d'acceptation se fixe d'abord, avant l'appréciation, comme la matrice et le seuil d'EBIOS Risk Manager avant toute cotation.

# FICHE 17 | Les principes d'EBIOS Risk Manager et l'atelier 1 | 6

@qcm
Q: Pour Kestrel, lequel de ces éléments est une valeur métier ?
- Le serveur de RoutePro et sa base SQL Server
- La passerelle VPN
- Le NAS de sauvegarde
+ Recevoir les ordres de transport
E: Une valeur métier est un processus ou une information essentiels ; les trois autres sont des biens supports.

Q: Dans la cartographie de Kestrel, la salle serveur du siège sert plusieurs valeurs métier. Que signifie ce constat pour l'atelier 1 ?
+ Qu'elle concentre le risque de plusieurs valeurs
- Qu'elle devient elle-même une valeur métier
- Qu'il faut la retirer des biens supports
- Qu'on la compte une fois, puis qu'on l'oublie
E: Un bien support qui sert plusieurs valeurs métier concentre le risque et constitue un signal d'alerte.

Q: Pour Medisecure, un apprenant nomme un bien support « le logiciel des centres » alors que sa cartographie l'appelle autrement. Quel est le risque ?
- Aucun : le sens reste compréhensible
+ Le lien entre le risque et le SI est rompu
- Seule la présentation est pénalisée
- La gravité doit être relevée d'un niveau
E: Chaque bien support doit être un objet de la cartographie et porter le même nom ; sinon le correcteur ne peut pas relier le risque au SI, et la condition de E10 échoue.

Q: Une entreprise industrielle hésite à utiliser EBIOS Risk Manager pour des pannes accidentelles de ses machines. Que dit le cours ?
- La méthode traite pannes et attaques de la même façon
- Les pannes s'étudient à l'atelier 2, comme sources de risque
+ Le socle les couvre ; les scénarios visent les attaques
- Les pannes ne relèvent d'aucune analyse de risques
E: EBIOS Risk Manager consacre ses scénarios (ateliers 2 à 4) aux attaques ; les pannes y sont couvertes par le socle de l'atelier 1 et relèvent surtout de l'analyse d'impact et de la continuité (chapitre 8).

# FICHE 18 | L'atelier 2 : sources de risque et objectifs visés | 6

@qcm
Q: Pour un club sportif, « un groupe de supporters » est inscrit seul dans le tableau de l'atelier 2. Que manque-t-il ?
- Les biens supports qu'il vise
- Le scénario opérationnel associé
+ L'objectif visé par ce groupe
- La gravité de l'événement redouté
E: On raisonne sur le couple source de risque et objectif visé, par exemple perturber les ventes pour protester ; les moyens viennent plus tard.

Q: Chez Kestrel, quel fait justifie le mieux de retenir le couple « escroc, détourner un paiement » ?
- La marge opérationnelle de 3,1 %
+ La tentative de septembre 2025
- L'accès VPN permanent de l'éditeur de RoutePro
- Le nombre de colis livrés chaque jour
E: La tentative de fraude par usurpation d'un fournisseur, déjouée de justesse, est un incident passé de l'organisation : c'est la meilleure justification qui soit.

Q: Avec le barème de Kestrel, un couple obtient motivation 3, ressources 2, activité 2. Quelle est sa pertinence, et est-il retenu ?
- Élevée, retenu
- Faible, écarté
- Moyenne, écarté
+ Moyenne, retenu
E: La somme vaut 7 : pertinence moyenne (6 à 7), et les couples de pertinence moyenne ou élevée sont retenus.

Q: Pour l'atelier 2 d'un groupe hospitalier, quelle source appuie le mieux l'activité d'un groupe qui vise les données de santé ?
+ L'observatoire des incidents du CERT Santé
- Le panorama de l'ENISA sur les transports
- Un forum de discussion anonyme
- L'avis personnel du RSSI de l'établissement
E: La veille sur la menace, citée avec sa source, justifie le critère d'activité par des incidents comparables et publics.

# FICHE 19 | L'atelier 3 : parties prenantes et scénarios stratégiques | 6

@qcm
Q: L'éditeur de RoutePro obtient (4 × 4) / (2 × 2) = 4. Kestrel ne peut pas s'en séparer. Que prévoit l'atelier 3 ?
- Le laisser en zone de danger et le signaler
+ Agir sur ses critères, puis le réévaluer
- Le retirer de l'étude, puisqu'il est indispensable
- Relever les seuils pour le sortir de la zone
E: L'accès à la demande fait baisser la pénétration (de 4 à 2) et l'avenant de sécurité fait monter la confiance (de 2 à 3) : (4 × 2) / (2 × 3) ≈ 1,3, l'éditeur passe en zone de contrôle.

Q: Chez Kestrel, les fournisseurs payés par virement (PP-20) n'ont aucun accès au SI, mais leur niveau de menace vaut (2 × 1) / (1 × 2) = 1. Pourquoi sont-ils en zone de contrôle ?
+ Leur faible maturité ouvre la voie à une usurpation
- Tout fournisseur est critique par principe
- Leur pénétration de 1 suffit à les rendre critiques
- Ils n'y sont pas : sans accès, ils sont hors périmètre
E: La maturité, cotée 1, est au dénominateur : un escroc peut usurper un fournisseur ou compromettre sa messagerie (SS3) ; le niveau 1 tombe dans la zone de contrôle, de 1 à 3.

Q: Dans quel cas la fiche méthode de l'ANSSI suggère-t-elle de retirer la confiance de la formule ?
- Quand la partie prenante est un service interne
- Quand la dépendance atteint 4
- Quand on ignore tout de sa maturité
+ Quand elle peut être utilisée à son insu
E: Une partie prenante loyale peut servir de relais à un attaquant sans le savoir : la confiance ne l'atténue plus.

Q: Un apprenant cote la vraisemblance de ses scénarios stratégiques dès l'atelier 3. Que lui dire ?
- C'est correct : gravité et vraisemblance vont ensemble
- C'est correct avec la méthode expresse
+ C'est prématuré : elle se cote à l'atelier 4
- C'est inutile : un scénario stratégique n'a pas de cote
E: Le scénario stratégique porte la gravité de l'événement redouté ; sa vraisemblance vient du scénario opérationnel.

# FICHE 20 | L'atelier 4 : scénarios opérationnels et vraisemblance | 6

@qcm
Q: Un scénario opérationnel compte douze actions en série, toutes cotées 3 ou 4, et son indice cumulé vaut 3. Que conseille la fiche méthode de l'ANSSI ?
- Le garder à 3 : la longueur ne compte pas
- Le relever à 4 : l'attaquant a plus d'occasions
- Le couper en deux scénarios stratégiques
+ Envisager de baisser l'indice d'un niveau
E: Une chaîne d'une dizaine d'étapes en série multiplie les occasions d'échec de l'attaquant ; la fiche conseille alors de baisser l'indice d'un niveau, ce que le SO1 de Kestrel, sept étapes, n'a pas eu à faire.

Q: Un chemin d'attaque compte quatre actions en série cotées 4, 2, 4 et 4. Quel est l'indice cumulé final ?
+ 2
- 3
- 4
- 3,5, la moyenne
E: La chaîne vaut son maillon le plus faible pour l'attaquant : le minimum le long du chemin est 2.

Q: Une étude cote V3 un scénario dont une étape suppose l'absence d'authentification multifacteur, non vérifiée. Que faut-il faire ?
- Retirer l'étape du graphe, faute de preuve écrite
+ Écrire l'hypothèse et planifier sa vérification
- Coter V4 par prudence, sans autre mention
- Passer à la méthode avancée pour cette étape
E: Une hypothèse fausse changerait la vraisemblance : on l'écrit et on inscrit sa vérification au plan d'action.

Q: Pour Medisecure, un apprenant écrit l'étape « rentrer : l'attaquant pénètre dans le SI ». Quel défaut présente cette étape ?
- Elle relève de la phase « trouver »
- Elle devrait figurer à l'atelier 3
+ Elle ne nomme ni action ni bien support
- Elle n'en présente aucun
E: Chaque action élémentaire nomme un bien support de la cartographie ; sinon le scénario est invérifiable et E13 échoue.

# FICHE 21 | L'atelier 5 : traitement du risque, mesures et risques résiduels | 6

@qcm
Q: Le plan de Kestrel confie la mesure M5, règle de correction en 48 heures, au responsable de l'infrastructure. Pourquoi nommer une fonction plutôt qu'écrire « la DSI » ?
- Parce qu'EBIOS Risk Manager interdit de nommer un service
+ Pour qu'une personne réponde de la mesure au suivi
- Pour pouvoir chiffrer la mesure dès le D2
- Parce que la DSI ne peut pas porter de mesure
E: Chaque mesure du plan a une fonction responsable ; « la DSI s'en chargera » ne désigne personne et rend le suivi impossible.

Q: Chez Kestrel, pourquoi la gravité de R1 baisse-t-elle de G4 à G3 dans le risque résiduel ?
- Grâce à l'authentification multifacteur (M3)
- Parce que l'éditeur passe en zone de contrôle
+ Grâce à la sauvegarde isolée et au mode dégradé
- Parce que le comité de direction l'a accepté
E: M4 et M11, mesures de résilience, ramènent l'arrêt prévisible sous trois jours ; la protection agit surtout sur la vraisemblance.

Q: Pour Medisecure, un apprenant propose la mesure « migrer tout le SI vers un hébergeur certifié HDS ». Qu'en dire au regard du D2 ?
+ C'est un projet, qui relève du D3
- C'est une mesure de résilience recevable
- C'est une mesure de gouvernance, si elle est chiffrée
- C'est un transfert du risque vers l'hébergeur
E: Le D2 demande des mesures de sécurité typées et attribuées ; architecture et chiffrage relèvent du D3.

Q: Un risque élevé reste au-dessus du seuil pendant une migration de neuf mois. Comment le comité de direction peut-il l'accepter ?
- Il ne peut pas : un risque élevé doit être évité
- En le déclarant faible jusqu'à la fin des travaux
- En le confiant à l'équipe technique, qui surveillera
+ Temporairement, avec motif, compensation et réexamen
E: C'est la décision prise pour R4 chez Kestrel : motif, mesure compensatoire, échéance et date de réexamen, dans une trace écrite qui distingue un risque accepté d'un risque ignoré.
