# FT 12 | Critères de sécurité et vocabulaire du risque | 5

@situation
En janvier 2026, vous êtes stagiaire à la DSI de Kestrel Logistique, auprès de Romain Chevalier, responsable de l'infrastructure et RSSI à temps partiel. Il prépare pour le comité de direction le bilan des incidents de 2025 et veut qu'il parle le langage du risque, et non celui des pannes. Il vous confie un extrait du journal des incidents, ses notes d'entretien et les durées d'interruption relevées. Vous devez qualifier chaque incident, puis décomposer les plus instructifs.

@capacites
Identifier le critère de sécurité atteint par un incident
Décomposer un incident en valeur métier, bien support, menace, vulnérabilité et impact
Calculer l'écart entre une interruption constatée et la durée tolérée
Distinguer menace, vulnérabilité, impact et mesure
Argumenter des besoins de sécurité

@duree 60 minutes

@annexe 1 | Ce que disent les métiers | Source fictive : notes d'entretien de Romain Chevalier, janvier 2026
Le responsable de l'agence de Clermont-Ferrand revient sur la coupure de novembre. « Les travaux de voirie, on ne les maîtrise pas. Le problème, c'est que l'agence n'a qu'une fibre : quand elle est coupée, nous n'avons plus RoutePro, puisque tout tourne au siège. Nous avons fait les lettres de voiture à la main, et 140 colis sont partis le lendemain. »

Sébastien Morin, directeur des opérations, évoque la contestation de novembre. « Les chauffeurs d'un même sous-traitant se passent le même identifiant KDriver. La photo et la signature étaient bien là, mais nous n'avons pas pu dire qui avait livré. Un sous-traitant pourrait très bien déclarer livré un colis qu'il a gardé. Nous avons dû faire un avoir de 420 €. »

Isabelle Roux, directrice administrative et financière, commente l'erreur de décembre. « Le compte générique du service comptable est utilisé par quatre personnes. Nous savons que la grille tarifaire a été modifiée, mais pas par qui. Les factures ont été rectifiées. Il faudrait que chacun ait son propre compte et que les modifications de tarifs soient tracées. »

@annexe 2 | Extrait du journal des incidents de 2025 | APP-11 Outil de tickets, extraction de janvier 2026
| N° | Mois | Élément touché | Ce qui s'est passé | Conséquence |
| --- | --- | --- | --- | --- |
| INC‑1 | Mars | APP-02 StockFlow | Panne chez l'éditeur : application inaccessible 3 h un matin | Préparation arrêtée à Saint-Priest et à Moirans ; 400 commandes livrées avec une demi-journée de retard |
| INC‑2 | Mai | APP-08 Paie | Erreur de ressaisie des temps de conduite tirés d'APP-05 TeleFleet (FLX-05) | 14 chauffeurs payés sur des heures fausses ; régularisation le mois suivant |
| INC‑3 | Juin | APP-10 Microsoft 365 | Fichier des tournées de Clermont-Ferrand envoyé par erreur à une adresse extérieure à Kestrel | Noms, adresses et téléphones de 870 destinataires exposés ; violation inscrite au registre interne |
| INC‑4 | Novembre | RES-02 VPN Clermont | Fibre coupée par des travaux de voirie ; aucun lien de secours | Agence privée d'APP-01 RoutePro pendant 7 h 30 ; 140 colis livrés le lendemain |
| INC‑5 | Novembre | APP-04 KDriver | Livraison de 3 colis contestée par un e-commerçant ; compte partagé par les chauffeurs d'un sous-traitant | Livreur impossible à identifier ; avoir de 420 € |
| INC‑6 | Décembre | APP-07 ERP finance | Grille tarifaire d'un client de la grande distribution modifiée par erreur avec le compte générique du service comptable | 212 factures émises à un tarif trop bas pendant 3 semaines, puis rectifiées |

@annexe 3 | Plus longue interruption constatée en 2025, par élément | Tableau de bord de la DSI, janvier 2026
@graphique barres heures
StockFlow : 3
Kestrel Track : 5
KDriver : 2
Portail EDI : 1,5
VPN Clermont : 7,5

@annexe 4 | Le chemin de l'agence de Clermont-Ferrand vers RoutePro | Extrait de la vue des infrastructures physiques, version 1.0
@schema
TRM-05 Postes de Clermont-Ferrand -> RES-02 VPN Clermont (fibre, 100 Mbit/s, sans secours) -> SAL-01 Salle serveur du siège -> SRV-01 Virtualisation 1 et SRV-02 Virtualisation 2 -> APP-01 RoutePro

@question 1 | Identifier | Annexe 2
Pour chacun des six incidents, indiquez le critère de sécurité principalement atteint (disponibilité, intégrité, confidentialité ou traçabilité) et justifiez-le en une phrase.
@tableau
| Incident | Critère atteint | Justification |
| --- | --- | --- |
| INC-1 | | |
| INC-2 | | |
| INC-3 | | |
| INC-4 | | |
| INC-5 | | |
| INC-6 | | |

@question 2 | Analyser | Annexes 1 et 2
INC-5 et INC-6 mettent tous deux en jeu la traçabilité. Expliquez pourquoi, en montrant ce qui distingue ce critère de l'intégrité. Quelle faiblesse commune ces deux incidents révèlent-ils ?
@lignes 5

@question 3 | Mobiliser | Annexes 1, 2 et 4
Décomposez INC-4 et INC-6 avec le vocabulaire du risque.
@tableau
| Notion | INC-4 Coupure de Clermont-Ferrand | INC-6 Erreur tarifaire |
| --- | --- | --- |
| Valeur métier atteinte | | |
| Bien support | | |
| Menace | | |
| Vulnérabilité | | |
| Impact | | |

@question 4 | Calculer | Annexe 3
Les directions tolèrent les arrêts suivants : StockFlow 4 h, Kestrel Track et KDriver 8 h, Portail EDI 4 h, RoutePro 2 h. Pour l'agence de Clermont-Ferrand, une coupure de RES-02 équivaut à un arrêt de RoutePro. Calculez la marge (durée tolérée moins interruption constatée) et la part de la durée tolérée consommée.
@tableau
| Élément | Interruption constatée (h) | Durée tolérée (h) | Marge (h) | Part consommée |
| --- | --- | --- | --- | --- |
| APP-02 StockFlow | | 4 | | |
| APP-03 Kestrel Track | | 8 | | |
| APP-04 KDriver | | 8 | | |
| APP-06 Portail EDI | | 4 | | |
| RES-02 VPN Clermont | | 2 | | |

@question 5 | Analyser | Annexes 1, 3 et 4
RES-02 VPN Clermont n'est pas une application, et c'est pourtant lui qui a le plus dépassé la durée tolérée. Expliquez pourquoi à l'aide du schéma. Cet élément est-il un point unique de défaillance ? Un incident de ce type relève-t-il des scénarios d'EBIOS Risk Manager ?
@lignes 6

@question 6 | Mobiliser | Annexe 1
Classez chacune des phrases suivantes, tirées des entretiens : menace, vulnérabilité, impact ou mesure ? Justifiez d'un mot.
@tableau
| Phrase | Classement et justification |
| --- | --- |
| « Les travaux de voirie, on ne les maîtrise pas. » | |
| « L'agence n'a qu'une fibre. » | |
| « Un sous-traitant pourrait déclarer livré un colis qu'il a gardé. » | |
| « Nous avons dû faire un avoir de 420 €. » | |
| « Le compte générique est utilisé par quatre personnes. » | |
| « Que chacun ait son propre compte. » | |

@question 7 | Argumenter | Toutes les annexes
Romain Chevalier doit coter les besoins de sécurité d'APP-04 KDriver de 1 (faible) à 4 (critique), dans l'ordre D, I, C, T. Proposez une cotation et argumentez-la, en vous appuyant sur les annexes et sur ce que vous savez de KDriver : tournée, preuve de livraison avec photo et signature, arrêt toléré de 8 heures.
@lignes 10

@retiens
La [[disponibilité]] est la propriété d'être accessible et utilisable au moment voulu par une personne autorisée ; l'[[intégrité]], celle d'être exact et complet ; la [[confidentialité]], celle de n'être accessible qu'aux personnes autorisées. La [[traçabilité]] est la capacité à retrouver qui a fait quoi et quand. Une [[menace]] est la cause potentielle d'un incident ; une [[vulnérabilité]] est une faiblesse qu'une menace peut exploiter. Le [[bien support]] est l'élément du SI sur lequel repose la [[valeur métier]], et l'[[impact]] est l'effet de l'incident sur l'organisation.

@corrige 1
| Incident | Critère atteint | Justification |
| --- | --- | --- |
| INC-1 | Disponibilité | StockFlow était intact mais inutilisable pendant 3 h. |
| INC-2 | Intégrité | Les heures saisies dans la paie étaient fausses : la donnée n'était plus exacte. |
| INC-3 | Confidentialité | Des données personnelles de destinataires ont été accessibles à une personne non autorisée. |
| INC-4 | Disponibilité | RoutePro fonctionnait, mais l'agence ne pouvait pas l'atteindre pendant 7 h 30. |
| INC-5 | Traçabilité | La preuve existe, mais on ne peut pas savoir quel chauffeur a agi. |
| INC-6 | Intégrité (traçabilité aussi atteinte) | Les tarifs ont été faussés ; de plus, l'auteur de la modification est inconnu. |

Le critère se déduit de la conséquence, non de la cause : INC-3 n'arrête rien, mais expose des données. INC-3 est en outre une violation de données au sens du RGPD, d'où son inscription au registre. Notion : critères de sécurité DICT (chapitre 5, section « Ce que la sécurité protège : les critères de sécurité »).

@corrige 2
La traçabilité est la capacité à retrouver qui a fait quoi et quand ; l'intégrité est la propriété d'être exact et complet. Dans INC-5, la preuve de livraison est intacte : la photo et la signature existent. L'intégrité n'est donc pas en cause au premier chef. Ce qui manque, c'est l'imputation : on ne sait pas quel chauffeur a livré. Dans INC-6, la grille a été altérée (intégrité), et l'on ne sait pas qui l'a modifiée (traçabilité).

La faiblesse commune est le compte partagé : un identifiant KDriver pour les chauffeurs d'un sous-traitant, et un compte générique pour quatre personnes dans l'ERP finance. Le journal établit le premier pour un seul sous-traitant ; l'hypothèse H10 du registre, plus large, garde son numéro et cite cette source. Un journal enregistre un compte, pas une personne : avec un compte partagé, la journalisation ne prouve plus rien. La mesure typique associe des comptes nominatifs et une journalisation horodatée (chapitre 5, tableau des critères).

@corrige 3
| Notion | INC-4 Coupure de Clermont-Ferrand | INC-6 Erreur tarifaire |
| --- | --- | --- |
| Valeur métier atteinte | Processus « Trier et préparer » (lettres de voiture) et « Livrer et prouver la livraison » à l'agence de Clermont-Ferrand | Processus « Facturer le client » ; information : les tarifs du client |
| Bien support | RES-02 VPN Clermont, par lequel l'agence atteint APP-01 RoutePro | APP-07 ERP finance (grille tarifaire) ; compte générique du service comptable |
| Menace | Accident : des travaux de voirie coupent la fibre (aucune intention malveillante) | Erreur humaine d'un utilisateur du service comptable |
| Vulnérabilité | Aucun lien de secours ; RoutePro accessible seulement par le siège | Compte partagé par quatre personnes ; aucune trace ni contrôle des modifications de tarifs |
| Impact | 7 h 30 sans RoutePro, lettres de voiture à la main, 140 colis livrés le lendemain | 212 factures fausses pendant 3 semaines, rectification, image atteinte auprès d'un grand client |

La décomposition montre où agir : on ne supprime ni les travaux de voirie ni l'erreur humaine, mais on peut traiter la vulnérabilité (lien de secours, comptes nominatifs) ou réduire l'impact (procédure dégradée). Notion : vocabulaire du risque, chapitre 5, section « Le vocabulaire du risque ».

@corrige 4
| Élément | Interruption constatée (h) | Durée tolérée (h) | Marge (h) | Part consommée |
| --- | --- | --- | --- | --- |
| APP-02 StockFlow | 3 | 4 | 1 | 75 % |
| APP-03 Kestrel Track | 5 | 8 | 3 | 62,5 % |
| APP-04 KDriver | 2 | 8 | 6 | 25 % |
| APP-06 Portail EDI | 1,5 | 4 | 2,5 | 37,5 % |
| RES-02 VPN Clermont | 7,5 | 2 | − 5,5 | 375 % |

Calculs : marge = durée tolérée − interruption ; part consommée = interruption ÷ durée tolérée, par exemple 3 ÷ 4 = 0,75 et 7,5 ÷ 2 = 3,75. Seule la coupure de RES-02 dépasse la durée tolérée, de 5 h 30 : l'interruption a duré près de quatre fois la durée admise. StockFlow a consommé les trois quarts de sa durée tolérée : un incident d'une heure de plus l'aurait dépassée. Les durées tolérées sont les besoins de disponibilité exprimés par les directions (chapitre 5 ; DMIA, chapitre 8).

@corrige 5
Le schéma montre une chaîne en série : les postes de l'agence n'atteignent RoutePro qu'à travers RES-02, puis la salle serveur du siège. RoutePro n'a pas été arrêté, mais pour l'agence, perdre le lien revient à perdre l'application. L'arrêt toléré de RoutePro, 2 heures, s'applique donc au lien, même si personne ne l'a exprimé pour lui.

RES-02 est un point unique de défaillance : sa panne suffit à arrêter un service, et il n'existe pas d'autre chemin (chapitre 4, définition ; l'exemple du chapitre 4 le signale déjà sur la vue physique). On peut discuter avec les métiers si 2 heures est le bon seuil pour une seule agence, mais l'incident a eu un effet réel sur les livraisons.

La menace est accidentelle. EBIOS Risk Manager consacre ses scénarios des ateliers 2 à 4 aux attaques ; une panne ou un accident relève du socle de sécurité de l'atelier 1, et surtout de l'analyse d'impact et de la continuité (chapitre 5, fin de la section « Le vocabulaire du risque » ; chapitre 8). Elle se traite par un lien de secours ou par une procédure dégradée écrite.

@corrige 6
| Phrase | Classement et justification |
| --- | --- |
| « Les travaux de voirie, on ne les maîtrise pas. » | Menace : cause potentielle de l'incident, accidentelle et extérieure |
| « L'agence n'a qu'une fibre. » | Vulnérabilité : faiblesse qui permet à la menace de produire l'arrêt |
| « Un sous-traitant pourrait déclarer livré un colis qu'il a gardé. » | Menace : cause potentielle, cette fois malveillante |
| « Nous avons dû faire un avoir de 420 €. » | Impact : effet mesuré sur l'organisation |
| « Le compte générique est utilisé par quatre personnes. » | Vulnérabilité : faiblesse d'une mesure de sécurité, l'identification |
| « Que chacun ait son propre compte. » | Mesure : action qui traite la vulnérabilité |

Une menace sans vulnérabilité reste théorique ; une vulnérabilité sans menace crédible reste dormante (chapitre 5, définition « Menace et vulnérabilité »).

@corrige 7
Cotation attendue : D 2, I 3, C 3, T 4 ; des écarts d'un niveau sont acceptés s'ils sont argumentés.

La disponibilité vaut 2 : les directions tolèrent 8 heures d'arrêt, comme pour Kestrel Track, cotée 2 en disponibilité dans l'inventaire de l'exemple du cours. Un arrêt court se contourne : le chauffeur livre et fait signer sur papier. L'intégrité vaut 3 : une preuve de livraison fausse entraîne des litiges et des avoirs, et ses statuts alimentent le suivi des clients. La confidentialité vaut 3 : KDriver porte les noms, adresses, photos et signatures des destinataires, données personnelles soumises au RGPD. La traçabilité vaut 4 : la valeur d'une preuve de livraison tient tout entière dans la capacité à dire qui a livré, où et quand. INC-5 montre qu'une preuve non imputable ne protège pas Kestrel dans un litige.

Barème indicatif sur 10 points : cotation de la disponibilité cohérente avec les 8 heures et l'échelle de l'inventaire (2 points) ; intégrité justifiée par un impact (2 points) ; confidentialité justifiée par les données personnelles (2 points) ; traçabilité reliée à INC-5 et aux comptes partagés (3 points) ; expression (1 point). Notion : besoins de sécurité, chapitre 4, définition « Besoins de sécurité (DICT) », et chapitre 5.

# FT 13 | Coter un risque : échelles, matrice et options de traitement | 5

@situation
En mars 2026, Isabelle Roux, directrice administrative et financière, prépare le comité de direction. Romain Chevalier lui a signalé quatre risques qui sortent du périmètre de l'étude de risques en cours : deux touchent la paie, un le site web, un StockFlow. Vous êtes son assistant en alternance. Elle vous demande de les coter avec les échelles de Kestrel, de les placer sur la matrice et de préparer les décisions de traitement.

@capacites
Lire une échelle de gravité et une échelle de vraisemblance
Coter un risque en citant le descripteur qui justifie le niveau
Lire la matrice et appliquer le seuil d'acceptation
Choisir une option de traitement et désigner qui décide

@duree 60 minutes

@annexe 1 | Échelle de gravité de Kestrel Logistique | Étude des risques de Kestrel Logistique, version 1.0 ; échelle construite avec la DAF et le directeur des opérations
| Niveau | Livraisons et clients | Finances | Juridique et conformité | Image et personnes |
| --- | --- | --- | --- | --- |
| G1 Mineure | Retard de moins de 2 h sur l'affectation des tournées, sans colis livré en retard | Moins de 10 k€ | Aucune suite | Aucun effet visible à l'extérieur |
| G2 Significative | Tournées perturbées moins d'une journée ; jusqu'à 3 000 colis en retard ; pénalités ponctuelles | 10 à 100 k€ | Manquement contractuel isolé | Réclamations de clients, sans perte de client |
| G3 Grave | Tournées perturbées d'une journée entière à 3 jours, ou sur un site entier ; plus de 3 000 colis en retard ; fuite de données de destinataires | 100 k€ à 1,3 M€ | Notification à la CNIL, contrôle ou mise en demeure | Article dans la presse régionale ; client qui suspend ses commandes |
| G4 Critique | Arrêt des livraisons de plus de 3 jours sur tout le réseau | Plus de 1,3 M€, soit une année de marge | Sanction lourde, mise en cause pénale de la direction | Perte d'un client de la grande distribution ; atteinte à la sécurité d'un salarié |

Une seule dimension atteinte suffit à classer l'événement à ce niveau.

@annexe 2 | Quatre risques à coter | Source fictive : note de Romain Chevalier à Isabelle Roux, mars 2026
RA. Un escroc se fait passer pour un salarié et demande par courriel au service paie de changer son RIB. Aucun contre-appel n'est prévu. En janvier 2026, un salaire de 2 400 € a ainsi été versé sur un faux compte ; Kestrel a payé le salarié une seconde fois. L'affaire n'a eu aucun écho à l'extérieur.

RB. Un attaquant hameçonne la gestionnaire de paie et se connecte à son compte d'APP-08 Paie, protégé par un simple mot de passe : le prestataire propose l'authentification multifacteur, mais elle n'a jamais été activée. Il télécharge les bulletins des 300 salariés, avec salaires, RIB et numéros de sécurité sociale. Une telle fuite devrait être notifiée à la CNIL. Les kits d'hameçonnage qui imitent une page de connexion se vendent à bas prix.

RC. Le formulaire de devis d'APP-12 Site web repose sur une extension du CMS dont une faille critique a été publiée en février 2026. Elle n'est pas corrigée : le contrat de maintenance de l'agence web qui a créé le site a pris fin en 2024. Un attaquant pourrait détourner le formulaire vers une page frauduleuse. Effet estimé : des réclamations de clients et moins de 10 k€ de pertes.

RD. Un groupe cybercriminel chiffre la plateforme de PP-06 Éditeur de StockFlow : la préparation serait arrêtée deux jours à Saint-Priest et à Moirans. L'éditeur déclare un SMSI certifié ISO/IEC 27001 ; aucune vulnérabilité de son service n'est connue.

@annexe 3 | Vraisemblance, matrice et seuil d'acceptation | Étude des risques de Kestrel Logistique, version 1.0
| Niveau | Descripteur |
| --- | --- |
| V1 Peu vraisemblable | L'attaquant doit lever plusieurs protections efficaces, avec des moyens importants, ou employer une vulnérabilité non publique ; aucune vulnérabilité connue n'est exposée |
| V2 Vraisemblable | L'attaque demande un savoir-faire réel et la combinaison de plusieurs faiblesses ; des mesures existent mais présentent des faiblesses |
| V3 Très vraisemblable | L'attaque exploite une faiblesse connue et documentée, avec des outils disponibles ; peu de mesures la ralentissent |
| V4 Quasi certain | L'attaque est à la portée d'un attaquant peu qualifié ; la faiblesse est publique, exposée et non corrigée, ou le scénario s'est déjà produit |

| Gravité / Vraisemblance | V1 | V2 | V3 | V4 |
| --- | --- | --- | --- | --- |
| G4 Critique | Élevé | Critique | Critique | Critique |
| G3 Grave | Moyen | Élevé | Élevé | Critique |
| G2 Significative | Faible | Moyen | Moyen | Élevé |
| G1 Mineure | Faible | Faible | Faible | Moyen |

Un risque faible peut être accepté par le responsable de l'infrastructure ; un risque moyen par le comité de direction, avec un motif écrit ; un risque élevé ou critique doit être traité. Tant que son traitement est en cours, un risque élevé ne peut être accepté que temporairement, par le directeur général, avec une mesure compensatoire et une date de réexamen.

@annexe 4 | Demandes de changement de RIB reçues par le service paie | Source fictive : registre du service paie ; cinq de ces demandes se sont révélées frauduleuses
@graphique barres demandes
Septembre 2025 : 2
Octobre 2025 : 1
Novembre 2025 : 3
Décembre 2025 : 2
Janvier 2026 : 4
Février 2026 : 3

@question 1 | Calculer | Annexe 1
Retrouvez par le calcul le seuil de 1,3 M€ à partir du chiffre d'affaires 2025 de Kestrel (42 M€) et de sa marge opérationnelle (3,1 %). Pourquoi ancrer les seuils financiers sur la marge plutôt que sur le chiffre d'affaires ?
@lignes 4

@question 2 | Calculer | Annexes 2 et 4
Calculez le nombre total de demandes de changement de RIB sur la période, la moyenne mensuelle et la part des demandes frauduleuses. Que traduisent ces chiffres pour la vraisemblance du risque RA ?
@lignes 4

@question 3 | Mobiliser | Annexes 1, 2 et 3
Cotez la gravité et la vraisemblance des quatre risques en citant le descripteur qui justifie chaque niveau, puis lisez le niveau de risque sur la matrice.
@tableau
| Risque | Gravité et descripteur | Vraisemblance et descripteur | Niveau de risque |
| --- | --- | --- | --- |
| RA Faux RIB d'un salarié | | | |
| RB Vol des données de paie | | | |
| RC Formulaire du site web détourné | | | |
| RD StockFlow chiffré chez l'éditeur | | | |

@question 4 | Analyser | Annexe 3
RA est quasi certain, RD peu vraisemblable, et ils obtiennent pourtant le même niveau. Expliquez-le par la construction de la matrice. Quel niveau obtiendrait un risque G4 et V1 ? Que traduit ce choix de Kestrel ?
@lignes 5

@question 5 | Mobiliser | Annexes 2 et 3
Pour chaque risque, choisissez une option de traitement (réduire, transférer, éviter, accepter), proposez une mesure s'il y a lieu et indiquez ce que permet le seuil d'acceptation.
@tableau
| Risque | Option | Mesure proposée | Ce que permet le seuil |
| --- | --- | --- | --- |
| RA | | | |
| RB | | | |
| RC | | | |
| RD | | | |

@question 6 | Calculer | Annexes 2 et 3
On active l'authentification multifacteur d'APP-08 Paie (RB) et un contre-appel au numéro connu du salarié avant tout changement de RIB (RA). Romain Chevalier estime que la vraisemblance de RB tombe à V1 et celle de RA à V2. Lisez le niveau résiduel de chaque risque et dites qui peut l'accepter. Pourquoi la gravité ne change-t-elle pas ?
@lignes 5

@question 7 | Argumenter | Toutes les annexes
En comité, Paul Vidal propose de « classer RB en risque accepté, puisque la paie est externalisée et que le prestataire est responsable ». Rédigez la réponse argumentée d'Isabelle Roux.
@lignes 9

@retiens
La gravité se lit sur l'[[échelle de gravité]] : une seule [[dimension]] atteinte suffit à classer l'événement. La vraisemblance exprime la [[facilité]] avec laquelle un attaquant réussirait ; ce n'est pas une prédiction. La [[matrice]] croise les deux et donne le niveau de risque ; le [[seuil d'acceptation]], fixé par la direction avant l'analyse, dit quels risques doivent être traités. Les quatre options sont [[réduire]], [[transférer]], [[éviter]] et [[accepter]] ; une acceptation est une décision [[écrite]], motivée et prise par un responsable qui en a l'autorité.

@corrige 1
Calcul : 42 M€ × 3,1 % = 42 × 0,031 = 1,302 M€, soit environ 1,3 M€ : une année de marge opérationnelle. La marge mesure ce que l'entreprise peut perdre sans entamer ses réserves ; le chiffre d'affaires ne le dit pas. Un seuil de 1 % du chiffre d'affaires, 420 k€, paraîtrait faible, alors qu'il représente près d'un tiers de la marge annuelle d'une entreprise à 3,1 %. Ancrer les seuils sur des repères chiffrés de l'organisation est l'étape 3 de la méthode de construction des échelles (chapitre 5, section « Construire des échelles de gravité et de vraisemblance »).

@corrige 2
Total : 2 + 1 + 3 + 2 + 4 + 3 = 15 demandes en six mois, soit 15 ÷ 6 = 2,5 par mois. Part frauduleuse : 5 ÷ 15 ≈ 0,33, soit une demande sur trois. Les demandes augmentent en janvier et en février 2026.

Ces chiffres montrent que la menace est active et répétée, et l'annexe 2 indique qu'une fraude a réussi en janvier 2026. Le descripteur de V4 s'applique : « le scénario s'est déjà produit », et l'attaque, un simple courriel, est à la portée d'un attaquant peu qualifié. La vraisemblance n'est pas une probabilité calculée : ces chiffres justifient le niveau, ils ne le remplacent pas (chapitre 5, section « Le vocabulaire du risque »).

@corrige 3
| Risque | Gravité et descripteur | Vraisemblance et descripteur | Niveau de risque |
| --- | --- | --- | --- |
| RA Faux RIB d'un salarié | G1 : 2 400 €, moins de 10 k€ ; aucun effet visible à l'extérieur | V4 : le scénario s'est déjà produit ; attaque à la portée d'un attaquant peu qualifié | G1 × V4 : Moyen |
| RB Vol des données de paie | G3 : fuite de données personnelles de 300 salariés, notification à la CNIL (dimension juridique) | V3 : faiblesse connue et documentée (mot de passe seul), outils disponibles (kits d'hameçonnage), peu de mesures la ralentissent | G3 × V3 : Élevé |
| RC Formulaire du site web détourné | G2 : réclamations de clients, sans perte de client (dimension image), même si les pertes restent sous 10 k€ | V4 : faille publique, exposée sur Internet et non corrigée | G2 × V4 : Élevé |
| RD StockFlow chiffré chez l'éditeur | G3 : préparation perturbée deux jours sur deux sites, « d'une journée entière à 3 jours, ou sur un site entier » | V1 : plusieurs protections efficaces à lever ; aucune vulnérabilité connue n'est exposée | G3 × V1 : Moyen |

Pour RC, la dimension financière donnerait G1, mais la dimension image donne G2 : c'est la dimension la plus haute qui l'emporte. Pour RB, V4 n'est pas retenu : le mot de passe seul n'est pas une faille publiée et exposée, et le scénario ne s'est pas encore produit ; un élève qui retient V4 doit citer un descripteur, mais obtient alors un risque critique peu défendable. Notion : échelles et matrice de Kestrel (chapitre 5, section « Construire des échelles de gravité et de vraisemblance »).

@corrige 4
La matrice n'est pas symétrique. La ligne G1 ne dépasse jamais le niveau moyen, même quasi certaine ; la ligne G3 est déjà moyenne en V1. RA et RD arrivent donc au même niveau par deux chemins opposés : l'un est fréquent et peu coûteux, l'autre rare et lourd. Un risque G4 et V1 serait élevé : il devrait être traité, alors même qu'il est peu vraisemblable.

Ce choix traduit l'aversion de Kestrel pour l'arrêt total de ses livraisons : on préfère traiter un désastre improbable qu'ignorer sa possibilité. Il est assumé et écrit. Deux risques de même niveau n'appellent pas pour autant la même réponse : RA se réduit par une mesure simple, RD se gère surtout par le contrat et la continuité (chapitre 5, commentaire de la matrice).

@corrige 5
| Risque | Option | Mesure proposée | Ce que permet le seuil |
| --- | --- | --- | --- |
| RA | Réduire | Contre-appel obligatoire au numéro connu du salarié avant tout changement de RIB | Moyen : le comité de direction pourrait l'accepter avec un motif écrit ; la mesure est si peu coûteuse que la réduction s'impose |
| RB | Réduire | Activer l'authentification multifacteur proposée par le prestataire ; sensibiliser la gestionnaire | Élevé : doit être traité ; acceptation seulement temporaire, par le directeur général, avec mesure compensatoire et date de réexamen |
| RC | Réduire, ou éviter | Mettre à jour ou retirer l'extension ; reprendre un contrat de maintenance ; ou supprimer le formulaire au profit d'une simple adresse de contact (éviter) | Élevé : doit être traité |
| RD | Accepter, avec un transfert partiel | Vérifier dans le contrat de l'éditeur ses engagements de reprise et sa responsabilité ; écrire un mode dégradé de préparation | Moyen : acceptable par le comité de direction, avec un motif écrit |

On accepte d'autres choix argumentés, par exemple « réduire » pour RD par un mode dégradé. Le transfert ne porte que sur l'impact financier, jamais sur l'arrêt de la préparation (chapitre 5, section « Risque inhérent, initial et résiduel ; options de traitement »).

@corrige 6
RB passe de G3 × V3 à G3 × V1 : risque moyen, qui peut être accepté par le comité de direction avec un motif écrit. RA passe de G1 × V4 à G1 × V2 : risque faible, que le responsable de l'infrastructure peut accepter. La gravité ne change pas, car ces deux mesures sont des mesures de protection : elles rendent l'attaque plus difficile, mais si elle réussit, les conséquences restent les mêmes (fuite de 300 dossiers, salaire détourné). Seule une mesure qui limite les conséquences ferait baisser la gravité. Le risque résiduel n'est jamais nul et doit être accepté explicitement (chapitre 5, définition « Risque initial et risque résiduel »).

@corrige 7
Éléments attendus. RB est un risque élevé (G3 × V3) : selon le seuil fixé par la direction elle-même, il doit être traité. L'accepter tel quel serait un risque ignoré, pas un risque accepté. Externaliser n'est pas transférer : le prestataire de paie traite les données pour le compte de Kestrel, qui reste responsable du traitement au sens du RGPD et devrait notifier la fuite à la CNIL. De plus, la faiblesse est chez Kestrel : c'est Kestrel qui n'a pas activé l'authentification multifacteur. Un transfert, par contrat ou par assurance, ne couvrirait que l'impact financier, jamais l'atteinte aux salariés ni à l'image. La mesure est disponible, puisque le prestataire la propose, et elle ramène le risque au niveau moyen. Si le traitement ne pouvait être immédiat, seule une acceptation temporaire serait possible, signée par le directeur général, avec une mesure compensatoire et une date de réexamen.

Barème indicatif sur 8 points : niveau élevé et règle du seuil (2 points) ; distinction entre externaliser et transférer, responsabilité de Kestrel (2 points) ; mesure disponible et risque résiduel (2 points) ; acceptation temporaire et ses conditions (1 point) ; ton adapté à un directeur général (1 point). Notion : chapitre 5, encadré « Accepter n'est pas oublier ».

# FT 14 | EBIOS RM, ateliers 1 et 2 : ce que l'on protège et qui menace | 6

@situation
En avril 2026, Hélène Garnier, directrice des SI, lance une étude EBIOS Risk Manager complémentaire sur l'activité e-commerce, que le plan « Cap 2029 » doit porter à 40 % du chiffre d'affaires. L'étude principale couvrait le transport et la livraison ; celle-ci couvre le stockage, la préparation et la facturation des commandes des e-commerçants. Romain Chevalier anime les ateliers 1 et 2, et vous préparez les tableaux.

@capacites
Identifier des valeurs métier et les relier à leurs biens supports
Formuler un événement redouté et coter sa gravité
Évaluer des couples source de risque et objectif visé
Justifier la sélection et l'exclusion des couples par des faits

@duree 75 minutes

@annexe 1 | Entretien à l'entrepôt de Moirans | Source fictive : compte rendu de Romain Chevalier, validé par Sébastien Morin, avril 2026
L'entrepôt de Moirans stocke les marchandises de 18 e-commerçants et prépare environ 1 800 commandes par jour. Les commandes arrivent des sites marchands dans APP-02 StockFlow par un connecteur de l'éditeur. Les agents scannent chaque article ; selon l'administrateur, le trafic de Moirans vers StockFlow passe par RES-01 VPN Moirans, puis par la sortie Internet du siège.

Les 30 agents permanents ont un compte StockFlow nominatif. Les intérimaires, jusqu'à 20 en été et en fin d'année, se partagent quatre comptes génériques. « En 2025, des smartphones ont été préparés, puis n'ont jamais été livrés. Avec les comptes génériques, impossible de savoir qui les a scannés », explique le responsable de l'entrepôt. Ces produits valent en moyenne 600 € pièce.

Les contrats des e-commerçants comportent une clause de confidentialité sur leurs volumes de vente. La facturation relève de la valeur métier VM5 de l'étude principale, « Facturer le client et payer les fournisseurs » : APP-07 ERP finance émet les factures mensuelles, que le service facturation envoie en PDF depuis sa boîte d'APP-10 Microsoft 365. Le plus gros e-commerçant reçoit une facture d'environ 140 k€ par mois.

@annexe 2 | Objets de la cartographie dans le périmètre | Extrait de l'inventaire de la DSI, version 1.0
| Objet | Rôle dans le périmètre | Lieu ou hébergement |
| --- | --- | --- |
| APP-02 StockFlow | Réception, stockage, préparation ; connecteur des sites marchands | SaaS de PP-06 Éditeur de StockFlow, en France |
| TRM-01 Scanners des quais | Lecture des articles à la réception et à la préparation | Quais des trois sites ; ici, ceux de Moirans |
| RES-03 Wi-Fi des quais | Relie les scanners au réseau | Quais |
| RES-01 VPN Moirans | Fibre de 300 Mbit/s vers le siège, sans secours | Entre SITE-02 Moirans et SITE-01 Saint-Priest |
| TRM-04 Postes de Moirans | Bureau de l'entrepôt : suivi des stocks, étiquettes | SITE-02 Moirans |
| APP-07 ERP finance | Facturation mensuelle des e-commerçants | SAL-01 Salle serveur du siège |
| APP-10 Microsoft 365 | Messagerie du service facturation | SaaS de PP-09 Microsoft |

@annexe 3 | Échelle de gravité (extrait) | Étude des risques de Kestrel Logistique, version 1.0
| Niveau | Livraisons et clients | Finances | Juridique, conformité, image et personnes |
| --- | --- | --- | --- |
| G1 Mineure | Retard de moins de 2 heures sur l'affectation des tournées, sans colis livré en retard | Moins de 10 k€ | Aucune suite ; aucun effet visible à l'extérieur |
| G2 Significative | Tournées perturbées moins d'une journée ; jusqu'à 3 000 colis en retard ; pénalités ponctuelles | 10 à 100 k€ | Manquement contractuel isolé ; réclamations de clients, sans perte de client |
| G3 Grave | Tournées perturbées d'une journée entière à 3 jours, ou sur un site entier ; plus de 3 000 colis en retard ; fuite de données de destinataires | 100 k€ à 1,3 M€ | Notification à la CNIL, contrôle ou mise en demeure ; article dans la presse régionale ; client qui suspend ses commandes |
| G4 Critique | Arrêt des livraisons de plus de 3 jours sur tout le réseau | Plus de 1,3 M€, soit une année de marge | Sanction lourde, mise en cause pénale de la direction ; perte d'un client de la grande distribution ; atteinte à la sécurité d'un salarié |

@annexe 4 | Colis de valeur préparés à Moirans mais jamais livrés, en 2025 | Source fictive : rapprochement des stocks, direction des opérations, janvier 2026
@graphique barres colis
1er trimestre : 4
2e trimestre : 3
3e trimestre : 9
4e trimestre : 7

@annexe 5 | Ce que dit la veille | Source fictive : note de veille de Romain Chevalier, avril 2026
Le panorama de la cybermenace de l'ANSSI compte les PME et les ETI parmi les premières victimes des rançongiciels. Cybermalveillance.gouv.fr décrit des fraudes au changement de coordonnées bancaires et des SMS frauduleux « colis en attente », qui exploitent des noms et des adresses de destinataires.

En février 2026, un e-commerçant client a reçu un courriel imitant le service facturation de Kestrel, qui lui demandait de régler sa facture sur un nouveau RIB. Il a rappelé Kestrel, et la fraude a échoué. Aucun indice d'espionnage par un concurrent n'est connu, ni aucun sabotage par un intérimaire.

@question 1 | Identifier | Annexes 1 et 2
Formulez les valeurs métier du périmètre et reliez chacune à ses biens supports, sous leur nom de cartographie.
@tableau
| N° et nature | Valeur métier formulée | Biens supports, sous leur nom de cartographie |
| --- | --- | --- |
| VM6 Processus | | |
| VM7 Information | | |
| VM5 Processus repris | | |

@question 2 | Analyser | Annexes 1 et 2
Quel bien support sert plusieurs valeurs métier, et pourquoi est-ce un signal d'alerte ? Pourquoi RES-01 VPN Moirans est-il un bien support de la préparation, alors que StockFlow est un SaaS ?
@lignes 5

@question 3 | Mobiliser | Annexe 1
Un participant propose l'événement redouté « Piratage de StockFlow par un intérimaire ». Expliquez pourquoi cette formulation ne convient pas et reformulez-la.
@lignes 4

@question 4 | Calculer | Annexes 1 et 4
Calculez le nombre de colis de valeur manquants en 2025, leur valeur et la part du second semestre. Quel lien faites-vous avec l'organisation du travail décrite en annexe 1 ?
@lignes 4

@question 5 | Mobiliser | Annexes 1, 3 et 4
Complétez le tableau des événements redoutés. Posez les calculs et citez le descripteur de l'échelle qui justifie la gravité.
@tableau
| Événement redouté | Valeur métier | Critère atteint | Impacts chiffrés, calculs posés | Gravité et descripteur cité |
| --- | --- | --- | --- | --- |
| ER7 Préparation impossible à Moirans pendant deux jours | | | | |
| ER8 Colis de valeur non livrés, au rythme de 2025 | | | | |
| ER9 Volumes d'un e-commerçant divulgués à un concurrent | | | | |
| ER10 Paiement mensuel du plus gros e-commerçant détourné | | | | |

@question 6 | Calculer | Annexes 1, 4 et 5
Atelier 2 : cotez l'activité de chaque source de 1 (faible) à 3 (forte), calculez la somme et la pertinence (élevée de 8 à 9, moyenne de 6 à 7, faible en dessous), puis indiquez si le couple est retenu (pertinence moyenne ou élevée).
@tableau
| Couple source de risque / objectif visé | Motivation | Ressources | Activité | Somme | Pertinence | Retenu |
| --- | --- | --- | --- | --- | --- | --- |
| SR7 Groupe cybercriminel / extorquer une rançon en bloquant la préparation | 3 | 3 | | | | |
| SR8 Réseau de voleurs avec un complice interne / détourner des colis de valeur | 3 | 2 | | | | |
| SR9 Escroc / détourner les paiements des e-commerçants par un faux RIB | 3 | 2 | | | | |
| SR10 Concurrent d'un e-commerçant / obtenir ses volumes de vente | 2 | 1 | | | | |
| SR11 Intérimaire mécontent / saboter le stock | 2 | 1 | | | | |
| SR12 Cybercriminel / voler les adresses des clients finaux | 2 | 2 | | | | |

@question 7 | Argumenter | Toutes les annexes
SR11 est écarté. Rédigez la justification de cette exclusion, puis montrez que la question des comptes génériques ne disparaît pas pour autant : où et comment l'étude doit-elle la reprendre ?
@lignes 8

@retiens
Une [[valeur métier]] est un processus ou une information essentiels à la mission ; un [[bien support]] est l'élément du SI sur lequel elle repose, nommé comme dans la cartographie. Un [[événement redouté]] décrit la conséquence pour le métier, jamais l'attaquant ni le moyen ; sa [[gravité]] se lit sur l'échelle. À l'atelier 2, on évalue chaque couple [[source de risque]] et [[objectif visé]] selon la motivation, les [[ressources]] et l'[[activité]], puis on retient les plus pertinents en justifiant chaque choix, et chaque [[exclusion]], par un fait.

@corrige 1
| N° et nature | Valeur métier formulée | Biens supports, sous leur nom de cartographie |
| --- | --- | --- |
| VM6 Processus | Préparer les commandes e-commerce | APP-02 StockFlow ; TRM-01 Scanners des quais ; RES-03 Wi-Fi des quais ; RES-01 VPN Moirans et la sortie Internet du siège ; TRM-04 Postes de Moirans ; agents d'entrepôt et intérimaires |
| VM7 Information | Données de stock des e-commerçants (articles, quantités, mouvements, volumes de vente) | APP-02 StockFlow, dont les données sont chez PP-06 Éditeur de StockFlow ; TRM-01 Scanners des quais ; TRM-04 Postes de Moirans ; comptes StockFlow, dont les quatre comptes génériques |
| VM5 Processus repris | Facturer le client et payer les fournisseurs, volet e-commerçants | APP-07 ERP finance (SAL-01 Salle serveur du siège) ; APP-10 Microsoft 365, messagerie du service facturation ; service facturation |

Les personnes sont désignées par leur fonction, les autres biens supports par leur nom de cartographie, identifiant compris. La sortie Internet du siège n'a pas d'identifiant dans l'extrait : il faut la créer dans la cartographie avant de la citer (chapitre 6, définition « Valeur métier et bien support »). Reprendre VM5 plutôt que créer une valeur nouvelle garde l'étude cohérente : la facturation des e-commerçants est un volet d'un processus déjà analysé.

@corrige 2
APP-02 StockFlow sert à la fois VM6 et VM7 ; TRM-01 et TRM-04 aussi. Un bien support qui sert plusieurs valeurs métier concentre le risque : une seule atteinte touche plusieurs activités (chapitre 6, atelier 1).

StockFlow est hébergé chez l'éditeur, mais Moirans ne l'atteint qu'à travers RES-01, sans secours, puis la sortie Internet du siège. Une coupure du lien, ou une panne du réseau du siège, arrête la préparation à Moirans alors que StockFlow fonctionne. C'est une dépendance cachée, que seule la cartographie révèle : un SaaS n'est pas indépendant du réseau interne. Le fait repose sur une déclaration de l'administrateur : il faut le vérifier, ou l'écrire comme hypothèse numérotée.

@corrige 3
La formulation décrit une source de risque (l'intérimaire) et un mode opératoire (le piratage), pas une conséquence pour le métier. Or un événement redouté est l'atteinte à un critère de sécurité d'une valeur métier, formulée du point de vue du métier (chapitre 6, définition « Événement redouté » et tableau des erreurs fréquentes). Reformulations acceptées : « le stock d'un e-commerçant est faussé : des articles sortent sans être livrés » (intégrité, VM7), ou « la préparation des commandes e-commerce est impossible à Moirans pendant deux jours » (disponibilité, VM6). L'intérimaire relève de l'atelier 2, le moyen de l'atelier 4.

@corrige 4
Total : 4 + 3 + 9 + 7 = 23 colis. Valeur : 23 × 600 € = 13 800 €. Second semestre : 9 + 7 = 16 colis, soit 16 ÷ 23 ≈ 0,70, environ 70 %.

Les pertes se concentrent sur les périodes où les intérimaires sont les plus nombreux, l'été et la fin d'année, et où ils partagent quatre comptes génériques. La coïncidence ne prouve pas leur responsabilité : les volumes sont aussi plus élevés à ces périodes. Elle montre surtout qu'on ne peut rien prouver, faute de traçabilité.

@corrige 5
| Événement redouté | Valeur métier | Critère atteint | Impacts chiffrés, calculs posés | Gravité et descripteur cité |
| --- | --- | --- | --- | --- |
| ER7 Préparation des commandes e-commerce impossible à Moirans pendant deux jours | VM6 | Disponibilité | 2 × 1 800 = 3 600 commandes en retard ; un site entier ; deux jours | G3 : « d'une journée entière à 3 jours, ou sur un site entier ; plus de 3 000 colis en retard » |
| ER8 Colis de valeur sortis du stock sans être livrés, au rythme de 2025 | VM7 | Intégrité | 23 × 600 € = 13 800 € par an ; réclamations des e-commerçants | G2 : « 10 à 100 k€ » ; « réclamations de clients, sans perte de client » |
| ER9 Volumes de vente d'un e-commerçant divulgués à un concurrent | VM7 | Confidentialité | Clause de confidentialité violée ; impact financier non chiffrable | G2 : manquement contractuel isolé ; G3 si le client suspend ses commandes |
| ER10 Paiement mensuel du plus gros e-commerçant versé sur un faux compte | VM5 | Intégrité | Environ 140 k€ non encaissés, recouvrement incertain, litige avec le client | G3 : 100 k€ à 1,3 M€ |

Une commande est assimilée à un colis pour lire l'échelle ; c'est une approximation à écrire. Une seule dimension suffit à classer l'événement (chapitre 5, échelle de gravité ; chapitre 6, atelier 1).

@corrige 6
| Couple source de risque / objectif visé | Motivation | Ressources | Activité | Somme | Pertinence | Retenu |
| --- | --- | --- | --- | --- | --- | --- |
| SR7 Groupe cybercriminel / extorquer une rançon en bloquant la préparation | 3 | 3 | 3 | 9 | Élevée | Oui |
| SR8 Réseau de voleurs avec un complice interne / détourner des colis de valeur | 3 | 2 | 3 | 8 | Élevée | Oui |
| SR9 Escroc / détourner les paiements des e-commerçants par un faux RIB | 3 | 2 | 3 | 8 | Élevée | Oui |
| SR10 Concurrent d'un e-commerçant / obtenir ses volumes de vente | 2 | 1 | 1 | 4 | Faible | Non |
| SR11 Intérimaire mécontent / saboter le stock | 2 | 1 | 1 | 4 | Faible | Non |
| SR12 Cybercriminel / voler les adresses des clients finaux | 2 | 2 | 2 | 6 | Moyenne | Oui |

Justification de l'activité : SR7, panorama de la cybermenace de l'ANSSI ; SR8, 23 colis manquants en 2025 (annexe 4) ; SR9, tentative réelle de février 2026 ; SR10 et SR11, aucun indice ni incident connu ; SR12, SMS frauduleux répandus selon Cybermalveillance.gouv.fr, mais aucune attaque connue contre StockFlow. Pour SR12, une activité de 3 est acceptée si elle est justifiée par la diffusion des SMS frauduleux : la somme vaut 7, la pertinence reste moyenne et le couple reste retenu. Chaque choix repose sur un fait, ce que vérifie la grille (chapitre 6, atelier 2).

@corrige 7
Éléments attendus. L'exclusion se justifie par les trois critères : une motivation possible chez un intérimaire en fin de mission (2), mais des ressources faibles (1) et aucune activité connue, puisque aucun sabotage n'a été signalé (1). La somme vaut 4 : la pertinence est faible. On écrit ce motif dans le tableau, ce qui montre que la question a été posée.

Les comptes génériques ne disparaissent pas pour autant. Ils sont d'abord un écart au socle de sécurité de l'atelier 1 : dans sa partie consacrée à l'authentification et au contrôle des accès, le guide d'hygiène informatique de l'ANSSI recommande d'identifier nommément chaque personne qui accède au système, et donc de supprimer les comptes génériques. Ils sont ensuite une vulnérabilité d'un couple retenu, SR8 : un complice interne profite de l'absence d'imputation. Ils pèseront donc sur la vraisemblance du scénario opérationnel à l'atelier 4 et appelleront une mesure à l'atelier 5, des comptes nominatifs ouverts et fermés avec chaque mission. La méthode est itérative : l'atelier 2 enrichit l'atelier 1.

Barème indicatif sur 8 points : justification par les trois critères (3 points) ; écart au socle (2 points) ; lien avec SR8 et les ateliers 4 et 5 (2 points) ; expression (1 point). Notion : chapitre 6, ateliers 1 et 2.

# FT 15 | EBIOS RM, ateliers 3 et 4 : écosystème, scénarios et vraisemblance | 6

@situation
En mai 2026, l'étude complémentaire sur l'activité e-commerce de Kestrel Logistique arrive aux ateliers 3 et 4. L'atelier 2 a retenu le couple SR9 : un escroc qui veut détourner les paiements des e-commerçants par un faux changement de RIB. L'événement redouté visé est ER10, le paiement mensuel d'un e-commerçant versé sur un faux compte, de gravité G3. Romain Chevalier vous demande d'évaluer les parties prenantes, puis de construire et de coter le scénario opérationnel.

@capacites
Calculer le niveau de menace d'une partie prenante et la placer dans une zone
Construire un scénario stratégique qui passe par l'écosystème
Combiner les probabilités de succès le long d'un graphe d'attaque
Justifier une vraisemblance et mesurer l'effet d'une mesure

@duree 75 minutes

@annexe 1 | Ce que l'on sait des parties prenantes | Source fictive : compte rendu de l'atelier 3, mai 2026
PP-02 E-commerçants. Les e-commerçants clients ont des comptes sur le portail B2B d'APP-03 Kestrel Track et reçoivent leurs factures en PDF par courriel. Ce sont souvent de petites structures, à la messagerie peu protégée ; leurs contrats ne contiennent aucune exigence de sécurité. La vue de l'écosystème note une dépendance moyenne : leur arrêt réduirait le chiffre d'affaires, sans interrompre une activité de réalisation dans la journée.

PP-11 Hébergeur du site web. Il héberge APP-12 Site web sur un serveur mutualisé. Le site publie une page « Ils nous font confiance » qui cite douze e-commerçants clients. PP-15 Banque. Elle reçoit les paiements des clients ; elle est réputée bien protégée, mais l'escroc n'a pas besoin de la compromettre : il lui suffit d'invoquer son nom, ou un changement de banque. PP-18 Vidal Participations. La holding dispose d'un compte de consultation dans APP-07 ERP finance pour consolider les comptes.

Le service facturation. Les comptables ne sont pas cadres : leurs comptes d'APP-10 Microsoft 365 n'ont pas d'authentification multifacteur. Selon un entretien, aucune alerte de connexion inhabituelle n'est configurée et personne ne surveille les règles de messagerie. La mesure M3 de l'étude principale, l'authentification multifacteur pour tous, n'est pas encore déployée.

@annexe 2 | Cotation des parties prenantes | Groupe de travail de l'étude complémentaire ; critères cotés de 1 à 4
| Partie prenante | Dépendance | Pénétration | Maturité cyber | Confiance |
| --- | --- | --- | --- | --- |
| PP-02 E-commerçants | À déduire de l'annexe 1 | 2 | 1 | 2 |
| PP-11 Hébergeur du site web | 1 | 2 | 2 | 2 |
| PP-12 Opérateur télécom | 4 | 2 | 3 | 3 |
| PP-15 Banque | 2 | 2 | 4 | 4 |
| PP-18 Vidal Participations | 2 | 3 | 2 | 3 |

Niveau de menace = (dépendance × pénétration) / (maturité cyber × confiance). Zones : danger au-dessus de 3 ; contrôle de 1 à 3 ; veille de 0,5 à moins de 1 ; hors périmètre en dessous de 0,5. Dépendance : forte vaut 4 ; moyenne vaut 3 si un arrêt du partenaire interrompt dans la journée une activité de réalisation, 2 sinon ; faible vaut 1.

@annexe 3 | Scénario stratégique SS5 : deux chemins vers ER10 | Groupe de travail, version de travail
@schema
Chemin 1 :: SR9 Escroc -> [[Prend la boîte APP-10 d'une comptable]] -> Faux RIB envoyé à PP-02 -> [[ER10 Paiement détourné (G3)]]
Chemin 2 :: SR9 Escroc -> [[Compromet la messagerie d'un client PP-02]] -> Facture interceptée, RIB modifié -> [[ER10 Paiement détourné (G3)]]

@annexe 4 | Scénario opérationnel SO5, chemin 1 | Groupe de travail ; Pr : probabilité de succès, de 1 (faible) à 4 (quasi certaine)
| Étape | Phase | Action élémentaire et bien support visé | Vulnérabilité ou mesure | Pr | Précédée de |
| --- | --- | --- | --- | --- | --- |
| 1 | Connaître | Repérer les e-commerçants clients et le service facturation (APP-12 Site web, réseaux professionnels) | Page « Ils nous font confiance » | 4 | — |
| 2a | Rentrer | Hameçonner une comptable par une fausse page de connexion (APP-10 Microsoft 365) | Pas d'authentification multifacteur pour les non-cadres | 3 | 1 |
| 2b | Rentrer | Essayer des mots de passe courants sur les comptes du service (APP-10 Microsoft 365) | Idem ; politique de mots de passe non documentée | 2 | 1 |
| 3 | Rentrer | Se connecter à la boîte depuis l'étranger (APP-10 Microsoft 365) | Aucune alerte de connexion inhabituelle | 4 | 2a ou 2b |
| 4 | Trouver | Lire les échanges et repérer les factures du mois, éditées par APP-07 ERP finance | Factures envoyées en PDF par courriel | 4 | 3 |
| 5 | Trouver | Créer une règle qui cache les réponses des clients (APP-10 Microsoft 365) | Règles de messagerie non surveillées | 4 | 4 |
| 6 | Exploiter | Envoyer le faux avis de RIB et obtenir les paiements (PP-02 E-commerçants) | Aucune procédure convenue avec les clients ; un client a rappelé Kestrel en février 2026 | 3 | 5 |

Règle : l'indice cumulé d'une étape est la plus petite de deux valeurs, sa probabilité et le meilleur indice cumulé des étapes qui y mènent. L'indice global se lit sur l'échelle : 1 = V1, 2 = V2, 3 = V3 très vraisemblable, 4 = V4.

@question 1 | Calculer | Annexes 1 et 2
Déduisez la cote de dépendance de PP-02, puis calculez le niveau de menace de chaque partie prenante, sa zone, et dites si elle est critique.
@tableau
| Partie prenante | Calcul posé | Niveau de menace | Zone | Critique ? |
| --- | --- | --- | --- | --- |
| PP-02 E-commerçants | | | | |
| PP-11 Hébergeur du site web | | | | |
| PP-12 Opérateur télécom | | | | |
| PP-15 Banque | | | | |
| PP-18 Vidal Participations | | | | |

@question 2 | Analyser | Annexes 1 et 2
PP-15 Banque est hors périmètre, et son nom sert pourtant à l'escroc. La fiche méthode de l'ANSSI permet de retirer la confiance de la formule quand une partie prenante risque d'être utilisée à son insu. Recalculez son niveau de menace et discutez le résultat.
@lignes 5

@question 3 | Mobiliser | Annexes 1 et 3
Complétez les boîtes vides du schéma de l'annexe 3. Indiquez ensuite la gravité de SS5 et la partie prenante critique par laquelle passe le chemin 2.
@lignes 3

@question 4 | Calculer | Annexe 4
Calculez l'indice cumulé de chaque étape, puis la vraisemblance de SO5.
@tableau
| Étape | Pr | Meilleur indice cumulé des étapes qui y mènent | Indice cumulé |
| --- | --- | --- | --- |
| 1 | 4 | — | |
| 2a | 3 | | |
| 2b | 2 | | |
| 3 | 4 | | |
| 4 | 4 | | |
| 5 | 4 | | |
| 6 | 3 | | |

@question 5 | Analyser | Annexes 1 et 4
Justifiez en quelques phrases la vraisemblance obtenue : vulnérabilités décisives, longueur de la chaîne, faits qui restent à vérifier.
@lignes 5

@question 6 | Calculer | Annexe 4
Mesurez l'effet de deux mesures. Avec M3 déployée, la probabilité de 2a tombe à 2 (un hameçonnage élaboré peut contourner une authentification simple) et celle de 2b à 1. Si, en plus, Kestrel convient avec chaque client d'un contre-appel au numéro du contrat, la probabilité de l'étape 6 tombe à 1.
@tableau
| Situation | Indice cumulé à l'étape 3 | Indice global | Vraisemblance |
| --- | --- | --- | --- |
| Initiale | | | |
| Avec M3 | | | |
| Avec M3 et le contre-appel | | | |

@question 7 | Proposer | Toutes les annexes
Proposez des mesures sur l'écosystème pour PP-02 E-commerçants et PP-18 Vidal Participations, puis réévaluez leur niveau de menace en indiquant quel critère chaque mesure modifie.
@lignes 8

@retiens
Le niveau de menace d'une partie prenante combine deux critères d'exposition, la [[dépendance]] et la [[pénétration]], et deux critères de fiabilité cyber, la [[maturité]] et la [[confiance]]. Les parties prenantes des zones de danger et de [[contrôle]] sont critiques et entrent dans les scénarios stratégiques. Un scénario opérationnel suit quatre phases : [[connaître]], rentrer, trouver, [[exploiter]]. L'indice cumulé d'une étape est le [[minimum]] de sa probabilité et du meilleur indice des étapes qui y mènent : une chaîne vaut son maillon le plus faible, et l'attaquant choisit le [[meilleur chemin]].

@corrige 1
| Partie prenante | Calcul posé | Niveau de menace | Zone | Critique ? |
| --- | --- | --- | --- | --- |
| PP-02 E-commerçants | Dépendance moyenne sans interruption de réalisation dans la journée : 2. (2 × 2) / (1 × 2) = 4 / 2 | 2 | Contrôle | Oui |
| PP-11 Hébergeur du site web | (1 × 2) / (2 × 2) = 2 / 4 | 0,5 | Veille | Non |
| PP-12 Opérateur télécom | (4 × 2) / (3 × 3) = 8 / 9 | 0,89 | Veille | Non |
| PP-15 Banque | (2 × 2) / (4 × 4) = 4 / 16 | 0,25 | Hors périmètre | Non |
| PP-18 Vidal Participations | (2 × 3) / (2 × 3) = 6 / 6 | 1 | Contrôle | Oui |

Les parties prenantes des zones de danger et de contrôle sont critiques : elles doivent être prises en compte dans les scénarios stratégiques (chapitre 6, atelier 3, formule et seuils de l'étude Kestrel). PP-02 doit sa place à sa faible maturité cyber, PP-18 à sa pénétration dans l'ERP finance.

@corrige 2
Sans la confiance : (2 × 2) / 4 = 4 / 4 = 1. PP-15 passe de hors périmètre en zone de contrôle. Le résultat traduit une idée juste : la confiance que les clients et les comptables accordent au nom de la banque est précisément ce que l'escroc exploite. Dans ce cas, la note de confiance ne protège plus, elle aggrave.

Il faut toutefois lire le résultat avec prudence. L'attaque ne passe pas par les systèmes de la banque : sa maturité cyber n'y change rien, et les mesures porteront sur Kestrel et ses clients, pas sur PP-15. Le retrait de la confiance est une adaptation de la formule permise par la fiche méthode de l'ANSSI : il doit être écrit et justifié dans le barème de l'étude (chapitre 6, atelier 3).

@corrige 3
Chemin 1 : l'escroc hameçonne une comptable et prend sa boîte d'APP-10 Microsoft 365, puis provoque ER10, le paiement versé sur un faux compte (G3). Chemin 2 : il compromet la messagerie du service comptable d'un e-commerçant de PP-02, puis aboutit au même ER10. Toute formulation équivalente est acceptée, pourvu que le bien support ou la partie prenante soit nommé comme dans la cartographie.

La gravité de SS5 est celle de l'événement redouté le plus grave qu'il provoque : G3 (ER10). Le chemin 2 passe par PP-02 E-commerçants, partie prenante critique en zone de contrôle : c'est le chemin par l'écosystème. Au chemin 1, PP-02 n'est que la victime trompée (chapitre 6, définition « Scénario stratégique »).

@corrige 4
| Étape | Pr | Meilleur indice cumulé des étapes qui y mènent | Indice cumulé |
| --- | --- | --- | --- |
| 1 | 4 | — | 4 |
| 2a | 3 | 4 | min(3 ; 4) = 3 |
| 2b | 2 | 4 | min(2 ; 4) = 2 |
| 3 | 4 | max(3 ; 2) = 3 | min(4 ; 3) = 3 |
| 4 | 4 | 3 | 3 |
| 5 | 4 | 3 | 3 |
| 6 | 3 | 3 | 3 |

L'indice global est 3 : SO5 est très vraisemblable (V3). L'attaquant choisit le meilleur chemin, celui de l'hameçonnage (2a) ; la pulvérisation de mots de passe (2b) reste un mode opératoire alternatif (chapitre 6, règle de combinaison de la méthode standard).

@corrige 5
Les deux étapes cotées 3 fixent la vraisemblance : l'hameçonnage, qui vise une personne précise, et l'envoi du faux avis, car un client peut rappeler, comme en février 2026. Tout le reste est quasi certain : pas d'authentification multifacteur pour les non-cadres (fait de la fiche Kestrel), aucune alerte de connexion, règles de messagerie non surveillées. La chaîne compte six actions en série, moins que la dizaine au-delà de laquelle la fiche conseille de baisser d'un niveau : V3 est maintenu. L'absence d'alerte et de surveillance des règles repose sur un entretien, sans document : il faut l'écrire comme hypothèse numérotée et la vérifier. La tentative de février 2026 montre que le scénario est réel ; son échec explique qu'on ne retienne pas V4.

@corrige 6
| Situation | Indice cumulé à l'étape 3 | Indice global | Vraisemblance |
| --- | --- | --- | --- |
| Initiale | min(4 ; max(3 ; 2)) = 3 | 3 | V3 |
| Avec M3 | min(4 ; max(2 ; 1)) = 2 | min(3 ; 2) = 2 | V2 |
| Avec M3 et le contre-appel | 2 | min(1 ; 2) = 1 | V1 |

Avec M3, l'étape 2a ne vaut plus que 2, et toute la suite de la chaîne hérite de cet indice. Le contre-appel agit en bout de chaîne : il suffit à ramener l'indice global à 1, quelle que soit la facilité des étapes précédentes. C'est l'intérêt du graphe : une mesure bien placée coupe tous les chemins qui passent par l'étape qu'elle protège.

@corrige 7
Pour PP-02 : un avenant ou un courrier qui fixe la règle « Kestrel ne change jamais de RIB par courriel » et un contre-appel convenu au numéro du contrat ; la confiance passe de 2 à 3. La maturité cyber des clients ne se décrète pas : elle reste à 1. Nouveau niveau : (2 × 2) / (1 × 3) ≈ 1,33, toujours en zone de contrôle. Ce résultat est acceptable : la zone de contrôle est tolérable sous contrôle, et la mesure agit surtout sur l'étape 6 du scénario.

Pour PP-18 : un compte nominatif, avec authentification multifacteur, limité à la consultation des états de consolidation, et une revue annuelle des droits ; la pénétration passe de 3 à 2. Nouveau niveau : (2 × 2) / (2 × 3) ≈ 0,67, zone de veille.

Barème indicatif sur 8 points : une mesure pertinente par partie prenante (2 points chacune) ; critère modifié et calcul juste (1 point chacun) ; lecture de la zone obtenue (2 points). Notion : chapitre 6, atelier 3, mesures sur l'écosystème.

# FT 16 | EBIOS RM, atelier 5 : décider, mesurer le risque résiduel | 6

@situation
En juillet 2026, l'étude complémentaire sur l'activité e-commerce de Kestrel Logistique arrive à l'atelier 5. Les ateliers précédents ont produit quatre scénarios, désormais traités comme les risques R5 à R8, à la suite des risques R1 à R4 de l'étude principale. Isabelle Roux, Sébastien Morin, Hélène Garnier et Romain Chevalier se réunissent pour décider. Vous rédigez le relevé de décisions.

@capacites
Placer des risques sur la matrice et appliquer le seuil d'acceptation
Typer des mesures et les relier aux risques
Estimer un risque résiduel et désigner qui l'accepte
Construire un cadre de suivi et lire un indicateur avec prudence

@duree 75 minutes

@annexe 1 | Les risques de l'étude complémentaire | Synthèse des ateliers 1 à 4, juin 2026 ; ER11 a été ajouté pendant l'atelier 2 pour le couple SR12
| Risque | Couple | Événement redouté et gravité | Vraisemblance et vulnérabilités décisives |
| --- | --- | --- | --- |
| R5 Fraude aux paiements des e-commerçants | SR9 | ER10 Paiement d'un e-commerçant versé sur un faux compte : G3 | V3 : pas d'authentification multifacteur pour les comptables ; aucune alerte de connexion ; aucune procédure convenue avec les clients |
| R6 Vol de colis de valeur avec un complice interne | SR8 | ER8 Colis de valeur sortis du stock sans être livrés : G2 | V3 : comptes StockFlow génériques des intérimaires ; 23 colis manquants en 2025 |
| R7 Extorsion par le compte d'administration de StockFlow | SR7 | ER7 Préparation impossible à Moirans pendant deux jours : G3 | V2 : compte d'administration de Kestrel protégé par un simple mot de passe |
| R8 Vol des adresses des clients finaux dans StockFlow | SR12 | ER11 Données des clients finaux divulguées : G3 | V2 : comptes génériques partagés et jamais changés ; compte d'administration protégé par un simple mot de passe |

@annexe 2 | Relevé de l'atelier 5 | Source fictive : notes de séance, juillet 2026
Le groupe propose huit mesures, numérotées à la suite du plan de l'étude principale. M15 : authentification multifacteur sur le compte d'administration de StockFlow, que l'éditeur ne proposera qu'à partir de sa version d'octobre 2026. M16 : un compte StockFlow nominatif par intérimaire, ouvert et fermé avec sa mission ; l'essai mené depuis avril coûte 9 € par compte et par mois. M17 : écrire aux e-commerçants que Kestrel ne change jamais de RIB par courriel, et convenir avec chacun d'un contre-appel au numéro du contrat. M18 : bloquer les transferts automatiques vers l'extérieur et activer les alertes de connexion inhabituelle d'APP-10 Microsoft 365.

M19 : rapprocher chaque jour le stock des références de valeur et relire les mouvements par compte. M20 : exporter chaque semaine les données de stock hors de StockFlow et écrire une procédure de préparation sur listes papier, exercée deux fois par an. M21 : avenant au contrat de PP-06 Éditeur de StockFlow : notification des incidents, journal des accès aux données, prise en charge des frais en cas de faute de l'éditeur. M22 : zone grillagée et contrôle à la sortie pour les produits de valeur.

La mesure M3 de l'étude principale, l'authentification multifacteur pour tous, n'est toujours pas décidée : chiffrée en avril, elle attend un arbitrage du comité. M20 sera opérationnelle en septembre, M15 en octobre. Selon Sébastien Morin, avec M20, la préparation reprendrait en moins d'une journée. En attendant M15, Romain Chevalier propose de changer le mot de passe du compte d'administration et de relire chaque semaine son journal de connexions.

@annexe 3 | Matrice et seuil d'acceptation | Étude des risques de Kestrel Logistique, version 1.0
| Gravité / Vraisemblance | V1 | V2 | V3 | V4 |
| --- | --- | --- | --- | --- |
| G4 Critique | Élevé | Critique | Critique | Critique |
| G3 Grave | Moyen | Élevé | Élevé | Critique |
| G2 Significative | Faible | Moyen | Moyen | Élevé |
| G1 Mineure | Faible | Faible | Faible | Moyen |

Un risque faible peut être accepté par le responsable de l'infrastructure ; un risque moyen par le comité de direction, avec un motif écrit ; un risque élevé ou critique doit être traité. Tant que son traitement est en cours, un risque élevé ne peut être accepté que temporairement, par le directeur général, avec une mesure compensatoire et une date de réexamen.

@annexe 4 | Écarts d'inventaire sur les références de valeur à Moirans, en 2026 | Source fictive : direction des opérations ; essai de comptes nominatifs pour les intérimaires depuis avril 2026
@graphique lignes k€
Janvier : 1,8
Février : 1,5
Mars : 1,9
Avril : 0,7
Mai : 0,5
Juin : 0,4

@question 1 | Calculer | Annexes 1 et 3
Placez les quatre risques sur la matrice et indiquez ce qu'impose le seuil d'acceptation.
@tableau
| Risque | Gravité | Vraisemblance | Niveau initial | Ce qu'impose le seuil |
| --- | --- | --- | --- | --- |
| R5 | | | | |
| R6 | | | | |
| R7 | | | | |
| R8 | | | | |

@question 2 | Mobiliser | Annexe 2
Donnez le type de chaque mesure (gouvernance, protection, défense, résilience), les risques qu'elle traite et ce sur quoi elle agit d'abord : la gravité ou la vraisemblance.
@tableau
| Mesure | Type | Risques traités | Agit sur |
| --- | --- | --- | --- |
| M15 | | | |
| M16 | | | |
| M17 | | | |
| M18 | | | |
| M19 | | | |
| M20 | | | |
| M21 | | | |
| M22 | | | |

@question 3 | Calculer | Annexes 1, 2 et 3
R6 est un risque moyen : le comité de direction pourrait l'accepter. À quelles conditions ? Calculez le coût annuel maximal de M16, en supposant que les 20 intérimaires des périodes de pointe (été et fin d'année) soient présents toute l'année, et comparez-le aux pertes de 2025 (23 colis à 600 €). Pourquoi le groupe choisit-il de réduire ce risque ?
@lignes 5

@question 4 | Calculer | Annexes 1, 2 et 3
Estimez le risque résiduel de chaque risque une fois toutes les mesures appliquées, et dites qui peut l'accepter.
@tableau
| Risque | Mesures appliquées | Gravité résiduelle | Vraisemblance résiduelle | Niveau résiduel | Qui l'accepte |
| --- | --- | --- | --- | --- | --- |
| R5 | | | | | |
| R6 | | | | | |
| R7 | | | | | |
| R8 | | | | | |

@question 5 | Calculer | Annexes 2 et 4
Calculez les écarts d'inventaire du premier et du deuxième trimestre 2026, puis leur variation en pourcentage. Peut-on attribuer cette baisse à l'essai de comptes nominatifs ?
@lignes 5

@question 6 | Proposer | Annexes 2 et 4
Proposez trois indicateurs du cadre de suivi de l'étude complémentaire.
@tableau
| Indicateur | Mesure ou risque suivi | Rythme | Instance qui l'examine |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

@question 7 | Argumenter | Annexes 1, 2 et 3
De juillet à octobre, R7 reste au-dessus du seuil d'acceptation. Rédigez la demande d'acceptation temporaire soumise au directeur général, telle qu'elle figurera au procès-verbal du comité.
@lignes 9

@retiens
Chaque scénario devient un [[risque]], de gravité égale à celle du scénario stratégique et de vraisemblance égale à celle du scénario opérationnel. Le [[seuil d'acceptation]] dit quels risques doivent être traités. Les mesures sont de quatre types : [[gouvernance]], [[protection]], [[défense]] et [[résilience]]. Une mesure de protection ou de défense fait baisser la [[vraisemblance]] ; une mesure de résilience fait souvent baisser la [[gravité]]. Le risque [[résiduel]] n'est jamais nul : il est accepté par écrit par un responsable qui en a l'autorité. Le [[cadre de suivi]] fixe les indicateurs, l'instance et le rythme de revue.

@corrige 1
| Risque | Gravité | Vraisemblance | Niveau initial | Ce qu'impose le seuil |
| --- | --- | --- | --- | --- |
| R5 | G3 | V3 | Élevé | Doit être traité |
| R6 | G2 | V3 | Moyen | Peut être accepté par le comité de direction, avec un motif écrit, ou traité |
| R7 | G3 | V2 | Élevé | Doit être traité ; acceptation seulement temporaire par le directeur général |
| R8 | G3 | V2 | Élevé | Doit être traité |

Chaque risque prend la gravité de son scénario stratégique et la vraisemblance de son scénario opérationnel ; placés sur la matrice, ils forment la cartographie des risques initiaux (chapitre 6, atelier 5).

@corrige 2
| Mesure | Type | Risques traités | Agit sur |
| --- | --- | --- | --- |
| M15 | Protection | R7, R8 | Vraisemblance |
| M16 | Protection | R6, R8 | Vraisemblance ; rétablit aussi la traçabilité |
| M17 | Gouvernance | R5 | Vraisemblance (coupe l'étape finale) |
| M18 | Défense | R5 | Vraisemblance (détection) |
| M19 | Défense | R6 | Vraisemblance (détection rapide) |
| M20 | Résilience | R7 | Gravité |
| M21 | Gouvernance | R7, R8 | Gravité financière (transfert partiel des frais) ; détection par le journal des accès |
| M22 | Protection | R6 | Vraisemblance |

Les mesures de gouvernance organisent (procédures, contrats), celles de protection empêchent, celles de défense détectent et répondent, celles de résilience limitent les conséquences (chapitre 6, atelier 5). M21 comporte un volet de transfert : il ne couvre que les frais, jamais l'arrêt de la préparation. M18 a un double volet : le blocage des transferts relève de la protection, les alertes de la défense ; les deux réponses sont acceptées.

@corrige 3
Le comité peut accepter un risque moyen à condition d'écrire sa décision, avec un motif, et de la dater. Coût de M16 : 20 comptes × 9 € = 180 € par mois au plus, soit 180 × 12 = 2 160 € par an si les 20 intérimaires étaient présents toute l'année, ce qui majore le coût réel. Les pertes de 2025 s'élèvent à 23 × 600 € = 13 800 €, plus de six fois ce montant (13 800 ÷ 2 160 ≈ 6,4).

Le groupe réduit donc le risque parce que la mesure coûte peu au regard des pertes, et parce qu'elle corrige aussi un écart au socle (comptes non nominatifs) qui sert R8. Accepter un risque que l'on peut réduire à si bon compte serait difficile à défendre (chapitre 5, options de traitement).

@corrige 4
| Risque | Mesures appliquées | Gravité résiduelle | Vraisemblance résiduelle | Niveau résiduel | Qui l'accepte |
| --- | --- | --- | --- | --- | --- |
| R5 | M3, M17, M18 | G3 | V1 | Moyen | Comité de direction, motif écrit |
| R6 | M16, M19, M22 | G2 | V1 | Faible | Responsable de l'infrastructure |
| R7 | M15, M20, M21 | G2 | V1 | Faible | Responsable de l'infrastructure |
| R8 | M15, M16, M21 | G3 | V1 | Moyen | Comité de direction, motif écrit |

Le résiduel de R5 suppose que M3 soit enfin décidée et déployée. Les mesures de protection et de défense font tomber la vraisemblance ; on accepte V2 pour R5 ou R8 si la justification est écrite, ce qui laisse le risque élevé et impose un traitement complémentaire. Seule M20, mesure de résilience, abaisse une gravité : avec elle, la préparation reprend en moins d'une journée, ce qui correspond à G2. Pour R6, le seuil confie l'acceptation au responsable de l'infrastructure ; il est sage d'y associer le directeur des opérations, propriétaire du processus (chapitre 6, atelier 5).

@corrige 5
Premier trimestre : 1,8 + 1,5 + 1,9 = 5,2 k€. Deuxième trimestre : 0,7 + 0,5 + 0,4 = 1,6 k€. Variation : (1,6 − 5,2) ÷ 5,2 = − 3,6 ÷ 5,2 ≈ − 0,69, soit une baisse d'environ 69 %.

La baisse coïncide avec l'essai de comptes nominatifs, mais la coïncidence ne prouve pas la cause. Le printemps compte moins d'intérimaires que l'été ou la fin d'année (question 3) : la baisse peut tenir à la saison. Pour l'enseignant : la fiche FT 14 montre que les pertes de 2025 étaient déjà basses au deuxième trimestre ; l'élève ne dispose pas de ce chiffre ici. Six mois de données ne suffisent pas. Il faudra comparer avec les mêmes trimestres de 2025, sur la même mesure, et suivre l'indicateur pendant la pointe d'été et de fin d'année. Un indicateur se lit avec sa référence, comme tout chiffre d'un diagnostic.

@corrige 6
| Indicateur | Mesure ou risque suivi | Rythme | Instance qui l'examine |
| --- | --- | --- | --- |
| Écarts d'inventaire sur les références de valeur, en k€ | R6 ; M16, M19, M22 | Mensuel | Comité de direction, chaque trimestre |
| Part des comptes d'APP-10 Microsoft 365 protégés par authentification multifacteur | R5 ; M3 | Mensuel jusqu'à 100 %, puis trimestriel | Comité de direction, chaque trimestre |
| Nombre de comptes génériques encore actifs dans StockFlow | R6, R8 ; M16 | Mensuel | Comité de direction, chaque trimestre |

Autres réponses acceptées : date et durée du dernier exercice de préparation sur listes papier (M20, semestriel) ; nombre de demandes de changement de RIB reçues et de contre-appels faits (M17). Le cadre de suivi de Kestrel fait examiner les indicateurs par le comité de direction une fois par trimestre ; le cycle opérationnel est annuel (chapitre 6, atelier 5).

@corrige 7
Éléments attendus. Le risque : R7, extorsion par le compte d'administration de StockFlow, G3 × V2, niveau élevé, au-dessus du seuil. Le motif : la mesure principale, M15, dépend de la version d'octobre 2026 de l'éditeur ; le risque ne peut pas être évité, car StockFlow porte la préparation des commandes e-commerce, au cœur du plan « Cap 2029 ». La mesure compensatoire : changement immédiat du mot de passe du compte d'administration et relecture hebdomadaire de son journal de connexions. Le calendrier : en septembre, M20 abaisse la gravité à G2 et le risque devient moyen (G2 × V2), acceptable par le comité ; en octobre, M15 le rend faible. La date de réexamen : fin octobre 2026, après le déploiement de M15. Le signataire : Paul Vidal, directeur général. Le procès-verbal indique le risque, son niveau, le motif, la mesure compensatoire et la date de réexamen.

Barème indicatif sur 9 points : risque et niveau (1 point) ; motif, dont l'impossibilité d'éviter (2 points) ; mesure compensatoire (2 points) ; évolution du niveau avec M20 puis M15 (2 points) ; date de réexamen et signataire (1 point) ; forme d'une décision écrite (1 point). Notion : chapitre 5, encadré « Accepter n'est pas oublier » ; chapitre 6, atelier 5.
