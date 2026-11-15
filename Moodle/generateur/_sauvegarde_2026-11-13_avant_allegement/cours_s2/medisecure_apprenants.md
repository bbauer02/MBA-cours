
# Medisecure – Dossier de présentation (cas fil rouge)
2026-10-16 · Baptiste
Medisecure est une organisation **fictive** créée pour le cycle Expert en informatique et systèmes d'information de la 3W Academy. Toute ressemblance avec une entreprise existante est fortuite. Ce dossier décrit l'organisation telle qu'elle est en octobre 2026. Il sert de base à tous les travaux de l'année.

## Carte d'identité
Medisecure est un réseau de 14 centres de santé qui suit 410 000 patients. Ses centres sont situés en Hauts-de-France et en Île-de-France.
| Élément | Valeur |
| Raison sociale | Association Medisecure Santé (gestionnaire des centres) et Medisecure Services SAS (société de services) |
| Siège | Lille (Nord) |
| Création | 2009 |
| Métier | Centres de santé polyvalents : médecine générale, spécialités, imagerie de proximité, prélèvements ; téléconsultation ; télésurveillance de patients chroniques |
| Implantations | 14 centres : 9 en Hauts-de-France, 5 en Île-de-France |
| Chiffre d'affaires 2025 | 68 M€ de recettes de soins ; excédent de 1,9 M€, réinvesti dans le réseau |
| Effectif | 620 salariés, dont 230 professionnels de santé |
| Patients actifs | 410 000 (au moins un contact en 24 mois) |
| Activité annuelle | 1,1 million de consultations, dont 38 000 téléconsultations ; 95 000 examens d'imagerie |
| Télésurveillance | 4 200 patients suivis en septembre 2026 (3 000 diabétiques, 1 200 insuffisants cardiaques) |
| Actionnariat | Medisecure Services SAS : fondateurs 52 %, fonds d'investissement spécialisé en santé 48 % (depuis 2021) |
| Budget SI 2026 | 2,84 M€, soit 4,2 % des recettes 2025, dont environ 0,6 M€ pour le pôle plateforme |
| Équipe SI | 24 salariés, plus une régie infrastructure d'un jour par semaine |

### Structure juridique et effectifs
Les 14 centres sont gérés par l'association Medisecure Santé, comme l'exige le Code de la santé publique : ses excédents ne peuvent pas être distribués. Les fonctions support (DSI, finance, ressources humaines, achats, immobilier) sont portées par Medisecure Services SAS, détenue par les fondateurs et un fonds d'investissement. La société facture ses prestations à l'association par une convention annuelle : c'est donc elle qui héberge et exploite le SI des centres.
Le fonds siège au comité stratégique de la société. L'association a son propre conseil d'administration, présidé par l'un des fondateurs. Dans ce dossier, « Medisecure » désigne l'ensemble formé par les deux structures.
| Population | Effectif | Employeur |
| Professionnels de santé (médecins, infirmiers, manipulateurs radio) | 230 | Association |
| Accueil et secrétariat médical des centres | 210 | Association |
| Directeurs de centre, facturation et gestion administrative | 48 | Association |
| Centre d'appels | 22 | Association |
| Directions et fonctions support du siège | 86 | Medisecure Services |
| DSI | 24 | Medisecure Services |
| Total | 620 |  |

### Les 14 centres
Les six premiers centres, ouverts autour de Lille entre 2009 et 2014, forment le cœur historique du réseau. Ce sont les seuls à disposer d'un secours 4G et, pour trois d'entre eux (Lille-Centre, Roubaix et Douai), d'un plateau d'imagerie. Les cinq centres rachetés utilisaient déjà le dossier patient informatisé (DPI) CareOne et l'ont gardé.
| Centre | Région | Depuis | DPI | Praticiens et soignants | Consultations 2025 | Rendez-vous non honorés | Débit (Mbit/s) | Secours 4G |
| Lille-Centre | Hauts-de-France | 2009 | MediDossier | 26 | 128 000 | 5,1 % | 100 | Oui |
| Lille-Fives | Hauts-de-France | 2009 | MediDossier | 18 | 84 000 | 5,8 % | 50 | Oui |
| Roubaix | Hauts-de-France | 2011 | MediDossier | 20 | 102 000 | 7,4 % | 50 | Oui |
| Tourcoing | Hauts-de-France | 2012 | MediDossier | 15 | 70 000 | 6,6 % | 30 | Oui |
| Villeneuve-d'Ascq | Hauts-de-France | 2013 | MediDossier | 14 | 66 000 | 4,8 % | 30 | Oui |
| Douai | Hauts-de-France | 2014 | MediDossier | 16 | 74 000 | 6,1 % | 50 | Oui |
| Lens | Hauts-de-France | 2019 (rachat) | CareOne | 17 | 79 000 | 7,2 % | 30 | Non |
| Arras | Hauts-de-France | 2019 (rachat) | CareOne | 15 | 70 000 | 6,4 % | 20 | Non |
| Béthune | Hauts-de-France | 2019 (rachat) | CareOne | 13 | 61 000 | 6,9 % | 20 | Non |
| Saint-Denis | Île-de-France | 2022 (rachat) | CareOne | 19 | 98 000 | 11,2 % | 50 | Non |
| Montreuil | Île-de-France | 2022 (rachat) | CareOne | 16 | 74 000 | 9,1 % | 30 | Non |
| Créteil | Île-de-France | 2023 | MediDossier | 12 | 58 000 | 8,3 % | 30 | Non |
| Nanterre | Île-de-France | 2023 | MediDossier | 11 | 52 000 | 7,9 % | 30 | Non |
| Argenteuil | Île-de-France | 2023 | MediDossier | 10 | 46 000 | 9,8 % | 20 | Non |
Les 230 professionnels de santé comprennent aussi les 6 infirmières de coordination de la télésurveillance et 2 médecins rattachés au siège.

## Histoire et stratégie
Medisecure a grandi vite, par ouvertures et par rachats, sans jamais unifier son système d'information. Le plan 2030 lui fixe de nouvelles cibles, présentées plus bas.

### Dates clés
| Année | Événement | Effet sur le SI |
| 2009 | Création à Lille avec 2 centres | — |
| 2014 | 6 centres | Déploiement du DPI MediDossier, hébergé au siège |
| 2017 | Ouverture de l'imagerie dans 3 centres | Installation d'un PACS sur site |
| 2019 | Rachat de 3 centres en Artois | Arrivée du DPI CareOne (SaaS) |
| 2020 | Crise sanitaire | Plateforme de téléconsultation développée en interne en 6 semaines |
| 2021 | Entrée d'un fonds d'investissement au capital (48 %) | Objectifs de croissance renforcés ; l'équipe qui a créé la téléconsultation devient un pôle de développement |
| 2022 | Rachat de 2 centres en Île-de-France | Ces centres utilisaient déjà CareOne, qui est conservé |
| 2023 | Ouverture de 3 centres en Île-de-France ; lancement de la télésurveillance MediSuivi | DPI historique étendu à l'Île-de-France ; application mobile, et console des infirmières fournie par le fabricant des appareils |
| 2024 | Recrutement d'une data analyst | Premiers tableaux de bord Power BI |
| 2025 (mars) | Rançongiciel sur le centre de Lens | 3 jours d'arrêt du centre, voir la section Sécurité |
| 2025 (septembre) | Recrutement d'un RSSI | Premier poste dédié à la sécurité |
| 2026 (juin) | Plan « Medisecure 2030 » validé par l'association et par la société | Demande d'un schéma directeur SI |
[FIGURE : Données fictives · contrôle de gestion Medisecure, 2018-2025]
La figure présente l'activité annuelle de 2018 à 2025. La téléconsultation n'est reliée à aucun des deux DPI.

### Plan Medisecure 2030
En juin 2026, les instances de l'association et de la société ont validé le plan « Medisecure 2030 ». Il fixe des cibles sur huit axes, presque toutes chiffrées, résumées dans le tableau suivant.
| Axe | Situation 2025 | Cible 2030 |
| Réseau de centres | 14 centres | 20 centres : 6 de plus, dont 3 par rachat |
| Télésurveillance | 4 100 patients fin 2025, 2 pathologies | 15 000 patients, 3 pathologies (ajout de l'insuffisance respiratoire chronique, dont la BPCO) |
| Parcours patient | En partie papier | Numérique de bout en bout, du rendez-vous au paiement |
| Pilotage | Reporting de direction à J+20 (20 jours après la fin du mois) | Reporting à J+2 |
| Rendez-vous non honorés | 7 % | 4 % |
| Alertes de télésurveillance pertinentes | 15 % | 50 % |
| Continuité d'activité | Un centre arrêté 3 jours en 2025 | Aucun arrêt de plus de 4 heures |
| Empreinte numérique par patient | Non mesurée (référence 2025 à établir) | −30 % |
Pour financer ce plan, la société a réservé une enveloppe d'investissement SI de 4,5 M€ sur 2027-2029, en plus du budget de fonctionnement. Le coût de chaque axe n'a pas été estimé et aucune priorité n'a été fixée. Le directeur général a demandé au DSI de piloter l'élaboration d'un schéma directeur, soumis au comité de direction puis aux instances : il doit dire ce qui est faisable dans cette enveloppe, et dans quel ordre.

## Marché et concurrence
Le marché des soins de proximité change vite. Les centres de santé se regroupent en réseaux, la téléconsultation s'est banalisée depuis 2020 et la télésurveillance, remboursée dans le droit commun depuis juillet 2023 après l'expérimentation ETAPES, attire de nouveaux acteurs. Medisecure fait face à cinq types de concurrents ; les noms cités sont fictifs.
| Concurrent | Type | Taille | Ce qu'il fait mieux que Medisecure | Point faible |
| Santéa | Réseau national de centres de santé | 38 centres, 2 100 salariés | Un seul DPI dans tous ses centres, application patient notée 4,4/5, rendez-vous intégrés | Peu présent dans les Hauts-de-France |
| Groupe Hippocrate | Réseau régional de centres | 9 centres en Hauts-de-France | Implanté à Lille et à Lens, délai moyen de rendez-vous de 3 jours | Téléconsultation par la plateforme de réservation, pas de télésurveillance |
| Plateformes nationales de téléconsultation | Services en ligne | Plusieurs millions d'utilisateurs | Consultation en moins d'une heure, 7 jours sur 7 | Pas de suivi dans la durée ni d'examen physique |
| CardioLink | Start-up de télésurveillance | 60 salariés, 22 000 patients suivis | Tri des alertes par algorithme, 40 cardiologues partenaires | Dépend entièrement de médecins extérieurs |
| Hôpitaux de la région | Établissements publics | 3 grands établissements | Expertise spécialisée, plateaux techniques lourds | Délais longs pour les consultations courantes |
Trois évolutions pèsent sur Medisecure. Les patients comparent désormais les services numériques de leurs soignants à ceux des applications grand public. Une partie des financements des centres de santé dépend d'indicateurs numériques, comme l'usage de l'INS, du DMP et de la MSSanté. Enfin, les médecins sont rares et choisissent aussi leur employeur selon la qualité de ses outils : deux praticiens ont quitté le centre de Saint-Denis en 2025 pour rejoindre Santéa.

## Activités et processus métier
Quatre processus portent l'essentiel de l'activité. Ils sont décrits ici tels qu'ils fonctionnent aujourd'hui, défauts compris.

### Le parcours du patient en centre
Le patient prend rendez-vous en ligne dans 62 % des cas, sur une plateforme de réservation grand public. Les autres appellent le centre d'appels du siège (30 %) ou se présentent à l'accueil (8 %). Seuls les agendas des centres MediDossier sont synchronisés avec la plateforme de réservation : dans les centres CareOne, l'accueil recopie chaque rendez-vous à la main.
À son arrivée, le patient présente sa carte Vitale et l'agent d'accueil cherche son dossier dans le DPI du centre. La pièce d'identité n'est pas contrôlée systématiquement, alors que ce contrôle est nécessaire pour qualifier l'identité nationale de santé (INS) : elle n'est qualifiée que pour 40 % des patients. Il n'existe pas de cellule d'identitovigilance. Un patient qui fréquente deux centres équipés de logiciels différents a deux dossiers distincts.
Le praticien consulte et rédige dans le DPI. Les centres MediDossier émettent des ordonnances numériques, enregistrées auprès de l'Assurance Maladie avec un QR code ; les centres CareOne émettent des ordonnances classiques, car le module n'a jamais été activé. La facture part ensuite vers l'Assurance Maladie sous forme de feuille de soins électronique (FSE) ; 4,5 % des FSE sont rejetées et corrigées à la main par le service facturation du siège.
Les résultats du laboratoire partenaire arrivent automatiquement dans MediDossier. Les centres CareOne les reçoivent par courriel non sécurisé, en PDF, et les secrétaires les classent dans le dossier. En imagerie, les radiologues dictent leurs comptes rendus, que les secrétaires saisissent ensuite, souvent en fin de journée.

### La téléconsultation
Le patient réserve un créneau sur la même plateforme, puis reçoit un lien vers l'outil de téléconsultation développé par Medisecure en 2020 sur une API vidéo tierce. Pendant la séance, le médecin garde le DPI ouvert dans une autre fenêtre, car les deux outils ne communiquent pas. Il envoie ensuite l'ordonnance par courriel non sécurisé, en PDF, et saisit la facturation à la main dans le DPI du centre.

### La télésurveillance (MediSuivi)
Le médecin prescrit l'inclusion d'un patient diabétique ou insuffisant cardiaque. Les patients diabétiques portent un capteur de glucose en continu ; les insuffisants cardiaques utilisent une balance et un tensiomètre connectés. Les appareils transmettent leurs mesures à la plateforme du fabricant, par l'application MediSuivi installée sur le téléphone du patient. Le service Télésurveillance de Medisecure interroge ensuite cette plateforme toutes les cinq minutes.
Des règles à seuils fixes, les mêmes pour tous les patients, déclenchent des alertes. Six infirmières de coordination les traitent dans leur console et préviennent le médecin quand c'est nécessaire. La console enregistre pour chaque alerte l'heure d'acquittement et un statut (« appel du patient », « information du médecin » ou « sans suite »), sans motif. Les infirmières reçoivent environ 1 900 alertes par semaine et estiment que 85 % ne justifient aucune action.
Le dispositif inscrit sur la liste des activités de télésurveillance médicale (LATM) est celui du fabricant des appareils, marqué CE comme dispositif médical : c'est le fabricant qui perçoit le forfait technique. Medisecure, déclarée opérateur de télésurveillance auprès de l'agence régionale de santé, perçoit chaque mois le forfait opérateur pour chaque patient suivi. MediSuivi et la console sont des outils ajoutés par Medisecure ; leur statut au regard du règlement européen sur les dispositifs médicaux n'a jamais été analysé.

### Le pilotage
Au début de chaque mois, le contrôle de gestion extrait des fichiers des deux DPI, de la facturation et de la paie, puis les consolide dans Excel. Le tableau de bord du mois écoulé est diffusé vers le 20, soit à J+20.

### Indicateurs actuels
| Indicateur | Valeur 2025 |
| Délai moyen pour un rendez-vous de médecine générale | 6 jours |
| Rendez-vous non honorés | 7 % des rendez-vous confirmés, soit environ 77 000 créneaux perdus par an |
| Factures rejetées | 4,5 % |
| Satisfaction patient (NPS) | +31 |
| Note de l'application MediSuivi sur les magasins d'applications | 2,9/5 |
| Délai du reporting de direction | J+20 |

## Organisation
[FIGURE : Organigramme de Medisecure · comité de direction]
Le directeur général réunit chaque lundi un comité de direction avec les six directeurs. Le comité stratégique de la société, où siègent les fondateurs et le fonds, et le conseil d'administration de l'association se réunissent chacun une fois par trimestre.
Il n'existe pas d'instance dédiée au SI. Les demandes de projets arrivent au comité de direction, souvent par courriel, et sont arbitrées au cas par cas. Les 14 directeurs de centre rendent compte au directeur des opérations ; chacun gère son accueil, son secrétariat et les plannings de ses praticiens. Le DPO, un prestataire externe, est présent deux jours par mois et n'a aucun relais dans les centres.

## La DSI
La DSI compte 24 personnes et consacre 85 % de son budget au fonctionnement courant. Elle n'a pas de gouvernance de projets formalisée, et sa chaîne de développement n'est qu'en partie outillée.

### Équipe
| Pôle | Effectif | Composition | Remarque |
| Direction | 1 | Directeur des SI, rattaché au directeur général | En poste depuis 2016 |
| Sécurité | 1 | RSSI, rattaché au DSI | Arrivé en septembre 2025, seul sur le sujet |
| Infrastructure et support | 9 | 1 responsable, 3 administrateurs systèmes et réseaux, 5 techniciens support (3 au siège, 2 itinérants en Île-de-France) | 1 450 tickets par mois |
| Applications | 3 | 1 responsable, 1 cheffe de projet, 1 administrateur fonctionnel des DPI | Gèrent les progiciels et la relation avec les éditeurs |
| Plateforme | 10 | 1 tech lead, 3 développeurs Python, 3 développeurs JavaScript (Angular et Node.js) dont 1 alternant, 1 développeur mobile alternant, 1 développeur .NET et Java, 1 ingénieur d'exploitation (DevOps) | Développe et exploite Medisecure Connect, la plateforme interne décrite plus loin |
La data analyst recrutée en 2024, Laura Petit, dépend de la direction financière et non de la DSI. Elle a accès aux exports mais pas aux bases de production.

### Budget 2026 : 2,84 M€
| Poste | Montant |
| Personnel interne | 1 710 k€ |
| Licences et abonnements | 538 k€ |
| Hébergement et télécoms | 408 k€ |
| Prestations | 125 k€ |
| Matériel | 60 k€ |

### Principaux contrats
Le tableau suivant détaille les dépenses externes de 2026, hors matériel. L'hébergement de la plateforme, le réseau entre les centres et les deux DPI en représentent à eux seuls 60 %.
| Poste | Fournisseur ou objet | Montant annuel (k€) |
| Licences et abonnements | MediDossier : maintenance et support de l'éditeur | 140 |
| Licences et abonnements | CareOne : abonnement SaaS pour 5 centres | 115 |
| Licences et abonnements | Microsoft 365 : 170 licences E3 (bureaux), 450 licences F3 (accueils et soignants) | 118 |
| Licences et abonnements | Plateforme de réservation : tarif réseau négocié en 2021, renégociation annoncée pour 2027 | 62 |
| Licences et abonnements | PACS : maintenance | 35 |
| Licences et abonnements | FactuSanté : maintenance | 30 |
| Licences et abonnements | Autres logiciels (Veeam, Power BI, antivirus, outils divers) | 38 |
| Hébergement et télécoms | Hébergeur cloud HDS : 22 machines virtuelles de la plateforme | 214 |
| Hébergement et télécoms | Opérateur télécom : réseau MPLS et secours 4G | 168 |
| Hébergement et télécoms | Téléphonie du centre d'appels | 26 |
| Prestations | Régie infrastructure : expert systèmes, un jour par semaine | 48 |
| Prestations | API vidéo de la téléconsultation (abonnement) | 24 |
| Prestations | Intégrateur Microsoft 365 | 15 |
| Prestations | Agence web (site WordPress) | 12 |
| Prestations | Divers | 26 |

### Fonctionnement
Selon le DSI, l'essentiel du temps de l'équipe va au traitement des incidents et des demandes. La DSI traite environ 1 450 tickets de support par mois dans GLPI, un outil qu'elle n'utilise pas pour suivre ses projets. Faute de gestion de portefeuille (recensement, priorisation et suivi des projets) et de méthode commune, la cheffe de projet et le tech lead utilisent chacun leurs propres outils.
[FIGURE : Données fictives · outil de tickets GLPI, janvier-septembre 2026]
Parmi les tickets « comptes et mots de passe », 60 % portent sur une réinitialisation de mot de passe et 30 % sur les comptes communs des accueils. 78 % des tickets « lenteurs de MediDossier » viennent des centres d'Île-de-France.
Le pôle plateforme travaille en sprints de deux semaines, sans product owner : le tech lead arbitre seul entre les demandes de la direction innovation et les incidents. Le code est conservé dans un GitLab interne. Une intégration continue lance les tests unitaires, qui couvrent moins de 40 % du code, mais aucune analyse de sécurité. Les mises en production se font à la main, une à deux fois par mois, souvent le vendredi soir.

### Indicateurs du service informatique
La DSI ne publie pas de tableau de bord. Les valeurs ci-dessous portent sur 2025, sauf mention contraire. Elles ont été reconstituées à partir de GLPI, de la supervision et de la comptabilité.
| Indicateur | Valeur | Commentaire |
| Disponibilité de MediDossier sur les heures d'ouverture | 98,6 % | Environ 50 heures d'indisponibilité dans l'année |
| Disponibilité de Medisecure Connect | 99,1 % | 79 heures d'arrêt, dont 41 non planifiées |
| Disponibilité du réseau des centres | 99,4 % | Coupures surtout dans les centres sans secours 4G |
| Résolution au premier contact | 48 % | Le support n'a pas de base de connaissances |
| Délai moyen de résolution des incidents majeurs | 6 h 40 | Mesuré sur 38 incidents majeurs |
| Délai moyen de résolution, toutes demandes | 2,3 jours | Aucun objectif de délai n'est fixé |
| Satisfaction des utilisateurs internes | 5,9/10 | Enquête de juin 2026, 212 réponses |
| Sauvegardes réussies | 91 % | Les échecs ne sont pas analysés |
| Postes à jour des correctifs de sécurité | 72 % | Les postes des centres rachetés sont les moins à jour |
| Personnel formé à la sécurité dans les 12 derniers mois | 0 % | Aucune session depuis 2022 |
| Délai de détection d'une intrusion | Non suivi | 41 heures constatées entre la connexion de l'attaquant et la découverte, en mars 2025 |
| Durée de restauration constatée | 3 jours | Centre de Lens, mars 2025 |
| Projets livrés dans les délais et le budget | 2 sur 7 | Projets 2024-2025 |
| Dépenses SI par rapport au budget 2025 | +11 % | Dont environ 120 k€ liés à l'incident (prestataire et matériel) ; le reste n'est pas expliqué |
| Coût informatique par salarié | 4 580 € | Budget 2026 (2,84 M€) pour 620 salariés |
| Part du budget consacrée aux projets | 15 % | Les évolutions de Medisecure Connect sont comptées en fonctionnement |

### Compétences de la DSI
En septembre 2026, le DSI a évalué son équipe sur une échelle de 1 (notions) à 4 (expert). Le tiret signale une compétence absente.
| Domaine | Niveau | Qui | Remarque du DSI |
| Administration Windows et VMware | 3 | 3 administrateurs | Aucun n'est formé au cloud ni aux versions récentes |
| Réseau et pare-feu | 3 | 1 administrateur | Une seule personne compétente |
| Python et frameworks web | 3 | Tech lead et 3 développeurs | Pas de pratique du typage ni des tests avancés |
| Angular et Node.js | 2 | 3 développeurs, dont 1 alternant | Aucun ne connaît les versions récentes |
| Développement mobile React Native | 2 | 1 développeur alternant | Personne pour le remplacer |
| .NET et Java | 2 | 1 développeur | Seul à maintenir le service Documents et la console |
| DevOps, conteneurs, intégration continue | 2 | 1 ingénieur d'exploitation | Pas de conteneurs en production |
| Cloud public | — | Personne | L'hébergeur gère tout |
| Sécurité applicative | 1 | RSSI | Personne ne relit le code sous l'angle de la sécurité |
| Architecture logicielle | 2 | Tech lead | Aucune documentation d'architecture |
| Données et BI | 2 | Data analyst (hors DSI) | Pas d'ingénieur data |
| Intelligence artificielle | — | Personne | Aucune expérience en apprentissage automatique |
| Gestion de projet et agilité | 2 | Cheffe de projet, tech lead | Pas de product owner, méthodes non partagées |
| Management | 2 | DSI, responsables de pôle | Aucun responsable formé au management |
Deux départs à la retraite sont prévus d'ici 2028 : un administrateur systèmes et le responsable du pôle infrastructure et support. Les deux alternants terminent leur contrat en septembre 2027.

### La veille aujourd'hui
Medisecure n'a pas de dispositif de veille. Chacun suit ce qui le concerne avec ses propres outils ; le partage reste informel et rien n'est conservé.
| Qui | Ce qu'il suit | Comment | Partage |
| DSI | Offres des éditeurs, actualité du secteur | Newsletters, deux salons professionnels par an | À l'oral, en comité de direction |
| RSSI | Alertes de sécurité | Bulletins du CERT-FR, sites spécialisés | Courriels ponctuels à l'équipe infrastructure |
| Tech lead et développeurs | Frameworks et bibliothèques | Forums, GitHub, réseaux sociaux, à titre personnel | Discussions informelles sur Teams |
| DPO externe | Doctrine de la CNIL | Veille de son cabinet | Une note par trimestre au directeur général |
| Directrice innovation | Télémédecine, start-ups, IA en santé | Salons, réseau personnel, LinkedIn | Présentations en comité de direction |
| Direction financière | Remboursements, financements publics | Site de l'Assurance Maladie | Aucun |
Personne ne suit la réglementation de l'IA ni le numérique responsable. Les développeurs ont découvert en 2024 que Node.js 14 n'était plus maintenu depuis avril 2023. Enfin, plusieurs alertes publiques sur l'hameçonnage visant les établissements de santé ont été diffusées en 2024 ; elles n'ont pas été relayées en interne.

## Parc applicatif
Le SI compte 18 applications, dont deux dossiers patients informatisés (DPI) différents et plusieurs briques hors support. L'éditeur de MediDossier arrêtera la maintenance de la version 8 fin 2027.
| Application | Domaine | Technologie | Hébergement | Utilisateurs | État et points connus |
| MediDossier v8 | DPI | Progiciel client lourd, SQL Server 2014 | Salle serveur du siège | 9 centres, environ 400 | Fin de maintenance fin 2027 ; SQL Server 2014 hors support |
| CareOne | DPI | SaaS web | Éditeur certifié HDS | 5 centres, environ 170 | Version référencée Ségur, mais modules DMP, INSi et ordonnance numérique jamais activés ; pas d'interface avec le laboratoire ; exports limités |
| Plateforme de réservation | Rendez-vous | SaaS tiers grand public | Éditeur | Patients, accueil | Agendas synchronisés avec MediDossier seulement ; double saisie dans les centres CareOne |
| Téléphonie du centre d'appels | Rendez-vous | Téléphonie IP cloud | Opérateur | 22 téléconseillers | 480 000 appels par an, 18 % non décrochés |
| FactuSanté | Facturation, tiers payant | Progiciel | Salle serveur du siège | Centres MediDossier | Les centres CareOne facturent avec le module de CareOne |
| PACS et RIS | Imagerie | Progiciel, une instance et un stockage local par centre d'imagerie | 3 centres | Manipulateurs, radiologues | 45 To, stockage plein à 82 % |
| Portail patient et téléconsultation | Espace patient, soins à distance | Développement interne : Angular 12, Node.js 14 | Cloud certifié HDS | Patients, médecins | Angular 12 et Node.js 14 hors support ; aucun test de bout en bout |
| Services de la plateforme Medisecure Connect | Patients, rendez-vous, documents, facturation, télésurveillance | Développement interne : Python, .NET, Node.js | Cloud certifié HDS | Applications de la plateforme | Détail dans la section sur la plateforme |
| MediSuivi (application mobile) | Télésurveillance | React Native 0.63, repris d'un prototype de 2020 | Magasins d'applications | 4 200 patients | Version obsolète, qui ne peut plus être mise à jour sur Google Play depuis fin 2025 ; notée 2,9/5 ; déconnexions des appareils fréquentes |
| Console de coordination | Télésurveillance | Java Swing, JDK 8, installée sur les postes ; fournie en 2023 par le fabricant des appareils, reprise en interne en 2024 | Postes des infirmières | 6 infirmières | Aucune évolution depuis 2024, seulement des corrections urgentes |
| ERP finance | Comptabilité, achats | Progiciel | Salle serveur du siège | Direction financière | Fonctionnel |
| Paie | RH | SaaS externalisé | Prestataire | Service RH | Fonctionnel |
| Plannings des praticiens | RH, opérations | Fichiers Excel sur SharePoint | Microsoft 365 | Directeurs de centre | Aucun lien avec les agendas de rendez-vous |
| Microsoft 365 | Bureautique, messagerie | SaaS | Microsoft | Tous | Licences E3 et F3 ; authentification multifacteur pour la DSI seulement |
| Messagerie sécurisée de santé (MSSanté) | Échanges entre soignants | Service d'un opérateur | Opérateur | Praticiens | Utilisée pour 12 % des courriers seulement |
| Power BI | Reporting | SaaS, 3 licences Pro | Microsoft | Direction financière | Alimenté par des exports CSV manuels |
| Site web | Communication | WordPress | Hébergeur mutualisé | Public | Extensions non mises à jour |
| GLPI | Support, inventaire | Open source | Salle serveur du siège | DSI | Inventaire incomplet |
Hors inventaire officiel : des secrétaires et des médecins utilisent des assistants d'IA générative gratuits pour rédiger des courriers. Les journaux du pare-feu relèvent environ 1 500 connexions par semaine vers ces services.

## La plateforme Medisecure Connect
Medisecure Connect regroupe les applications développées en interne depuis 2020 : le portail patient avec la téléconsultation, l'application MediSuivi, la console des infirmières de coordination et les services qui les font fonctionner. Issue de l'outil de téléconsultation de 2020, elle s'est étendue entre 2021 et 2023 ; aucune architecture cible n'a été documentée.

### Architecture actuelle
[FIGURE : Schéma d'architecture logicielle · tech lead de la plateforme, septembre 2026]
La plateforme a été découpée en services entre 2021 et 2023, mais quatre d'entre eux partagent la même base PostgreSQL et lisent directement les tables des autres. Une modification de la structure des tables du service Patient peut ainsi casser la facturation ou la télésurveillance. La base MariaDB, héritée de 2020, sert aujourd'hui à Keycloak ; MinIO et MongoDB stockent les documents.
Elle échange avec l'extérieur de quatre façons. Le service Patient reçoit chaque nuit un export CSV des identités de MediDossier, mais rien de CareOne. Le service Télésurveillance interroge toutes les cinq minutes l'API de la plateforme du fabricant des appareils. Le service Rendez-vous synchronise les créneaux de téléconsultation avec la plateforme de réservation. Le service Facturation produit un fichier mensuel des forfaits, ressaisi ensuite dans FactuSanté.

### Qualité du code
Le code compte environ 210 000 lignes, dont 140 000 en Python. Trois versions de Python coexistent (3.7, 3.8 et 3.9) et les dépendances ne sont pas figées : les fichiers requirements.txt ne correspondent plus à ce qui tourne en production. Le code n'est pas typé et n'a pas de documentation générée. La création des objets métier est dispersée dans une quarantaine de modules. La connexion à la base passe par un objet global partagé, non conçu pour les accès simultanés, à l'origine de plusieurs incidents sous charge. Les règles de facturation tiennent dans une fonction de 1 200 lignes.
[FIGURE : Données fictives · rapports de couverture de l'intégration continue]
Sur les douze derniers mois, 31 % des mises en production ont été suivies d'un correctif urgent dans la semaine.

### Ce que les directions attendent de la nouvelle plateforme
| Attente | Exprimée par | Volume ou contrainte |
| Un dossier patient unique, partagé entre les centres et la télémédecine | Direction médicale | 500 000 dossiers à rapprocher, dont 30 000 doublons |
| Prise de rendez-vous intégrée, y compris pour la téléconsultation et les centres CareOne | Direction des opérations | 1,3 million de rendez-vous par an, pics de 1 200 connexions simultanées le lundi matin |
| Tri intelligent des alertes de télésurveillance | Direction innovation | 15 000 patients et 9 millions de mesures par mois en 2030 |
| Ordonnance numérique et documents versés au DMP | Direction médicale | Ordonnance numérique obligatoire ; alimentation du DMP attendue par les financeurs |
| Facturation automatique des forfaits et des téléconsultations | Direction financière | 4 200 forfaits par mois aujourd'hui, 15 000 en 2030 |
| Disponibilité de 99,9 % et temps de réponse inférieur à 2 secondes | DSI | Sur 24 h/24 et 7 j/7, soit moins de 9 heures d'arrêt par an ; 95 % des requêtes en moins de 2 secondes |
| Accessibilité de niveau AA (WCAG 2.1) | Direction générale | Patients âgés ou en situation de handicap |
| Échanges avec les laboratoires, l'imagerie et l'Assurance Maladie | DSI | HPRIM et HL7 FHIR, DICOM, SESAM-Vitale |

## Infrastructure, réseau et postes de travail
L'essentiel du SI tourne dans une seule salle serveur au siège, sur une virtualisation hors support, sans site de secours ni plan de reprise.

### Architecture technique
[FIGURE : Schéma réseau Medisecure · version DSI 2024]
La salle serveur compte trois serveurs physiques. La virtualisation repose sur VMware vSphere 6.7, que l'éditeur ne maintient plus depuis 2022. En 2026, l'intégrateur a remis un devis de remise en support sous forme d'abonnement : 38 k€ par an, contre 6 k€ de support en 2021. L'annuaire Active Directory est synchronisé avec Microsoft Entra ID pour Microsoft 365. La salle a une climatisation simple et un onduleur de 30 minutes d'autonomie, mais pas de groupe électrogène.
Les sauvegardes sont faites chaque nuit avec Veeam sur un NAS installé dans la même salle que les serveurs, et conservées 14 jours seulement. Une copie part chaque semaine sur bande, et la bande est rangée au domicile du DSI. Aucun plan de reprise d'activité n'a été écrit ni testé ; le dernier test de restauration complète du SI date de 2023. Les 22 machines virtuelles du cloud sont sauvegardées par une instance Veeam chez l'hébergeur, dans la même zone.
Les 14 centres sont reliés au siège par le réseau privé de l'opérateur. Le contrat signé en 2019 limite leur débit garanti de 20 à 100 Mbit/s, et le lien du siège, à 200 Mbit/s, est saturé aux heures de pointe. Les centres d'Île-de-France utilisent MediDossier par des sessions de bureau à distance ouvertes sur des serveurs du siège. Tous les centres sortent sur Internet par le pare-feu de Lille, y compris pour utiliser les services SaaS. À Béthune, le Wi-Fi des patients n'est toujours pas séparé du réseau interne ; il l'a été en urgence à Lens après l'incident. La plateforme Medisecure Connect tourne chez un hébergeur certifié HDS, sur 22 machines virtuelles, dans une seule zone et sans réplication.

### Postes de travail et équipements
| Équipement | Nombre | Remarque |
| Postes de travail | 780 | 15 % encore sous Windows 10, hors support depuis octobre 2025 |
| dont postes d'accueil partagés | 64 | Un compte commun par centre |
| Imprimantes | 210 | Modèles différents selon l'origine des centres |
| Lecteurs de cartes Vitale et de cartes professionnelles | 290 | Indispensables à la facturation |
| Smartphones des infirmières de coordination | 6 | Aucune gestion centralisée |
Les postes sont protégés par un antivirus classique, sans outil de détection et de réponse aux menaces (EDR).

## Données et échanges
Les données de Medisecure sont dispersées : pas de référentiel patient commun, pas d'entrepôt de données, et beaucoup d'échanges encore manuels. La télésurveillance deviendra la source la plus volumineuse en nombre d'enregistrements si le plan 2030 est tenu.

### Volumétries
| Données | Volume actuel | Évolution | Format |
| Dossiers MediDossier | 340 000 patients, 9,5 millions de documents, base de 2,8 To | +8 % par an | SQL Server, PDF |
| Dossiers CareOne | 160 000 patients | +5 % par an | SaaS, exports CSV |
| Rendez-vous | 1,3 million par an, annulations comprises, 5 ans d'historique | Suit l'activité | API de la plateforme de réservation (payante) |
| Factures | 1,2 million de feuilles de soins par an | Suit l'activité | Base FactuSanté, module CareOne |
| Imagerie | 45 To | +5 To par an | DICOM |
| Mesures de télésurveillance | 2,5 millions par mois, base de 1,1 To (réponses brutes de l'API conservées) | Environ 9 millions par mois si 15 000 patients | PostgreSQL, JSON |
| Alertes de télésurveillance | 1 900 par semaine | Suit le nombre de patients | PostgreSQL |
| Appels du centre d'appels | 480 000 par an | Stable | Journaux de téléphonie |
| Journaux techniques | Non centralisés | — | Divers |

### La télésurveillance
Depuis son lancement mi-2023, MediSuivi a gagné des patients chaque trimestre, jusqu'au plafond atteint début 2026.
[FIGURE : Données fictives · base MediSuivi, juillet 2023 - septembre 2026]
Un patient diabétique produit 24 valeurs par jour : la plateforme du fabricant transmet une valeur de glucose par heure, et conserve les valeurs brutes, relevées toutes les 5 minutes. Un insuffisant cardiaque en produit environ 7 (poids, tension, pouls). La taille de la base vient d'un choix de conception : le service Télésurveillance enregistre aussi la réponse brute de chaque appel à l'API du fabricant. À 15 000 patients, la cible du plan 2030, MediSuivi recevrait environ 9 millions de mesures par mois et, au rythme actuel, près de 7 000 alertes par semaine.

### Qualité des données
Les 500 000 dossiers des deux DPI correspondent à environ 470 000 personnes, dont 410 000 ont consulté au moins une fois en 24 mois. Environ 30 000 patients ont un dossier dans chacun des deux DPI, sans aucun lien entre les deux. Chaque DPI a aussi son propre référentiel de praticiens et de lieux, ce qui oblige le contrôle de gestion à faire les correspondances à la main. Les diagnostics sont codés en CISP-2 dans MediDossier mais saisis en texte libre dans CareOne. L'identité nationale de santé n'est qualifiée que pour 40 % des patients. Enfin, la plateforme de réservation conserve le statut « non honoré » de chaque rendez-vous depuis 2021.

### Échanges avec l'extérieur et entre applications
| Flux | De → vers | Format | Fréquence | Remarque |
| Feuilles de soins | FactuSanté et CareOne → Assurance Maladie | SESAM-Vitale | Par lots, chaque jour | 4,5 % de rejets |
| Résultats de laboratoire | Laboratoire → MediDossier | HPRIM Santé | Quotidienne | Automatique |
| Résultats de laboratoire | Laboratoire → centres CareOne | PDF par courriel non sécurisé | Quotidienne | Classement manuel |
| Documents patients | MediDossier → DMP (Mon espace santé) | Documents CDA via l'API DMP | Au fil de l'eau | 35 % des documents envoyés ; rien depuis CareOne |
| Courriers médicaux | DPI → confrères | MSSanté ou courriel | Au fil de l'eau | MSSanté pour 12 % des courriers |
| Rendez-vous | Plateforme de réservation ↔ MediDossier | API | Toutes les 5 minutes | Rien vers CareOne |
| Créneaux de téléconsultation | Plateforme de réservation ↔ service Rendez-vous | API | Au fil de l'eau | Seul lien entre la téléconsultation et les rendez-vous |
| Mesures | Dispositifs → plateforme du fabricant → MediSuivi | API REST | Toutes les 5 minutes | Dépend du fabricant |
| Synthèses de télésurveillance | MediSuivi → DPI | Ressaisie manuelle | Mensuelle | Aucune interface |
| Pilotage | DPI, FactuSanté, paie → Excel et Power BI | Exports CSV | Mensuelle | Consolidation à la main |
| Identités des patients | MediDossier → service Patient | Export CSV | Chaque nuit | Rien depuis CareOne |
| Forfaits de télésurveillance | Service Facturation → FactuSanté | Fichier, puis ressaisie | Mensuelle | Double saisie |

## Sécurité et conformité
L'état des lieux du RSSI conclut à un niveau de sécurité insuffisant au regard des données traitées. L'incident de mars 2025 a porté le sujet devant les instances dirigeantes.

### L'incident de mars 2025
[FIGURE : Chronologie reconstituée par le prestataire de réponse à incident]
Le VPN et le serveur de fichiers hérités de l'ancien propriétaire du centre avaient été conservés après le rachat de 2019, ce qui explique que seul ce centre ait été touché. L'intrusion date du 10 mars, le chiffrement du 12 mars à 2 h 40 et la découverte du même jour à 7 h 45. Les journaux disponibles ne permettent pas de savoir si des données de patients ont été copiées avant le chiffrement. Le coût de l'incident est estimé à 310 k€ : 190 k€ d'activité perdue (trois jours de fermeture puis trois semaines de fonctionnement dégradé), 85 k€ pour le prestataire de réponse à incident et 35 k€ de remplacement de matériel. L'incident a été signalé au CERT Santé par le portail de signalement le 15 mars, et une plainte a été déposée. La violation a été notifiée à la CNIL le 17 mars, au-delà du délai de 72 heures prévu par le RGPD. Medisecure n'a pas d'assurance cyber, et la question de l'information des patients n'a pas été tranchée.

### État des lieux
Le RSSI a dressé cet état des lieux à son arrivée, en septembre 2025, et l'a mis à jour en septembre 2026. Après l'incident, seules des mesures d'urgence ont été prises : EDR déployé par le prestataire sur Lens et le siège avec une licence de six mois non renouvelée, réinitialisation des mots de passe, authentification multifacteur sur le VPN des prestataires, séparation du Wi-Fi des patients à Lens. Le programme de fond n'a pas été financé.
| Domaine | Constat |
| Gouvernance | Politique de sécurité (PSSI) de 2018, jamais révisée. Ni cartographie ni analyse de risques à jour. |
| Identités et accès | Authentification multifacteur pour la DSI et, depuis l'incident, pour le VPN des prestataires. Comptes partagés aux accueils. Environ 120 comptes de personnes parties toujours actifs. Prestataires avec un accès VPN permanent. Les soignants se connectent à la console et au portail avec des comptes Keycloak locaux ; Pro Santé Connect n'est pas intégré. |
| Postes et serveurs | Antivirus classique ; l'EDR déployé en urgence en 2025 n'est plus sous licence. Correctifs appliqués irrégulièrement. Composants hors support sur site : vSphere 6.7 et SQL Server 2014 au siège, Windows 10 sur 15 % des postes. Sur la plateforme : Python 3.7, 3.8 et 3.9, Django 2.2, Flask 2.0, .NET Core 3.1, Node.js 14 et 16, Angular 12, React Native 0.63, PostgreSQL 13, MariaDB 10.5, RabbitMQ 3.8, Redis 6.0, HAProxy 2.4, CentOS 7, Keycloak 15. |
| Détection | Pas de supervision de sécurité. Journaux non centralisés, conservés quelques jours sur chaque serveur. |
| Sauvegarde et reprise | Sauvegardes quotidiennes dans la même salle que les serveurs, non isolées du réseau ; seule une bande hebdomadaire sort du site, au domicile du DSI. Aucun plan de reprise, ni écrit ni testé. |
| Réseau | Wi-Fi des patients non séparé à Béthune. Une seule sortie Internet, au siège. |
| Personnel | Aucune sensibilisation depuis 2022. Usage d'IA génératives gratuites non encadré. |

### Conformité
| Cadre | Situation | Question ouverte |
| RGPD | DPO externe 2 jours par mois ; registre incomplet (MediSuivi absent) ; aucune analyse d'impact (AIPD) ; durées de conservation non appliquées | Quelles analyses d'impact sont obligatoires ? |
| Hébergement de données de santé (HDS) | Hébergeurs externes certifiés ; la salle du siège, exploitée par Medisecure Services, héberge les données de santé des centres gérés par l'association | Quelles obligations s'appliquent à chaque hébergement, au regard du référentiel HDS de 2024 ? |
| NIS2 | Non analysé | Medisecure est-elle concernée, quelle entité, et à quel titre ? |
| AI Act | Non analysé | Quel niveau de risque pour chaque projet d'IA envisagé ? |
| Référentiels e-santé (Ségur) | INS qualifiée pour 40 % des patients ; DMP partiellement alimenté ; MSSanté peu utilisée | Quel plan de mise en conformité ? |
| Accessibilité | Application MediSuivi et site jamais audités ; nombreux patients âgés ou en situation de handicap | Quelle obligation légale, et quel engagement volontaire ? |
| Dispositifs médicaux (règlement UE 2017/745) | Le dispositif du fabricant est marqué CE ; MediSuivi et la console, qui affichent des alertes, n'ont jamais été évalués | MediSuivi est-il un dispositif médical ? Quelles conséquences pour le projet de tri des alertes ? |
| Espace européen des données de santé (EHDS) | Non analysé | Quelles exigences s'appliqueront aux logiciels de dossier patient d'ici 2030 ? |

### Continuité d'activité : ce que demandent les métiers
En septembre 2026, le RSSI a demandé à chaque direction combien de temps elle pouvait se passer de chaque application, et quelle perte de données elle pouvait accepter. Les réponses n'ont pas encore été confrontées aux coûts.
| Application | Direction consultée | Arrêt toléré | Perte de données tolérée | Situation actuelle |
| Télésurveillance et console des infirmières | Innovation | 2 heures | 15 minutes | Une seule zone, sauvegarde chaque nuit, restauration jamais testée |
| Téléphonie du centre d'appels | Opérations | 1 heure | Sans objet | Service de l'opérateur |
| MediDossier | Médicale | 4 heures | 1 heure | Sauvegarde chaque nuit, restauration complète estimée à 2 jours |
| CareOne | Médicale | 4 heures | 1 heure | Engagement de l'éditeur : 99,5 % de disponibilité |
| Plateforme de réservation | Opérations | 8 heures | 1 heure | Engagement de l'éditeur : 99,9 % de disponibilité |
| Microsoft 365 | Toutes | 8 heures | 1 heure | Service Microsoft |
| Portail patient et téléconsultation | Innovation | 24 heures | 4 heures | Sauvegarde chaque nuit |
| PACS | Médicale | 24 heures | 4 heures | Stockage local, aucune copie hors site |
| FactuSanté | Financière | 48 heures | 24 heures | Sauvegarde chaque nuit |
| ERP finance | Financière | 5 jours | 24 heures | Sauvegarde chaque nuit |
| Paie | Ressources humaines | 5 jours, sauf en fin de mois | 24 heures | Prestataire externe |
Toutes les directions ont d'abord répondu « le moins possible » ; les valeurs du tableau ont été obtenues après relance.

## Ce que disent les acteurs
Ces propos ont été recueillis lors d'entretiens internes en septembre 2026.
| Partie prenante | Verbatim |
| Thomas Reynaud, directeur général | « Je découvre les chiffres du mois quand il est déjà trop tard pour agir. » |
| Dr Nadia Benali, directrice médicale | « Un patient vu à Lens puis à Lille a deux dossiers. Un jour, on passera à côté d'une allergie. » |
| Sophie Marchand, directrice administrative et financière | « L'incident nous a coûté 310 k€, et on me demande encore d'arbitrer des projets SI sans aucun chiffrage. » |
| Karim Haddad, directeur des opérations | « Les plannings des médecins sont dans Excel, les rendez-vous ailleurs : on ouvre des créneaux sans médecin. » |
| Claire Vasseur, directrice innovation et e-santé | « On me demande de multiplier les patients par trois et demi, avec une appli que les patients notent mal et une équipe qui ne suit déjà plus les alertes. » |
| Philippe Lemaire, directeur des SI | « On m'a demandé pendant dix ans de faire tourner l'existant avec un budget de fonctionnement, je l'ai fait. Un schéma directeur, personne ne me l'a demandé avant juin. » |
| Julien Morel, RSSI | « Je n'ai ni cartographie ni journaux. Si nous sommes attaqués demain, je ne saurai pas ce qui a été touché. » |
| DPO externe | « Le traitement de télésurveillance n'est même pas au registre, et aucune analyse d'impact n'a été faite. » |
| Laura Petit, data analyst | « Je passe 80 % de mon temps à nettoyer des exports CSV. » |
| Médecin généraliste, centre de Roubaix | « J'ai trois fenêtres ouvertes : le DPI, la téléconsultation et la messagerie. Rien ne se parle. » |
| Infirmière de coordination | « La plupart des alertes, c'est une balance posée sur le tapis ou un capteur qui n'a pas synchronisé. On les acquitte à la chaîne, et j'ai peur d'en rater une vraie. » |
| Secrétaire médicale, centre de Douai | « On tape les comptes rendus dictés le soir. Certaines collègues utilisent une IA gratuite pour aller plus vite. » |
| Patient télésurveillé (avis sur un magasin d'applications) | « L'appli perd la connexion avec mon tensiomètre tous les deux jours. » |
| Mehdi Saïdi, tech lead de la plateforme | « Chaque service lit les tables des autres. Plus personne n'ose toucher aux tables du service Patient sans prévenir tout le monde. » |
| Émilie Roussel, directrice des ressources humaines | « Je n'ai aucune visibilité sur les compétences dont la DSI aura besoin dans trois ans, ni sur les départs à anticiper. » |
| Directrice du centre de Saint-Denis | « On a changé d'outil deux fois en quatre ans. Si on nous impose un autre DPI sans nous demander notre avis, je vais perdre des médecins. » |
| Représentant du fonds au comité stratégique | « Nous financerons la transformation si nous voyons son effet sur la marge de la société avant notre sortie, prévue vers 2030. » |

## Projets envisagés et contraintes
Les directions ont proposé 12 projets, sans chiffrage ni priorités, pour une enveloppe de 4,5 M€ sur 3 ans. Selon la directrice financière, l'enveloppe ne suffira pas à tout financer, mais aucun chiffrage ne le montre encore.
| Projet | Porté par | Ce que l'on sait |
| Unification des DPI | DSI, direction médicale | La fin de maintenance de MediDossier v8 (décembre 2027) impose une décision ; l'unification est demandée par la direction médicale. Options citées : tout migrer vers CareOne, passer à MediDossier v9 en SaaS, ou lancer un appel d'offres |
| Entrepôt de données et pilotage | Direction générale, direction financière | Objectif : reporting à J+2 |
| Prédiction des rendez-vous non honorés (IA) | Direction des opérations | Objectif : passer de 7 % à 4 % |
| Priorisation des alertes de télésurveillance (IA) | Direction innovation | 85 % d'alertes jugées non actionnables par les infirmières (estimation) |
| Assistant IA de rédaction des comptes rendus | Direction médicale | Motivation : usages actuels d'IA gratuites, non encadrés |
| Refonte de la plateforme Medisecure Connect | Direction innovation | Sortir de la dette technique, intégrer les DPI, ordonnance électronique |
| Passage à l'échelle de MediSuivi | Direction innovation | 15 000 patients et l'insuffisance respiratoire chronique d'ici 2030 |
| Programme de cybersécurité | RSSI | Authentification multifacteur, EDR, sauvegardes isolées, plan de reprise, supervision, sensibilisation |
| Modernisation de l'infrastructure | DSI | Sortie de vSphere 6.7 ; question du passage au cloud |
| Interopérabilité Ségur | Direction médicale | INS, DMP, MSSanté |
| Plannings et rendez-vous unifiés | Direction des opérations | Supprimer les plannings Excel |
| Intégration des futurs centres | Direction générale | 6 centres d'ici 2030, dont 3 rachats |

### Contraintes
| Contrainte | Détail |
| Budget | 4,5 M€ d'investissement sur 2027-2029. Le budget de fonctionnement SI ne peut pas augmenter de plus de 10 % par an. L'enveloppe couvre les dépenses externes des projets et le coût des nouveaux recrutements sur la période ; le temps des équipes existantes n'y est pas imputé. |
| Calendrier | Fin de maintenance de MediDossier v8 en décembre 2027 ; l'éditeur propose un support étendu de 12 mois facturé 40 % plus cher. Aucun budget de projet n'est prévu en 2026. |
| Équipe | 24 personnes à la DSI, 4 postes supplémentaires au plus d'ici 2029, hors remplacement des départs. |
| Continuité des soins | Centres ouverts de 8 h à 20 h, du lundi au samedi ; télésurveillance 7 jours sur 7. Les bascules se font la nuit ou le dimanche. |
| Réglementation | Données de santé (RGPD article 9, HDS), obligations du Ségur du numérique ; NIS2 et AI Act à analyser. |
| Conduite du changement | Deux cultures de DPI chez les soignants, forte résistance à un outil imposé. |
| Actionnaire | Le fonds attend une amélioration de la marge de Medisecure Services dès 2028 et prévoit de céder sa participation vers 2030. |
| Environnement | −30 % d'empreinte numérique par patient d'ici 2030. |

### Coûts de référence
Ces ordres de grandeur, fictifs mais réalistes, servent à chiffrer les propositions. Un chiffrage doit dire lesquels il utilise et justifier ceux qu'il ajoute.
| Poste | Coût |
| Développeur interne confirmé | 68 k€ par an, charges comprises |
| Alternant | 25 k€ par an, charges comprises |
| Développeur externe en régie | 650 € par jour |
| Chef de projet externe | 800 € par jour |
| Architecte ou expert sécurité externe | 1 000 € par jour |
| Machine virtuelle chez l'hébergeur HDS | 810 € par mois en infogérance complète (sauvegarde, supervision, administration) ; 200 à 300 € en simple location |
| Stockage objet chez l'hébergeur HDS | 0,03 € par Go et par mois |
| Baie en colocation dans un second centre de données | 2 500 € par mois |
| Licence Microsoft 365 E3 | 36 € par utilisateur et par mois, authentification multifacteur comprise |
| Outil EDR | 60 € par poste et par an |
| Supervision de sécurité externalisée (SOC) | 90 k€ par an |
| Sensibilisation à la sécurité (module en ligne) | 25 € par salarié et par an |
| Test d'intrusion | 15 k€ par campagne |
| Poste de travail renouvelé | 1 100 €, installation comprise |
| Abonnement CareOne | 23 k€ par centre et par an |
| Formation d'un développeur | 2 500 € pour une session de 3 jours |
| Recette moyenne d'une consultation | 45 € |
| Recette moyenne d'un examen d'imagerie | 90 € |
| Forfait opérateur de télésurveillance | 30 € par patient et par mois |
| Autres recettes (rémunération forfaitaire des centres, actes techniques) | Environ 8 M€ par an |
| Rémunération forfaitaire liée aux indicateurs numériques | 3 k€ perçus par centre et par an ; environ 9 k€ atteignables |
| Infirmière de coordination | 52 k€ par an, charges comprises |
| Secrétaire médicale | 38 k€ par an, charges comprises |
| MediDossier v9 en SaaS (offre de l'éditeur) | 26 k€ par centre et par an |
| Support étendu de MediDossier v8 | 196 k€ pour 12 mois |
| Reprise des données d'un DPI | 15 à 25 k€ par base |
| Formation d'un soignant à un nouveau DPI | 1 jour, soit environ 600 € de temps médical |
| Baisse d'activité d'un centre pendant un changement de DPI | 20 à 30 % pendant 2 à 4 semaines |
| Abonnement VMware (devis 2026) | 38 k€ par an |

## Glossaire
| Terme | Définition |
| AI Act | Règlement européen sur l'intelligence artificielle, qui classe les systèmes d'IA par niveau de risque |
| AIPD | Analyse d'impact relative à la protection des données, exigée par le RGPD pour les traitements à risque élevé |
| API | Interface qui permet à deux logiciels d'échanger des données automatiquement |
| BI | Informatique décisionnelle : tableaux de bord et analyses |
| BPCO | Bronchopneumopathie chronique obstructive, maladie respiratoire chronique |
| CDA | Format standard des documents médicaux structurés, utilisé par le DMP |
| CERT-FR | Centre gouvernemental de veille et d'alerte sur les cyberattaques, rattaché à l'ANSSI |
| CERT Santé | Centre d'alerte et de réponse aux incidents de sécurité du secteur de la santé, rattaché à l'Agence du numérique en santé |
| CISP-2 | Classification internationale des soins primaires, utilisée en médecine de ville pour coder les motifs de consultation et les diagnostics |
| Client lourd | Logiciel installé sur chaque poste de travail, par opposition à une application web |
| CNIL | Autorité française de protection des données personnelles |
| CSV | Fichier texte en colonnes, lisible par un tableur |
| DICOM | Format standard des images médicales |
| DMP | Dossier médical partagé, accessible au patient dans Mon espace santé |
| DPI | Dossier patient informatisé : le logiciel métier des soignants (en ville, on parle aussi de logiciel métier) |
| DPO | Délégué à la protection des données |
| DSI | Direction des systèmes d'information |
| EDR | Outil de détection et de réponse aux menaces sur les postes et les serveurs |
| EHDS | Espace européen des données de santé : règlement européen de 2025 sur le partage et la réutilisation des données de santé |
| Empreinte numérique | Impact environnemental du numérique (fabrication des équipements, énergie, réseau), exprimé en kilogrammes d'équivalent CO2 |
| ERP | Progiciel de gestion intégré (comptabilité, achats) |
| ETAPES | Programme d'expérimentation qui a financé la télésurveillance de 2018 à 2023, avant son passage dans le droit commun |
| Forfait opérateur, forfait technique | Les deux forfaits de télésurveillance : le premier rémunère l'équipe qui surveille les patients, le second l'exploitant du dispositif médical |
| FSE | Feuille de soins électronique transmise à l'Assurance Maladie |
| HDS | Certification obligatoire pour héberger des données de santé pour le compte d'un tiers |
| HL7 FHIR | Norme internationale d'échange de données de santé par API |
| HPRIM Santé | Format d'échange des résultats de biologie entre laboratoires et logiciels médicaux |
| Hors support | Se dit d'un logiciel pour lequel l'éditeur ne publie plus de correctifs, y compris de sécurité |
| Identitovigilance | Organisation qui garantit qu'un patient est correctement identifié tout au long de sa prise en charge |
| INS, INSi | Identité nationale de santé, obligatoire pour référencer les données de santé d'un patient ; INSi est le téléservice qui permet de la récupérer et de la vérifier |
| Intégration continue | Pratique qui lance automatiquement la compilation et les tests à chaque modification du code |
| LATM | Liste des activités de télésurveillance médicale prises en charge par l'Assurance Maladie |
| MPLS | Réseau privé loué à un opérateur, qui relie les sites d'une organisation |
| MSSanté | Messageries sécurisées de santé, pour les échanges entre professionnels et avec les patients via Mon espace santé |
| NAS | Serveur de stockage en réseau |
| NIS2 | Directive européenne sur la cybersécurité des entités essentielles et importantes, dont la santé |
| NPS | Indicateur de recommandation : part des promoteurs moins part des détracteurs, de −100 à +100 |
| PACS | Système d'archivage et de diffusion des images médicales |
| Pro Santé Connect | Service d'authentification des professionnels de santé, avec leur carte CPS ou e-CPS |
| Product owner | Personne chargée de prioriser les besoins à développer dans une équipe agile |
| Régie | Prestation facturée au temps passé, réalisée sous la direction du client |
| Règlement sur les dispositifs médicaux | Règlement européen 2017/745 qui encadre la mise sur le marché des dispositifs médicaux, y compris des logiciels |
| RGPD | Règlement européen sur la protection des données personnelles |
| RIS | Logiciel de gestion d'un service d'imagerie (rendez-vous, comptes rendus) |
| RSSI | Responsable de la sécurité des systèmes d'information |
| SaaS | Logiciel loué sous forme d'abonnement, utilisé en ligne et maintenu par l'éditeur |
| Schéma directeur | Plan pluriannuel qui fixe la cible du SI, les projets, leur ordre et leur budget |
| SESAM-Vitale | Système de facturation électronique avec l'Assurance Maladie |
| Ségur du numérique en santé | Programme public qui finance le partage des données de santé (INS, DMP, MSSanté, ordonnance numérique) |
| SI | Système d'information : applications, données, infrastructures et processus numériques d'une organisation |
| SOC | Centre de supervision qui surveille les alertes de sécurité en continu |
| Télésurveillance médicale | Suivi à distance des patients chroniques, remboursé dans le droit commun depuis juillet 2023 |
| Tiers payant | Le patient n'avance pas les frais : le centre est payé directement par l'Assurance Maladie et, le cas échéant, par la complémentaire santé |
| VPN | Connexion chiffrée qui donne accès au réseau interne à distance |
| WCAG | Règles internationales d'accessibilité des contenus web ; le niveau AA est la référence habituelle |
