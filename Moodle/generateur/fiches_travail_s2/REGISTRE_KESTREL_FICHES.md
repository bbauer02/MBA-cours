# Registre des faits Kestrel ajoutés par les fiches de travail S2

Ce registre recense les faits nouveaux sur Kestrel Logistique introduits par les 21 fiches de travail (ft_A.md à ft_D.md), après arbitrage. Il complète la fiche Kestrel de `cours_s2/CHARTE.md` et les valeurs de référence des chapitres, qui priment toujours. Règle d'arbitrage appliquée : le cours d'abord ; ensuite la version la plus utilisée ou la plus cohérente, les autres fiches étant réécrites, calculs, tableaux, corrigés et « Je retiens » compris. Tout nouvel auteur reprend ces valeurs telles quelles et numérote ses ajouts à la suite des numéros listés en fin de document.

## 1. Organisation, personnes et sites

| N° | Fait canonique | Fiches |
| --- | --- | --- |
| K01 | Les fonctions sans nom s'écrivent ainsi : « responsable de l'agence de Clermont-Ferrand » (jamais « chef d'agence »), « gestionnaire de paie », « chef de quai », « assistante d'exploitation », « responsable comptable », « responsable de l'entrepôt » de Moirans, « chef de projet applicatif ». Les sept noms de la fiche Kestrel gardent leur fonction exacte. | FT 01, 06, 07, 11, 12, 13, 14, 17, 18 |
| K02 | Agence de Clermont-Ferrand : 35 salariés (1 responsable de l'agence, 1 chef de quai, 11 agents de quai, 18 chauffeurs, 2 assistantes d'exploitation, 1 commercial, 1 technicien d'atelier) ; 24 tournées par jour, dont 6 confiées aux sous-traitants du dernier kilomètre ; rattachée au directeur des opérations, le commercial à la directrice commerciale. | FT 01, 11 |
| K03 | Rythme de Clermont-Ferrand : navette de nuit depuis Saint-Priest vers 3 h 30 ; départ des chauffeurs de Kestrel vers 6 h (les camions du siège partent à 5 h, fiche Kestrel) ; tournées des sous-traitants vers 8 h ; navette du soir vers Saint-Priest. | FT 01, 11 |
| K04 | Volume de Clermont-Ferrand, semaine type de février 2026 : 1 520, 1 310, 1 260, 1 290, 1 220 colis du lundi au vendredi, soit 1 320 colis par jour en moyenne (14,7 % des 9 000 colis de Kestrel). Arbitrage : la valeur de 1 100 colis de FT 11 est remplacée par 1 310, volume d'un mardi. | FT 01, 11 |
| K05 | Infrastructure de SITE-03 Clermont-Ferrand : accès à Internet par le siège, à travers RES-02 ; un routeur de l'opérateur et un commutateur uniques, sans onduleur ; 2 bornes Wi-Fi des quais ; 14 scanners (dont 2 de réserve) sur les 60 de TRM-01 ; 12 postes (TRM-05) ; une seule imprimante d'étiquettes, pilotée depuis APP-02 StockFlow. Identifiants proposés : RES-04 Routeur de Clermont-Ferrand, RES-05 Commutateur de Clermont-Ferrand, TRM-07 Imprimante d'étiquettes de Clermont-Ferrand, STO-03 Clé USB des litiges de Clermont-Ferrand. | FT 11 (et FT 14 : scanners présents sur les quais des trois sites) |
| K06 | Seul le responsable de l'agence détient dans StockFlow les droits de validation des écarts de réception. Le mot de passe du Wi-Fi des quais de Clermont-Ferrand est affiché ; des téléphones personnels de sous-traitants s'y connectent (franchissement FR-07). | FT 11 |
| K07 | Préparation des commandes : à Saint-Priest et à Moirans ; Clermont-Ferrand réceptionne, trie et expédie, sans entreposage. L'entrepôt de Moirans stocke les marchandises de 18 e-commerçants, prépare environ 1 800 commandes par jour, avec 30 agents permanents (comptes StockFlow nominatifs) et jusqu'à 20 intérimaires l'été et en fin d'année (quatre comptes génériques ; essai de comptes nominatifs depuis avril 2026, 9 € par compte et par mois). | FT 12, 13, 14, 15, 16, 18 |
| K08 | Cellule service client du siège : 4 conseillères dont une responsable, 180 appels par jour (avril 2026 : 92 « où est mon colis », 38 reprogrammations, 24 colis endommagés, 11 litiges de facture, 15 autres). Elle traite les réclamations de Saint-Priest et de Moirans dans le classeur « Litiges 2026 » sur Microsoft 365, hors inventaire. | FT 03 |
| K09 | Litiges de Clermont-Ferrand : les colis arrivés abîmés sont notés au cahier de quai ; les réclamations des clients sont saisies par l'assistante d'exploitation dans le fichier Excel « Litiges Clermont », enregistré sur le poste du responsable de l'agence et partagé avec l'équipe, non inscrit à l'inventaire (connu de la DSI depuis mars 2026) ; copie chaque vendredi sur une clé USB rangée dans le même bureau. Réclamations 2026 : 42, 38, 51, 47, 55 de janvier à mai. | FT 01, 07, 11 |
| K10 | Frais de garde : chaque mois, le responsable de l'agence exporte de StockFlow la liste des colis gardés en instance pour les e-commerçants ; le service comptable la ressaisit dans l'ERP finance (3 heures par mois ; 9 factures sur 150 corrigées en 2025). Le même envoi a un bordereau StockFlow et une lettre de voiture RoutePro, aux poids parfois différents. Arbitrage : remplace l'« entreposage » facturé à Clermont-Ferrand. | FT 07 |

## 2. Stratégie, clients et gouvernance

| N° | Fait canonique | Fiches |
| --- | --- | --- |
| K11 | Vidal Participations (janvier 2026) : pas d'autre métier logistique, par exemple le transport sous température dirigée ; attentes pour 2029 : chiffre d'affaires d'au moins 48 M€ et marge de 5 %. Arbitrage : l'exemple « entreposage pour le compte de tiers » est retiré, car Kestrel entrepose déjà pour des e-commerçants (K07). Convention de trésorerie et reporting mensuel extrait de l'ERP finance ; compte de consultation dans l'ERP finance. | FT 04, 09, 15 |
| K12 | Part du e-commerce dans le chiffre d'affaires : 20, 22, 25, 28 et 30 % de 2021 à 2025. Objectifs 2026 des directions : ponctualité (non chiffré), écoconduite de 100 % des chauffeurs avant le 30 septembre 2026, 30 nouveaux e-commerçants, délai de paiement des clients de 58 à 50 jours, « Moderniser le SI ». | FT 04 |
| K13 | Démarrage d'un e-commerçant transporté : 15 jours ouvrés réels ; 180 demandes de devis en 2025 (38, 45, 41, 56), 27 contrats signés. Ces e-commerçants envoient leurs ordres par tableur ; ceux dont Kestrel stocke la marchandise passent par un connecteur de StockFlow. | FT 02, 14 |
| K14 | Premier client de la grande distribution : contrat renouvelé en juin 2026 pour trois ans, à condition de recevoir d'ici mars 2027 les statuts de livraison en temps réel par une API. Une enseigne nationale imposera dès mars 2027 la prise de rendez-vous par son portail et la preuve de livraison dans l'heure. | FT 05, 19, 20, 21 |
| K15 | Budget SI 2026 : 1 300 k€, dont personnel de la DSI 560, SaaS et licences 310, maintenance des progiciels 120, matériel et réseau 50, projets 260 (80 % en fonctionnement, conforme au cours). | FT 05, 06 |
| K16 | Registre des demandes de projets 2026, numéros et coûts uniques : D1 module d'optimisation de RoutePro 95 k€ ; D2 migration de Django 70 k€ ; D3 outil de relation client 38 k€ (devis reçu en avril, non signé) ; D4 authentification multifacteur pour tous (APP-10 Microsoft 365 et SEC-01 Passerelle VPN) 18 k€ ; D5 interface TeleFleet et paie 25 k€ ; D6 liens 4G de secours de Clermont-Ferrand et Moirans 12 k€ ; D7 remplacement de 20 scanners de Saint-Priest 45 k€ ; D8 API de statuts en temps réel 70 k€ (juin). Total d'avril (D1 à D7) : 303 k€ ; demandes en attente en juin (D1 à D5 et D8) : 316 k€. Arbitrage : valeurs de FT 06 retenues ; FT 05 recalculé (dépassement 56 k€, 21,5 % ; D1, D2, D8 = 90,4 % de l'enveloppe ; Kestrel Track 53,8 %). | FT 05, 06 |
| K17 | Authentification multifacteur : le comité de février 2026 l'a confiée à la DSI « sans coût supplémentaire » (ch02) ; la DSI l'a chiffrée à 18 k€ en avril ; aucune décision en 2026. Elle reste réservée aux cadres jusqu'à fin 2026 (fiche Kestrel, faiblesse F3) ; M3 n'est pas déployée. Arbitrage : FT 16 ne dit plus « M3 achevée en septembre ». Elle n'est pas activée non plus sur APP-08 Paie (proposée par le prestataire), sur la console d'APP-05 TeleFleet, ni sur le compte d'administration de StockFlow (possible avec la version d'octobre 2026 de l'éditeur). | FT 05, 06, 13, 15, 16, 17, 20, 21 |
| K18 | Comités : en février, cinq demandes présentées (la demande de la DRH non examinée) ; en mars, aucun point SI ; en mai, D6 et D7 renvoyées à 2027, la grille de cotation de la DSI non examinée. L'option 4G de RES-02 n'est toujours pas souscrite en octobre 2026. Demandes de 2025 par canal : 14 courriels, 9 à l'oral, 4 en comité, 3 par l'outil de tickets. | FT 05, 06, 18 |

## 3. Cartographie, inventaires et flux

| N° | Fait canonique | Fiches |
| --- | --- | --- |
| K19 | Cartographie version 1.0 (Romain Chevalier, 2025, sponsor Isabelle Roux) : écosystème, applications, infrastructures physiques, administration, registre H1 à H7 ; version 2 en préparation en février 2026 (charge à la granularité la plus fine : 48 jours-personnes). | FT 08, 09 |
| K20 | Règle de dépendance du modèle : forte si la défaillance arrête en moins d'une journée un processus de réalisation ; moyenne si elle arrête un processus de support ou si le partenaire porte plus de 20 % du chiffre d'affaires ; faible sinon ; sans objet pour une obligation légale. Cotations : PP-02 moyenne, PP-03 faible, PP-10 moyenne, PP-11 faible, PP-15 moyenne, PP-17 sans objet, PP-18 moyenne. Seules PP-01, PP-04, PP-05 et PP-12 sont fortes (ch03). | FT 09, 15 |
| K21 | Flux ajoutés : FLX-07 APP-01 RoutePro vers APP-07 ERP finance (lettres de voiture livrées, fichier par partage interne non chiffré, chaque nuit, automatique, tâches EXP_LV à 1 h 30 et IMP_LV à 2 h) ; FLX-08 APP-07 ERP finance vers PP-15 Banque (virements, dépôt manuel deux fois par semaine) ; FLX-09 APP-08 Paie vers APP-07 ERP finance (écritures de paie, courriel mensuel, manuel). Tâche SAUV_ERP à 23 h : sauvegarde nocturne de l'ERP finance sur STO-01, qui appuie H1 pour l'ERP finance seulement. | FT 10, 20 |
| K22 | ERP finance : utilisé par six comptables et la DAF, client lourd, non exposé, maintenu par l'éditeur ; compte générique du service comptable partagé par quatre personnes ; pas de connecteur de facturation électronique (option payante). | FT 10, 12, 19 |
| K23 | Usages hors inventaire : service gratuit de transfert de fichiers (photos de colis abîmés) à Clermont-Ferrand ; assistant d'IA gratuit utilisé par deux commerciaux depuis l'été 2026 ; connexions vers des assistants d'IA en septembre 2026 : commercial 410, planification 160, paie et RH 95, DSI 60, quais 35. Ce relevé rend H15 plausible sans la confirmer. | FT 10, 17 |
| K24 | Inventaire v0.3 (juin 2026), refonte de l'inventaire pour la version 2 de la cartographie (la version 1.0 de 2025 reste en vigueur), attributs renseignés sur 12 applications : type 12, hébergement 12, éditeur 11, processus 9, exposition 8, utilisateurs 7, état du support 6, besoins DICT 4. | FT 10 |
| K25 | TeleFleet : boîtiers installés en janvier 2021 ; une position toutes les 2 minutes, 10 heures par jour, 250 jours par an ; conservation pendant tout le contrat ; un compte partagé « exploitation » (trois planificateurs et la gestionnaire de paie), mot de passe de 2021, journal de 30 jours jamais consulté ; export CSV par site le 24 de chaque mois vers le dossier SharePoint « Paie – Temps de conduite » (26 personnes, exports depuis janvier 2022), puis ressaisie mensuelle dans la paie (une journée et demie), ce qui appuie H6 ; clé d'API de 2023 en clair dans le dépôt GitHub de Kestrel Track. | FT 17, 18, 20 |

## 4. Incidents (une seule version par incident)

| N° | Fait canonique | Fiches |
| --- | --- | --- |
| K26 | Coupures de RES-02 VPN Clermont : février 2025, 2 h 30 ; juin 2025, 4 h ; novembre 2025, 7 h 30 (travaux de voirie, lettres de voiture à la main, 140 colis livrés le lendemain) ; 17 mars 2026, de 7 h 40 à 13 h 40, soit 6 h (travaux de voirie). Arbitrage : FT 12 (octobre 2025, 6 h) est ramené à l'incident de novembre 2025 de FT 11 ; FT 18 (6 h 10 à 12 h 40) suit la version de FT 06, 07 et 11. | FT 06, 07, 11, 12, 18 |
| K27 | Bilan du 17 mars 2026 : les camions de Kestrel, partis vers 6 h, livrent normalement ; les six tournées des sous-traitants sont préparées sur papier ; sur environ 1 310 colis traités, 330 partent l'après-midi (25,2 %) ; deux réceptions bloquées jusqu'au lendemain. Arbitrage : remplace « 640 en retard sur 1 100 » (FT 11) et « 180 colis » (FT 18). Garantie de rétablissement de l'opérateur : 8 heures, option 4G non souscrite. | FT 11, 18 |
| K28 | Journal des incidents de 2025 : INC-1 mars, StockFlow indisponible 3 h chez l'éditeur, 400 commandes retardées ; INC-2 mai, temps de conduite mal ressaisis, 14 chauffeurs ; INC-3 juin, fichier des tournées de Clermont-Ferrand envoyé à l'extérieur, 870 destinataires exposés (arbitrage : 640 était déjà employé pour des colis) ; INC-4, coupure de RES-02 de novembre (K26) ; INC-5 novembre, livraison contestée, compte KDriver partagé d'un sous-traitant, avoir de 420 € ; INC-6 décembre, grille tarifaire modifiée avec le compte générique, 212 factures. Plus longues interruptions de 2025 : StockFlow 3 h, Kestrel Track 5 h, KDriver 2 h, Portail EDI 1 h 30, RES-02 7 h 30. | FT 12 |
| K29 | Fraude au RIB des salariés : 15 demandes de changement de septembre 2025 à février 2026, dont 5 frauduleuses ; un salaire de 2 400 € détourné en janvier 2026. Distincte de la tentative de septembre 2025 sur un fournisseur (fiche Kestrel). | FT 13 |
| K30 | Février 2026 : un e-commerçant reçoit un faux courriel du service facturation de Kestrel lui demandant un nouveau RIB ; il rappelle Kestrel, la fraude échoue. | FT 14, 15 |
| K31 | Site web : faille critique d'une extension du formulaire publiée en février 2026, non corrigée ; contrat de maintenance de l'agence web terminé en 2024. | FT 10, 13 |
| K32 | StockFlow en 2026 : interruptions de 0,5 h (janvier), 3,5 h (un seul incident le 24 mars, de 9 h à 12 h 30, distinct de la coupure du 17 mars), 1 h (mai), 0,5 h (juillet), 2,5 h (septembre). Contrat : 99,7 % par mois hors maintenance du dimanche de 1 h à 5 h, aucun délai de rétablissement, sauvegarde toutes les 4 heures conservée 30 jours. Contrat de la paie : 99,5 % par mois, rétablissement en 3 jours ouvrés, sauvegarde quotidienne à 23 h ; besoin de fin de mois (du 24 au dernier jour ouvré) : 24 h d'arrêt, 24 h de données. | FT 18 |
| K33 | Moirans : 23 colis de valeur (600 € pièce) préparés mais jamais livrés en 2025 (4, 3, 9, 7 par trimestre) ; écarts d'inventaire 2026 : 1,8 ; 1,5 ; 1,9 ; 0,7 ; 0,5 ; 0,4 k€ de janvier à juin. Compte d'administration de StockFlow protégé par un simple mot de passe. | FT 14, 15, 16 |
| K34 | SAL-01 a dépassé 30 °C deux après-midi en juillet 2026 ; un seul groupe froid. | FT 19 |

## 5. Diagnostic, environnement et DSI

| N° | Fait canonique | Fiches |
| --- | --- | --- |
| K35 | Développeurs : deux sur Kestrel Track, un sur KDriver (seul à savoir publier une version ; documentation de deux pages), un sur les interfaces ; les deux administrateurs se remplacent pour les sauvegardes, pas pour le réseau ; 3 compétences critiques sur 9 portées par une seule personne ; 0,8 jour de formation par salarié de la DSI en 2025 ; délai moyen de résolution des tickets 1,6 jour. | FT 20 |
| K36 | Données : adresse saisie dans RoutePro, StockFlow et Kestrel Track ; 1,2 % des livraisons en seconde présentation pour adresse erronée, 4,80 € l'une ; disponibilité de Kestrel Track de janvier à septembre 2026 : 99,4 %. Notes de maturité : gouvernance 1, organisation 2, applications 2, données 1, infrastructure 2 (sauvegarde nocturne selon H1, non isolée, sans test documenté), sécurité 2, compétences 2, budget 2. | FT 20 |
| K37 | Environnement : délai de recrutement d'un chauffeur de 28 jours (2021) à 58 jours (2026) ; J+1 assuré dans 9 départements sur 12 en 2025 ; hausse de 12 % de l'abonnement de StockFlow au 1er janvier 2027 ; base de veille V1 à V6. | FT 19 |

## 6. Accords avec le cours vérifiés

| N° | Point | Fiches |
| --- | --- | --- |
| K38 | Les échelles G1 à G4 et V1 à V4, la matrice et le seuil d'acceptation sont repris mot pour mot du ch05. Arbitrage : l'extrait de FT 14, reformulé, est rétabli dans les termes du cours, et ses corrigés citent les descripteurs exacts. | FT 13, 14, 16 |
| K39 | Hypothèses du registre H1 à H19 jamais présentées comme des faits : H1 appuyée pour l'ERP finance seulement (FT 10) ; H6 appuyée par un entretien (FT 17) ; H10 établie par le journal pour un seul sous-traitant, le numéro restant inchangé (FT 12) ; H15 rendue plausible, non confirmée (FT 17) ; H3 aggravée par FR-07 (FT 11). | FT 10, 11, 12, 17, 20 |
| K40 | Dates techniques : SQL Server 2016 hors support depuis le 14 juillet 2026 ; Django 3.2 hors support depuis avril 2024 ; numérotation OWASP du ch07 (LLM03 capacité d'agir excessive, LLM08 exposition du contexte caché). | FT 05, 06, 17, 20, 21 |
| K41 | Dates des annexes antérieures ou égales au mois de la situation. Arbitrage : FT 03 (annexe 4 datée de mai 2026) et FT 04 (article de février 2026). | FT 03, 04 |

## Numéros attribués par les fiches, à poursuivre sans collision

| Série | Cours | Fiches | Prochain numéro libre |
| --- | --- | --- | --- |
| Flux | FLX-01 à FLX-06 | FLX-07 à FLX-09 (FT 10) | FLX-10 |
| Franchissements | FR-01 à FR-06 | FR-07 (FT 11) | FR-08 |
| Liens et réseaux | RES-01 à RES-03 | RES-04, RES-05 (FT 11) | RES-06 |
| Postes et terminaux | TRM-01 à TRM-06 | TRM-07 (FT 11) | TRM-08 |
| Stockage | STO-01, STO-02 | STO-03 (FT 11) | STO-04 |
| Valeurs métier | VM1 à VM5 | VM6, VM7 (FT 14) | VM8 |
| Événements redoutés | ER1 à ER6 | ER7 à ER10 (FT 14), ER11 (FT 16) | ER12 |
| Couples SR/OV | SR1 à SR6 | SR7 à SR12 (FT 14) | SR13 |
| Scénarios | SS1 à SS4, SO1 à SO4 | SS5, SO5 (FT 15) | SS6, SO6 |
| Risques | R1 à R4 | R5 à R8 (FT 16) ; RA à RD hors étude (FT 13) | R9 |
| Mesures | M1 à M14 | M15 à M22 (FT 16) | M23 |
| Faiblesses | F1 à F7 | F8 à F11 (FT 20) | F12 |
| Demandes de projets | aucune | D1 à D8 (FT 05, 06) | D9 |
| Incidents de 2025 | aucun | INC-1 à INC-6 (FT 12) | INC-7 |
| Hypothèses | H1 à H19 | aucune nouvelle | H20 |
