# FT 17 | Repérer les vulnérabilités des données et de l'IA | 7

@situation
Vous êtes en alternance à la DSI de Kestrel Logistique, auprès de Romain Chevalier, responsable de l'infrastructure et RSSI à temps partiel. En octobre 2026, il a déjà étudié les données des destinataires stockées dans Kestrel Track. Il vous confie une autre partie du SI : les données de temps de conduite et de position des chauffeurs, qui circulent entre TeleFleet, Microsoft 365 et la paie, ainsi que les usages d'IA repérés au siège. Il attend un relevé des vulnérabilités et l'ébauche d'un scénario opérationnel.

@capacites
Repérer les composants d'une infrastructure de données
Rattacher une vulnérabilité à sa famille et au critère atteint
Chiffrer un volume de données et une part d'usage
Inscrire un usage d'IA dans la cartographie
Construire et justifier un scénario opérationnel

@duree 60 minutes

@annexe 1 | Ce que deviennent les temps de conduite | Source fictive : note de Romain Chevalier après un entretien avec la gestionnaire de paie, octobre 2026
Chaque mois, le 24 au plus tard, la gestionnaire de paie se connecte à la console de TeleFleet avec le compte « exploitation », que partagent aussi les trois planificateurs. Elle exporte un fichier CSV par site. Pour chaque chauffeur, le fichier donne les temps de conduite jour par jour, mais aussi l'heure et le lieu du premier et du dernier arrêt de chaque journée, que la console ajoute d'office à l'export.

Les fichiers sont déposés dans le dossier « Paie – Temps de conduite » d'un site SharePoint de Microsoft 365. Ce dossier est ouvert à tout le groupe « Administration », soit 26 personnes, dont deux intérimaires. Il contient tous les exports depuis janvier 2022 : personne n'a prévu de les supprimer. La gestionnaire ressaisit ensuite les temps dans l'outil de paie, ce qui lui prend une journée et demie.

Les positions détaillées restent chez le fabricant des boîtiers. Celui-ci propose une API pour les récupérer. La DSI ne l'utilise pas, mais un développeur a créé en 2023 une clé d'accès pour un essai. Cette clé, sans date d'expiration, figure en clair dans un script du dépôt GitHub privé de Kestrel Track.

@annexe 2 | TeleFleet : ce que disent le contrat et la console | Extrait du contrat du fabricant et relevé de la DSI, octobre 2026
| Élément | Valeur relevée |
| --- | --- |
| Camions équipés | 40 porteurs, boîtiers 4G installés en janvier 2021 |
| Envoi d'une position | Toutes les 2 minutes, moteur allumé |
| Circulation moyenne | 10 heures par jour et par camion, 250 jours par an |
| Conservation chez le fabricant | « Pendant toute la durée du contrat » ; aucune purge paramétrée |
| Comptes de la console | 1 compte partagé « exploitation » ; 2 comptes nominatifs de la DSI |
| Mot de passe du compte « exploitation » | Inchangé depuis l'installation, en 2021 |
| Authentification multifacteur | Proposée par le fabricant, non activée |
| Journal des connexions à la console | Conservé 30 jours par le fabricant, jamais consulté |
| Exports CSV dans SharePoint | 3 fichiers par mois (un par site) depuis janvier 2022 |

@annexe 3 | Connexions vers des assistants d'IA grand public depuis le siège, par service, en septembre 2026 | Relevé des journaux de la sortie Internet du siège, DSI, octobre 2026
@graphique barres connexions
Commercial : 410
Planification : 160
Paie et RH : 95
DSI : 60
Quais : 35

@annexe 4 | « Un assistant pour les devis » | Source fictive : courriel de Léa Fontaine, directrice commerciale, à Hélène Garnier, septembre 2026
Hélène, depuis l'été, deux commerciaux collent les demandes de devis reçues par le site web dans un assistant d'IA gratuit pour préparer leurs réponses. Ces demandes contiennent le nom, la société et le téléphone du prospect, et parfois les tarifs que lui pratique son transporteur actuel. Le gain de temps est réel : une réponse en dix minutes au lieu d'une heure.

Je voudrais aller plus loin. Un assistant placé sur le site web dialoguerait avec les prospects, calculerait un prix à partir de notre grille tarifaire et de nos contrats types, et enverrait lui-même la proposition par courriel. Pourriez-vous inscrire ce projet à l'étude pour le comité de décembre ? Romain me dit qu'il faudrait « en faire un scénario de risque » dès maintenant.

@question 1 | Identifier | Annexes 1 et 2
Relevez les éléments de l'infrastructure de données, au sens du chapitre 7, par lesquels passent ou restent les temps de conduite et les positions des chauffeurs, de leur source jusqu'à leurs copies. Nommez les objets comme dans la cartographie de Kestrel quand c'est possible.
@lignes 5

@question 2 | Analyser | Annexes 1 et 2
Pour chaque constat, indiquez la famille de vulnérabilité du chapitre 7, le critère de sécurité atteint en priorité et l'endroit de la cartographie où il doit apparaître.
@tableau
| Constat | Famille de vulnérabilité | Critère atteint | Où le noter |
| --- | --- | --- | --- |
| Compte « exploitation » partagé | | | |
| Exports gardés depuis 2022 | | | |
| Clé d'API en clair | | | |
| Journal jamais consulté | | | |

@question 3 | Calculer | Annexe 2
Calculez le nombre de positions envoyées chaque année par la flotte, puis le nombre de positions conservées chez le fabricant à la fin de 2026. Vérifiez par le calcul le nombre de fichiers d'export présents dans le dossier SharePoint à la fin d'octobre 2026.
@lignes 4

@question 4 | Calculer | Annexe 3
Calculez la part du service commercial et celle de la planification dans les connexions vers des assistants d'IA grand public. Expliquez à quoi ce relevé peut servir dans l'analyse de risques.
@lignes 4

@question 5 | Mobiliser | Annexes 3 et 4
L'usage décrit par Léa Fontaine relève-t-il de l'IA fantôme ? Complétez les attributs qui permettent de l'inscrire dans l'inventaire applicatif et la matrice des flux.
@tableau
| Attribut | Valeur à inscrire |
| --- | --- |
| Statut | |
| Fournisseur et hébergement | |
| Données envoyées | |
| Contrat | |
| Flux : source, cible, mode, protection | |

@question 6 | Mobiliser | Annexe 4
Romain Chevalier a-t-il raison de vouloir « en faire un scénario de risque » ? Dites si le projet d'assistant sur le site web peut fonder un scénario opérationnel, puis nommez deux catégories du Top 10 de l'OWASP pour les applications LLM qu'il exposerait le plus, en justifiant chacune par un élément du courriel.
@lignes 6

@question 7 | Analyser | Annexes 1 et 2
Une bande organisée de vol de marchandises cherche à connaître les lieux et heures d'arrêt habituels des camions de Kestrel. Construisez le scénario opérationnel le plus simple. Pour chaque phase, décrivez l'action élémentaire, le bien support nommé comme dans la cartographie, la vulnérabilité et le fait qui l'établit.
@tableau
| Phase | Action élémentaire | Bien support | Vulnérabilité et fait qui l'établit |
| --- | --- | --- | --- |
| Connaître | | | |
| Rentrer | | | |
| Trouver | | | |
| Exploiter | | | |

@question 8 | Argumenter | Toutes les annexes
Rédigez le paragraphe qui justifie la vraisemblance de ce scénario, puis indiquez deux points où une seule mesure couperait le chemin d'attaque.
@lignes 9

@retiens
L'infrastructure de données regroupe tout ce qui [[stocke]], transporte, transforme ou expose des données hors du cœur des applications ; chaque élément est un [[bien support]] qui hérite de la [[sensibilité]] des données qu'il porte. Un export jamais supprimé relève de la [[fuite par export]] et se note dans la [[matrice des flux]], même si sa protection est « aucune ». L'[[IA fantôme]] est un flux sortant vers un tiers inconnu : elle s'inscrit à l'annexe A comme [[usage hors inventaire]]. Un scénario opérationnel enchaîne connaître, [[rentrer]], trouver et exploiter, sur des biens supports [[existants]].

@corrige 1
Les données naissent dans TRM-03 Boîtiers des 40 camions et partent automatiquement vers APP-05 TeleFleet (FLX-04), où elles sont stockées chez PP-07 Fabricant des boîtiers sans durée définie (annexe 2). Elles en sortent par trois chemins. Le premier est la console web de TeleFleet, d'où partent des exports CSV mensuels, un par site. Le deuxième est le partage de fichiers : le dossier « Paie – Temps de conduite » d'un site SharePoint d'APP-10 Microsoft 365, qui conserve tous les exports depuis 2022. Le troisième est l'API du fabricant, avec une clé d'accès stockée dans un script du dépôt GitHub de Kestrel Track (annexe 1). Les temps finissent enfin dans APP-08 Paie par ressaisie (FLX-05, flux manuel). On attend au moins quatre éléments : stockage chez le fabricant, export CSV, partage SharePoint, API, flux manuel vers la paie (chapitre 7, « Ce qu'on appelle une infrastructure de données »).

@corrige 2
| Constat | Famille de vulnérabilité | Critère atteint | Où le noter |
| --- | --- | --- | --- |
| Compte « exploitation » partagé (mot de passe de 2021, sans authentification multifacteur) | Droits trop larges (compte unique pour plusieurs personnes et plusieurs usages) | Confidentialité, et traçabilité : on ne sait pas qui a fait quoi | Vue de l'administration (compte partagé) ; attributs d'APP-05 TeleFleet |
| Exports gardés depuis 2022 (dossier ouvert à 26 personnes) | Fuite par export, aggravée par des droits trop larges sur le dossier | Confidentialité | Matrice des flux : flux manuel APP-05 TeleFleet vers le dossier SharePoint, avec lieu de dépôt et durée de conservation |
| Clé d'API en clair (sans expiration, dans un script) | Données en clair (identifiant stocké en clair dans un script, faiblesse typique des pipelines) | Confidentialité, puis intégrité si la clé permet d'écrire | Annexe B et vue de l'écosystème : API du fabricant, authentification |
| Journal jamais consulté | Absence de journalisation exploitée (le journal existe, mais 30 jours et sans lecture) | Traçabilité | Inventaire de l'infrastructure ; socle de sécurité |

On accepte « fuite par export » pour la deuxième ligne seule, et « absence de journalisation » pour la quatrième, si la justification montre qu'un journal non lu ne permet ni détection ni mesure d'une fuite (chapitre 7, tableau des sept familles).

@corrige 3
Positions par an : 30 positions par heure (une toutes les 2 minutes) × 10 heures × 250 jours × 40 camions = 3 000 000 positions. De janvier 2021 à fin 2026, six années sont écoulées : 6 × 3 000 000 = 18 000 000 positions conservées, faute de purge (annexe 2). Exports : de janvier 2022 à octobre 2026, il y a 48 mois (2022 à 2025) plus 10 mois (2026), soit 58 mois ; 58 × 3 = 174 fichiers. Chacun contient un mois de temps de conduite et de lieux d'arrêt de tous les chauffeurs d'un site : c'est un historique complet des habitudes de déplacement. Ce n'est pas une « donnée sensible » au sens de l'article 9 du RGPD, mais c'est une donnée personnelle dont la CNIL encadre strictement la conservation dans sa doctrine sur la géolocalisation des véhicules des salariés.

@corrige 4
Total des connexions : 410 + 160 + 95 + 60 + 35 = 760. Part du commercial : 410 / 760 = 53,9 %. Part de la planification : 160 / 760 = 21,1 %. Les deux services font donc 75 % des connexions. Ce relevé est un fait mesuré : il établit l'usage d'assistants grand public et sert à justifier la vraisemblance d'un scénario qui passe par l'IA fantôme, plutôt qu'une impression (chapitre 7, « Construire un scénario opérationnel sur les données ou l'IA »). Il rend aussi plausible l'hypothèse H15, qui visait un planificateur, sans la confirmer : il montre des connexions, pas les données collées. Le courriel de l'annexe 4 apprend ce qui a été collé, mais pour le service commercial seulement.

@corrige 5
Oui : les commerciaux utilisent un outil d'IA non approuvé ni encadré, sans contrat, et des données personnelles sortent du SI vers un tiers inconnu (définition de l'IA fantôme, chapitre 7).

| Attribut | Valeur à inscrire |
| --- | --- |
| Statut | Hors inventaire (usage non approuvé, connu de la direction commerciale) |
| Fournisseur et hébergement | Service d'IA grand public, fournisseur et lieu d'hébergement inconnus |
| Données envoyées | Nom, société et téléphone des prospects ; besoins de transport ; tarifs pratiqués par des concurrents |
| Contrat | Aucun ; durée de conservation des données inconnue |
| Flux : source, cible, mode, protection | APP-12 Site web, puis APP-10 Microsoft 365 (FLX-06, courriel), vers le service d'IA grand public ; mode manuel (copier-coller) ; protection inconnue, aucune maîtrise après l'envoi ; trait en pointillés sur la vue applicative |

@corrige 6
Non pour le scénario opérationnel : l'atelier 4 analyse le SI tel qu'il est, et chaque étape doit reposer sur un bien support existant (chapitre 7, encadré ATTENTION). Le projet peut être cité comme facteur aggravant et signalé comme risque à traiter dès sa conception, ce que le dossier D3 reprendra. En revanche, l'usage actuel de l'assistant gratuit existe et peut, lui, fonder un scénario. Deux catégories sont les plus exposées. LLM01, injection de prompt : n'importe quel visiteur du site public peut saisir des instructions dans le dialogue ou dans le texte d'une demande. LLM03, capacité d'agir excessive : l'assistant « enverrait lui-même la proposition », donc une injection aurait un effet direct, par exemple un prix aberrant engageant Kestrel. On accepte aussi LLM08, exposition du contexte caché, puisque la grille tarifaire et les contrats types seraient placés dans le contexte du modèle, et LLM02, divulgation d'informations sensibles. Le classement 2026 est à vérifier sur le site de l'OWASP.

@corrige 7
| Phase | Action élémentaire | Bien support | Vulnérabilité et fait qui l'établit |
| --- | --- | --- | --- |
| Connaître | Identifier le fabricant des boîtiers et sa console en ligne ; repérer les planificateurs et la gestionnaire de paie sur les réseaux professionnels | APP-05 TeleFleet (console) | Outil standard du marché, accessible depuis Internet ; contacts publics |
| Rentrer | Hameçonner un planificateur ou réutiliser un mot de passe divulgué pour ouvrir le compte « exploitation » | APP-05 TeleFleet, compte partagé | Mot de passe inchangé depuis 2021, quatre utilisateurs, authentification multifacteur non activée (annexe 2) |
| Trouver | Consulter l'historique et exporter les lieux de premier et dernier arrêt ; variante : ouvrir le dossier SharePoint avec le compte d'un intérimaire du groupe « Administration » | APP-05 TeleFleet ; dossier SharePoint d'APP-10 Microsoft 365 | Export qui ajoute les lieux d'arrêt ; 174 fichiers ouverts à 26 personnes (annexes 1 et 2) |
| Exploiter | Déduire les arrêts réguliers de chaque camion et choisir le lieu et l'heure d'un vol de chargement | Données de position des chauffeurs | Aucune détection : journal de 30 jours jamais consulté (annexe 2) |

Une variante par la clé d'API est acceptée si l'élève indique qu'elle suppose d'abord l'accès au dépôt GitHub, donc une étape de plus.

@corrige 8
Éléments attendus, sur 6 points. La source de risque est motivée : les chargements ont une valeur de revente immédiate, et les lieux d'arrêt réguliers sont l'information qui manque pour préparer un vol (1 point). Le chemin ne demande aucune compétence technique : un mot de passe partagé par quatre personnes, inchangé depuis 2021, sans authentification multifacteur (annexe 2) (1 point). Les données sont abondantes et faciles à extraire : 18 millions de positions sans purge et 174 exports ouverts à 26 personnes (questions 1 et 3) (1 point). Rien ne détecterait l'attaque, puisque le journal n'est jamais lu (1 point). Une cote haute, V3 « très vraisemblable » sur l'échelle de Kestrel, est défendable ; l'élève qui retient V2 en invoquant le ciblage préalable de Kestrel doit le justifier (1 point). Deux points de coupure : des comptes nominatifs avec authentification multifacteur sur la console coupent la phase « rentrer » ; un export réduit aux seuls temps de conduite et un dossier restreint et purgé coupent la phase « trouver » ; la révocation de la clé d'API ferme la variante (1 point pour deux points de coupure correctement placés). On pénalise un paragraphe qui décrit des mesures détaillées au lieu de points de coupure : le choix des mesures relève de l'atelier 5 et du dossier D3.

# FT 18 | Analyse d'impact sur l'activité : besoins, capacité, écarts | 8

@situation
Vous assistez Hélène Garnier, directrice des SI de Kestrel Logistique, en octobre 2026. La grille d'impact de la DSI laisse plusieurs lignes « non estimables » faute de contrats, et la paie de fin de mois n'y est pas encore traitée. La directrice a obtenu trois contrats et interrogé le DRH, le directeur des opérations et le responsable de l'agence de Clermont-Ferrand. Elle vous demande de compléter la grille pour ces lignes et de préparer la discussion avec les directions.

@capacites
Relever et convertir des besoins de continuité
Calculer un taux de disponibilité et un arrêt autorisé
Estimer une capacité de reprise à partir de faits
Chiffrer des écarts en heures et attribuer une classe
Repérer une dépendance cachée et discuter une demande

@duree 75 minutes

@annexe 1 | Ce que disent les directions | Source fictive : compte rendu d'entretiens conduits par la DSI, octobre 2026
Nicolas Perrin, DRH : « Hors fin de mois, la paie peut attendre une semaine de travail, cinq jours, comme nous l'avons écrit. Mais du 24 au dernier jour ouvré, c'est autre chose. Les variables sont saisies jusqu'au 26, le prestataire calcule les bulletins le 27 et le fichier de virement part à la banque l'avant-dernier jour ouvré. Pendant cette semaine-là, au-delà d'une journée d'arrêt, 300 salaires partent en retard. Et en aucun cas je ne veux refaire plus d'une journée de saisie. »

Sébastien Morin, directeur des opérations : « Je confirme pour StockFlow : quatre heures d'arrêt au plus, une heure de données perdues au plus. Au-delà, les quais de Saint-Priest et de Moirans s'engorgent. Pour RoutePro, je maintiens deux heures d'arrêt et une heure de données au plus, pour tous les sites. »

Le responsable de l'agence de Clermont-Ferrand : « Nos équipes éditent les lettres de voiture et suivent les tournées locales dans RoutePro, à distance, par le lien avec le siège. Le 17 mars 2026, des travaux de voirie ont coupé la fibre à 7 h 40 ; rien n'est revenu avant 13 h 40. Nous avons rédigé les lettres de voiture à la main et 330 colis sont partis l'après-midi au lieu du matin. On nous dit que RoutePro est en classe 1 ; pour nous, c'est le lien qui compte. »

@annexe 2 | Extraits des trois contrats | Contrats en vigueur, relus par la DSI en octobre 2026
| Clause | APP-02 StockFlow | APP-08 Paie | RES-02 VPN Clermont |
| --- | --- | --- | --- |
| Disponibilité | 99,7 % par mois, hors maintenance programmée (dimanche, de 1 h à 5 h) | 99,5 % par mois, hors maintenance | Non précisée |
| Délai de rétablissement | Aucun engagement chiffré | 3 jours ouvrés en cas d'incident majeur | Garantie de temps de rétablissement : 8 heures, 7 jours sur 7 |
| Sauvegarde | Toutes les 4 heures, conservée 30 jours | Quotidienne, à 23 h | Sans objet |
| Sanction | Avoir sur l'abonnement mensuel | Avoir sur l'abonnement mensuel | Pénalité forfaitaire |
| Secours | Sans objet | Sans objet | Aucun : option 4G non souscrite |

@annexe 3 | Durée cumulée des interruptions de StockFlow, par mois, en 2026 | Rapports mensuels de l'éditeur ; l'interruption de mars est un seul incident, le 24 mars, de 9 h à 12 h 30
@graphique barres heures
Janvier : 0,5
Février : 0
Mars : 3,5
Avril : 0
Mai : 1
Juin : 0
Juillet : 0,5
Août : 0
Septembre : 2,5

@annexe 4 | Deux chaînes de dépendance à compléter | Brouillon de la DSI
@schema
Agence de Clermont-Ferrand -> [[RES-02 VPN Clermont (fibre, sans secours)]] -> [[SAL-01 Salle serveur du siège]] -> APP-01 RoutePro
APP-05 TeleFleet -> [[Ressaisie des temps de conduite (FLX-05)]] -> [[APP-08 Paie]] -> Virement des salaires

@question 1 | Identifier | Annexe 1
Relevez les besoins exprimés par les directions et convertissez-les en heures.
@tableau
| Application ou ressource | Période | DMIA demandée | PDMA demandée |
| --- | --- | --- | --- |
| APP-08 Paie | Du 24 au dernier jour ouvré | | |
| APP-08 Paie | Reste du mois | | |
| APP-02 StockFlow | Toute l'année | | |
| APP-01 RoutePro, vu de Clermont-Ferrand | Toute l'année | | |

@question 2 | Calculer | Annexe 3
Calculez la disponibilité de StockFlow en mars 2026 (31 jours), puis sur les neuf premiers mois de 2026 (273 jours). Comparez chaque valeur à l'engagement du contrat et commentez l'écart entre les deux résultats.
@lignes 5

@question 3 | Mobiliser | Annexes 2 et 3
Le directeur des opérations lit « 99,7 % » et conclut que StockFlow tient son besoin de 4 heures. Calculez l'arrêt cumulé que cet engagement autorise sur un mois de 30 jours, puis expliquez pourquoi sa conclusion est fausse.
@lignes 6

@question 4 | Calculer | Annexes 1 à 3
Complétez la grille d'impact à partir des besoins relevés à la question 1 ; la dernière ligne vise une coupure du lien de l'agence. Pour chaque capacité, indiquez sa source (contrat, incident constaté). Écrivez « non estimable » quand l'information manque.
@tableau
| Ligne | Capacité DMIA (source) | Capacité PDMA (source) | Écart DMIA | Écart PDMA | Classe |
| --- | --- | --- | --- | --- | --- |
| Paie, fin de mois | | | | | |
| Paie, reste du mois | | | | | |
| StockFlow | | | | | |
| RoutePro, Clermont | | | | | |

@question 5 | Analyser | Annexes 1 et 4
Complétez les cases vides du schéma de l'annexe 4. Expliquez ensuite quelle dépendance chacune des deux chaînes révèle, que les directions n'avaient pas citée.
@lignes 5

@question 6 | Mobiliser | Annexes 1 et 4
Appliquez la règle de classement de Kestrel (chapitre 8). Quelle classe retenir pour APP-08 Paie, dont la DMIA varie selon le moment ? Quelle classe reçoit le lien RES-02 VPN Clermont ? Quelle conséquence pour APP-05 TeleFleet ?
@lignes 6

@question 7 | Argumenter | Toutes les annexes
Rédigez une note à Isabelle Roux, directrice administrative et financière, qui discute deux demandes des directions en nommant le motif de chaque discussion (incohérence, dépendance cachée, coût probable). La note constate et interroge : elle ne propose aucune solution technique.
@lignes 10

@retiens
La [[DMIA]] est la durée d'arrêt à ne pas dépasser pour reprendre une application ; la [[PDMA]] est la quantité de données, exprimée en durée, qu'on accepte de perdre. L'écart se calcule en heures, capacité [[moins]] besoin ; un écart [[négatif]] signifie que le besoin est tenu. Un taux de [[disponibilité]] n'est pas une durée d'interruption : seule une durée maximale de [[rétablissement]] écrite au contrat permet d'estimer la capacité d'un service externe. Une ressource dont dépend une application d'une classe supérieure [[hérite]] de cette classe, et une DMIA peut [[varier]] selon le moment.

@corrige 1
| Application ou ressource | Période | DMIA demandée | PDMA demandée |
| --- | --- | --- | --- |
| APP-08 Paie | Du 24 au dernier jour ouvré | 24 h (« au-delà d'une journée ») | 24 h (« plus d'une journée de saisie ») |
| APP-08 Paie | Reste du mois | 120 h (5 jours, besoin de la fiche Kestrel) | 24 h (« en aucun cas ») |
| APP-02 StockFlow | Toute l'année | 4 h | 1 h |
| APP-01 RoutePro, vu de Clermont-Ferrand | Toute l'année | 2 h (besoin de RoutePro, « pour tous les sites ») | 1 h |

Le besoin de Clermont-Ferrand n'est pas une demande nouvelle : c'est celui de RoutePro, qui s'applique à tous les sites qui l'utilisent (chapitre 8, méthode, étape 1).

@corrige 2
Mars : 31 × 24 = 744 heures ; (744 − 3,5) / 744 = 740,5 / 744 = 99,53 %, inférieur à l'engagement de 99,7 %. L'éditeur doit un avoir. Neuf mois : 273 × 24 = 6 552 heures ; arrêt cumulé 0,5 + 3,5 + 1 + 0,5 + 2,5 = 8 heures ; (6 552 − 8) / 6 552 = 99,88 %, supérieur à 99,7 %. Commentaire : la moyenne sur neuf mois paraît excellente, mais elle cache un incident de 3 h 30 en pleine matinée de travail, proche du besoin de 4 heures. Un taux sur une longue période lisse les incidents ; seul l'incident le plus long renseigne sur la durée d'interruption (chapitre 10, « Les indicateurs et leurs références » : convertir pour rendre l'écart parlant).

@corrige 3
Sur 30 jours : 30 × 24 = 720 heures ; 720 × 0,3 % = 2,16 heures, soit environ 2 h 10 d'arrêt cumulé autorisé, sans compter la maintenance du dimanche. La conclusion est fausse pour trois raisons. Le taux autorise un arrêt cumulé, qui peut tomber en une seule fois ; il ne dit rien de la durée d'un incident. Le contrat ne contient aucun délai de rétablissement : rien n'oblige l'éditeur à redémarrer en 4 heures, et sa seule sanction est un avoir. Enfin, quand l'engagement n'est pas tenu, comme en mars, Kestrel obtient seulement cet avoir : rien ne raccourcit l'interruption. La capacité de reprise de StockFlow n'est donc pas garantie (chapitre 8, encadré ATTENTION « Un taux de disponibilité n'est pas une durée d'interruption »).

@corrige 4
| Ligne (besoin DMIA / PDMA) | Capacité DMIA (source) | Capacité PDMA (source) | Écart DMIA | Écart PDMA | Classe |
| --- | --- | --- | --- | --- | --- |
| Paie, fin de mois (24 h / 24 h) | 72 h au mieux, 120 h si un week-end s'intercale (contrat : 3 jours ouvrés) | 24 h (contrat : sauvegarde quotidienne) | +48 h (jusqu'à +96 h) | 0 h, tenu | 2 |
| Paie, reste du mois (120 h / 24 h) | 72 h à 120 h (contrat) | 24 h (contrat) | −48 h, tenu (0 h au pire, tenu) | 0 h, tenu | 4 pour cette période ; 2 pour l'application |
| StockFlow (4 h / 1 h) | Non garantie : aucun délai au contrat ; 3 h 30 constatées en mars | 4 h (contrat : sauvegarde toutes les 4 heures) | Non estimable : délai de rétablissement absent du contrat (le constaté, −0,5 h, ne garantit rien) | +3 h | 1 |
| RoutePro, Clermont, lien coupé (2 h / 1 h) | 8 h (garantie de l'opérateur) ; 6 h constatées le 17 mars | Sans objet : les données restent au siège, rien n'est perdu | +6 h (+4 h constatées) | Sans objet | 1, par RoutePro |

Remarques : la capacité de la paie se calcule à partir du contrat, ce qui est un fait ; le pire cas (incident un jeudi) donne 120 heures. Pour StockFlow, la PDMA réelle se déduit de la fréquence de sauvegarde (chapitre 8, « Estimer la capacité actuelle de reprise »). Les lettres de voiture rédigées à la main devront être ressaisies : c'est un retour à la normale, pas une perte de données.

@corrige 5
Cases : RES-02 VPN Clermont (fibre, sans secours) ; SAL-01 Salle serveur du siège ; ressaisie des temps de conduite (FLX-05), ou « export puis ressaisie des temps de conduite » ; APP-08 Paie. Première chaîne : le besoin de 2 heures exprimé pour RoutePro ne vaut pour Clermont-Ferrand que si le lien RES-02 fonctionne ; or ce lien n'a pas de secours, et son contrat autorise 8 heures de coupure. Pour 35 salariés, le point unique de défaillance n'est pas le serveur, c'est le lien (chapitre 4, point unique de défaillance ; chapitre 8, dépendances). Seconde chaîne : la paie de fin de mois dépend de TeleFleet, puisque les temps de conduite en sont exportés le 24 puis ressaisis (FLX-05). Une panne de TeleFleet autour du 24 retarde la paie, alors que le DRH n'a cité que l'outil de paie.

@corrige 6
La règle de Kestrel classe selon la DMIA validée : classe 1 jusqu'à 4 heures, classe 2 au-delà et jusqu'à 24 heures, classe 3 jusqu'à 72 heures, classe 4 au-delà. La paie a deux DMIA : 24 heures en fin de mois (classe 2) et 120 heures le reste du mois (classe 4). On retient l'exigence la plus forte, la classe 2, sinon le besoin de fin de mois ne peut pas être tenu ; la DMIA variable est précisée dans la grille, comme le chapitre 8 le fait pour Kestrel Track entre 4 h et 7 h. Le lien RES-02 hérite de la classe 1 de RoutePro pour les besoins de Clermont-Ferrand : une ressource dont dépend une application d'une classe supérieure hérite de cette classe. APP-05 TeleFleet est déjà en classe 2 (24 heures) : l'héritage ne change pas sa classe, mais sa DMIA doit être tenue en particulier autour du 24 de chaque mois, ce qu'il faut écrire.

@corrige 7
Éléments attendus, sur 8 points. Forme : note datée, adressée, courte, sans solution (1 point). Première discussion, au choix (3 points) : dépendance cachée à Clermont-Ferrand, avec le fait du 17 mars, l'écart de +6 heures et la question à trancher (le besoin de 2 heures vaut-il aussi pour l'agence, et que fait-elle pendant une coupure ?) ; ou incohérence entre la PDMA de 1 heure demandée pour StockFlow et une sauvegarde toutes les 4 heures, que la direction des opérations ignorait. Seconde discussion (3 points) : coût probable de la paie de fin de mois, où l'écart de +48 à +96 heures vient d'un contrat signé ; la question est de savoir si un mode dégradé (par exemple reconduire le virement du mois précédent) suffit, ce qui relève de la direction et non de la DSI ; ou dépendance de la paie à TeleFleet. Conclusion (1 point) : les décisions attendues, et le rappel que les solutions relèvent du dossier D3. On retire 2 points si la note recommande un équipement ou un changement de prestataire.

# FT 19 | Analyser l'environnement du SI : PESTEL et cinq forces | 9

@situation
Vous êtes stagiaire auprès d'Hélène Garnier, directrice des SI de Kestrel Logistique. En novembre 2026, elle prépare l'analyse de l'environnement externe du SI pour le comité de direction. Léa Fontaine, directrice commerciale, lui a transmis un article de la presse professionnelle ; la DSI tient une base de veille et la DRH suit ses recrutements. Vous devez trier ces informations, compléter le PESTEL du SI, évaluer les facteurs et traduire les cinq forces en exigences sur le SI.

@capacites
Distinguer facteur externe et fait interne
Classer des facteurs dans le PESTEL du SI
Calculer une évolution en pourcentage
Appliquer une règle de niveau d'impact
Traduire les cinq forces en exigences sur le SI
Rédiger le commentaire d'une analyse

@duree 60 minutes

@annexe 1 | « Colis régionaux : la bataille du dernier kilomètre » | Source fictive : article du « Courrier du Transport », septembre 2026
En Auvergne-Rhône-Alpes, la livraison de colis change de visage. Les grands réseaux nationaux baissent leurs prix sur les colis du e-commerce pour remplir leurs camions. Une plateforme régionale de vente en ligne a lancé son propre service de livraison, avec des chauffeurs indépendants et une application qui propose au destinataire un créneau de deux heures et un suivi sur carte.

Les consignes automatiques se multiplient dans les gares, les parkings et les supermarchés. Les e-commerçants les proposent comme mode de livraison moins cher que le domicile. Pour un transporteur, un colis déposé en consigne est un colis de moins livré à domicile, ou un nouvel échange de données avec l'opérateur des consignes.

La grande distribution durcit ses exigences. Une enseigne nationale imposera à ses transporteurs, à partir de mars 2027, la prise de rendez-vous de livraison par son portail et l'envoi de la preuve de livraison dans l'heure, sous peine de pénalités.

Les entreprises peinent toujours à recruter des conducteurs. « Les candidats regardent l'âge des camions et les outils embarqués », constate un dirigeant lyonnais. Côté technologie, plusieurs éditeurs proposent désormais l'optimisation des tournées en SaaS, à l'abonnement, branchée sur le TMS existant.

@annexe 2 | Extrait de la base de veille de la DSI | Base de veille de la DSI, mise à jour en octobre 2026
| N° | Information | Source citée |
| --- | --- | --- |
| V1 | Facturation électronique : depuis le 1er septembre 2026, toutes les entreprises doivent pouvoir recevoir des factures électroniques, et les grandes entreprises et les ETI doivent les émettre ; les PME et micro-entreprises émettront à partir du 1er septembre 2027 | impots.gouv.fr, page consacrée à la facturation électronique ; catégorie de Kestrel (ETI au regard de ses 300 salariés) à vérifier au niveau du groupe |
| V2 | L'éditeur de StockFlow annonce une hausse de 12 % de ses abonnements au 1er janvier 2027 | Courrier de l'éditeur, septembre 2026 |
| V3 | Hausse du nombre de jours de forte chaleur dans la vallée du Rhône | Bilans climatiques de Météo-France, à citer avec leur date |
| V4 | La climatisation de SAL-01 Salle serveur du siège n'a qu'un groupe froid ; la salle a dépassé 30 °C deux après-midi en juillet 2026 | Relevé de la DSI |
| V5 | La Commission européenne a présenté en novembre 2025 un paquet « omnibus numérique » qui modifierait certaines règles du RGPD et le calendrier de l'AI Act ; texte en discussion | Proposition de la Commission sur EUR-Lex ; état à vérifier |
| V6 | L'ERP finance n'a pas de connecteur vers une plateforme agréée de facturation électronique ; l'éditeur le vend en option | Entretien avec la comptabilité |

@annexe 3 | Délai moyen pour pourvoir un poste de chauffeur chez Kestrel | Tableaux de bord de la DRH ; 2026 sur neuf mois
@graphique barres jours
2021 : 28
2022 : 33
2023 : 39
2024 : 44
2025 : 51
2026 : 58

@annexe 4 | Les repères de Cap 2029 | Plan stratégique de Kestrel et contrôle de gestion, situation 2025
| Objectif de Cap 2029 | Situation 2025 | Cible 2029 |
| --- | --- | --- |
| Livrer à J+1 sur toute la région | J+1 assuré dans 9 départements sur 12 | 12 départements sur 12 |
| Réduire les kilomètres à vide | Référence 2025 | −20 % |
| Part du e-commerce dans le chiffre d'affaires | 30 % de 42 M€ | 40 % |
| Certification ISO 14001 | Démarche non engagée | Certification obtenue |

@question 1 | Identifier | Annexe 2
Pour chaque information de la base de veille, dites s'il s'agit d'un facteur externe ou d'un fait interne, et où elle sera utilisée dans le dossier.
@tableau
| N° | Externe ou interne | Justification et usage dans le dossier |
| --- | --- | --- |
| V1 | | |
| V2 | | |
| V3 | | |
| V4 | | |
| V5 | | |
| V6 | | |

@question 2 | Analyser | Annexes 1 et 2
Complétez le PESTEL du SI de Kestrel avec un facteur par dimension, pris dans les annexes 1 et 2. Pour chacun, écrivez son effet sur le SI en nommant l'élément touché, puis classez-le en opportunité (O) ou en menace (M).
@tableau
| Dimension | Facteur (annexe) | Effet sur le SI | O ou M |
| --- | --- | --- | --- |
| Politique | | | |
| Économique | | | |
| Socioculturelle | | | |
| Technologique | | | |
| Environnementale | | | |
| Légale | | | |

@question 3 | Calculer | Annexes 3 et 4
Calculez l'évolution en pourcentage du délai de recrutement d'un chauffeur entre 2021 et 2026. Calculez ensuite, à chiffre d'affaires constant, le chiffre d'affaires du e-commerce en 2025 et celui que vise Cap 2029, et leur écart en valeur et en pourcentage.
@lignes 5

@question 4 | Mobiliser | Annexes 1, 2 et 4
Appliquez la règle à trois niveaux du chapitre 9 à quatre facteurs. Pour chacun, indiquez ce qu'il touche, son échéance, sa certitude, puis le niveau retenu.
@tableau
| Facteur | Ce qu'il touche | Échéance et certitude | Niveau |
| --- | --- | --- | --- |
| Facturation électronique (V1) | | | |
| Hausse de l'abonnement de StockFlow (V2) | | | |
| Optimisation des tournées en SaaS (annexe 1) | | | |
| Omnibus numérique (V5) | | | |

@question 5 | Analyser | Annexe 1
Traduisez chacune des cinq forces de Porter en une exigence vérifiable sur le SI de Kestrel, à partir d'un fait de l'article.
@tableau
| Force | Fait de l'annexe 1 | Exigence sur le SI |
| --- | --- | --- |
| Rivalité entre concurrents | | |
| Nouveaux entrants | | |
| Produits de substitution | | |
| Pouvoir des clients | | |
| Pouvoir des fournisseurs | | |

@question 6 | Mobiliser | Annexes 1 et 4
Déduisez de l'article deux facteurs clés de succès qui reposent sur le SI de Kestrel. Pour chacun, dites quelle application est sollicitée et ce que le diagnostic interne devra vérifier.
@lignes 5

@question 7 | Argumenter | Toutes les annexes
Rédigez le commentaire qui conclut l'analyse de l'environnement : les facteurs les plus forts, ce qu'ils touchent en commun dans le SI, et leur sens dominant. Aucune solution ne doit apparaître.
@lignes 9

@retiens
Le [[PESTEL]] classe les facteurs du macro-environnement en six dimensions ; appliqué au SI, il exige d'écrire pour chaque facteur son [[effet sur le SI]]. Une obligation [[opposable]] se classe en légal, un texte encore en discussion en [[politique]]. Les [[cinq forces]] de Porter se traduisent en exigences vérifiables : c'est la [[pression concurrentielle]] sur le SI. Chaque facteur est classé en [[opportunité]] ou en menace, avec un niveau d'impact fixé par une [[règle écrite]] qui combine portée, échéance et [[certitude]].

@corrige 1
| N° | Externe ou interne | Justification et usage dans le dossier |
| --- | --- | --- |
| V1 | Externe | Obligation légale qui s'impose à Kestrel sans qu'elle la maîtrise ; section 5.1, dimension légale |
| V2 | Externe | Décision d'un fournisseur ; section 5.1 (économique) et force « pouvoir des fournisseurs » |
| V3 | Externe | Tendance climatique ; section 5.1, dimension environnementale |
| V4 | Interne | Caractéristique de l'infrastructure de Kestrel : c'est une faiblesse, au diagnostic interne (section 5.2, domaine infrastructure), à rapprocher de V3 dans le SWOT |
| V5 | Externe | Texte européen en discussion ; section 5.1, dimension politique |
| V6 | Interne | État de l'ERP finance de Kestrel ; diagnostic interne (section 5.2, domaine applications), à rapprocher de V1 |

Le piège est celui du chapitre 9 (« Les erreurs fréquentes ») : V1 et V6, comme V3 et V4, vont par paires, un facteur externe et un fait interne, que le SWOT placera dans deux cases différentes.

@corrige 2
| Dimension | Facteur (annexe) | Effet sur le SI | O ou M |
| --- | --- | --- | --- |
| Politique | Omnibus numérique en discussion (V5) | Pourrait modifier certaines obligations sur les données personnelles traitées par Kestrel Track et TeleFleet ; effet incertain, à surveiller | O (allègement possible) ; M accepté si justifié par l'incertitude |
| Économique | Hausse de 12 % de l'abonnement de StockFlow (V2) | Alourdit un budget SI déjà consacré à 80 % au fonctionnement, au détriment des projets | M |
| Socioculturelle | Difficulté de recrutement des conducteurs (annexes 1 et 3) | APP-04 KDriver et les terminaux deviennent un argument de recrutement ; la prise en main par de nouveaux chauffeurs doit être rapide | M |
| Technologique | Optimisation des tournées en SaaS branchée sur le TMS (annexe 1) | Donne accès à une capacité d'optimisation que RoutePro n'a pas, sans changer de TMS, si l'interface est possible | O |
| Environnementale | Jours de forte chaleur en hausse (V3) | Menace la salle SAL-01, qui héberge RoutePro et l'ERP finance avec une climatisation unique | M |
| Légale | Facturation électronique (V1) | APP-07 ERP finance doit recevoir et émettre des factures électroniques par une plateforme agréée | M |

Pour la dimension légale, une obligation en vigueur va en « légal » ; le texte en discussion de V5 va en « politique » (chapitre 9, règle de classement).

@corrige 3
Délai de recrutement : (58 − 28) / 28 = 30 / 28 = +107 % ; le délai a plus que doublé en cinq ans. E-commerce : en 2025, 30 % × 42 M€ = 12,6 M€ ; cible 2029, 40 % × 42 M€ = 16,8 M€ ; écart 16,8 − 12,6 = 4,2 M€, soit 4,2 / 12,6 = +33 %. Le calcul à chiffre d'affaires constant est une hypothèse de travail, à écrire comme telle. Il montre que Cap 2029 suppose un tiers de colis e-commerce en plus, donc plus de suivi, de créneaux et de preuves de livraison à produire.

@corrige 4
| Facteur | Ce qu'il touche | Échéance et certitude | Niveau |
| --- | --- | --- | --- |
| Facturation électronique (V1) | Une obligation légale et APP-07 ERP finance | Réception obligatoire pour toutes les entreprises depuis le 1er septembre 2026 ; émission dès cette date si Kestrel est une ETI, au 1er septembre 2027 sinon ; certaine | 3 |
| Hausse de l'abonnement de StockFlow (V2) | APP-02 StockFlow, application critique (classe 1), et le budget SI | Janvier 2027 ; certaine | 3 par application stricte de la règle ; 2 accepté si l'élève argumente que la hausse touche le budget et non le fonctionnement de l'application |
| Optimisation des tournées en SaaS (annexe 1) | L'objectif chiffré de −20 % de kilomètres à vide | Offres disponibles dès maintenant ; compatibilité avec RoutePro de 2017 non établie | 2 (réalisation incertaine) ; 3 accepté si justifié |
| Omnibus numérique (V5) | Les obligations du RGPD, applicables à Kestrel Track et TeleFleet | Texte non adopté ; incertain | 2 (obligation touchée, réalisation incertaine, comme NIS2 dans l'exemple du cours) ; 1 accepté si l'élève montre un effet seulement indirect |

La règle est appliquée dans l'ordre : on teste le niveau 3, puis le niveau 2, et le reste reçoit le niveau 1 (chapitre 9, « Évaluer les facteurs »). Ce qui compte est la justification par la portée, l'échéance et la certitude.

@corrige 5
| Force | Fait de l'annexe 1 | Exigence sur le SI |
| --- | --- | --- |
| Rivalité entre concurrents | Les réseaux nationaux baissent leurs prix sur les colis e-commerce | Connaître le coût réel par tournée et par colis : données de tournées fiables dans RoutePro et TeleFleet |
| Nouveaux entrants | Plateforme régionale avec créneau de deux heures et suivi sur carte | Kestrel Track et KDriver doivent pouvoir annoncer et tenir un créneau au destinataire |
| Produits de substitution | Consignes automatiques moins chères que le domicile | Échanger les statuts de livraison avec les opérateurs de consignes ; suivi de bout en bout dans Kestrel Track |
| Pouvoir des clients | Rendez-vous par le portail de l'enseigne et preuve de livraison dans l'heure, dès mars 2027 | Relier RoutePro au portail de rendez-vous ; transmettre la preuve horodatée de KDriver au client en moins d'une heure |
| Pouvoir des fournisseurs | Éditeurs en position de fixer leurs prix (hausse de StockFlow, annexe 2) | Maîtriser les contrats : échéances, conditions de sortie, réversibilité des données |

Le correcteur du D2 attend au moins deux constats de ce type (élément E16, condition b) ; une liste de concurrents ne suffit pas (chapitre 9, encadré ATTENTION).

@corrige 6
Premier facteur clé de succès : annoncer au destinataire un créneau de livraison et le tenir. Il sollicite APP-03 Kestrel Track et APP-04 KDriver ; le diagnostic vérifiera si ces applications savent calculer et diffuser un créneau, et ce que coûte à chaque évolution le framework hors support de Kestrel Track. Second facteur : s'intégrer vite aux portails et formats imposés par la grande distribution. Il sollicite APP-06 Portail EDI et APP-01 RoutePro ; le diagnostic vérifiera la capacité de RoutePro, version de 2017, à échanger avec un nouveau portail avant mars 2027. On accepte aussi la preuve de livraison transmise dans l'heure. Les deux facteurs servent l'objectif de 40 % d'e-commerce et le maintien des contrats de la grande distribution, qui pèse 60 % du chiffre d'affaires.

@corrige 7
Éléments attendus, sur 6 points. Les facteurs les plus forts sont nommés (2 points) : la facturation électronique, obligation déjà applicable ; l'exigence de rendez-vous et de preuve dans l'heure de la grande distribution dès mars 2027 ; la tension sur le recrutement, chiffrée par un délai qui a doublé. Une convergence est dégagée (2 points) : plusieurs facteurs indépendants pèsent sur les échanges de données avec l'extérieur (plateformes de facturation, portails clients, consignes) et sur le couple Kestrel Track et KDriver, au moment où Cap 2029 veut un tiers d'e-commerce en plus. Le sens dominant est donné (1 point) : les menaces l'emportent, la seule opportunité notable étant l'optimisation en SaaS. La hausse de StockFlow, de niveau 3, peut être citée parmi les facteurs les plus forts. Absence de solution (1 point) : le commentaire ne dit pas qu'il faut changer d'ERP ou de TMS ; il annonce que le diagnostic interne dira si ces applications peuvent répondre.

# FT 20 | Diagnostiquer : maturité, forces et faiblesses hiérarchisées, SWOT | 10

@situation
En novembre 2026, Hélène Garnier, directrice des SI de Kestrel Logistique, a diagnostiqué la gouvernance, l'infrastructure et la sécurité, et classé sept faiblesses, F1 à F7. Il reste à établir la note de deux domaines, données et compétences, à classer quatre faiblesses nouvelles et à vérifier un premier SWOT. Elle vous confie ce travail, en vous rappelant que chaque jugement doit être prouvé par un fait.

@capacites
Relever des faits sourcés par domaine
Comparer un indicateur à une référence
Attribuer une note de maturité justifiée
Calculer une moyenne et en discuter la portée
Classer des faiblesses par impact × urgence
Construire un SWOT sans fait nouveau

@duree 75 minutes

@annexe 1 | « Qui sait faire quoi, et qui tient les adresses ? » | Source fictive : entretien avec Hélène Garnier, octobre 2026
« Nos quatre développeurs se répartissent ainsi : deux sur Kestrel Track, qui se remplacent l'un l'autre ; un sur KDriver ; un sur les interfaces et les extractions. Pour KDriver, c'est simple : une seule personne sait publier une nouvelle version sur les terminaux des chauffeurs, et la documentation tient en deux pages. Les deux administrateurs se remplacent pour les sauvegardes, pas pour le réseau. J'ai recensé neuf compétences critiques pour ce diagnostic : c'était la première fois. Hors formations obligatoires, nous n'avons eu aucun budget de formation en 2025.

Les adresses des destinataires sont saisies trois fois : dans RoutePro à partir des ordres de transport, dans StockFlow à la réception, puis dans Kestrel Track pour le suivi. Quand un e-commerçant corrige une adresse sur le portail, la correction n'est faite que dans Kestrel Track. Personne n'est responsable de la qualité des adresses, et la DSI ne suit aucun indicateur sur ce point. C'est le service client qui compte les secondes présentations. »

@annexe 2 | Indicateurs relevés pour le diagnostic | Tableaux de bord de la DSI et du service client, janvier à septembre 2026
| Indicateur | Valeur | Référence disponible |
| --- | --- | --- |
| Disponibilité de Kestrel Track (273 jours) | 99,4 % | Besoin exprimé : 8 heures d'arrêt toléré (fiche Kestrel) |
| Livraisons en seconde présentation pour adresse erronée ou incomplète | 1,2 % des livraisons | Aucune cible fixée |
| Coût d'une seconde présentation | 4,80 € (contrôle de gestion) | Sans objet |
| Compétences critiques portées par une seule personne | 3 sur 9 (KDriver, réseau, interfaces EDI) | Aucune |
| Jours de formation par salarié de la DSI en 2025 | 0,8 jour | Aucune règle interne |
| Délai moyen de résolution des tickets de support | 1,6 jour | Aucun objectif fixé |

@annexe 3 | Notes de maturité provisoires | Brouillon du diagnostic, échelle de 1 (initial) à 5 (optimisé), novembre 2026
| Domaine | Note | Justification résumée |
| --- | --- | --- |
| Gouvernance du SI | 1 | Aucune règle d'arbitrage écrite, aucun portefeuille de projets |
| Organisation et processus | 2 | Processus outillés, mais ressaisies chaque soir (tournées) et chaque mois (temps de conduite) |
| Applications | 2 | Parc qui couvre les besoins ; deux composants hors support |
| Données | ? | À établir |
| Infrastructure | 2 | Sauvegarde chaque nuit (hypothèse H1), non isolée, sans test de restauration documenté |
| Sécurité | 2 | Mesures existantes, aucune politique écrite |
| Compétences et RH | ? | À établir |
| Budget | 2 | Budget connu et suivi ; 80 % en fonctionnement ; aucune ligne pluriannuelle |

@annexe 4 | Faiblesses nouvelles et éléments proposés pour le SWOT | Brouillon de la DSI, novembre 2026
| Repère | Élément |
| --- | --- |
| F8 | Adresses des destinataires saisies dans trois applications, sans référentiel ni responsable de leur qualité |
| F9 | Publication des versions de KDriver maîtrisée par un seul développeur ; documentation de deux pages |
| F10 | Temps de conduite exportés de TeleFleet et ressaisis chaque mois pour la paie (FLX-05) |
| F11 | Aucun budget de formation de la DSI hors formations obligatoires |
| S1 | Équipe de développement interne qui a construit Kestrel Track et KDriver |
| S2 | Offres d'optimisation des tournées en SaaS (section 5.1) |
| S3 | Exigence de rendez-vous et de preuve dans l'heure d'une enseigne, dès mars 2027 (section 5.1) |
| S4 | Passer toute l'infrastructure du siège dans le cloud |
| S5 | Canal EDI qui reçoit 70 % des ordres de transport |
| S6 | Un concurrent régional vient de perdre un client de la grande distribution après une panne |

@question 1 | Identifier | Annexes 1 et 2
Relevez deux faits sourcés pour le domaine « données » et deux pour le domaine « compétences et ressources humaines ».
@lignes 5

@question 2 | Calculer | Annexe 2
Convertissez deux indicateurs dans une unité parlante. Calculez les heures d'arrêt cumulées de Kestrel Track de janvier à septembre 2026, puis le nombre annuel de secondes présentations dues aux adresses et leur coût, sur la base de 2,5 millions de livraisons par an. Comparez chaque résultat à une référence.
@lignes 6

@question 3 | Mobiliser | Annexes 1 à 3
Attribuez une note de maturité aux deux domaines restants, avec l'échelle à cinq niveaux du chapitre 10. Pour chacun, écrivez « noté N parce que… » en citant les critères de l'échelle et les faits.
@lignes 7

@question 4 | Calculer | Annexe 3
Avec vos deux notes, calculez la moyenne des huit domaines. Le directeur général propose d'écrire dans la synthèse : « maturité moyenne du SI : 1,75 sur 5 ». Discutez cette proposition.
@lignes 5

@question 5 | Calculer | Annexes 1, 2 et 4
Classez les faiblesses F8 à F11 selon la règle impact × urgence du chapitre 10. Situez-les ensuite par rapport à F1 et F7 (score 9) et aux faiblesses de score 6 (F2 à F6).
@tableau
| N° | Impact | Urgence | Score | Justification |
| --- | --- | --- | --- | --- |
| F8 | | | | |
| F9 | | | | |
| F10 | | | | |
| F11 | | | | |

@question 6 | Analyser | Annexe 4
Placez les éléments S1 à S6 dans le SWOT du SI, ou écartez-les en donnant le motif.
@tableau
| Élément | Case du SWOT ou motif du rejet |
| --- | --- |
| S1 | |
| S2 | |
| S3 | |
| S4 | |
| S5 | |
| S6 | |

@question 7 | Argumenter | Toutes les annexes
Rédigez le paragraphe de diagnostic du domaine « données » : faits, indicateur comparé à une référence, note justifiée, phrase de jugement au regard de Cap 2029. Croisez enfin ce domaine avec un élément externe du SWOT. Aucune solution ne doit apparaître.
@lignes 10

@retiens
Un diagnostic critique est un jugement [[argumenté]], [[prouvé]] et [[hiérarchisé]]. Une note de maturité respecte la règle du [[maillon faible]] et s'écrit « noté N parce que… ». Un indicateur n'a de sens que comparé à une [[référence]]. Les faiblesses se classent par le produit de l'[[impact]] et de l'[[urgence]], chacun noté de 1 à 3. Le SWOT ne contient aucun [[fait nouveau]], et une solution n'est jamais une [[opportunité]].

@corrige 1
Données : les adresses des destinataires sont saisies dans trois applications, RoutePro, StockFlow et Kestrel Track, et une correction n'est reportée que dans Kestrel Track (annexe 1) ; personne n'est responsable de leur qualité et la DSI ne suit aucun indicateur (annexe 1) ; 1,2 % des livraisons partent en seconde présentation pour adresse erronée (annexe 2). Compétences : trois compétences critiques sur neuf reposent sur une seule personne, dont la publication de KDriver (annexes 1 et 2) ; 0,8 jour de formation par salarié de la DSI en 2025, sans budget hors formations obligatoires (annexes 1 et 2) ; le recensement des compétences a été fait pour la première fois (annexe 1). On attend la source de chaque fait. La saisie multiple d'une adresse dans des applications de fonctions différentes est un défaut de donnée de référence, pas une redondance (définitions communes du cours).

@corrige 2
Kestrel Track : 273 × 24 = 6 552 heures ; 6 552 × 0,6 % = 39,3 heures d'arrêt cumulé en neuf mois. La référence est un arrêt toléré de 8 heures par incident : la comparaison n'est pas directe, mais 39 heures représentent l'équivalent de près de cinq fois l'arrêt toléré, ce qui justifie de demander la durée du plus long incident. Adresses : 2 500 000 × 1,2 % = 30 000 secondes présentations par an ; 30 000 × 4,80 € = 144 000 €. Aucune cible n'existe : l'absence de référence est en soi un constat (chapitre 10, « Les indicateurs et leurs références »). On peut rapporter le coût à la marge opérationnelle (3,1 % de 42 M€, soit environ 1,3 M€) : il en représente environ 11 %.

@corrige 3
| Domaine | Note | « Noté N parce que… » (critères de l'échelle et faits) |
| --- | --- | --- |
| Données | 1 | Pratiques absentes ou improvisées : aucun responsable ni indicateur de qualité, aucune donnée de référence pour l'adresse, corrections faites au cas par cas dans une seule application (annexe 1). Le seul chiffre vient du service client, pas d'une pratique de gestion des données |
| Compétences et RH | 2 | Pratiques existantes mais partielles : binômes sur Kestrel Track et sur les sauvegardes ; mais trois compétences critiques sur neuf portées par une seule personne, aucun plan de formation, recensement fait une seule fois. Le niveau 3 est exclu par la règle du maillon faible |

On accepte 1 pour les compétences si la justification s'appuie sur l'absence de toute gestion formalisée. On refuse une note sans critère cité.

@corrige 4
Avec 1 pour les données et 2 pour les compétences : (1 + 2 + 2 + 1 + 2 + 2 + 2 + 2) / 8 = 14 / 8 = 1,75. La proposition est à écarter pour trois raisons. Une moyenne efface les creux, alors que ce sont eux qui comptent : la gouvernance et les données sont au niveau 1. Les notes sont ordinales : un niveau 2 n'est pas « deux fois » un niveau 1, et une moyenne avec deux décimales donne une précision fausse. Enfin, le chiffre n'a de sens que si l'échelle et ses critères sont présentés avant, ce qu'une synthèse d'une page ne permet pas (chapitre 10, étude « Deux synthèses pour un comité de direction »). Mieux vaut un radar, ou la phrase « deux domaines sur huit restent au niveau initial ».

@corrige 5
| N° | Impact | Urgence | Score | Justification |
| --- | --- | --- | --- | --- |
| F8 | 2 | 3 | 6 | Dégrade la livraison, processus de réalisation, et renchérit l'objectif e-commerce sans l'empêcher ; effet déjà constaté : 30 000 secondes présentations par an |
| F9 | 3 | 2 | 6 | Sans cette personne, aucun correctif de KDriver ne peut être publié : la continuité de la livraison et de la preuve est en jeu ; aucun départ annoncé, échéance d'un à trois ans (urgence 3, score 9, acceptée si l'élève la relie aux évolutions de la preuve exigées dès mars 2027) |
| F10 | 1 | 3 | 3 | Effet limité à une fonction support, la paie ; effet constaté chaque mois (une journée et demie de ressaisie) |
| F11 | 2 | 2 | 4 | Ralentit l'atteinte des objectifs qui supposent de nouvelles compétences, sans l'empêcher ; effet progressif |

F8 et F9 rejoignent le groupe des scores 6, derrière F1 et F7. F11 et F10 viennent ensuite. Les cinq premières restent donc F1, F7 et trois faiblesses de score 6, à départager par une règle écrite, par exemple l'impact, puis le lien avec un risque ou un écart de continuité. D'autres notes sont acceptées si la règle du chapitre 10 est citée.

@corrige 6
| Élément | Case du SWOT ou motif du rejet |
| --- | --- |
| S1 | Force (interne, utile à la stratégie, prouvée par la fiche Kestrel) |
| S2 | Opportunité (facteur externe présent en section 5.1) |
| S3 | Menace (facteur externe présent en section 5.1 : pénalités en cas de retard de preuve) |
| S4 | Rejeté : c'est une solution, pas une opportunité ; elle relève du schéma directeur (dossier D3) |
| S5 | Force (interne, fait de la fiche Kestrel) |
| S6 | Rejeté : fait nouveau, absent de la section 5.1, et non sourcé ; l'élément E19 interdit tout fait nouveau dans le SWOT |

@corrige 7
Éléments attendus, sur 8 points. Faits sourcés, au moins deux : triple saisie des adresses, correction dans une seule application, aucun responsable ni indicateur (annexe 1) (2 points). Indicateur et référence : 1,2 % de secondes présentations, soit 30 000 par an et 144 000 €, sans cible fixée, ce qui est un constat (2 points). Note : « noté 1 parce que » aucune pratique de gestion de la qualité des données n'existe (1 point). Jugement : le domaine ne permet pas aujourd'hui de garantir l'adresse juste dans les trois applications, alors que Cap 2029 prévoit un tiers de colis e-commerce en plus ; chaque colis supplémentaire augmente le coût des erreurs (1 point). Croisement : la menace S3, preuve de livraison dans l'heure exigée dès mars 2027, frappe une donnée de livraison non fiable ; ou l'opportunité d'une optimisation des tournées suppose des adresses justes (1 point). Absence de solution (1 point) : pas de « mettre en place un référentiel unique ».

# FT 21 | Formuler des enjeux et rédiger une synthèse pour la direction | 10

@situation
Le diagnostic du SI de Kestrel Logistique est terminé. En novembre 2026, Paul Vidal, directeur général, demande une synthèse d'une page pour le comité de direction et une présentation de huit minutes, suivie de quatre minutes de questions. Un stagiaire de la DSI a préparé un premier jet. Hélène Garnier vous demande de le reprendre : les enjeux, les chiffres, le vocabulaire, le minutage et la préparation des questions.

@capacites
Reconnaître un enjeu recevable
Reformuler une solution ou un constat en enjeu daté
Vérifier et recalculer les chiffres d'une synthèse
Écrire pour un lecteur non informaticien
Minuter et adapter une restitution orale

@duree 60 minutes

@annexe 1 | Les enjeux proposés par le stagiaire | Brouillon, novembre 2026
| N° | Formulation proposée | Faiblesse citée |
| --- | --- | --- |
| P1 | Acheter le module d'optimisation de RoutePro pour réduire les kilomètres à vide. | F6 tournées construites sous Excel |
| P2 | La sécurité des accès à distance est insuffisante. | F3 accès permanent de l'éditeur, authentification multifacteur limitée aux cadres |
| P3 | Qui doit garantir la qualité des adresses des destinataires, utilisées par trois applications, et selon quels critères ? Échéance : avant mars 2027, date des nouvelles exigences de preuve de la grande distribution. | F8 adresses saisies trois fois |
| P4 | Recruter un deuxième développeur Android. | F9 publication de KDriver maîtrisée par une seule personne |
| P5 | Quel niveau de protection pour la salle serveur ? | F1 une seule salle serveur, sans secours |

@annexe 2 | Premier jet du paragraphe sur la continuité | Brouillon du stagiaire, novembre 2026
« Le BIA met en évidence des gaps majeurs vs les RTO et RPO métiers. Le TMS, SPOF on-premise, a subi en 2024 un downtime de 9 jours, soit 83 k€ de pénalités, près de 30 % de la marge. En cas de sinistre de SAL-01, le RTO réel atteint 120 h (H2) et le RPO 168 h, le seul backup off-site étant hebdo. Pour StockFlow, le SLA de 99,7 % garantit le RTO de 4 h. Voir la vue physique en annexe G. »

@annexe 3 | Chiffres de référence du corps du dossier | Dossier de diagnostic de la DSI, novembre 2026
| Donnée | Valeur | Partie du dossier |
| --- | --- | --- |
| Panne de RoutePro, novembre 2024 | 9 heures ; 2 300 colis en retard ; 38 k€ de pénalités | Partie 4 |
| Besoin pour RoutePro | Arrêt toléré : 2 heures ; perte de données tolérée : 1 heure | Partie 4 |
| Marge opérationnelle 2025 | 3,1 % de 42 M€ | Contexte |
| Remise en service après perte de la salle serveur | 5 jours (hypothèse H2) | Partie 4 |
| Âge maximal de la seule copie hors de la salle | 7 jours (copie hebdomadaire) | Partie 4 |
| Colis traités par jour | Environ 9 000 | Contexte |
| StockFlow | Aucun délai de rétablissement au contrat | Partie 4 |

@annexe 4 | Le comité et le plan du stagiaire | Source fictive : note d'Hélène Garnier, novembre 2026
Paul Vidal raisonne en trajectoire : que faut-il décider pour tenir Cap 2029 ? Isabelle Roux, directrice administrative et financière, à qui la DSI est rattachée, raisonne en coûts, en pertes évitées et en budget. Sébastien Morin, directeur des opérations, pense en camions partis à 5 h et en colis livrés. Léa Fontaine, directrice commerciale, pense aux contrats de la grande distribution et aux e-commerçants. Chacun posera au moins une question.

Le stagiaire a prévu ce minutage : ouverture, 1 min 30 ; ce que montre la cartographie, 3 min ; les trois risques les plus graves, 2 min 30 ; le diagnostic, 1 min 30 ; les enjeux, 45 s ; clôture, 15 s.

@question 1 | Identifier | Annexe 1
Pour chaque proposition, dites si c'est un enjeu recevable et, sinon, quel défaut elle présente (solution imposée, constat, échéance absente, question trop vague).
@tableau
| N° | Recevable ? | Défaut relevé |
| --- | --- | --- |
| P1 | | |
| P2 | | |
| P3 | | |
| P4 | | |
| P5 | | |

@question 2 | Mobiliser | Annexe 1
Reformulez P1, P2 et P4 en enjeux recevables. Pour chacun, écrivez une question sans verbe qui impose la réponse, la faiblesse liée et une échéance justifiée.
@lignes 7

@question 3 | Calculer | Annexes 2 et 3
Vérifiez les chiffres du premier jet à l'aide de l'annexe 3 et corrigez-les. Posez les calculs.
@tableau
| Chiffre du premier jet | Valeur exacte | Calcul ou correction |
| --- | --- | --- |
| Arrêt de 9 jours | | |
| 83 k€ de pénalités | | |
| Près de 30 % de la marge | | |
| Arrêt réel de 120 h après sinistre | | |
| Perte de 168 h de données | | |

@question 4 | Analyser | Annexe 2
Relevez les sigles et anglicismes du premier jet qu'un comité de direction ne comprendrait pas, et les deux autres défauts qui le rendent inacceptable dans une synthèse.
@lignes 5

@question 5 | Calculer | Annexe 4
Calculez la durée totale du plan du stagiaire et son dépassement. Avec la grille de la restitution orale du D2, quelle en serait la conséquence ? Proposez un minutage qui tienne en huit minutes.
@tableau
| Temps | Durée du stagiaire | Durée proposée |
| --- | --- | --- |
| Ouverture | 1 min 30 | |
| Ce que montre la cartographie | 3 min | |
| Les trois risques les plus graves | 2 min 30 | |
| Le diagnostic | 1 min 30 | |
| Les enjeux à trancher | 45 s | |
| Clôture | 15 s | |
| Total | | |
| Dépassement et conséquence | | |

@question 6 | Mobiliser | Annexes 3 et 4
Le même constat, la perte possible de la salle serveur, doit être présenté à Isabelle Roux, à Sébastien Morin et à Léa Fontaine. Pour chacun, indiquez l'angle à choisir et rédigez la phrase d'ouverture.
@lignes 7

@question 7 | Argumenter | Toutes les annexes
Réécrivez le paragraphe de l'annexe 2 en cinq à six lignes, sans sigle ni renvoi à un schéma, pour le bloc « Les écarts de continuité » de la synthèse. Rédigez ensuite la réponse à la question d'Isabelle Roux : « Combien cela va-t-il nous coûter ? »
@lignes 10

@retiens
Un [[enjeu]] est une question que la direction devra trancher, formulée sans imposer de [[solution]], reliée à une [[faiblesse]] ou à un risque et dotée d'une [[échéance]]. La synthèse d'une page s'écrit en [[dernier]] ; elle ne contient aucun [[sigle]] non expliqué, ne renvoie à aucun [[schéma]], et chacun de ses chiffres se retrouve dans le [[corps]] du dossier. À l'oral, on parle à chaque membre du comité dans sa langue et on reconnaît les [[limites]] du travail.

@corrige 1
| N° | Recevable ? | Défaut relevé |
| --- | --- | --- |
| P1 | Non | Solution imposée : « acheter le module » présuppose la réponse |
| P2 | Non | Constat, pas une question ; aucune échéance |
| P3 | Oui | Question ouverte, reliée à F8, échéance justifiée par une date externe |
| P4 | Non | Solution imposée (recrutement) ; aucune échéance |
| P5 | Non | Question trop vague (protection contre quoi, pour quel niveau de continuité ?) et sans échéance ; elle recoupe aussi EN1, qu'il vaut mieux citer |

Le chapitre 10 (« Formuler des enjeux sans imposer de solution ») donne les quatre propriétés : question ou arbitrage ouvert, aucun verbe d'action qui présuppose la réponse, lien avec une faiblesse numérotée, échéance justifiée.

@corrige 2
| N° | Enjeu reformulé | Faiblesse liée | Échéance justifiée |
| --- | --- | --- | --- |
| P1 | Quelle capacité d'optimisation des tournées Kestrel veut-elle se donner pour réduire de 20 % les kilomètres à vide ? | F6 | Décision en 2027, pour produire un effet mesurable avant l'échéance de Cap 2029 |
| P2 | Quel niveau de protection Kestrel exige-t-elle pour chaque accès à distance, salariés comme prestataires ? | F3 | Avant la fin du premier semestre 2027 ; plus tôt si Kestrel relève de NIS2 |
| P4 | Comment Kestrel garantit-elle la maintenance de l'application des chauffeurs si la seule personne qui sait la publier est absente ? | F9 | Avant mars 2027, date à laquelle la preuve de livraison devra parvenir à un client dans l'heure |

D'autres formulations sont acceptées si elles respectent les quatre propriétés. Pour P2, une formulation proche de l'exemple du cours est acceptée, mais l'élève doit citer F3.

@corrige 3
| Chiffre du premier jet | Valeur exacte | Calcul ou correction |
| --- | --- | --- |
| Arrêt de 9 jours | 9 heures | Erreur d'unité, qui multiplie la durée par 24 |
| 83 k€ de pénalités | 38 k€ | Chiffres inversés |
| Près de 30 % de la marge | Près de 3 % | Marge : 3,1 % × 42 M€ = 1,302 M€ ; 38 / 1 302 = 2,9 % |
| Arrêt réel de 120 h après sinistre | 120 h, soit 5 jours, exact (hypothèse H2) | Écart : 120 − 2 = 118 h, à présenter comme « près de cinq jours de plus que le besoin » et comme hypothèse |
| Perte de 168 h de données | 168 h, soit 7 jours, exact | Écart : 168 − 1 = 167 h ; « jusqu'à une semaine de données perdues, contre une heure tolérée » |

On peut ajouter que 2 300 colis représentent 2 300 / 9 000 = 25,6 %, soit environ un quart d'une journée d'activité, ce qui parle davantage à un directeur que le nombre brut.

@corrige 4
Sigles et anglicismes : BIA, gaps, RTO, RPO, TMS, SPOF, on-premise, downtime, SAL-01, H2, backup, off-site, hebdo, SLA. Une direction ne comprend ni les sigles techniques ni les identifiants de la cartographie ; il faut décrire la fonction (« le logiciel qui affecte les tournées »). Deux autres défauts : le renvoi à « la vue physique en annexe G », interdit dans la synthèse (élément E19, condition c) ; et l'erreur de raisonnement sur StockFlow, car un taux de disponibilité ne garantit aucune durée de reprise, et le contrat n'en prévoit aucune (annexe 3). On accepte aussi les erreurs de chiffres relevées à la question 3.

@corrige 5
Durée : 1 min 30 + 3 min + 2 min 30 + 1 min 30 + 45 s + 15 s = 9 min 30, soit 1 min 30 de dépassement. Avec la grille de la restitution orale du D2, un dépassement de plus d'une minute fait perdre la moitié des points du premier critère (structure et temps), soit 2,5 points sur 5. Le plan sacrifie aussi les enjeux, qui sont ce que le comité doit décider.

| Temps | Durée du stagiaire | Durée proposée |
| --- | --- | --- |
| Ouverture | 1 min 30 | 45 s |
| Ce que montre la cartographie | 3 min | 2 min |
| Les trois risques les plus graves | 2 min 30 | 2 min |
| Le diagnostic | 1 min 30 | 1 min 30 |
| Les enjeux à trancher | 45 s | 1 min 15 |
| Clôture | 15 s | 30 s |
| Total | 9 min 30 | 8 min |
| Dépassement et conséquence | 1 min 30 : moitié des points du critère « structure et temps » perdue, soit 2,5 sur 5 | Aucun |

La répartition proposée reprend celle du chapitre 10 ; toute répartition de 8 minutes qui donne au moins une minute aux enjeux est acceptée.

@corrige 6
| Membre du comité | Angle | Phrase d'ouverture |
| --- | --- | --- |
| Isabelle Roux | Coûts et pertes : pénalités, marge, sauvegardes rangées dans son propre bureau | « Une seule panne de 9 heures nous a coûté 38 000 € de pénalités, près de 3 % de notre marge annuelle ; la perte de la salle nous arrêterait près de cinq jours. » |
| Sébastien Morin | Camions et colis : départ à 5 h, tournées | « Si la salle du siège brûle cette nuit, aucun camion ne part demain avec une tournée calculée, ni pendant près de cinq jours. » |
| Léa Fontaine | Clients : grande distribution, 60 % du chiffre d'affaires | « Deux clients de la grande distribution nous ont déjà appliqué des pénalités après 9 heures d'arrêt ; un arrêt de plusieurs jours met leurs contrats en jeu. » |

Le chapitre 10 (« La restitution orale ») demande de présenter le même risque sous l'angle qui touche la personne qui pose la question.

@corrige 7
Proposition de bloc : « Le logiciel qui affecte les tournées doit pouvoir redémarrer en 2 heures, car les camions partent à 5 heures. En novembre 2024, une simple panne de disque l'a arrêté 9 heures : 2 300 colis ont été livrés en retard et deux clients ont appliqué 38 000 € de pénalités. Si la salle informatique du siège était détruite, il faudrait selon notre estimation près de cinq jours pour le remettre en service, et jusqu'à une semaine de données pourrait être perdue, faute de copie récente hors de la salle. Enfin, le contrat du logiciel d'entrepôt en ligne ne fixe aucun délai de redémarrage. » Réponse à Isabelle Roux : « Ce dossier mesure les écarts ; il ne chiffre pas les solutions, qui seront comparées dans le schéma directeur. L'ordre de grandeur à mettre en face est connu : 38 000 € pour une seule panne de 9 heures. » Barème sur 8 points : chiffres justes et cohérents avec l'annexe 3 (2 points) ; aucun sigle ni renvoi à un schéma (2 points) ; conséquences métier plutôt que causes techniques (2 points) ; réponse qui reconnaît la limite du dossier sans esquiver la question (2 points).
