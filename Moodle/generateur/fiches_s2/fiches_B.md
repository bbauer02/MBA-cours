# FICHE 11 | Collecter et conduire les entretiens | 4

@essentiel
Aucune cartographie ne part de zéro. On commence par l'étude de l'existant : contrats, factures, inventaires techniques, anciens schémas, plans de continuité, rapports d'incident, outil de tickets. Chaque document a une date et un auteur ; un écart entre deux documents est une question à poser, pas une erreur à corriger en silence.

Les documents ignorent les usages réels. Le guide de l'ANSSI recommande donc des entretiens ciblés et préparés. Le cours conseille une grille tirée des trous de l'inventaire, des questions ouvertes sur le travail réel, puis un compte rendu court, envoyé dans les 48 heures et validé par l'interlocuteur.

Enfin, on recoupe : une information confirmée par deux sources de nature différente vaut plus qu'une information répétée par deux personnes du même service. Dans le D2, le dossier de présentation fourni tient lieu d'existant.

@tableau Les sources de la collecte et leurs angles morts
| Source | Ce qu'elle dit bien | Ce qu'elle dit mal |
| --- | --- | --- |
| Documents | L'organisation voulue, les engagements, les dates | L'état réel, les usages non prévus |
| Entretiens | Les usages réels, les contournements, les irritants | Les détails techniques, les chiffres exacts |
| Outils de gestion de parc | L'état technique exact à une date | Le sens métier, les flux manuels, les prestataires |
| Consoles des hébergeurs et des SaaS | Machines virtuelles, comptes d'administration, accès ouverts | Ce qui tourne sur site, l'usage métier |

@rappel Question ouverte
Question qui fait raconter le travail plutôt que répondre par oui ou non : « Racontez-moi une journée type », « Que faites-vous quand l'application ne répond pas ? ». La plus productive est souvent la dernière : « Qu'est-ce que je n'ai pas demandé et que je devrais savoir ? ».

@rappel CMDB
Base de données de gestion des configurations, issue des bonnes pratiques ITIL. Elle recense les éléments de configuration et leurs relations. C'est une excellente source pour l'inventaire, mais elle ignore en général les processus, les flux manuels et les zones de confiance.

@rappel Outil de gestion de parc
Logiciel qui inventorie postes et serveurs, avec leur système et leurs logiciels installés ; GLPI, logiciel libre répandu en France, en est un exemple. Peu d'outils de cartographie font eux-mêmes la collecte.

@attention Un compte rendu non validé n'est pas une source
Une conversation devient une source citable quand l'interlocuteur a relu et validé son compte rendu. Sans cette validation, on cite sa propre mémoire.

@document Document · compte rendu d'entretien fictif, Mutuelle Solènes (organisation fictive), service des prestations, mars 2026
Entretien du 3 mars avec Mme D., gestionnaire des remboursements depuis onze ans. Compte rendu rédigé le 15 mars par le chef de projet cartographie ; non relu par l'intéressée.

Questions posées : « Utilisez-vous l'application Prestaflux ? » (oui). « Prestaflux reçoit-il automatiquement les décomptes de l'Assurance maladie ? » (oui). « Avez-vous des difficultés particulières ? » (non).

En fin d'entretien, Mme D. a ajouté spontanément plusieurs éléments. Les dossiers refusés par Prestaflux, environ quarante par jour, sont copiés dans un classeur Excel partagé sur le drive de l'équipe, « Rejets 2026 », puis ressaisis à la main le lendemain. Le classeur contient les noms, numéros de sécurité sociale et montants des adhérents. Quand Prestaflux est arrêté, l'équipe se connecte avec le compte « presta_equipe », dont le mot de passe est noté dans le classeur. Enfin, depuis l'été dernier, les décomptes d'un des deux centres de traitement arrivent par courriel en PDF, « parce que le lien ne marche plus », et sont saisis par une collègue.

Le schéma applicatif de 2023, fourni par la DSI, montre un flux automatique unique entre l'Assurance maladie et Prestaflux. L'outil de tickets ne contient aucun ticket sur ce flux depuis un an. Le chef de projet propose de retenir le schéma, « document officiel validé par la DSI ».

@questions
1. Quels usages réels l'entretien révèle-t-il, que le schéma de 2023 ne montre pas ?
2. Relevez les défauts de préparation et de conduite de l'entretien, puis dites comment recouper l'information sur le flux des décomptes.
3. La proposition finale du chef de projet est-elle fondée ? Que feriez-vous à sa place ?
4. Dans votre entreprise d'alternance, quel processus vous semble le plus exposé à des usages réels absents des documents, et quelle question ouverte poseriez-vous pour les faire apparaître ?

@pistes
1. Un classeur Excel partagé qui sert de file d'attente des rejets, avec des données sensibles ; une ressaisie manuelle quotidienne ; un compte partagé dont le mot de passe est écrit dans le classeur ; un flux de décomptes devenu manuel (PDF par courriel puis saisie) pour l'un des centres. Ce sont un usage hors inventaire, deux flux manuels et un compte partagé.
2. Les questions sont fermées et ne font pas raconter le travail ; l'essentiel est venu spontanément, après la grille. Le compte rendu est rédigé douze jours après et n'est pas validé : il n'est pas encore une source citable. Pour recouper, on confronte une source de nature différente : journaux de l'interface, console du prestataire du lien, boîte de messagerie qui reçoit les PDF.
3. Non : un document est daté et décrit l'organisation voulue en 2023 ; l'absence de ticket ne prouve rien, puisque le contournement évite justement l'incident. L'écart entre le schéma et l'entretien est une question à poser. Il faut faire valider le compte rendu, recouper, puis cartographier les deux flux réels en signalant la source de chacun.
4. Une bonne réponse nomme un processus précis, explique pourquoi il favorise les contournements (pic d'activité, application rigide, prestataire) et formule une question ouverte sur le travail réel. Elle indique aussi avec quelle source de nature différente la réponse serait recoupée.

@qcm
Q: Quand faut-il envoyer le compte rendu d'un entretien de cartographie ?
+ Dans les 48 heures, pour validation par l'interlocuteur
- À la fin de l'étude, en même temps que les autres sources
- Après la cartographie, pour faire valider les vues dessinées
E: Un compte rendu court, envoyé vite et validé, transforme une conversation en source citable.

Q: Un scan réseau trouve un serveur que personne n'a cité en entretien. Que montre ce cas ?
- Que les entretiens deviennent inutiles
- Que le scan est forcément erroné
+ Que les sources de nature différente se complètent
E: Un outil de collecte voit l'état technique exact, qu'un entretien peut ignorer ; c'est le principe du recoupement.

Q: Pourquoi une CMDB bien tenue ne suffit-elle pas à faire une cartographie ?
- Elle ne recense jamais les serveurs ni leurs relations techniques
+ Elle ignore en général les processus métier et les flux manuels
- Le guide de l'ANSSI la déconseille comme source d'inventaire
E: La CMDB décrit les éléments de configuration et leurs relations techniques, pas le métier ni les contournements.

# FICHE 12 | Inventaires, matrice des flux et matrice processus × applications | 4

@essentiel
Les inventaires précèdent le dessin : dessiner avant d'inventorier produit de beaux schémas faux. L'inventaire applicatif, annexe A du D2, décrit chaque application par au moins dix attributs en plus de son nom, dont quatre de sécurité : besoins de sécurité, exposition à Internet, hébergement, état du support. Il inclut au moins un usage hors inventaire.

La matrice des flux, annexe B, décrit chaque échange par sept champs : source, cible, données, format, fréquence, mode et protection du canal. Un flux manuel est un flux à part entière. La matrice processus × applications, annexe C, vérifie qu'aucun processus n'est oublié et qu'aucune application n'est orpheline ; elle servira au chapitre 8. L'inventaire de l'infrastructure, annexe D, se tient par catégorie et note le lieu de chaque élément.

@tableau Les sept champs d'un flux
| Champ | Ce qu'on écrit | Exemple chez Kestrel |
| --- | --- | --- |
| Source et cible | Deux objets de l'inventaire, nom exact | APP-06 Portail EDI vers APP-01 RoutePro |
| Données | Ce qui transite, avec sa sensibilité | Ordres de transport de la grande distribution |
| Format et fréquence | Forme technique et rythme | Messages EDI (norme non documentée) ; fréquence non documentée |
| Mode | Automatique ou manuel | Automatique (hypothèse H7) |
| Protection du canal | Chiffrement, aucun, ou « non documentée » | Non documentée |

@rappel État du support
Il porte sur l'application et sur ses composants. RoutePro est maintenu par son éditeur, mais repose sur SQL Server 2016, hors support étendu depuis le 14 juillet 2026 : il faut le signaler.

@rappel Usage hors inventaire
Outil utilisé sans être connu ni validé par la DSI (« shadow IT ») : service gratuit en ligne, tableur devenu application, IA générative. L'inventorier ne revient pas à l'approuver : on rend un risque visible.

@rappel Matrice CRUD
Repère non exigé dans le D2. Elle indique si chaque application crée, lit, modifie ou supprime chaque information. Une information créée dans deux applications annonce doublons et incohérences.

@astuce
« Non documentée » est une réponse honnête et un constat. Si vous devez néanmoins poser une valeur absente des sources, notez-la comme hypothèse numérotée, à confirmer en entretien.

@document Document · courriel interne fictif, Communauté d'agglomération du Val de Brenne (collectivité fictive), avril 2026
De : chef de projet SI. À : directeur des systèmes d'information. Objet : premier jet de la matrice des flux.

Bonjour, voici les cinq premières lignes de la matrice. J'ai fait simple pour aller vite.

Flux 1 : logiciel de l'état civil vers la plateforme de l'Insee, données, automatique. Flux 2 : logiciel des marchés publics vers l'ERP financier, données, chaque mois, fichier. Flux 3 : la régie des piscines envoie ses recettes à la trésorerie par un tableau Excel que l'agent remplit le soir ; je ne l'ai pas mis, ce n'est pas une application. Flux 4 : portail famille et logiciel enfance, synchronisation dans les deux sens, données, chiffré je pense. Flux 5 : ERP financier vers le logiciel des marchés publics, retour des mandats payés, automatique, TLS.

Pour l'inventaire applicatif, j'ai noté le logiciel de l'état civil « maintenu » : l'éditeur publie encore des mises à jour. Notre prestataire m'a pourtant dit qu'il tourne sur un Windows Server 2012 R2 qui n'est plus mis à jour. Le service jeunesse utilise aussi un outil gratuit de formulaires en ligne pour les inscriptions aux séjours, avec les certificats médicaux joints ; je l'ai laissé de côté puisque la DSI ne l'a jamais validé.

Dans la matrice processus × applications, le logiciel de gestion des cimetières n'est rattaché à aucun processus : je propose de le supprimer de l'inventaire.

Bonne journée.

@questions
1. Pour chacun des cinq flux, dites quels champs manquent ou sont mal renseignés.
2. Le chef de projet a écarté trois éléments : le tableau Excel des piscines, l'outil de formulaires et le logiciel des cimetières. Discutez chacun de ces choix au regard du cours.
3. Comment noter l'état du support du logiciel de l'état civil, et pourquoi ?
4. Quel usage hors inventaire repérez-vous dans votre entreprise d'alternance, et quels attributs resteraient « inconnus » ?

@pistes
1. Le champ « données » est vague aux flux 1, 2 et 4 (« données ») : il faut écrire ce qui transite et sa sensibilité (actes d'état civil, pièces de marché, identités des familles). La fréquence manque aux flux 1, 4 et 5, le format aux flux 1, 4 et 5, la protection du canal aux flux 1, 2 et 3, le mode au flux 2 ; « fichier » ne suffit pas comme format (CSV, XML, norme ?) et « chiffré je pense » doit devenir « hypothèse » ou « non documentée ». Le flux 4 est noté dans les deux sens alors que les flux 2 et 5 sont séparés : la convention doit être constante.
2. Le tableau Excel des piscines est un flux manuel, donc un flux à part entière, et son outil est un objet à inventorier. L'outil de formulaires est un usage hors inventaire traitant des données de santé : il doit figurer à l'inventaire, sans que cela vaille approbation. Une application orpheline ne se supprime pas : la matrice révèle soit un processus oublié dans la vue métier, soit une application inutile, ce qu'il faut vérifier.
3. Il faut signaler un composant hors support : l'application est maintenue, mais son système ne l'est plus. Une application peut être maintenue par son éditeur et reposer sur un composant hors support. L'information vient d'un entretien : elle se note avec sa source et se recoupe dans la console ou l'outil de parc.
4. Une bonne réponse nomme un usage précis, explique pourquoi il est hors inventaire (gratuit, adopté par un service, inconnu de la DSI) et le décrit avec les attributs habituels en signalant ceux qui sont inconnus : hébergement, état du support, protection des flux.

@qcm
Q: Dans la matrice des flux, quel champ distingue une ressaisie au clavier d'un échange par interface ?
- La fréquence
- La protection du canal
+ Le mode de l'échange
E: Le mode distingue automatique et manuel ; la fréquence donne le rythme de l'échange et la protection du canal sa sécurité.

Q: Que signale une application rattachée à aucun processus dans la matrice processus × applications ?
+ Qu'elle est orpheline ou qu'un processus manque
- Qu'il faut la retirer de l'inventaire pour l'alléger
- Qu'elle est hors support, faute d'utilisateurs connus
E: La matrice vérifie que rien n'est oublié ; l'anomalie se vérifie avant de conclure.

Q: Dans la matrice des flux, que faut-il écrire quand la protection d'un canal n'apparaît dans aucune source ?
- « Chiffré », valeur par défaut des échanges récents
+ « Non documentée », ce qui est déjà un constat
- Rien : la case reste vide jusqu'à l'entretien
E: C'est une réponse honnête et utile à l'analyse de risques ; une valeur posée sans source devient une hypothèse numérotée.

# FICHE 13 | Points uniques de défaillance, zones de confiance, outils et maintien à jour | 4

@essentiel
Un point unique de défaillance est un élément dont la panne suffit à arrêter un service, faute de redondance ou de repli : salle, lien, serveur, fournisseur ou personne. On le repère en suivant chaque chaîne de dépendance : « s'il disparaît, qu'est-ce qui s'arrête, et existe-t-il un autre chemin ? ».

Une zone de confiance regroupe des ressources protégées de la même manière ; un franchissement est un passage autorisé vers une zone de niveau différent, donc un point de contrôle et un chemin d'attaque possible.

L'outil doit tenir l'inventaire et garder les mêmes noms d'une vue à l'autre : Archi le facilite par son modèle unique ; draw.io suffit, avec une liste des objets et un nommage strict. Enfin, la cartographie se maintient (responsable, rythme, déclencheurs) et se protège : jamais stockée sur le SI qu'elle décrit.

@tableau Quelle anomalie, sur quelle vue ?
| Anomalie | Vue où elle se lit |
| --- | --- |
| Point unique de défaillance | Infrastructures physiques |
| Flux manuel | Applicative, trait pointillé |
| Redondance ou trou fonctionnel | Fonctionnelle |
| Zone de confiance et franchissement | Infrastructures logiques et administration |
| Dépendance cachée ou concentration | Plusieurs vues croisées |

@rappel Constat de cartographie
Relation entre plusieurs faits que seule leur mise en image révèle. « Kestrel Track est hors support » est un fait ; « une panne de son unique zone coupe le suivi des clients et la remontée des preuves de livraison » est un constat.

@rappel Archi et draw.io
Archi, gratuit, tient un modèle unique : un objet renommé l'est dans toutes les vues. draw.io, gratuit et très simple, n'a pas de modèle commun : un même objet dessiné deux fois fait deux formes à renommer à la main.

@rappel Déclencheur de mise à jour
Événement qui impose de mettre à jour la cartographie sans attendre la revue : nouvelle application, prestataire avec accès, changement de réseau, incident majeur, fin de support.

@attention Une cartographie périmée est plus dangereuse que pas de cartographie
On lui fait confiance. Le guide de l'ANSSI demande aussi qu'elle reste accessible en cas de coupure du réseau, par exemple sur papier conservé de manière sécurisée.

@document Document · compte rendu de crise fictif, Groupe Ardelle (réseau fictif de neuf agences d'intérim en Occitanie), mars 2026
Objet : retour d'expérience sur la coupure du 12 mars.

À 9 h 10, un engin de chantier sectionne la fibre qui relie le siège de Montpellier à Internet. Le siège n'a qu'un seul lien, sans secours 4G. Les neuf agences se connectent au logiciel de paie et de gestion des missions, hébergé dans la salle serveur du siège, par des tunnels VPN qui passent tous par ce lien. Toutes les agences s'arrêtent : aucun contrat de mission ne peut être édité.

Pour organiser un mode dégradé, la cellule de crise cherche la cartographie du réseau. Elle est enregistrée sur le serveur de fichiers du siège, inaccessible depuis les agences, et sa dernière version date de 2023. Elle ne montre ni le nouveau pare-feu installé en 2025, ni le déménagement de l'agence de Nîmes.

Le seul administrateur qui connaît la configuration des tunnels est en congé à l'étranger. Il faut l'appeler pour découvrir qu'un prestataire de maintenance de la téléphonie dispose d'un accès d'administration permanent au pare-feu, depuis Internet, avec un compte partagé. Personne d'autre ne le savait.

Le lien est rétabli à 17 h 40. Le directeur général demande « une cartographie à jour d'ici la fin du mois », sans désigner de responsable ni dire ce qui déclenchera les mises à jour suivantes.

@questions
1. Relevez les points uniques de défaillance révélés par la coupure, y compris humains, et dites sur quelle vue chacun aurait dû apparaître.
2. Repérez le franchissement de zones de confiance découvert pendant la crise. Pourquoi est-il préoccupant, et sur quelle vue doit-il figurer ?
3. Expliquez pourquoi la cartographie n'a pas servi, au regard des règles de protection et de maintien à jour du guide de l'ANSSI. Que manque-t-il à la demande du directeur général ?
4. Dans votre entreprise d'alternance, quel élément unique arrêterait plusieurs sites à la fois, et où la cartographie serait-elle consultable si le réseau tombait ?

@pistes
1. Le lien Internet unique du siège, sans secours, par lequel passent tous les tunnels VPN ; la salle serveur du siège, qui héberge seule l'application dont dépendent les neuf agences ; l'administrateur qui détient seul la configuration des tunnels. Les deux premiers se lisent sur la vue des infrastructures physiques, le troisième se note en commentaire ou sur la vue de l'administration.
2. L'accès d'administration permanent du prestataire de téléphonie au pare-feu, depuis Internet, avec un compte partagé : il relie la zone Internet ou prestataires à l'équipement qui protège le réseau interne. C'est un chemin d'attaque direct, inconnu et non traçable. Il doit figurer sur la vue de l'administration, avec les zones et les comptes à privilèges.
3. Elle était stockée sur le SI qu'elle décrit, donc inaccessible en pleine crise, sans copie papier ; elle était périmée, faute de déclencheurs (nouveau pare-feu, déménagement d'agence, accès de prestataire). La demande du directeur général fixe un délai mais ni responsable nommé, ni rythme de revue, ni déclencheurs, ni lieu de stockage.
4. Une bonne réponse nomme un élément précis et sourcé dont la panne arrêterait plusieurs sites, explique la chaîne de dépendance, et propose un lieu de conservation de la cartographie conforme au guide de l'ANSSI : hors du SI décrit, sauvegardé, accessible hors ligne, réservé aux personnes qui ont besoin d'en connaître.

@qcm
Q: Lequel de ces éléments est un point unique de défaillance humain ?
- Un administrateur parmi trois qui connaissent le réseau
+ Le seul agent qui connaît la configuration du réseau
- Un prestataire qui détient un contrat de maintenance
E: Une personne qui détient seule une compétence ou un accès est un point unique de défaillance.

Q: Un prestataire accède en VPN permanent aux serveurs internes. Sur la vue de l'administration, c'est :
- Une redondance fonctionnelle
- Un flux manuel entre le prestataire et la DSI
+ Un franchissement entre deux zones de confiance
E: Le passage de la zone des prestataires au réseau interne est un franchissement, donc un chemin d'attaque possible.

Q: Où le guide de l'ANSSI recommande-t-il de ne pas stocker la cartographie ?
+ Sur le système d'information qu'elle représente
- Sur un support chiffré, conservé hors du siège
- Dans une armoire fermée, en version papier datée
E: Un intrus y trouverait toute l'architecture, et elle serait inaccessible en cas de coupure.

# FICHE 14 | Les critères de sécurité DICT | 5

@essentiel
La sécurité ne protège pas des machines : elle protège des propriétés de l'information et des processus. La disponibilité est la propriété d'être accessible et utilisable au moment voulu par une personne autorisée. L'intégrité est celle d'être exact et complet, non modifié de façon illégitime. La confidentialité est celle de n'être accessible qu'aux personnes autorisées. La traçabilité, ou preuve, est la capacité à retrouver qui a fait quoi et quand.

Les trois premiers critères viennent d'ISO/IEC 27000 ; le quatrième est un ajout courant des méthodes françaises. Un même élément n'a pas les mêmes besoins sur chaque critère. La disponibilité s'exprime en durée (DMIA, PDMA), les autres sur une échelle de trois ou quatre niveaux. Ces besoins, notés dans l'inventaire applicatif, deviennent la matière première de l'analyse de risques.

@tableau Une question par critère
| Critère | Question au métier | Mesure typique |
| --- | --- | --- |
| Disponibilité | Combien de temps pouvez-vous vous en passer ? | Redondance, sauvegarde restaurable |
| Intégrité | Et si les données étaient fausses sans que vous le sachiez ? | Contrôle de cohérence, droits limités en écriture |
| Confidentialité | Qui ne doit en aucun cas les voir ? | Contrôle d'accès, chiffrement |
| Traçabilité | Faudra-t-il prouver qui a fait quoi ? | Journalisation, horodatage |

@rappel Besoin de sécurité
Niveau de protection qu'exige un élément donné sur chaque critère. Chez Kestrel, RoutePro a un besoin de disponibilité très fort (2 heures d'arrêt toléré) mais un besoin de confidentialité moyen.

@rappel DICT ou DICP
Deux sigles pour la même grille : le T de traçabilité et le P de preuve désignent le même quatrième critère.

@rappel DMIA et PDMA
Durée maximale d'interruption admissible et perte de données maximale admissible. Elles expriment le besoin de disponibilité en durée ; le chapitre 8 les approfondit.

@attention Le besoin n'est pas la mesure
« Chiffré » ou « sauvegardé » décrit une mesure, pas un besoin. Le besoin se demande au métier, avant de savoir ce qui existe.

@document Document · article de presse fictif, « La Lettre du e-commerce », février 2026 ; l'entreprise Maison Calade est fictive
Mauvaise semaine pour Maison Calade, vendeur en ligne de linge de maison installé près d'Avignon. Tout commence un lundi matin : pendant quarante minutes, le site affiche tous les draps à 1 euro. Plus de 600 commandes sont passées avant que l'équipe ne s'en aperçoive. « Quelqu'un a modifié la base des prix pendant la nuit », explique le gérant.

Le mardi, l'enquête piétine. Les six personnes qui administrent la boutique utilisent le même compte, et l'hébergeur ne conserve les journaux de connexion que vingt-quatre heures. Impossible de savoir qui a fait la modification, ni depuis où. Faute de preuve, l'entreprise hésite à annuler les commandes.

Le mercredi, un client signale qu'un fichier contenant les noms, adresses et numéros de téléphone d'environ 18 000 clients circule sur un forum. Il proviendrait d'un export réalisé par un ancien stagiaire et stocké sur un espace de partage public.

Par prudence, le gérant ferme le site de jeudi à samedi pour faire auditer la plateforme. Trois jours sans vente, en pleine période de soldes : le manque à gagner est estimé à 45 000 euros. « On avait tout misé sur la disponibilité : deux serveurs, une sauvegarde chaque nuit. On n'avait jamais pensé au reste », reconnaît-il.

@questions
1. Classez chacun des quatre événements de la semaine selon le critère de sécurité atteint.
2. Pourquoi l'absence de traçabilité aggrave-t-elle l'atteinte à l'intégrité ? Quelle décision métier en dépend ?
3. Le gérant dit avoir « tout misé sur la disponibilité ». Formulez les besoins de sécurité de la base des prix et du fichier clients sur les quatre critères, en justifiant chaque niveau par une question au métier.
4. Pour une application de votre entreprise d'alternance, quel critère vous paraît sous-estimé par rapport à la disponibilité, et sur quel fait vous appuyez-vous ?

@pistes
1. Les prix modifiés relèvent de l'intégrité ; l'impossibilité de savoir qui les a modifiés, de la traçabilité ; le fichier diffusé, de la confidentialité ; la fermeture de trois jours, de la disponibilité, bien qu'elle soit décidée par le gérant et non subie.
2. Sans journaux ni compte nominatif, on ne peut ni prouver une malveillance ni situer l'erreur, donc ni corriger avec certitude ni porter plainte. La décision d'annuler ou d'honorer les 600 commandes dépend de cette preuve.
3. La base des prix a un besoin d'intégrité fort (une erreur coûte immédiatement), de traçabilité fort, de confidentialité faible ; le fichier clients a un besoin de confidentialité élevé (données personnelles, RGPD) et d'intégrité moyen. La disponibilité se donne en durée tolérée. Chaque niveau se justifie par la question du tableau, posée au métier.
4. Une bonne réponse nomme un élément précis, cite le fait qui révèle le critère négligé (compte partagé, absence de journaux, export non maîtrisé) et propose un niveau sur l'échelle retenue, sans décider seule de la mesure.

@qcm
Q: Une commande EDI est modifiée en transit et envoie des palettes à la mauvaise adresse. Quel critère est atteint ?
- La confidentialité, car elle a circulé
- La disponibilité, car les palettes arrivent en retard
+ L'intégrité, car la commande a été altérée
E: L'information n'est plus exacte : elle a été modifiée de façon illégitime.

Q: Comment s'exprime habituellement le besoin de disponibilité ?
+ En durée d'arrêt tolérée et de perte de données
- En nombre de personnes autorisées à accéder à l'application
- En niveau de chiffrement exigé sur les données
E: La disponibilité se mesure en temps : ce sont la DMIA et la PDMA du chapitre 8.

Q: D'où viennent les trois premiers critères du sigle DICT ?
- Du RGPD, article 32
+ De la norme ISO/IEC 27000
- Du guide d'hygiène de l'ANSSI
E: La traçabilité est un ajout courant des méthodes françaises.

# FICHE 15 | Menace, vulnérabilité, impact, risque et options de traitement | 5

@essentiel
Une analyse de risques décompose ce que le langage courant mélange. La menace est la cause potentielle d'un incident : attaquant, panne, erreur, incendie. La vulnérabilité est une faiblesse qu'elle peut exploiter. L'impact est l'effet sur l'organisation ; la gravité le mesure sur une échelle. La vraisemblance n'est pas une prédiction : elle exprime la facilité de réussite d'un attaquant qui le décide.

Le risque est la possibilité qu'une menace exploite des vulnérabilités d'un actif et cause un impact. On le décrit en scénario et on l'estime en croisant gravité et vraisemblance. Le risque initial correspond à la situation constatée ; le risque résiduel subsiste après les mesures, et n'est jamais nul. Quatre options : réduire, transférer, éviter, accepter. Accepter est une décision écrite, motivée, signée par un responsable.

@tableau Les quatre options de traitement
| Option | Principe | Limite |
| --- | --- | --- |
| Réduire | Agir sur la vraisemblance ou la gravité | Coûte ; ne supprime jamais tout |
| Transférer | Faire porter une partie des conséquences par un tiers | Seulement l'impact financier |
| Éviter | Renoncer à l'activité ou à l'élément | Peut priver le métier d'un service |
| Accepter | Ne rien faire de plus, en connaissance de cause | Doit être écrit, motivé et signé |

@rappel Valeur métier et bien support
La valeur métier est le processus ou l'information essentiels ; le bien support est l'élément du SI sur lequel elle repose. C'est le pont entre la cartographie et l'analyse de risques.

@rappel Risque initial
Dans ce cours et dans EBIOS Risk Manager, risque estimé avec les mesures existantes et leurs défauts. Le risque inhérent, lui, est estimé sans aucune mesure.

@rappel Vocabulaire d'ISO/IEC 27005
La norme parle de modifier, partager, éviter ou maintenir le risque ; le D2 retient réduire, transférer, éviter et accepter.

@attention Accepter n'est pas oublier
Un risque que personne n'a traité est un risque ignoré, pas un risque accepté.

@document Document · cas réel résumé pour le cours d'après la presse spécialisée (SecurityWeek, Dark Reading, Insurance Journal, 2018 à 2022)
Le 27 juin 2017, le logiciel malveillant NotPetya se propage à partir de la mise à jour piégée d'un logiciel de comptabilité ukrainien, M.E.Doc. Il se présente comme un rançongiciel, mais il détruit les données sans possibilité réelle de les restaurer. Il se répand ensuite d'un réseau à l'autre chez des entreprises du monde entier qui ont une activité en Ukraine.

Le groupe agroalimentaire Mondelez International en fait partie. Selon sa plainte, environ 1 700 serveurs et 24 000 ordinateurs portables sont rendus inutilisables, ce qui perturbe la production et les livraisons. Le groupe estime son préjudice à plus de 100 millions de dollars et le déclare à son assureur, Zurich American, au titre d'une police multirisque qui couvre les dommages aux données et aux logiciels.

En février 2018, les gouvernements américain et britannique attribuent NotPetya à l'armée russe. Zurich refuse alors de payer en invoquant l'exclusion de guerre du contrat, qui écarte les actes hostiles d'un gouvernement. Mondelez l'assigne en octobre 2018 devant un tribunal de l'Illinois. L'affaire dure quatre ans et se termine fin 2022 par un accord transactionnel au montant non divulgué. Dans une affaire voisine, le laboratoire Merck a obtenu d'un tribunal du New Jersey, en 2022, que l'exclusion de guerre ne s'applique pas à son propre sinistre NotPetya.

@questions
1. Décomposez l'incident subi par Mondelez en menace, vulnérabilité, bien support et impact. Quelles informations manquent au texte ?
2. Quelle option de traitement Mondelez avait-elle choisie face à ce risque, et que montre cette affaire sur ses limites ?
3. NotPetya ne visait pas spécialement Mondelez. Comment cela influe-t-il sur la vraisemblance, telle que la définit EBIOS Risk Manager ?
4. Une direction vous dit : « nous sommes assurés, le risque cyber est traité ». Que lui répondez-vous, pour votre entreprise d'alternance ?

@pistes
1. La menace est un logiciel destructeur attribué à un État, introduit par la mise à jour d'un tiers ; les biens supports sont les serveurs et les postes ; l'impact est l'arrêt partiel de la production et des livraisons, plus de 100 millions de dollars selon Mondelez. Le texte ne dit pas quelle vulnérabilité a permis la propagation interne (réseau non cloisonné, comptes d'administration, correctifs) : c'est l'information manquante.
2. Un transfert, par l'assurance. L'affaire montre qu'un transfert ne couvre que l'impact financier, après coup et selon les clauses du contrat : il n'a pas évité l'arrêt, et il a donné lieu à quatre ans de procès. Un transfert doit donc compléter une réduction, pas la remplacer.
3. La vraisemblance n'est pas une prédiction de l'attaque : elle mesure la facilité de réussite si l'attaquant passe à l'acte, compte tenu de ses ressources et des vulnérabilités de l'organisation. Une attaque qui se propage seule exploite des faiblesses courantes : la vraisemblance dépend des vulnérabilités de l'organisation et de sa place dans l'écosystème (ici, une activité en Ukraine et un logiciel tiers), non du fait d'être visée.
4. Une bonne réponse explique que l'assurance transfère une partie de l'impact financier seulement, sous conditions et exclusions ; qu'elle ne rend ni l'activité ni les données ; qu'elle ne dispense pas de réduire le risque ; et que le risque résiduel doit toujours être accepté par écrit.

@qcm
Q: Un serveur unique, sans redondance, héberge une application critique. C'est :
+ Une vulnérabilité
- Une menace
- Un impact
E: C'est une faiblesse qu'une menace, comme une panne, peut exploiter.

Q: Que transfère une assurance cyber ?
- La totalité du risque
+ Une partie de l'impact financier
- L'arrêt de l'activité
E: Elle ne transfère jamais l'arrêt des opérations ni l'atteinte à l'image.

Q: Qui doit accepter un risque résiduel ?
- Celui qui a proposé la mesure, quel que soit le niveau du risque
- Personne : un risque résiduel est négligeable par définition
+ Un responsable qui en a l'autorité selon le seuil fixé
E: L'acceptation est une décision écrite et motivée, prise par un responsable qui en a l'autorité selon le seuil fixé par la direction ; le plus souvent, c'est la direction.

# FICHE 16 | Les normes ISO 27001, 27002, 27005 et le socle de sécurité | 5

@essentiel
ISO/IEC 27001:2022, publiée en octobre 2022, fixe les exigences d'un système de management de la sécurité de l'information (SMSI) ; c'est la norme certifiable de référence de la famille, rejointe en 2025 par ISO/IEC 27701. Son annexe A liste 93 mesures, que détaille ISO/IEC 27002:2022, catalogue non certifiable. ISO/IEC 27005:2022 donne la démarche de gestion des risques : contexte, appréciation (identification, analyse, évaluation), traitement, acceptation, avec communication et surveillance tout au long. EBIOS Risk Manager 1.5 s'y déclare conforme.

Le socle de sécurité regroupe les référentiels qui s'appliquent déjà : lois, normes, contrats, politique interne, guides. Pour chacun, on cite l'exigence, on décrit un constat vérifiable et on qualifie l'écart : appliqué, partiellement appliqué, non appliqué. Un écart sans fait n'est qu'une opinion.

@tableau Les normes de la famille ISO/IEC 27000
| Norme | Rôle | Certifiable |
| --- | --- | --- |
| ISO/IEC 27000 | Vocabulaire | Non |
| ISO/IEC 27001:2022 | Exigences du SMSI, annexe A de 93 mesures | Oui |
| ISO/IEC 27002:2022 | Catalogue détaillé des 93 mesures, en quatre thèmes | Non |
| ISO/IEC 27005:2022 | Démarche de gestion des risques | Non |

@rappel Guide d'hygiène informatique de l'ANSSI
« Renforcer la sécurité de son système d'information en 42 mesures », version 2 de 2017. C'est le minimum attendu de toute organisation.

@rappel NIS2
Directive (UE) 2022/2555, qui devait être transposée avant le 17 octobre 2024. À la date de rédaction du cours, la loi française n'est pas promulguée : vérifiez son état sur Légifrance avant de l'écrire.

@rappel HDS
Certification exigée de tout hébergeur de données de santé pour le compte d'un tiers. Référentiel en version 2, fixé par l'arrêté du 26 avril 2024 ; il s'appuie sur ISO/IEC 27001.

@attention Une méthode, un vocabulaire
Ne mélangez pas les termes d'ISO/IEC 27005, d'EBIOS Risk Manager et d'EBIOS 2010 dans un même dossier.

@document Document · compte rendu fictif du comité de direction de Talentis (éditeur fictif d'un logiciel de paie en SaaS, 80 salariés), janvier 2026
Présents : directeur général, directrice commerciale, directeur technique, responsable de la sécurité.

La directrice commerciale signale qu'un grand groupe de distribution exige, dans son appel d'offres, « une organisation conforme aux bonnes pratiques ISO/IEC 27001 ou équivalent ». Le directeur général demande que Talentis obtienne « la certification ISO 27002, plus simple », d'ici six mois.

Le directeur technique indique que l'entreprise est « déjà conforme à l'ANSSI » : les serveurs sont mis à jour chaque mois et sauvegardés chez l'hébergeur. Le responsable de la sécurité rappelle que la politique de sécurité date de 2016 et n'a jamais été révisée, que l'authentification multifacteur n'est activée que pour les développeurs et que les journaux d'administration ne sont pas conservés.

Sur la réglementation, le directeur technique affirme que « NIS2 s'applique en France depuis octobre 2024 » et que Talentis n'a donc « plus rien à faire ». La directrice commerciale ajoute que, les fiches de paie contenant des arrêts maladie, la certification HDS serait peut-être un argument.

Décision : le directeur général demande au responsable de la sécurité de lister « les mesures de la norme qu'on n'a pas », sans analyse de risques préalable, « pour gagner du temps ». Prochain point en mars.

@questions
1. Relevez les erreurs factuelles commises sur les normes et la réglementation, et corrigez-les.
2. Le directeur technique se dit « conforme à l'ANSSI ». Construisez un tableau de trois écarts au socle avec l'exigence, le constat et l'état d'application.
3. Que pensez-vous de la décision finale au regard d'ISO/IEC 27001 et 27005 ?
4. Dans votre entreprise d'alternance, quels référentiels composent le socle, et lequel demande une vérification de statut avant d'être cité ?

@pistes
1. ISO/IEC 27002 n'est pas certifiable : des normes citées, seule ISO/IEC 27001 l'est. NIS2 n'est pas transposée en France à la date du cours : la loi n'est pas promulguée, et une directive ne crée pas d'obligation directe pour l'entreprise ; en tout état de cause, être concerné crée des obligations, pas une dispense. La question HDS doit être examinée et non affirmée : elle dépend de l'hébergement de données de santé pour le compte d'un tiers.
2. Exemples attendus : authentification forte pour les accès sensibles, activée pour les développeurs seulement, partiellement appliqué ; journalisation des actions d'administration, absente, non appliqué ; PSSI à jour, document de 2016 jamais révisé, partiellement appliqué. Une sauvegarde « chez l'hébergeur » doit aussi être interrogée : copie isolée ou non ?
3. Elle inverse la logique : dans un SMSI, l'appréciation et le traitement des risques précèdent le choix des mesures, justifié dans une déclaration d'applicabilité. Cocher les 93 mesures sans analyse produit une liste, pas une sécurité adaptée aux risques. On peut adopter la démarche sans viser le certificat.
4. Une bonne réponse liste les référentiels avec leur nature (loi, norme, contrat, guide, politique interne), dit s'ils s'appliquent et pourquoi, et signale NIS2, et le cas échéant le Référentiel Cyber France de l'ANSSI, comme des points dont le statut doit être vérifié au moment du dépôt.

@qcm
Q: Combien de mesures de sécurité compte l'annexe A d'ISO/IEC 27001:2022 ?
- 42
- 114
+ 93
E: ISO/IEC 27002:2022 les détaille en quatre thèmes : organisationnelles, liées aux personnes, physiques et technologiques.

Q: Dans ISO/IEC 27005:2022, l'appréciation du risque regroupe :
+ L'identification, l'analyse et l'évaluation
- Le contexte et le traitement
- La communication et la surveillance
E: Le contexte la précède, le traitement et l'acceptation la suivent ; communication et surveillance accompagnent tout le processus.

Q: Comment qualifier un écart au socle pour qu'il soit recevable ?
- Par l'avis motivé de l'auditeur qui a mené les entretiens
+ Par l'exigence, un constat sourcé et un état d'application
- Par une note de 1 à 10 attribuée à chaque référentiel
E: Un écart sans fait n'est qu'une opinion.

# FICHE 17 | Les principes d'EBIOS Risk Manager et l'atelier 1 | 6

@essentiel
EBIOS Risk Manager est la méthode d'analyse de risques de l'ANSSI, publiée en 2018 ; la version en vigueur est la 1.5, de 2024. Elle combine une approche par conformité, qui vérifie le socle, et une approche par scénarios, pour les attaquants qui le contournent. Elle se déroule en cinq ateliers, avec un cycle stratégique de quelques années et un cycle opérationnel plus court.

L'atelier 1 dit ce que l'on protège. On choisit cinq à dix valeurs métier, on les relie à leurs biens supports, objets de la cartographie sous le même nom. On formule des événements redoutés du point de vue du métier, avec leurs impacts et une gravité lue sur l'échelle. On évalue enfin le socle et ses écarts, qui nourriront les ateliers 4 et 5.

@tableau Les cinq ateliers
| Atelier | Question | Section du D2 |
| --- | --- | --- |
| 1. Cadrage et socle | Que protège-t-on, quelles règles s'appliquent ? | 3.2 |
| 2. Sources de risque | Qui pourrait attaquer, pour quoi ? | 3.3 |
| 3. Scénarios stratégiques | Par quels chemins, y compris l'écosystème ? | 3.4 |
| 4. Scénarios opérationnels | Comment, et avec quelle facilité ? | 3.5 |
| 5. Traitement du risque | Que décide-t-on ? | 3.6 |

@rappel Valeur métier
Processus ou information essentiels à la mission : « livrer les colis », « les données des destinataires ». Elle relève de la responsabilité des métiers.

@rappel Bien support
Élément du SI sur lequel repose une valeur métier : application, serveur, réseau, local, personne, prestataire. Un bien support qui sert plusieurs valeurs métier concentre le risque.

@rappel Événement redouté
Atteinte à un critère de sécurité d'une valeur métier, formulée comme une conséquence : « les tournées ne peuvent pas être affectées pendant plus d'une journée ». Il ne décrit ni l'attaquant ni le moyen.

@attention Gravité par intuition
Chez Kestrel, le directeur des opérations voulait G4 pour deux jours sans affectation des tournées (ER1) ; la relecture de l'échelle a donné G3. Citez toujours le descripteur qui justifie le niveau.

@document Document · note de travail fictive d'un stagiaire, Cartonnerie Lefranc (PME industrielle fictive, 140 salariés, emballages pour l'agroalimentaire), mai 2026
Atelier 1, premier jet. Contexte : l'usine imprime chaque jour les emballages de trois grands industriels laitiers, dont les dates limites de consommation.

Valeurs métier retenues : le serveur de l'ERP ; la ligne d'impression numérique ; Microsoft 365 ; le pare-feu ; les fichiers de formules d'encres.

Biens supports : « l'informatique », « le cloud », « les machines ». Dans la cartographie, l'ERP s'appelle « APP-02 Sylvea ERP » et le logiciel de pilotage de la ligne « APP-05 PrintCtrl » ; je les ai renommés pour faire plus simple.

Événements redoutés et gravité :
ER1 Piratage de l'ERP par des hackers : gravité 4, c'est très grave.
ER2 Rançongiciel sur la ligne d'impression : gravité 4.
ER3 Vol des formules d'encres par un concurrent : gravité 3.
ER4 Panne du pare-feu : gravité 2.

Socle : nous respectons le RGPD et nous avons un antivirus. Je n'ai pas relevé d'écart, faute de temps.

Remarque du responsable qualité, en marge : « Il manque les commandes des clients. Une erreur d'impression sur la date limite de consommation d'un emballage, c'est un rappel de produits chez le client. »

@questions
1. Les valeurs métier proposées en sont-elles ? Classez chaque élément en valeur métier ou en bien support.
2. Réécrivez ER1 et ER2 sous forme d'événements redoutés recevables, avec le critère de sécurité atteint.
3. Quels autres défauts de la note vous paraissent les plus pénalisants pour la suite de l'étude ? Appuyez-vous sur le cours.
4. La remarque du responsable qualité révèle un critère oublié. Lequel, et quel événement redouté équivalent repérez-vous dans votre entreprise d'alternance ?

@pistes
1. Seuls les fichiers de formules d'encres peuvent être une valeur métier (une information essentielle). Le serveur de l'ERP, la ligne, Microsoft 365 et le pare-feu sont des biens supports. Les valeurs métier sont des processus ou informations : « produire les commandes », « les formules d'encres », « les commandes des clients ».
2. Par exemple : « la production est arrêtée plus de deux jours faute de pouvoir lancer les ordres de fabrication » (disponibilité) ; « les commandes des clients sont perdues ou altérées » (intégrité). Ces formulations décrivent la conséquence, sans attaquant ni moyen ; ER4 n'est pas non plus un événement redouté.
3. Les biens supports renommés ou vagues brisent le lien avec la cartographie et font échouer la condition de E10 : il faut reprendre les noms exacts. Les gravités sont fixées sans échelle, par intuition. Le socle est réduit à une affirmation, sans référentiel listé ni écart sourcé, alors que les écarts nourrissent les ateliers 4 et 5.
4. L'intégrité : une donnée fausse imprimée sur un emballage a des conséquences pour les consommateurs. Une bonne réponse formule un événement redouté d'intégrité qui touche les personnes, et pas seulement l'activité, avec son impact et une gravité justifiée par l'échelle.

@qcm
Q: Laquelle de ces formulations est un événement redouté recevable ?
- Piratage du serveur de paie
+ Les salaires ne peuvent pas être versés à la date prévue
- Rançongiciel sur l'ERP, qui chiffre les données comptables
E: Un événement redouté décrit la conséquence pour le métier, ni l'attaquant ni le moyen.

Q: Que vérifie l'approche par conformité d'EBIOS Risk Manager ?
+ Le socle de sécurité et ses écarts
- Les scénarios opérationnels des attaquants
- Les couples de sources de risque
E: Elle traite les risques courants par l'application des règles ; les scénarios traitent ensuite les attaquants plus ciblés.

Q: Quelle est la version en vigueur du guide EBIOS Risk Manager à la date du cours ?
- La version 2010
- La version 2
+ La version 1.5
E: L'ANSSI l'a annoncée en mars 2024 ; aucune source officielle ne confirme une « version 2 ».

# FICHE 18 | L'atelier 2 : sources de risque et objectifs visés | 6

@essentiel
L'atelier 2 répond à une question : qui pourrait vouloir atteindre les valeurs métier, et dans quel but ? On ne parle pas encore des moyens techniques. Une source de risque est une personne, un groupe ou une organisation susceptible d'engendrer un risque ; l'objectif visé est la finalité qu'elle poursuit. On raisonne sur le couple SR/OV, car une même source peut poursuivre plusieurs objectifs.

La démarche suit trois étapes. On dresse une liste large, sans censure. On évalue chaque couple sur des critères explicites : motivation, ressources, activité. On retient enfin les plus pertinents, en général trois à cinq, en justifiant chaque choix par un fait ; un couple écarté se justifie aussi. Les entrées sont les valeurs métier, les incidents passés et la veille sur la menace.

@tableau Évaluer un couple SR/OV
| Critère | Question | Exemple de fait qui l'appuie |
| --- | --- | --- |
| Motivation | La source tient-elle à cet objectif ? | Un arrêt de deux heures pousse à payer la rançon |
| Ressources | A-t-elle les moyens, les compétences, les outils ? | Groupe criminel organisé, outils prêts à l'emploi |
| Activité | Attaque-t-elle des organisations comparables ? | Panorama de la cybermenace de l'ANSSI ; incident passé |
| Pertinence | Que déduit-on des trois critères ? | Barème écrit, par exemple une somme de 3 à 9 |

@rappel Objectif visé
Finalité de la source de risque : extorquer de l'argent, voler des données pour les revendre, saboter une activité, se venger, se faire entendre.

@rappel Veille sur la menace
Source d'entrée de l'atelier, vue en S1 : panorama annuel de la cybermenace de l'ANSSI, observatoire des incidents du CERT Santé, avis du CERT-FR.

@rappel Méthode itérative
Un atelier peut enrichir le précédent. Chez Kestrel, la discussion d'un couple écarté a fait ajouter un écart au socle : « comptes non désactivés au départ ».

@attention Choisir sans justifier
Un couple retenu sans fait ni source citée fait échouer la condition de E11. Écrire pourquoi un couple est écarté montre que la question a été posée.

@document Document · entretien fictif paru dans « Le Mag des clubs », septembre 2026 ; le club Olympique de Brenne et son responsable sont fictifs
Le responsable des systèmes d'information de l'Olympique de Brenne, club de football de deuxième division, revient sur une saison agitée.

« Notre billetterie en ligne vend 9 000 places par match. En mars, des revendeurs ont utilisé des robots pour acheter en quelques secondes toutes les places du derby, puis les ont revendues trois fois plus cher. Nous avons aussi reçu un courriel imitant notre président, qui demandait au comptable un virement urgent de 85 000 euros pour un transfert de joueur. Le comptable a rappelé le président : le virement n'est pas parti.

En avril, après la hausse du prix des abonnements, un groupe de supporters a annoncé sur les réseaux sociaux qu'il allait « faire tomber le site ». Le site est resté inaccessible deux heures un soir de mise en vente. Nous n'avons pas de preuve que ce soit eux.

Notre fichier compte 40 000 abonnés et adhérents, avec leurs coordonnées bancaires pour les prélèvements. Un club voisin a vu ses données publiées par un groupe criminel l'an dernier.

Enfin, j'entends parler d'espionnage par des clubs concurrents qui chercheraient nos données de performance des joueurs. Franchement, je n'y crois pas : tout se sait dans le milieu, et nos analystes publient eux-mêmes des statistiques. »

@questions
1. Dressez la liste des couples source de risque et objectif visé que suggère l'entretien.
2. Évaluez trois de ces couples selon la motivation, les ressources et l'activité, avec un barème écrit, et justifiez chaque cote par un fait du texte.
3. Le responsable écarte l'espionnage par des clubs concurrents. Sa justification est-elle recevable au sens d'EBIOS Risk Manager ?
4. Pourquoi des données de santé intéressent-elles un attaquant davantage que les coordonnées des abonnés d'un club ? Quel fait de votre entreprise d'alternance utiliseriez-vous pour justifier un couple retenu ?

@pistes
1. Revendeurs organisés et accaparement des billets pour les revendre ; escroc et détournement d'un paiement par usurpation du président ; supporters militants et perturbation des ventes pour protester ; groupe cybercriminel et vol du fichier des abonnés pour l'extorsion ou la revente ; club concurrent et obtention des données de performance.
2. Par exemple, l'escroc : motivation forte, ressources moyennes, activité forte (tentative réelle de mars). Le groupe cybercriminel : motivation forte (données bancaires), ressources fortes, activité forte (club voisin attaqué). Les supporters : motivation forte mais ressources faibles et activité non prouvée. Le barème doit être écrit avant la cotation.
3. Oui sur le principe : il écarte le couple en l'écrivant et avec des motifs (information déjà circulante, statistiques publiées), ce qui montre que la question a été posée. Il faudrait seulement s'appuyer sur un fait vérifiable plutôt que sur « j'entends parler », et réexaminer ce choix au cycle suivant.
4. Les données de santé sont durables, très sensibles et se prêtent au chantage ; leur fuite touche les personnes et pèse sur la réputation de l'organisation. Une bonne réponse cite un fait précis et sourcé (incident passé, veille, source publique) et le relie à un couple, sans se contenter d'une généralité.

@qcm
Q: Pourquoi EBIOS Risk Manager raisonne-t-il sur des couples SR/OV ?
- Parce qu'il faut compter les attaquants un à un
- Parce que le couple donne la vraisemblance
+ Parce qu'une même source vise plusieurs objectifs
E: Un groupe criminel peut vouloir chiffrer le SI ou voler des données : ce sont deux couples distincts.

Q: Quels sont les trois critères d'évaluation d'un couple proposés par le guide ?
- Dépendance, pénétration, maturité
+ Motivation, ressources, activité
- Gravité, vraisemblance, impact
E: Les critères de dépendance et de pénétration servent à l'atelier 3.

Q: Que faire d'un couple jugé peu pertinent ?
+ L'écarter en écrivant pourquoi
- Le supprimer du dossier sans laisser de trace
- Le retenir quand même, par prudence
E: Écrire le motif d'exclusion montre que la question a été posée.

# FICHE 19 | L'atelier 3 : parties prenantes et scénarios stratégiques | 6

@essentiel
L'atelier 3 décrit à grandes mailles les chemins qu'une source de risque peut emprunter, en tenant compte de l'écosystème : les attaquants passent souvent par un prestataire, un éditeur ou un partenaire moins protégé que la cible. Chaque partie prenante s'évalue sur quatre critères cotés de 1 à 4 : dépendance et pénétration, qui augmentent la menace ; maturité cyber et confiance, qui l'atténuent.

La formule générique de l'ANSSI donne le niveau de menace : (dépendance × pénétration) / (maturité × confiance). On place les parties prenantes sur un radar en zones de danger, de contrôle et de veille ; les deux premières sont dites critiques. On construit ensuite les scénarios stratégiques, dont la gravité est celle de l'événement redouté le plus grave. On termine par des mesures sur l'écosystème et une réévaluation.

@tableau Les zones de la cartographie de la menace (seuils de Kestrel)
| Zone | Seuil chez Kestrel | Conséquence |
| --- | --- | --- |
| Danger | Au-dessus de 3 | Aucune partie prenante ne devrait y rester |
| Contrôle | De 1 à 3 | Critique : prise en compte dans les scénarios |
| Veille | De 0,5 à moins de 1 | Suivie, hors scénarios |
| Hors périmètre | Moins de 0,5 | Menace jugée négligeable |

@rappel Partie prenante
Acteur de l'écosystème qui interagit avec l'objet de l'étude : client, partenaire, prestataire, éditeur, hébergeur, ou service interne dont la sécurité ne dépend pas du commanditaire.

@rappel Scénario stratégique
Description à grandes mailles de la manière dont une source de risque atteint son objectif et provoque des événements redoutés. On ne cote pas encore sa vraisemblance.

@rappel Mesure sur l'écosystème
Clause contractuelle, réduction des accès, exigence de sécurité, audit. Chez Kestrel, l'accès de l'éditeur de RoutePro ouvert à la demande (pénétration de 4 à 2) et un avenant de sécurité (confiance de 2 à 3) font passer sa menace de 4 à environ 1,3.

@astuce
La formule peut s'adapter : pondérer un critère, ou retirer la confiance si la partie prenante risque d'être utilisée à son insu. Écrivez le barème.

@document Document · cas réel résumé pour le cours d'après la presse spécialisée (The Record, SecurityWeek, Dark Reading), juillet 2021
Le vendredi 2 juillet 2021, veille d'un long week-end aux États-Unis, le groupe criminel REvil exploite une faille de VSA, logiciel de l'éditeur américain Kaseya, signalée à l'éditeur en avril mais pas encore corrigée sur les serveurs installés chez les clients. VSA sert aux prestataires de services informatiques à administrer à distance les postes et les serveurs de leurs clients : il peut installer des logiciels sur des milliers de machines à la fois.

Les attaquants compromettent les serveurs VSA installés chez les prestataires eux-mêmes. Ils diffusent ensuite le rançongiciel sous l'apparence d'une mise à jour ordinaire de l'agent VSA. Kaseya indique que moins de 60 de ses clients, presque tous des prestataires, ont été directement touchés, mais que jusqu'à 1 500 entreprises clientes de ces prestataires ont été chiffrées par ricochet. REvil réclame 70 millions de dollars pour un outil de déchiffrement universel.

En Suède, la chaîne de supermarchés Coop ferme environ 800 magasins pendant plusieurs jours : ses caisses, administrées à distance par un prestataire qui utilisait VSA, ne fonctionnent plus. Coop n'avait aucune relation directe avec Kaseya. Trois semaines plus tard, Kaseya annonce avoir obtenu un outil de déchiffrement d'un tiers, sans préciser comment.

@questions
1. Décrivez le chemin d'attaque qui mène de REvil aux magasins de Coop, maillon par maillon.
2. Évaluez le prestataire de caisses de Coop sur les quatre critères de l'atelier 3 et calculez son niveau de menace. Dans quelle zone le placeriez-vous avec les seuils de Kestrel ?
3. Coop n'avait aucun contrat avec Kaseya. Que montre ce cas sur les limites d'un écosystème réduit aux partenaires directs ?
4. Quel outil d'administration à distance, chez un prestataire de votre entreprise d'alternance, jouerait le même rôle ? Quelles mesures sur l'écosystème proposeriez-vous ?

@pistes
1. REvil exploite une faille de VSA ; il compromet les serveurs VSA des prestataires ; il pousse une fausse mise à jour vers les machines administrées ; les caisses de Coop sont chiffrées ; les magasins ferment. Le scénario stratégique part d'un couple « groupe cybercriminel, extorquer une rançon » et passe par deux parties prenantes en chaîne.
2. Par exemple : dépendance 4 (sans caisses, pas de vente), pénétration 4 (installation de logiciels sur toutes les caisses), maturité 2, confiance 3, soit (4 × 4) / (2 × 3), environ 2,7 : zone de contrôle, voire de danger avec une maturité ou une confiance cotées plus bas. L'essentiel est que le barème soit écrit et chaque cote justifiée.
3. La menace passe par les fournisseurs des fournisseurs. L'écosystème doit partir des contrats, mais aussi des outils par lesquels les prestataires accèdent au SI. Une partie prenante très pénétrante devient critique même si on lui fait confiance.
4. Une bonne réponse nomme un outil ou un accès précis, tiré de la cartographie ou des contrats, évalue la partie prenante avec les quatre critères, et propose des mesures sur l'écosystème : clauses de sécurité et de notification, accès limités et journalisés, validation des mises à jour, réévaluation après mesure.

@qcm
Q: Quels critères augmentent le niveau de menace d'une partie prenante ?
+ La dépendance et la pénétration
- La maturité et la confiance
- La gravité et la vraisemblance du scénario
E: Ce sont les critères d'exposition ; la maturité et la confiance, critères de fiabilité, l'atténuent.

Q: Quelle gravité porte un scénario stratégique ?
- La moyenne des gravités des événements redoutés visés
+ Celle de l'événement redouté le plus grave
- Une gravité nouvelle, fixée à l'atelier 3
E: La gravité vient de l'atelier 1 et reste attachée à l'événement redouté.

Q: Une partie prenante obtient (4 × 3) / (2 × 2) = 3. Avec les seuils de Kestrel, où la place-t-on ?
- En zone de danger
- En zone de veille
+ En zone de contrôle
E: Chez Kestrel, la zone de danger commence au-dessus de 3 ; 3 reste en zone de contrôle.

# FICHE 20 | L'atelier 4 : scénarios opérationnels et vraisemblance | 6

@essentiel
L'atelier 4 décrit, étape par étape, comment l'attaquant réaliserait chaque scénario stratégique sur les biens supports, puis cote la vraisemblance. Un mode opératoire est une suite d'actions élémentaires ; on le représente par un graphe d'attaque en quatre phases : connaître, rentrer, trouver, exploiter. Chaque action nomme un bien support de la cartographie.

Le guide propose trois méthodes de cotation. L'expresse cote directement le scénario. La standard cote la probabilité de succès de chaque action, de 1 à 4, puis la combine : à chaque étape, l'indice cumulé est le minimum entre l'action et le meilleur indice des étapes qui y mènent. La chaîne vaut son maillon le plus faible, et l'attaquant choisit le meilleur chemin. La vraisemblance se justifie toujours par des vulnérabilités sourcées.

@tableau Les quatre phases d'un scénario opérationnel
| Phase | Ce que fait l'attaquant | Exemple d'action |
| --- | --- | --- |
| Connaître | Se renseigner sur la cible | Repérer les techniciens d'un éditeur en sources ouvertes |
| Rentrer | Obtenir un premier accès | Hameçonnage, faille exposée, accès d'un tiers |
| Trouver | Se déplacer, obtenir des droits élevés | Explorer un réseau non cloisonné, voler un compte d'administration |
| Exploiter | Atteindre l'objectif | Chiffrer, voler, modifier, supprimer les sauvegardes |

@rappel Méthode avancée
Elle ajoute à la méthode standard la difficulté technique de chaque action. Pour le D2, l'expresse ou la standard suffisent.

@rappel Chaîne longue
La fiche méthode de l'ANSSI conseille de baisser l'indice d'un niveau pour une chaîne d'une dizaine d'étapes en série. Le SO1 de Kestrel, sept étapes, garde V3.

@rappel Hypothèse
Une cotation qui repose sur une information absente des sources s'écrit « hypothèse » et sa vérification va au plan d'action : une hypothèse fausse changerait la vraisemblance.

@attention Pas de bien support, pas de scénario
Un scénario dont les étapes ne nomment aucun bien support de la cartographie est invérifiable et fait échouer la condition de E13.

@document Document · extrait fictif du rapport d'un prestataire de réponse à incident, commune de Saint-Arlès (collectivité fictive, 22 000 habitants), juin 2026
Chronologie reconstituée. J-20 : l'attaquant consulte le site de la mairie et un réseau social professionnel, et relève les noms et fonctions de douze agents du service urbanisme. Les adresses de messagerie suivent toutes le format prénom.nom. J-6 : un agent reçoit un faux courriel de dépôt de permis de construire et saisit son identifiant et son mot de passe sur une page imitant la messagerie. La messagerie n'exige pas d'authentification multifacteur. J-5 : l'attaquant se connecte à la passerelle VPN avec les mêmes identifiants : le VPN utilise le compte de l'annuaire et n'exige pas non plus de second facteur.

J-4 à J-1 : depuis le poste de l'agent, l'attaquant parcourt le réseau, qui n'est pas cloisonné. Il trouve sur un partage un fichier « mdp_admin.xlsx » contenant le mot de passe du compte d'administration « admin_mairie », utilisé par les trois techniciens. Il identifie le serveur de sauvegarde, intégré au domaine de l'annuaire. J0, dimanche, 2 h : il supprime les sauvegardes, puis chiffre 31 serveurs. L'état civil, la paie et les inscriptions scolaires sont arrêtés. Aucune alerte n'est émise avant l'arrivée des agents, le lundi à 8 h.

Seule une copie mensuelle sur bande, conservée au centre technique municipal, a échappé au chiffrement.

@questions
1. Classez chaque étape de la chronologie dans l'une des quatre phases et nommez le bien support visé.
2. Cotez la probabilité de succès de chaque action de 1 à 4, puis calculez l'indice cumulé avec la règle de la méthode standard. Quelle vraisemblance obtenez-vous, et quelles vulnérabilités sont décisives ?
3. Proposez un mode opératoire alternatif pour la phase « rentrer », et dites s'il modifierait la vraisemblance du scénario.
4. Pour un scénario opérationnel de votre entreprise d'alternance, quelle étape repose sur une hypothèse que vous devriez vérifier, et comment ?

@pistes
1. Connaître : collecte en sources ouvertes, cible le site et les agents. Rentrer : hameçonnage (messagerie), puis connexion VPN (passerelle VPN). Trouver : exploration du réseau, mot de passe d'administration trouvé (partage de fichiers, annuaire), repérage du serveur de sauvegarde. Exploiter : suppression des sauvegardes et chiffrement des serveurs.
2. Une cotation plausible donne 4 pour la reconnaissance, 3 pour l'hameçonnage (il faut tromper une personne), 4 pour le VPN sans second facteur, 4 pour la découverte du mot de passe sur un partage, 4 pour les sauvegardes dans le domaine : l'indice cumulé reste à 3, soit V3 « très vraisemblable » sur une échelle comme celle de Kestrel. Les vulnérabilités décisives sont l'absence d'authentification multifacteur, le compte d'administration partagé et noté en clair, le réseau plat et la sauvegarde intégrée au domaine.
3. Par exemple, l'exploitation d'une faille non corrigée de la passerelle VPN, ou l'achat d'identifiants volés. Si cette branche est cotée 3 ou 4, l'indice de l'étape suivante prend le meilleur des deux chemins : la vraisemblance reste au moins égale, puisque l'attaquant choisit le chemin le plus favorable.
4. Une bonne réponse cite une étape précise, l'hypothèse sur laquelle elle repose (par exemple l'absence d'un second facteur ou d'un cloisonnement), la source qui manque et la manière de la vérifier (entretien, console, test), et indique comment la cotation changerait si l'hypothèse était fausse.

@qcm
Q: Déjà connecté au réseau du siège, l'attaquant obtient un compte d'administration et s'en sert pour localiser le serveur de sauvegarde. Dans quelle phase se range cette action ?
- Rentrer
+ Trouver
- Exploiter
E: Trouver, c'est se déplacer dans le réseau et obtenir des droits élevés pour localiser les biens supports utiles ; le premier accès, lui, relève de « rentrer ».

Q: Deux étapes mènent à l'étape C, avec des indices cumulés de 2 et 4. L'action C vaut 3. Quel est l'indice cumulé de C ?
- 2
- 4
+ 3
E: On prend le meilleur chemin (4), puis le minimum avec l'action (3).

Q: Quelle méthode de cotation cote directement le scénario, sans détailler chaque action ?
+ La méthode expresse
- La méthode standard
- La méthode avancée
E: L'expresse cote le scénario à partir de la source et des vulnérabilités ; la standard cote chaque action.

# FICHE 21 | L'atelier 5 : traitement du risque, mesures et risques résiduels | 6

@essentiel
L'atelier 5 est celui de la décision. Chaque scénario devient un risque, de gravité égale à celle du scénario stratégique et de vraisemblance égale à celle du scénario opérationnel. Placés sur la matrice, ils forment la cartographie des risques initiaux. La stratégie attribue à chacun une option : réduire, transférer, éviter ou accepter, selon le seuil d'acceptation fixé avant l'analyse.

Les mesures sont de quatre types : gouvernance, protection, défense, résilience. Elles vont dans un plan d'amélioration continue de la sécurité, avec une fonction responsable. On estime ensuite les risques résiduels : la protection et la défense font baisser la vraisemblance, la résilience souvent la gravité. Au moins un risque est accepté explicitement. Un cadre de suivi termine l'atelier : indicateurs, instance, rythme des cycles.

@tableau Les quatre types de mesures
| Type | Rôle | Exemple chez Kestrel |
| --- | --- | --- |
| Gouvernance | Organiser la sécurité | Contre-appel avant tout changement de coordonnées bancaires |
| Protection | Empêcher ou compliquer l'attaque | Authentification multifacteur pour tous les comptes VPN |
| Défense | Détecter et répondre | Journaux de la passerelle VPN centralisés, avec alertes |
| Résilience | Limiter les conséquences, reprendre | Sauvegarde isolée hors du siège, restauration testée |

@rappel Acceptation explicite
Décision écrite qui indique le risque, son niveau, le motif, l'instance qui accepte, la mesure compensatoire éventuelle et la date de réexamen. C'est cette trace qui distingue un risque accepté d'un risque ignoré.

@rappel Mesure ou projet
Une mesure de sécurité se formule précisément (« authentification multifacteur pour tous les comptes VPN »). « Passer au cloud » est un projet : il relève du D3, comme le chiffrage.

@rappel Cadre de suivi
Indicateurs d'avancement et d'évolution des risques, instance qui les examine, rythme. Sans lui, l'analyse devient un rapport rangé dans un tiroir.

@attention Ne pas recopier Kestrel
Une étude qui reprend la structure et les formulations de l'exemple Kestrel en changeant noms et chiffres ne rapporte aucun point.

@document Document · procès-verbal fictif du comité de direction de l'Imprimerie Garance (PME fictive, 60 salariés), octobre 2026, point 4 : analyse de risques
Le responsable informatique présente quatre risques initiaux : R1, rançongiciel sur les serveurs de production, critique ; R2, fraude au faux fournisseur, élevé ; R3, vol du fichier clients, élevé ; R4, panne du traceur grand format, faible. Le seuil d'acceptation fixé en mars autorise le comité à accepter les risques moyens ; les risques élevés et critiques doivent être traités. Le dernier incident, une fausse facture payée en juin, a coûté 12 000 euros.

Le comité décide les mesures suivantes. M1 : passer toute l'informatique dans le cloud d'ici 2028. M2 : souscrire une assurance cyber, « ce qui règle R1 et R2 ». M3 : authentification multifacteur sur la messagerie. M4 : faire attention aux courriels suspects. M5 : copie de sauvegarde hors ligne chaque semaine. Aucun responsable n'est désigné : « la DSI s'en chargera ».

Après discussion, le risque R3 est jugé acceptable, « car nous n'avons jamais eu de fuite ». Le risque R4 n'est pas abordé faute de temps.

Le directeur général demande que l'analyse soit refaite « si un incident se produit ». Le responsable informatique estime que, après application des mesures, tous les risques seront nuls.

@questions
1. Classez les mesures M1 à M5 selon les quatre types d'EBIOS Risk Manager, en signalant celles qui ne sont pas des mesures de sécurité au sens du cours.
2. Relevez au moins quatre défauts du procès-verbal au regard de l'atelier 5.
3. Réécrivez la décision sur R3 sous la forme d'une acceptation explicite recevable, ou expliquez pourquoi le comité ne pouvait pas l'accepter en l'état.
4. Pour votre entreprise d'alternance, proposez trois indicateurs d'un cadre de suivi et l'instance qui les examinerait.

@pistes
1. M1 est un projet, qui relève du D3, et non une mesure. M2 est un transfert, classé en gouvernance ; il ne « règle » aucun risque, il en transfère une partie de l'impact financier. M3 est une mesure de protection. M4 est trop vague : il faut la formuler, par exemple en sensibilisation annuelle à l'hameçonnage (gouvernance). M5 est une mesure de résilience.
2. Aucune fonction responsable n'est désignée ; R3, risque élevé, est accepté alors que le seuil n'autorise que les risques moyens, et sans motif recevable ; R4 n'est pas traité, il est ignoré ; l'assurance est présentée comme un traitement complet ; les risques résiduels sont dits nuls, ce qui est impossible ; il n'y a pas de cadre de suivi, seulement une réaction après incident.
3. En l'état, le comité ne pouvait pas l'accepter : R3 est au-dessus du seuil. Il faut soit le réduire jusqu'au niveau moyen, soit, comme Kestrel pour R4, porter une acceptation temporaire à l'instance compétente, avec le niveau, un motif assumé, une mesure compensatoire, une échéance et une date de réexamen. « Jamais eu de fuite » n'est pas un motif : l'absence d'incident connu ne prouve rien.
4. Une bonne réponse propose des indicateurs mesurables et tirés de la situation réelle (part des comptes protégés par authentification multifacteur, délai de correction, date du dernier test de restauration, accès de prestataires ouverts), nomme l'instance qui les examine et fixe un rythme pour les cycles opérationnel et stratégique.

@qcm
Q: Un plan de reprise testé et un poste de travail de secours prêt à l'emploi sont des mesures :
- De protection, car elles évitent l'arrêt
- De défense, car elles détectent l'attaque
+ De résilience, car elles limitent l'impact
E: Elles limitent les conséquences et permettent de reprendre l'activité ; la protection, elle, empêche ou complique l'attaque.

Q: Comment obtient-on le niveau d'un risque initial à l'atelier 5 ?
- Par la moyenne des cotes de toutes les parties prenantes
+ En croisant sur la matrice gravité et vraisemblance
- Par le nombre de mesures du socle qui manquent
E: La gravité vient du scénario stratégique, la vraisemblance du scénario opérationnel ; la matrice est fixée avant l'analyse.

Q: Quelle mention est indispensable dans une acceptation explicite de risque ?
+ Le motif et l'instance qui accepte
- Le coût des mesures qui n'ont pas été retenues
- Le nom de l'attaquant le plus probable
E: Sans motif ni responsable identifié, le risque est ignoré, pas accepté.
