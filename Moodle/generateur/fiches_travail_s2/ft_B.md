# FT 06 | Gouverner le SI : instances, règles et portefeuille de projets | 2

@situation
En avril 2026, vous êtes en alternance auprès d'Hélène Garnier, directrice des SI de Kestrel Logistique. Sept demandes de projets attendent une décision, et leur total dépasse l'enveloppe de l'année. Isabelle Roux, la directrice administrative et financière, veut présenter au comité de direction de mai une méthode d'arbitrage écrite. Elle vous demande de tester la grille proposée par la DSI et d'en tirer les enseignements sur la gouvernance du SI.

@capacites
Repérer les acteurs et les instances de décision
Calculer un score pondéré et classer un portefeuille
Distinguer gouvernance et management du SI
Argumenter auprès d'une direction

@duree 60 minutes

@annexe 1 | « Je n'ai aucun moyen de dire laquelle passe avant l'autre » | Courriel fictif d'Hélène Garnier à Isabelle Roux, avril 2026
Isabelle, voici où nous en sommes avant le comité de mai. Depuis le comité de février, aucune des cinq demandes présentées n'a été lancée. Le devis de l'outil de relation client est arrivé, à 38 k€, mais personne ne l'a signé. Le module d'optimisation de RoutePro, jugé prioritaire en février « car il sert Cap 2029 », attend toujours son passage en comité, faute de devis à l'époque. La migration de Kestrel Track a été reportée « puisque l'application fonctionne », alors que Paul Vidal rappelait que notre client principal de la grande distribution, qui renégocie son contrat en juin, veut « du concret sur le suivi ».

Deux demandes nouvelles sont arrivées. Après la coupure de six heures de la fibre de Clermont-Ferrand en mars, le responsable de l'agence demande un lien 4G de secours ; Romain propose d'équiper aussi Moirans. Le chef de quai de Saint-Priest demande le remplacement de 20 scanners dont les batteries ne tiennent plus une demi-journée.

Les demandes m'arrivent par courriel, au téléphone ou dans le couloir. Je n'ai aucun moyen de dire au comité laquelle passe avant l'autre, sinon mon intuition. Le comité de mars n'a pas eu de point SI, faute de temps. J'ai fait chiffrer toutes les demandes : leur total dépasse l'enveloppe de projets de 2026, qui est de 260 k€.

Je te propose de présenter au comité une grille de cotation écrite, validée par Paul Vidal, puis de classer toutes les demandes avec elle. Je souhaite aussi que le comité fasse un point SI chaque trimestre pour suivre les projets retenus. Peux-tu porter le sujet ?

@annexe 2 | Le portefeuille des demandes et la grille de cotation proposée | Document fictif de la DSI, avril 2026
| Demande | Porteur | Objet concerné | Coût 2026 | Cap 2029 (40 %) | Risque (30 %) | Urgence (20 %) | Facilité (10 %) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D1 Module d'optimisation des tournées | Sébastien Morin | APP-01 RoutePro | 95 k€ | 4 | 1 | 1 | 2 |
| D2 Migration vers une version maintenue de Django | Hélène Garnier | APP-03 Kestrel Track | 70 k€ | 3 | 4 | 3 | 2 |
| D3 Outil de relation client | Léa Fontaine | Nouvelle application | 38 k€ | 3 | 1 | 2 | 4 |
| D4 Authentification multifacteur pour tous | Romain Chevalier | APP-10 Microsoft 365, SEC-01 Passerelle VPN | 18 k€ | 1 | 4 | 3 | 4 |
| D5 Interface entre TeleFleet et la paie | Nicolas Perrin | APP-05 TeleFleet, APP-08 Paie | 25 k€ | 1 | 2 | 1 | 3 |
| D6 Liens 4G de secours à Clermont-Ferrand et Moirans | Responsable de l'agence de Clermont-Ferrand | RES-01 VPN Moirans, RES-02 VPN Clermont | 12 k€ | 2 | 3 | 2 | 4 |
| D7 Remplacement de 20 scanners des quais | Chef de quai de Saint-Priest | TRM-01 Scanners des quais | 45 k€ | 2 | 2 | 2 | 3 |

Chaque critère est noté de 1 (faible) à 4 (fort) ; le poids figure entre parenthèses. « Cap 2029 » mesure la contribution aux quatre objectifs du plan ; « Risque », la réduction d'un risque de sécurité ou de continuité ; « Urgence », une échéance contractuelle, réglementaire ou technique ; « Facilité », la simplicité de mise en œuvre. Le score pondéré est la somme des notes multipliées par leur poids. En cas d'égalité, la demande la mieux notée sur Cap 2029 passe devant. Les demandes sont retenues dans l'ordre du classement tant que l'enveloppe le permet ; une demande qui la ferait dépasser est écartée, et l'on examine la suivante.

@annexe 3 | Demandes de projets SI reçues par la DSI en 2025, selon le canal | Relevé fictif de la DSI à partir de sa messagerie et de l'outil de tickets, mars 2026
@graphique barres demandes
Courriel : 14
À l'oral : 9
En comité : 4
Outil de tickets : 3

@question 1 | Identifier | Annexe 1, cours (chapitre 2)
Relevez les acteurs et les instances qui interviennent aujourd'hui dans la décision sur les projets SI de Kestrel. Qui décide, à quel rythme, et que devient une demande entre deux comités ?
@lignes 5

@question 2 | Calculer | Annexe 3
Calculez la part des demandes de 2025 arrivées hors d'un canal formel (le comité de direction et l'outil de tickets sont les deux seuls canaux formels). Que révèle ce chiffre sur le recensement du portefeuille ?
@lignes 3

@question 3 | Calculer | Annexe 2
Calculez le score pondéré de chaque demande, puis classez-les. Calculez enfin le coût total des sept demandes et son dépassement par rapport à l'enveloppe.
@tableau
| Demande | Calcul du score pondéré | Score | Rang |
| --- | --- | --- | --- |
| D1 | | | |
| D2 | | | |
| D3 | | | |
| D4 | | | |
| D5 | | | |
| D6 | | | |
| D7 | | | |
| Coût total et dépassement de l'enveloppe | | | |

@question 4 | Analyser | Annexe 2
Appliquez la règle de sélection de la grille. Quelles demandes sont retenues, pour quel montant total ? Laquelle est écartée ? Commentez le sort de D5, la demande la plus mal notée.
@lignes 5

@question 5 | Analyser | Annexes 1 et 2, cours
Comparez ce classement aux décisions du comité de février rappelées dans l'annexe 1. Sur quelle demande l'écart est-il le plus net, et qu'est-ce qui l'explique ?
@lignes 5

@question 6 | Mobiliser | Cours, chapitre 2
Pour chaque action, dites si elle relève de la gouvernance ou du management du SI. Pour la gouvernance, précisez le verbe de la norme ISO/IEC 38500 (évaluer, diriger, surveiller).
@tableau
| Action | Gouvernance ou management | Verbe ou nature de l'activité |
| --- | --- | --- |
| Le comité compare les demandes et leurs risques avant d'arbitrer | | |
| Le comité impose de coter toute demande de plus de 10 k€ avec la grille | | |
| Romain Chevalier active l'authentification multifacteur sur les comptes | | |
| Le comité examine chaque trimestre l'avancement et le coût des projets | | |
| La DSI rédige le cahier des charges du lien 4G | | |

@question 7 | Argumenter | Toutes les annexes
Rédigez pour Isabelle Roux une note d'une dizaine de lignes : ce que la grille et le point SI trimestriel apportent à la gouvernance de Kestrel, et les limites de la grille dont le comité doit avoir conscience.
@lignes 10

@retiens
La [[gouvernance]] du SI fixe les orientations, arbitre et contrôle ; le [[management]] planifie, construit et exploite dans ce cadre. La norme ISO/IEC 38500 la résume en trois verbes : [[évaluer]], [[diriger]] et [[surveiller]]. Gérer le [[portefeuille de projets]], c'est recenser toutes les demandes, les évaluer selon des [[critères]] communs et écrits, les classer, puis [[suivre]] les projets retenus. Sans ce dispositif, le plus [[insistant]] l'emporte.

@corrige 1
Aucune instance n'est dédiée au SI : les projets sont arbitrés par le comité de direction mensuel (Paul Vidal, Isabelle Roux, Sébastien Morin, Léa Fontaine, Nicolas Perrin), où Hélène Garnier n'est qu'invitée pour le point SI. Le rythme est irrégulier : le comité de mars n'a eu aucun point SI « faute de temps », et le module d'optimisation attend depuis février. Entre deux comités, une demande n'existe que dans la messagerie de la DSI : elle n'est ni recensée dans une liste commune, ni cotée, ni suivie, et même une décision prise (l'outil de relation client) n'est pas exécutée faute de signature. Notion mobilisée : chapitre 2, « Les acteurs et les instances de la gouvernance » (comité stratégique, comité de pilotage, comité de portefeuille).

@corrige 2
Demandes reçues hors canal formel : 14 + 9 = 23 sur 14 + 9 + 4 + 3 = 30, soit 23 / 30 = 76,7 %. Plus des trois quarts des demandes n'apparaissent dans aucun outil ni compte rendu : la DSI ne peut ni les dénombrer de façon fiable, ni les comparer, ni rendre compte de leur sort. Il n'existe pas de recensement du portefeuille, première étape de sa gestion (chapitre 2, « La gestion de portefeuille de projets est souvent le maillon manquant »).

@corrige 3
| Demande | Calcul du score pondéré | Score | Rang |
| --- | --- | --- | --- |
| D1 | 4 × 0,4 + 1 × 0,3 + 1 × 0,2 + 2 × 0,1 = 1,6 + 0,3 + 0,2 + 0,2 | 2,3 | 4 |
| D2 | 3 × 0,4 + 4 × 0,3 + 3 × 0,2 + 2 × 0,1 = 1,2 + 1,2 + 0,6 + 0,2 | 3,2 | 1 |
| D3 | 3 × 0,4 + 1 × 0,3 + 2 × 0,2 + 4 × 0,1 = 1,2 + 0,3 + 0,4 + 0,4 | 2,3 | 5 |
| D4 | 1 × 0,4 + 4 × 0,3 + 3 × 0,2 + 4 × 0,1 = 0,4 + 1,2 + 0,6 + 0,4 | 2,6 | 2 |
| D5 | 1 × 0,4 + 2 × 0,3 + 1 × 0,2 + 3 × 0,1 = 0,4 + 0,6 + 0,2 + 0,3 | 1,5 | 7 |
| D6 | 2 × 0,4 + 3 × 0,3 + 2 × 0,2 + 4 × 0,1 = 0,8 + 0,9 + 0,4 + 0,4 | 2,5 | 3 |
| D7 | 2 × 0,4 + 2 × 0,3 + 2 × 0,2 + 3 × 0,1 = 0,8 + 0,6 + 0,4 + 0,3 | 2,1 | 6 |
| Coût total et dépassement de l'enveloppe | 95 + 70 + 38 + 18 + 25 + 12 + 45 = 303 k€ ; 303 − 260 = 43 k€ ; 43 / 260 = 16,5 % | 303 k€ ; + 43 k€ (16,5 %) | |

D1 et D3 sont à égalité (2,3) : la règle d'égalité place D1 devant, car il est noté 4 sur Cap 2029 contre 3 pour D3.

@corrige 4
Cumul dans l'ordre du classement : D2, 70 k€ ; D4, 88 k€ ; D6, 100 k€ ; D1, 195 k€ ; D3, 233 k€. D7 ferait passer le cumul à 278 k€ : elle est écartée. D5 porte le cumul à 233 + 25 = 258 k€, sous l'enveloppe : elle est retenue. Six demandes sont donc retenues pour 258 k€, il reste 2 k€ ; seule D7 (45 k€) est écartée. Le sort de D5 montre un effet mécanique de la règle : la demande la moins prioritaire passe parce qu'elle est peu chère, alors que la sixième (D7) attend. Le comité doit décider s'il accepte cet effet ou s'il préfère réserver le reliquat (27 k€ après D3) à une partie de D7. C'est une décision de gouvernance, que la grille éclaire mais ne prend pas.

@corrige 5
L'écart le plus net porte sur D2, la migration de Kestrel Track : reportée en février « puisque l'application fonctionne », elle arrive en tête avec 3,2. La grille rend visibles deux critères que le comité n'avait pas pesés : le risque (Django 3.2 hors support depuis avril 2024, sur une application exposée au public, selon le cours) et l'urgence (le client principal de la grande distribution renégocie en juin et veut « du concret sur le suivi », annexe 1). À l'inverse, D1, jugé prioritaire « car il sert Cap 2029 », n'est que quatrième : il sert la stratégie mais ne réduit aucun risque et n'a pas d'échéance. En février, le critère implicite était la contribution à Cap 2029, appliqué à D1 et pas à D2 ; la grille impose les mêmes critères à toutes les demandes. On accepte aussi la remarque que D4, MFA, passe de « sans coût supplémentaire » à une demande chiffrée et classée deuxième.

@corrige 6
| Action | Gouvernance ou management | Verbe ou nature de l'activité |
| --- | --- | --- |
| Le comité compare les demandes et leurs risques avant d'arbitrer | Gouvernance | Évaluer |
| Le comité impose de coter toute demande de plus de 10 k€ avec la grille | Gouvernance | Diriger (fixer une politique) |
| Romain Chevalier active l'authentification multifacteur sur les comptes | Management | Bâtir et exploiter (mise en œuvre technique) |
| Le comité examine chaque trimestre l'avancement et le coût des projets | Gouvernance | Surveiller |
| La DSI rédige le cahier des charges du lien 4G | Management | Planifier et acquérir |

Justification : la gouvernance relève des instances dirigeantes et porte sur les orientations, les arbitrages et le contrôle ; le management agit dans le cadre ainsi fixé (chapitre 2, définition de la gouvernance du SI, ISO/IEC 38500 troisième édition, 2024, et COBIT 2019).

@corrige 7
Éléments attendus. La grille apporte des critères écrits et communs, appliqués à toutes les demandes, ce qui rend l'arbitrage explicable et contestable sur pièces ; elle oblige à chiffrer et à recenser (aujourd'hui 76,7 % des demandes arrivent hors canal formel) ; elle fait apparaître le risque, absent des décisions de février (D2, D4). Le point SI trimestriel installe le « surveiller » qui manque : suivre l'avancement et le coût des projets retenus, et vérifier que les décisions sont exécutées (le devis signé de l'outil de relation client). Limites : les poids et les notes restent des jugements qu'il faut justifier par des faits ; la règle de sélection a des effets mécaniques (D5 retenue avant D7) ; la grille ne remplace ni la décision du comité ni un schéma directeur, qui fixerait la cible à trois ou cinq ans. Une conclusion attendue : faire valider la grille par Paul Vidal, puis la réviser après un an. Barème indicatif sur 5 points : apports de la grille (1,5), apport du suivi trimestriel (1), limites (1,5), usage d'au moins deux chiffres des annexes et qualité de rédaction (1).

# FT 07 | Urbaniser : redondances, trous et flux manuels | 2

@situation
En mai 2026, vous êtes en stage à la DSI de Kestrel Logistique et vous aidez à compléter la vue fonctionnelle de la cartographie. Le plan d'urbanisation a été construit au siège ; il n'a jamais été confronté au travail réel de l'agence de Clermont-Ferrand. Vous avez interrogé le responsable de l'agence. Il vous faut maintenant classer ce que vous avez appris avec les définitions du cours, sans confondre redondance, trou, flux manuel et défaut de donnée de référence.

@capacites
Relever les fonctions et les outils dans un entretien
Appliquer les définitions de redondance, trou et flux manuel
Calculer le coût d'un flux manuel et l'évolution d'un indicateur
Hiérarchiser des constats de vue fonctionnelle

@duree 60 minutes

@annexe 1 | Entretien avec le responsable de l'agence de Clermont-Ferrand | Compte rendu fictif d'entretien, DSI de Kestrel Logistique, mai 2026, validé par l'interlocuteur
« Chaque nuit, la navette de Saint-Priest nous apporte les palettes ; s'y ajoutent quelques enlèvements locaux. Les agents de quai les réceptionnent avec leurs scanners dans StockFlow, puis les trient pour l'expédition ; nous n'entreposons rien. Pour les envois locaux, nous imprimons un bordereau d'expédition depuis StockFlow, alors que la lettre de voiture du même envoi est éditée dans RoutePro. Les deux documents n'indiquent pas toujours le même poids.

Les réclamations des clients, colis abîmés ou manquants, arrivent par courriel ou par téléphone. L'assistante d'exploitation les note dans un fichier Excel « Litiges Clermont », enregistré sur mon poste et partagé avec l'équipe, et les suit par courriel avec le client. Ce fichier n'est pas inscrit à l'inventaire de la DSI. En mars, la coupure de notre liaison avec le siège nous a obligés à travailler sur papier toute une matinée : les réclamations ont suivi.

Chaque début de mois, j'exporte de StockFlow la liste des colis gardés en instance à l'agence pour nos clients e-commerçants (refusés ou en attente de retour). Le service comptable de Saint-Priest la ressaisit dans l'ERP finance pour facturer les frais de garde : environ trois heures de travail par mois. En 2025, 9 factures de frais de garde sur 150 ont dû être corrigées.

Le planning des agents de quai est tenu sur un tableau blanc ; je le recopie chaque vendredi dans un courriel. Un client est créé deux fois : dans l'ERP finance pour la facture, dans StockFlow pour la réception et l'expédition de ses colis. Enfin, les planificateurs du siège m'ont dit qu'ils suivent la position des camions sur la carte de Kestrel Track, alimentée par KDriver, alors que l'exploitation la suit dans TeleFleet. »

@annexe 2 | Extrait de l'inventaire applicatif (annexe A) | Inventaire applicatif de la DSI, version de travail de mai 2026, document fictif
| Application | Fonctions déclarées |
| --- | --- |
| APP-01 RoutePro | Ordres de transport, affectation aux tournées, lettres de voiture |
| APP-02 StockFlow | Réception, stockage, préparation, bordereaux d'expédition |
| APP-03 Kestrel Track | Suivi des colis, portail B2B, carte de position des camions |
| APP-04 KDriver | Tournée, preuve de livraison, position du terminal |
| APP-05 TeleFleet | Position GPS, conduite, consommation |
| APP-07 ERP finance | Comptabilité, facturation clients, achats |
| APP-10 Microsoft 365 | Bureautique, messagerie |

Les autres applications du parc (APP-06, APP-08, APP-09, APP-11, APP-12) n'ont aucun rôle à l'agence. Aucun fichier propre à l'agence n'est inscrit à l'inventaire.

@annexe 3 | Réclamations enregistrées par l'agence de Clermont-Ferrand en 2026 | Décompte fictif établi à partir du fichier « Litiges Clermont », mai 2026
@graphique barres réclamations
Janvier : 42
Février : 38
Mars : 51
Avril : 47
Mai : 55

@annexe 4 | Le circuit de facturation des frais de garde | Schéma de travail fictif de la DSI, mai 2026
@schema
APP-02 StockFlow -> [[Export mensuel des colis en instance]] -> [[Ressaisie par la comptabilité]] -> APP-07 ERP finance

@question 1 | Identifier | Annexes 1 et 2
Pour chaque fonction exercée à l'agence, relevez l'outil utilisé et dites s'il est inscrit à l'annexe A comme application.
@tableau
| Fonction | Outil ou moyen utilisé aujourd'hui à l'agence | Inscrit à l'annexe A ? |
| --- | --- | --- |
| Réceptionner les palettes | | |
| Éditer les documents de transport | | |
| Traiter les réclamations des clients | | |
| Facturer les frais de garde | | |
| Planifier les équipes de quai | | |
| Suivre la position des camions | | |

@question 2 | Mobiliser | Annexes 1 et 2, cours
Classez chaque situation : redondance, trou, flux manuel ou défaut de donnée de référence. Justifiez en une phrase avec la définition.
@tableau
| Situation | Catégorie (redondance, trou…) | Justification par la définition du cours |
| --- | --- | --- |
| RoutePro et StockFlow éditent chacun un document de transport | | |
| Les réclamations sont suivies dans un fichier Excel et par courriel | | |
| La liste des colis en instance passe de StockFlow à l'ERP finance par ressaisie | | |
| Un client est créé dans l'ERP finance et dans StockFlow | | |
| La position des camions est suivie dans TeleFleet et dans Kestrel Track | | |
| Le planning des agents de quai est tenu sur un tableau blanc | | |

@question 3 | Analyser | Annexes 1 et 2
Le responsable de l'agence objecte : « Les réclamations ne sont pas un trou, puisque Microsoft 365 est à l'inventaire et que nous avons un fichier. » Répondez-lui. À quelle condition le fichier « Litiges Clermont » cesserait-il d'être un trou, et que deviendrait-il ?
@lignes 5

@question 4 | Analyser | Annexe 4
Complétez le schéma de l'annexe 4. Dites ensuite où ce flux se note dans le dossier de cartographie et comment il se distingue sur la vue applicative.
@lignes 3

@question 5 | Calculer | Annexes 1 et 3
Calculez les indicateurs suivants. Arrondissez au dixième.
@tableau
| Indicateur | Calcul posé avec les valeurs des annexes | Résultat arrondi |
| --- | --- | --- |
| Taux de factures de frais de garde corrigées en 2025 | | |
| Temps annuel consacré à la ressaisie | | |
| Moyenne mensuelle des réclamations, de janvier à mai | | |
| Évolution des réclamations de janvier à mai | | |

@question 6 | Analyser | Annexes 1 et 3
Comment expliquez-vous le pic de mars ? Que ne permet pas de savoir l'absence d'application pour les réclamations ?
@lignes 4

@question 7 | Argumenter | Toutes les annexes
Rédigez le paragraphe de constats de la cartographie pour l'agence de Clermont-Ferrand (vue fonctionnelle et matrice des flux). Classez les constats du plus important au moins important et justifiez cet ordre par des faits chiffrés.
@lignes 10

@retiens
Une [[redondance]] : deux applications inscrites à l'[[annexe A]] assurent la même fonction. Un [[trou]] : une fonction qu'aucune application de l'annexe A ne soutient spécifiquement ; la présence de la [[messagerie]] ou de la suite bureautique ne le comble pas. Une ressaisie entre deux applications est un [[flux manuel]], noté dans la [[matrice des flux]]. Une même donnée de référence saisie dans des applications de fonctions différentes est un [[défaut de donnée de référence]], signalé dans les [[constats]].

@corrige 1
| Fonction | Outil ou moyen utilisé | Inscrit à l'annexe A ? |
| --- | --- | --- |
| Réceptionner les palettes | APP-02 StockFlow, avec les scanners | Oui |
| Éditer les documents de transport | APP-02 StockFlow (bordereau) ; APP-01 RoutePro (lettre de voiture) | Oui, les deux |
| Traiter les réclamations des clients | Fichier Excel « Litiges Clermont » et courriels | Non (seule la messagerie est inscrite, pas le fichier) |
| Facturer les frais de garde | Export de StockFlow, ressaisie dans APP-07 ERP finance | Oui, les deux applications |
| Planifier les équipes de quai | Tableau blanc, puis courriel | Non |
| Suivre la position des camions | APP-05 TeleFleet ; APP-03 Kestrel Track alimentée par APP-04 KDriver | Oui, les deux |

@corrige 2
| Situation | Catégorie | Justification |
| --- | --- | --- |
| RoutePro et StockFlow éditent chacun un document de transport | Redondance | Deux applications de l'annexe A assurent la même fonction, « éditer les documents de transport » |
| Les réclamations sont suivies dans un fichier Excel et par courriel | Trou | Aucune application de l'annexe A ne soutient la fonction ; le fichier n'est pas inscrit et la messagerie ne comble pas un trou |
| La liste des colis en instance passe de StockFlow à l'ERP finance par ressaisie | Flux manuel | Ressaisie entre deux applications de fonctions différentes ; à noter dans la matrice des flux |
| Un client est créé dans l'ERP finance et dans StockFlow | Défaut de donnée de référence | Même donnée de référence saisie dans deux applications qui servent des fonctions différentes (facturer ; réceptionner et expédier) |
| La position des camions est suivie dans TeleFleet et dans Kestrel Track | Redondance | Deux applications de l'annexe A servent la même fonction, « suivre la position des camions » |
| Le planning des agents de quai est tenu sur un tableau blanc | Trou | Fonction faite à la main, sans application inscrite à l'annexe A |

Notion : définitions communes du kit, chapitre 2 (méthode du plan d'urbanisation, étape 5) et chapitre 3 (« Les quatre niveaux du référentiel et la vue fonctionnelle »).

@corrige 3
L'objection ne tient pas. La présence de Microsoft 365 à l'annexe A ne comble pas un trou : la messagerie et le tableur transportent l'information sans rendre la fonction « traiter les réclamations ». Le fichier « Litiges Clermont » n'est inscrit nulle part (annexe 2 : « aucun fichier propre à l'agence n'est inscrit ») : c'est de la seule bureautique. Si la DSI l'inscrivait à l'annexe A comme application, au besoin comme usage hors inventaire, il ne serait plus un trou : il serait placé sur le bloc « Traiter les réclamations » comme application à couverture fragile, ce qu'il faudrait signaler. Inscrire le fichier ne corrige rien ; cela rend le constat exact.

@corrige 4
Boîtes à compléter : « Export mensuel des colis en instance » puis « Ressaisie par la comptabilité ». L'ERP finance produit ensuite la facture des frais de garde. C'est un flux manuel d'APP-02 StockFlow vers APP-07 ERP finance : il se note dans la matrice des flux (annexe B du D2) avec ses sept champs, mode « manuel », fréquence mensuelle, protection du canal « non documentée », puisque l'annexe ne dit pas comment l'export parvient à la comptabilité. Sur la vue applicative, il se dessine en trait pointillé, selon la légende commune (chapitre 3, « Le modèle de cartographie »). Ce n'est ni une redondance ni un trou.

@corrige 5
| Indicateur | Calcul | Résultat |
| --- | --- | --- |
| Taux de factures de frais de garde corrigées en 2025 | 9 / 150 × 100 | 6,0 % |
| Temps annuel consacré à la ressaisie | 3 h × 12 mois | 36 heures |
| Moyenne mensuelle des réclamations, de janvier à mai | (42 + 38 + 51 + 47 + 55) / 5 = 233 / 5 | 46,6 réclamations |
| Évolution des réclamations de janvier à mai | (55 − 42) / 42 × 100 | + 31,0 % |

@corrige 6
Le pic de mars (51 réclamations, contre 38 en février) coïncide avec la coupure de la liaison avec le siège : l'agence a travaillé une matinée sur papier, d'où probablement des erreurs et des retards. L'explication reste une hypothèse : le fichier ne permet pas de la vérifier. Faute d'application, on ne sait pas classer les réclamations par cause, mesurer leur délai de traitement, ni les rattacher à un envoi, à une tournée ou à un client. Un trou se paie aussi en pilotage : la hausse de 31 % ne peut pas être expliquée par des faits.

@corrige 7
Éléments attendus, dans un ordre justifié. Premier constat : le flux manuel StockFlow vers ERP finance touche la facturation ; il coûte 36 heures par an et a produit 6 % de factures corrigées, avec un effet direct sur le chiffre d'affaires et la relation client. Deuxième : le trou « Traiter les réclamations », sur une activité en hausse de 31 % depuis janvier, sans traçabilité ni indicateur. Troisième : la redondance des documents de transport, qui produit des documents contradictoires sur le poids. Quatrième : la redondance de la position des camions et le trou du planning des équipes de quai, moins graves. Le défaut de donnée de référence sur le client est signalé à part, dans les constats de la section 2.8. Un autre ordre est accepté s'il est justifié par des faits. Le paragraphe ne propose pas de solution : il constate (chapitre 2, l'urbanisation sert à repérer les écarts). Barème indicatif sur 5 points : quatre catégories exactes (2), hiérarchie justifiée par au moins deux chiffres (2), absence de solution imposée et rédaction (1).

# FT 08 | Cadrer une cartographie selon la démarche de l'ANSSI | 3

@situation
En février 2026, Kestrel Logistique prépare la version 2 de sa cartographie. La version 1.0, construite par Romain Chevalier après la panne de RoutePro de novembre 2024, ne comporte pas encore de vue métier ni de vue des infrastructures logiques. Le chef de projet applicatif a rédigé un projet de note de cadrage. Romain Chevalier, qui vous accueille en alternance, vous demande de le confronter à la démarche du guide de l'ANSSI avant qu'il parte en comité de direction.

@capacites
Situer un document dans les cinq étapes du guide de l'ANSSI
Identifier le sponsor et le pilote d'une cartographie
Estimer la charge d'un projet de cartographie
Distinguer granularité et maturité
Exploiter l'existant et vérifier l'outil et la protection retenus
Proposer une cible et une trajectoire réalistes

@duree 75 minutes

@annexe 1 | Projet de note de cadrage « Cartographie du SI, version 2 » | Document fictif rédigé par le chef de projet applicatif de Kestrel Logistique, janvier 2026
1. Enjeux. Disposer d'une cartographie complète du SI pour préparer le futur schéma directeur.

2. Pilotage. Le projet est porté par la DSI. Un sponsor n'est pas nécessaire, le sujet étant technique. Les directions métier seront informées à la livraison.

3. Cible et calendrier. Les six vues du guide de l'ANSSI seront produites en une seule fois, toutes à la granularité la plus fine (niveau 3), pour l'ensemble du SI. Durée : six semaines. Équipe : Romain Chevalier et moi-même, chacun à 20 % de son temps.

4. Existant. Nous repartirons de zéro : les anciens schémas sont périmés.

5. Outil. Les vues seront dessinées dans PowerPoint, que le comité de direction sait lire. L'inventaire sera tenu dans un fichier Excel séparé.

6. Diffusion. La cartographie sera déposée sur un espace SharePoint de Microsoft 365 ouvert à tous les salariés, pour que chacun puisse la consulter.

7. Suite. Après la livraison, la DSI mettra la cartographie à jour quand elle en aura le temps.

@annexe 2 | Définir la cible et la trajectoire | Extrait du guide de l'ANSSI « Cartographie du système d'information. Guide d'élaboration en 5 étapes », version 1.0, novembre 2018 (ANSSI-PA-046), étape 1, p. 14, Licence ouverte
« La définition de la cible consiste à identifier l'ensemble des vues à réaliser ainsi que leur niveau de granularité. La granularité des différentes vues de la cartographie est à adapter au contexte et aux objectifs recherchés. Elle peut donc varier d'un système d'information à l'autre selon sa criticité ou l'importance accordée à celui-ci.

La trajectoire de construction de la cartographie permet de prévoir les différentes itérations et les grands jalons dans l'avancement de la cartographie. Il est recommandé d'adopter une trajectoire progressive basée sur l'atteinte échelonnée de niveaux de maturité croissants.

La définition de la cible et de la trajectoire permet de déterminer les responsabilités des différentes parties prenantes, d'estimer les ressources à prévoir et de définir le calendrier. […] Pour un système d'information de taille importante, il est recommandé de commencer par une cartographie limitée à certaines vues et centrée sur les systèmes critiques ou exposés, qui sera complétée avec d'autres vues par la suite. Pour un SI de petite taille, il est possible de réaliser une cartographie cumulant plusieurs vues dès le départ. »

@annexe 3 | Charge estimée par vue, à la granularité la plus fine | Estimation fictive de Romain Chevalier, en jours-personnes, février 2026
@graphique barres jours-personnes
Écosystème : 4
Métier : 14
Applications : 10
Administration : 6
Infra. logiques : 9
Infra. physiques : 5

@annexe 4 | L'existant disponible au siège | Relevé fictif de la DSI, février 2026
| Document | Auteur | Date | Ce qu'il contient |
| --- | --- | --- | --- |
| Cartographie version 1.0 | Romain Chevalier | 2025 | Écosystème, applications, infrastructures physiques, administration ; registre des hypothèses H1 à H7 |
| Schéma d'installation de RoutePro | PP-05 Éditeur de RoutePro | 2017 | Serveurs et base de données, sans les machines virtuelles actuelles |
| Export de l'outil de tickets | DSI | Janvier 2026 | Inventaire des postes de travail seulement |
| Liste des comptes de SEC-01 Passerelle VPN | Romain Chevalier | Décembre 2025 | Comptes des chauffeurs et des prestataires |
| Besoins de continuité exprimés par les directions | Directions | 2025 | Durée d'arrêt et perte de données tolérées par application |

@question 1 | Identifier | Annexe 1, cours
Rattachez chaque paragraphe de la note à l'étape du guide de l'ANSSI qu'il traite, puis indiquez ce qui manque ou pose problème au regard du guide.
@tableau
| Étape du guide | Paragraphes de la note | Ce qui manque ou pose problème |
| --- | --- | --- |
| 1. Initier la démarche | | |
| 2. Définir le modèle | | |
| 3. Choisir les outils | | |
| 4. Construire pas à pas | | |
| 5. Pérenniser | | |

@question 2 | Analyser | Annexe 1, cours
Qui devrait être le sponsor de la cartographie, qui devrait la coordonner, et pourquoi faut-il associer les directions métier dès le départ ?
@lignes 6

@question 3 | Calculer | Annexes 1 et 3
Calculez la charge totale estimée, la capacité de l'équipe prévue par la note sur six semaines (cinq jours ouvrés par semaine), l'écart entre les deux et la durée qu'il faudrait à cette équipe pour tout produire. Concluez.
@lignes 6

@question 4 | Mobiliser | Annexe 2, cours
Distinguez granularité et maturité. Quel niveau de maturité la note vise-t-elle sans le dire, et quel niveau la version 1.0 a-t-elle probablement atteint ? Justifiez.
@lignes 6

@question 5 | Analyser | Annexe 4
La note propose de « repartir de zéro ». Pour chaque document de l'existant, dites ce qu'il apporte et la précaution à prendre.
@tableau
| Document | Ce qu'il apporte à la version 2 | Précaution à prendre avant de l'utiliser |
| --- | --- | --- |
| Cartographie version 1.0 | | |
| Schéma d'installation de RoutePro | | |
| Export de l'outil de tickets | | |
| Liste des comptes de SEC-01 | | |
| Besoins de continuité | | |

@question 6 | Mobiliser | Annexe 1, cours
Discutez les paragraphes 5 et 6 de la note : l'outil et la diffusion proposés respectent-ils les exigences du guide de l'ANSSI ?
@lignes 6

@question 7 | Proposer | Toutes les annexes
Réécrivez le paragraphe 3 de la note : une cible et une trajectoire en deux itérations, compatibles avec la capacité de l'équipe, avec les vues, la granularité visée et la raison de cet ordre.
@lignes 10

@retiens
La démarche de l'ANSSI compte [[cinq]] étapes : initier, définir le [[modèle]], choisir les outils, construire pas à pas et [[pérenniser]]. Elle est pragmatique, participative et pérenne ; elle est aussi [[incrémentale]], car on ajoute des vues au fil du temps, et [[itérative]], car on affine les vues déjà construites. Les objectifs sont validés par un [[sponsor]], membre de la direction. La [[granularité]] s'applique aux objets et aux attributs, la [[maturité]] à la cartographie entière. La cartographie n'est pas stockée sur le [[SI qu'elle représente]].

@corrige 1
| Étape du guide | Paragraphes de la note | Ce qui manque ou pose problème |
| --- | --- | --- |
| 1. Initier la démarche | 1, 2, 3 | Enjeux réduits au schéma directeur, sans la sécurité ni la gestion de crise qui ont motivé la version 1.0 ; pas de sponsor ; métiers absents ; cible maximale sans trajectoire ; ressources sous-estimées |
| 2. Définir le modèle | 4 (collecte de l'existant) | L'étude de l'existant est écartée ; rien n'est dit du modèle (objets, attributs, légende, nommage) |
| 3. Choisir les outils | 5 | PowerPoint ne tient pas l'inventaire et ne relie pas les vues entre elles ni à l'inventaire tenu à part |
| 4. Construire pas à pas | 3 | Tout en une fois, au lieu d'une construction incrémentale et itérative |
| 5. Pérenniser | 6, 7 | Diffusion sans contrôle d'accès ; stockage sur le SI cartographié ; mise à jour sans responsable, sans rythme, sans déclencheur |

Notion : chapitre 3, « La démarche du guide de l'ANSSI en cinq étapes » ; chapitre 4, « Maintenir et protéger la cartographie ».

@corrige 2
Le guide demande un sponsor membre de la direction, qui valide les objectifs et prend part à la gouvernance du projet. Isabelle Roux, à qui la DSI est rattachée et qui a été sponsor de la version 1.0, est la candidate naturelle ; Paul Vidal convient aussi. La version 2 vise une démarche globale (schéma directeur) qui intègre la sécurité : le guide confie alors le projet au DSI, ici Hélène Garnier, avec le RSSI, Romain Chevalier, comme partie prenante clé ; une démarche purement orientée sécurité serait coordonnée par le RSSI. Le guide insiste pour que les équipes SI et SSI travaillent ensemble. Les métiers doivent être associés dès le départ, car ils sont « propriétaires de leurs processus et de leurs données » : sans Sébastien Morin, la vue métier, qui manque justement, ne peut pas être juste ; leur implication facilite aussi l'adoption. Les informer « à la livraison » est la pire option.

@corrige 3
Charge totale : 4 + 14 + 10 + 6 + 9 + 5 = 48 jours-personnes. Capacité prévue : 2 personnes × 20 % × 30 jours ouvrés (6 semaines × 5 jours) = 12 jours-personnes. Écart : 48 − 12 = 36 jours-personnes ; la charge vaut quatre fois la capacité. Avec cette équipe, il faudrait 48 / (2 × 0,2) = 120 jours ouvrés, soit 24 semaines, environ six mois. Conclusion : la cible de la note est irréalisable dans le délai annoncé. Il faut soit réduire la cible (vues et granularité), soit allonger le calendrier, soit renforcer l'équipe ; le guide recommande d'abord la trajectoire progressive (annexe 2).

@corrige 4
La granularité est le niveau de détail d'un objet ou d'un attribut (niveau 1, indispensable ; 2, important ; 3, utile). La maturité est le niveau atteint par la cartographie entière : niveau 1, premiers éléments indispensables sur un nombre limité de vues ; niveau 2, orientée sécurité, toutes les vues représentées ; niveau 3, exhaustive et détaillée. En demandant les six vues, toutes à la granularité la plus fine, pour tout le SI, la note vise sans le dire la maturité 3, et d'un seul coup. La version 1.0, avec quatre vues sur six, sans vue métier ni vue des infrastructures logiques, relève plutôt de la maturité 1 : elle ne représente pas toutes les vues. Notion : chapitre 3, « Granularité et maturité : les niveaux 1 à 3 ».

@corrige 5
| Document | Ce qu'il apporte | Précaution |
| --- | --- | --- |
| Cartographie version 1.0 | Quatre vues, un modèle, un nommage et un registre d'hypothèses : la base de la version 2 | Vérifier ce qui a changé depuis 2025 ; garder les identifiants et les numéros d'hypothèses |
| Schéma d'installation de RoutePro | L'architecture d'origine de l'application | Daté de 2017 : à recouper, il ignore les machines virtuelles actuelles |
| Export de l'outil de tickets | La liste des postes de travail | Ne couvre ni serveurs ni machines virtuelles : source partielle |
| Liste des comptes de SEC-01 | Les populations qui entrent par la passerelle : utile à la vue de l'administration | Document sensible ; peut confirmer ou infirmer des hypothèses (H5, H9) |
| Besoins de continuité | La criticité par application : aide à choisir quoi cartographier d'abord | Ce sont des besoins exprimés, pas des capacités constatées |

Le guide fait de l'étude de l'existant le début de l'étape 2 : elle accélère la démarche et révèle les premiers manques. « Repartir de zéro » gaspille la version 1.0.

@corrige 6
Outil : le guide attend un outil qui constitue l'inventaire, réalise les vues, représente les liens entre elles et soutient la mise à jour. PowerPoint ne fait rien de cela, et un inventaire Excel séparé ne garantit pas que les noms restent identiques d'une vue à l'autre (objets pivots, élément E8). Les consignes du D2 excluent d'ailleurs PowerPoint. Archi ou draw.io avec une discipline de nommage conviendraient mieux (chapitre 4, « Choisir un outil »). Diffusion : le guide demande de limiter l'accès aux personnes qui ont besoin d'en connaître (la vue métier peut être partagée, les vues d'infrastructure restent à la DSI), et interdit de stocker la cartographie sur le SI qu'elle représente : Microsoft 365 est une application de Kestrel. Un intrus ou un salarié malveillant y trouverait toute l'architecture. Il faut aussi une copie hors ligne, papier comprise, pour la gestion de crise.

@corrige 7
Proposition type, d'autres sont acceptées si elles sont cohérentes. Itération 1 (environ trois mois) : compléter les deux vues manquantes, la vue métier, à granularité 1 puis 2 pour les processus de réalisation, et la vue des infrastructures logiques à granularité 1 ; mettre à jour les quatre vues existantes. Kestrel atteint ainsi la maturité 2 : toutes les vues sont représentées, orientées sécurité. On commence par les systèmes les plus critiques ou exposés (APP-01 RoutePro, APP-03 Kestrel Track, SEC-01 Passerelle VPN), comme le recommande le guide. Itération 2 (environ trois mois) : affiner à granularité 2 ou 3 la vue métier et la vue des applications, utiles au schéma directeur. Charge : environ 20 à 25 jours-personnes par itération, compatible avec 12 jours-personnes par période de six semaines. Sponsor, coordination DSI et RSSI, revue par le comité à chaque jalon. Barème indicatif sur 5 points : deux itérations distinctes (1), vues et granularités précisées (1,5), justification par la criticité ou l'exposition (1), cohérence avec le calcul de la question 3 (1), rédaction (0,5).

# FT 09 | Les vues, les objets pivots et la vue de l'écosystème | 3

@situation
En juin 2026, Romain Chevalier met à jour la vue de l'écosystème de Kestrel Logistique. La version 1.0 recense vingt parties prenantes, mais en décrit seulement une partie en détail. Stagiaire à la DSI, vous êtes chargé de décrire sept autres parties prenantes à partir d'un courriel de la DAF et de la règle de dépendance écrite par Romain. Vous vérifierez aussi que les objets pivots portent le même nom dans tous les documents.

@capacites
Associer une question à la vue qui y répond
Décrire une partie prenante et coter sa dépendance avec une règle écrite
Calculer le poids d'une partie prenante dans le chiffre d'affaires
Repérer un objet pivot mal nommé
Formuler un constat tiré de la vue de l'écosystème

@duree 60 minutes

@annexe 1 | « Ce que je sais de nos contrats » | Courriel fictif d'Isabelle Roux à Romain Chevalier, juin 2026
Romain, voici ce que le registre des contrats dit des partenaires que tu m'as listés.

Les e-commerçants (PP-02) représentent 30 % de notre chiffre d'affaires ; ils suivent leurs envois sur le portail B2B de Kestrel Track. Les particuliers et petites entreprises (PP-03) en font 10 % ; ils nous contactent surtout par le formulaire de devis du site web.

Le prestataire de paie (PP-10) nous fournit la paie en SaaS : il détient les identités, les salaires et les coordonnées bancaires des 300 salariés. Sans lui, nous ne pouvons pas payer, mais l'exploitation continue. L'hébergeur du site web (PP-11) loue un hébergement mutualisé ; si le site tombe, les demandes de devis arrivent par téléphone ou par courriel.

Notre banque (PP-15) exécute les virements aux fournisseurs et les salaires ; nous préparons les fichiers de virement dans l'ERP finance. Vidal Participations (PP-18) détient 100 % du capital et gère la trésorerie du groupe par une convention de trésorerie : sans ses avances, nous ne pourrions plus régler nos fournisseurs au-delà de quelques semaines. Nous lui envoyons chaque mois un reporting financier extrait de l'ERP finance.

Enfin, l'ANSSI (PP-17) : si Kestrel relève de NIS2 au titre des services postaux et d'expédition, nous aurons des obligations de sécurité et de notification des incidents. Le point n'est toujours pas confirmé.

@annexe 2 | La règle de dépendance du modèle de cartographie | Modèle de cartographie de Kestrel, version 1.0, document fictif
| Niveau | Règle |
| --- | --- |
| Forte | La défaillance du partenaire arrête en moins d'une journée un processus de réalisation |
| Moyenne | Sa défaillance arrête un processus de support, ou le partenaire porte plus de 20 % du chiffre d'affaires |
| Faible | Aucun des cas précédents |
| Sans objet | La relation est une obligation légale, non une dépendance d'activité |

Le type de partie prenante se choisit dans une liste fermée : client, usager, fournisseur, sous-traitant, autorité, actionnaire.

@annexe 3 | Trois documents, trois façons de nommer | Relevé fictif établi par la DSI, juin 2026
| Objet | Vue des applications, v1.0 | Tableau des parties prenantes | Registre des contrats |
| --- | --- | --- | --- |
| Logiciel de gestion d'entrepôt | APP-02 StockFlow | Éditeur WMS | StockFlow v4 |
| Paie | APP-08 Paie | Prestataire paie (SaaS) | Logiciel de paie |
| Suivi des colis | APP-03 Kestrel Track | Hébergeur cloud | KTrack |

@annexe 4 | Deux chaînes de dépendance, du processus au fournisseur | Schéma de travail fictif de la DSI, juin 2026
@schema
Payer les salariés -> [[APP-08 Paie]] -> [[PP-10 Prestataire de paie]]
Informer le client du suivi -> APP-03 Kestrel Track -> [[PP-08 Hébergeur cloud de Kestrel Track]]

@question 1 | Identifier | Cours, chapitre 3
Pour chaque question, indiquez la vue du guide de l'ANSSI qui y répond et son objet principal.
@tableau
| Question posée | Vue qui y répond | Objet principal de la vue |
| --- | --- | --- |
| Quels partenaires reçoivent des données de Kestrel ? | | |
| Quelles activités enchaîne la préparation d'une commande, et qui les fait ? | | |
| Quelles applications échangent les preuves de livraison ? | | |
| Qui peut agir sur les serveurs de virtualisation, et par quel accès ? | | |
| Le Wi-Fi des quais est-il séparé du réseau des serveurs ? | | |
| Que perd-on si la salle serveur du siège brûle ? | | |

@question 2 | Analyser | Annexes 1 et 2
Décrivez les sept parties prenantes et cotez leur dépendance en appliquant la règle de l'annexe 2.
@tableau
| Partie prenante | Type (liste fermée) | Nature de la relation | Données ou services échangés | Dépendance selon la règle |
| --- | --- | --- | --- | --- |
| PP-02 E-commerçants | | | | |
| PP-03 Particuliers et petites entreprises | | | | |
| PP-10 Prestataire de paie | | | | |
| PP-11 Hébergeur du site web | | | | |
| PP-15 Banque | | | | |
| PP-17 ANSSI | | | | |
| PP-18 Vidal Participations | | | | |

@question 3 | Calculer | Annexe 1, fiche Kestrel
Le chiffre d'affaires 2025 est de 42 M€. Calculez le chiffre d'affaires apporté par PP-02 et par PP-03. Si le chiffre d'affaires total restait stable, de combien celui des e-commerçants devrait-il augmenter pour atteindre l'objectif de Cap 2029 (40 %) ? Qu'en déduisez-vous pour la dépendance envers PP-02 ?
@lignes 5

@question 4 | Analyser | Annexe 3, cours
Quels objets pivots sont rompus par ces désignations ? Donnez pour chaque objet le nom correct selon la règle de nommage de Kestrel, et expliquez pourquoi la version « v4 » ne doit pas figurer dans le nom.
@lignes 5

@question 5 | Mobiliser | Annexes 1, 3 et 4, cours
Complétez les deux chaînes de l'annexe 4. Indiquez ensuite à quelle vue appartient chaque type de boîte, et quel objet pivot permet de passer de la vue métier à la vue des applications.
@lignes 3

@question 6 | Mobiliser | Annexe 1, cours
Pourquoi l'ANSSI figure-t-elle sur la vue avec la mention « à confirmer » et une dépendance « sans objet », plutôt qu'avec une dépendance faible ?
@lignes 3

@question 7 | Argumenter | Toutes les annexes
Formulez un constat que la vue de l'écosystème rend visible et que le registre des contrats, lu ligne à ligne, ne montre pas. Appuyez-le sur au moins deux parties prenantes et un chiffre.
@lignes 8

@retiens
Une [[vue]] représente le SI selon un point de vue, pour répondre à une question. Le guide de l'ANSSI en définit [[six]], réparties en trois visions : métier, [[applicative]] et infrastructure. Un [[objet pivot]] apparaît dans plusieurs vues sous le [[même nom]] et permet de suivre les [[dépendances]]. La vue de l'[[écosystème]] décrit les entités avec lesquelles le SI interagit : la relation, les données échangées et le niveau de dépendance, fixé par une [[règle écrite]].

@corrige 1
| Question posée | Vue | Objet principal |
| --- | --- | --- |
| Quels partenaires reçoivent des données de Kestrel ? | Écosystème | Entité ou système, relation |
| Quelles activités enchaîne la préparation d'une commande, et qui les fait ? | Métier du SI | Processus, activité, acteur |
| Quelles applications échangent les preuves de livraison ? | Applications | Application, flux |
| Qui peut agir sur les serveurs de virtualisation, et par quel accès ? | Administration | Zone d'administration, annuaire d'administration |
| Le Wi-Fi des quais est-il séparé du réseau des serveurs ? | Infrastructures logiques | Réseau, sous-réseau, équipement de sécurité |
| Que perd-on si la salle serveur du siège brûle ? | Infrastructures physiques | Site, salle, serveur physique |

Notion : chapitre 3, « Trois visions, six vues ».

@corrige 2
| Partie prenante | Type | Nature de la relation | Données ou services échangés | Dépendance |
| --- | --- | --- | --- | --- |
| PP-02 E-commerçants | Client | Contrats de transport | Envois, suivi par le portail B2B d'APP-03 Kestrel Track | Moyenne (30 % du chiffre d'affaires, plus de 20 %) |
| PP-03 Particuliers et petites entreprises | Client | Prestations ponctuelles | Demandes de devis par APP-12 Site web | Faible (10 %, aucun processus arrêté) |
| PP-10 Prestataire de paie | Fournisseur | Service SaaS (APP-08 Paie) | Identités, salaires, coordonnées bancaires des salariés | Moyenne (arrête un processus de support, la paie) |
| PP-11 Hébergeur du site web | Fournisseur | Hébergement mutualisé | Hébergement d'APP-12 Site web, formulaire de devis | Faible (repli par téléphone et courriel) |
| PP-15 Banque | Fournisseur | Services bancaires | Virements aux fournisseurs et salaires, fichiers issus de l'ERP finance | Moyenne (arrête les paiements, processus de support) |
| PP-17 ANSSI | Autorité | Obligations NIS2, si Kestrel y est soumise (à confirmer) | Notifications d'incidents, mesures de sécurité | Sans objet |
| PP-18 Vidal Participations | Actionnaire | Détention à 100 % ; convention de trésorerie | Avances de trésorerie ; reporting financier mensuel | Moyenne (arrêterait le règlement des fournisseurs, processus de support) |

Les cotations découlent de la règle et non d'une intuition : c'est l'exigence du chapitre 3 (« votre niveau de dépendance doit reposer sur une règle écrite »). Une dépendance « faible » pour PP-03 peut être accompagnée d'une remarque sur l'objectif e-commerce, hors de la liste fermée.

@corrige 3
PP-02 : 42 × 0,30 = 12,6 M€. PP-03 : 42 × 0,10 = 4,2 M€. Objectif Cap 2029 : 42 × 0,40 = 16,8 M€, soit une hausse de 16,8 − 12,6 = 4,2 M€, ou + 33,3 % (4,2 / 12,6). La stratégie va donc renforcer le poids des e-commerçants, qui suivent leurs envois sur le portail B2B de Kestrel Track : la dépendance envers PP-02, aujourd'hui moyenne, et l'importance de Kestrel Track pour la relation commerciale vont croître. La cotation devra être revue à chaque mise à jour.

@corrige 4
Les trois objets sont rompus : un lecteur ne peut pas établir que « Éditeur WMS » et « StockFlow v4 » désignent les objets de la vue des applications. Noms corrects : « APP-02 StockFlow » pour l'application et « PP-06 Éditeur de StockFlow » pour son éditeur ; « APP-08 Paie » et « PP-10 Prestataire de paie » ; « APP-03 Kestrel Track » et « PP-08 Hébergeur cloud de Kestrel Track ». Le tableau des parties prenantes confond aussi l'application et son fournisseur, qui sont deux objets distincts reliés entre eux. La version n'entre pas dans le nom, car elle change : elle devient un attribut, sinon le nom changerait à chaque mise à jour et casserait le lien entre les vues. Le correcteur du D2 vérifie cinq objets pivots pris au hasard (élément E8). Notion : chapitre 3, « Le modèle de cartographie » (nomenclature).

@corrige 5
Boîtes à compléter : « APP-08 Paie », « PP-10 Prestataire de paie » ; « PP-08 Hébergeur cloud de Kestrel Track ». Les processus (« Payer les salariés », « Informer le client du suivi ») appartiennent à la vue métier ; les applications à la vue des applications ; les fournisseurs à la vue de l'écosystème. Entre APP-03 Kestrel Track et son hébergeur, une cartographie complète intercale les deux machines virtuelles, dans une seule zone, qui relèvent de la vue des infrastructures logiques (objet « serveur logique ») ; on valorise l'apprenant qui le signale. L'application est l'objet pivot qui relie la vue métier à la vue des applications : la vue métier porte l'attribut « liste des applications qui soutiennent le processus ».

@corrige 6
Kestrel « pourrait relever de NIS2 au titre des services postaux et d'expédition » : le point n'est pas confirmé, il serait faux de l'affirmer, d'où la mention « à confirmer » et un trait en tirets. La relation avec une autorité n'est pas une dépendance d'activité : la défaillance de l'ANSSI n'arrêterait aucun processus de Kestrel. C'est une relation d'obligation légale, que la règle classe « sans objet » ; la coter « faible » laisserait croire qu'elle compte peu, alors qu'elle peut imposer des mesures et des notifications. Notion : chapitre 3, exemple du modèle de Kestrel (liste fermée « forte, moyenne, faible, ou sans objet »).

@corrige 7
Exemple de constat attendu : « Des données personnelles sensibles sont confiées à plusieurs fournisseurs externes, sans que leur niveau de sécurité soit documenté : PP-10 Prestataire de paie détient les identités, salaires et coordonnées bancaires des 300 salariés, PP-15 Banque reçoit les fichiers de virement, et PP-08 Hébergeur cloud de Kestrel Track héberge les données des destinataires, environ 2,5 millions de livraisons par an. » Un autre constat acceptable porte sur la concentration financière : PP-15 Banque et PP-18 Vidal Participations conditionnent ensemble tous les paiements. Le constat relie plusieurs parties prenantes, ce que la lecture ligne à ligne ne fait pas ; il s'appuie sur un chiffre ; il ne propose pas de solution. Barème indicatif sur 4 points : constat de relation (1,5), deux parties prenantes nommées selon la nomenclature (1), un chiffre (0,5), absence de solution et rédaction (1).

# FT 10 | Inventorier les applications et les flux | 4

@situation
En juin 2026, vous assistez le chef de projet applicatif de Kestrel Logistique, qui tient l'inventaire applicatif et la matrice des flux. Pour la version 2 de la cartographie, la DSI refond l'inventaire avec des attributs plus nombreux : la version de travail 0.3 de ce nouvel inventaire est incomplète, en particulier pour les attributs de sécurité. Vous avez mené deux entretiens et Romain Chevalier vous a transmis le relevé des tâches planifiées des serveurs. À vous de compléter l'annexe A et l'annexe B, avec les listes fermées du modèle.

@capacites
Relever des flux dans des sources de nature différente
Renseigner les sept champs d'un flux et les attributs de sécurité
Mesurer la complétude d'un inventaire
Traiter une hypothèse du registre et un usage hors inventaire
Formuler des constats à partir de l'inventaire

@duree 75 minutes

@annexe 1 | Deux entretiens | Comptes rendus fictifs d'entretiens, DSI de Kestrel Logistique, juin 2026
Avec la responsable comptable. « L'ERP finance est utilisé par six personnes de la comptabilité et par Isabelle Roux. On y accède par un client lourd installé sur les postes du siège ; il n'est pas accessible depuis l'extérieur. Chaque nuit, un fichier des lettres de voiture livrées la veille arrive de RoutePro ; l'ERP l'intègre tout seul pour préparer la facturation. Les virements fournisseurs sont préparés dans l'ERP, exportés en fichier, puis déposés à la main sur le site de la banque, deux fois par semaine. Chaque mois, le prestataire de paie nous envoie par courriel un fichier des écritures de paie, que nous importons dans l'ERP. L'éditeur publie encore des mises à jour, et nous avons la dernière version. »

Avec un développeur de la DSI. « KDriver tourne sur les terminaux durcis des chauffeurs, et les sous-traitants du dernier kilomètre l'utilisent aussi. Elle se synchronise avec Kestrel Track toutes les 2 minutes par le réseau mobile. C'est nous qui la développons, mais personne ne suit la version d'Android des terminaux. Le site web repose sur un CMS ; personne ne sait quand ses extensions ont été mises à jour pour la dernière fois. Autre chose : à Clermont-Ferrand, les agents envoient aux clients les photos des colis abîmés par un service gratuit de transfert de fichiers en ligne, avec leur adresse personnelle. »

@annexe 2 | Les listes fermées du modèle | Modèle de cartographie de Kestrel, version 1.0, document fictif
| Attribut | Valeurs autorisées |
| --- | --- |
| Hébergement | Salle interne ; cloud d'un hébergeur ; SaaS du fournisseur ; poste ou terminal |
| Exposition à Internet | Non exposée ; exposée aux utilisateurs internes ; exposée aux partenaires ; exposée au public |
| État du support | Maintenu par l'éditeur ; fin de support annoncée ; support étendu payant ; hors support ; non documenté |
| Mode du flux | Automatique ; manuel |
| Protection du canal | TLS ; VPN ; messagerie sécurisée ; aucun chiffrement ; non documentée ; sans objet |

@annexe 3 | Tâches planifiées relevées sur les machines virtuelles du siège | Relevé fictif établi par Romain Chevalier, juin 2026
| Tâche | Machine virtuelle | Horaire | Action |
| --- | --- | --- | --- |
| EXP_LV | Machine virtuelle de RoutePro | Chaque nuit, 1 h 30 | Copie le fichier des lettres de voiture livrées dans un répertoire d'échange (partage de fichiers interne, non chiffré) |
| IMP_LV | Machine virtuelle de l'ERP finance | Chaque nuit, 2 h 00 | Intègre dans l'ERP finance le fichier du répertoire d'échange |
| SAUV_ERP | Machine virtuelle de l'ERP finance | Chaque nuit, 23 h 00 | Copie la base de l'ERP finance sur STO-01 NAS de sauvegarde |

@annexe 4 | Applications renseignées dans l'inventaire v0.3, par attribut (sur 12) | Tableau de suivi fictif du chef de projet applicatif, juin 2026
@graphique barres applications
Type : 12
Hébergement : 12
Éditeur : 11
Processus : 9
Exposition : 8
Utilisateurs : 7
État du support : 6
Besoins DICT : 4

@question 1 | Identifier | Annexes 1 et 3
Relevez les échanges d'informations décrits dans les annexes 1 et 3. Pour chacun, indiquez la source, la cible et s'il est automatique ou manuel. Quelle source confirme un échange décrit en entretien ?
@lignes 5

@question 2 | Mobiliser | Annexes 1, 2 et 3
Complétez les cinq champs manquants de ces trois flux de la matrice, avec les valeurs des listes fermées quand elles existent.
@tableau
| Champ | FLX-07 : APP-01 RoutePro vers APP-07 ERP finance | FLX-08 : APP-07 ERP finance vers PP-15 Banque | FLX-09 : APP-08 Paie vers APP-07 ERP finance |
| --- | --- | --- | --- |
| Données | | | |
| Format | | | |
| Fréquence | | | |
| Mode | | | |
| Protection du canal | | | |

@question 3 | Mobiliser | Annexes 1 et 2, fiche Kestrel
Renseignez les trois attributs de sécurité suivants. Une précision qui n'entre pas dans la liste va entre parenthèses.
@tableau
| Application | Hébergement | Exposition à Internet | État du support |
| --- | --- | --- | --- |
| APP-04 KDriver | | | |
| APP-07 ERP finance | | | |
| APP-12 Site web | | | |

@question 4 | Calculer | Annexe 4
Huit attributs sont suivis pour douze applications. Calculez le taux de complétude global de l'inventaire v0.3, puis celui des quatre attributs de sécurité exigés par le D2. Que concluez-vous ?
@lignes 4

@question 5 | Analyser | Annexe 3, cours
La tâche SAUV_ERP change-t-elle quelque chose au registre des hypothèses de Kestrel (hypothèse H1) ? Que faut-il y écrire, et que ne faut-il pas faire ?
@lignes 4

@question 6 | Analyser | Annexe 1, cours
Le service de transfert de fichiers utilisé à Clermont-Ferrand doit-il figurer dans l'inventaire ? Sous quelle forme, avec quels attributs connus et inconnus ?
@lignes 4

@question 7 | Argumenter | Toutes les annexes
Formulez trois constats tirés de votre inventaire et de votre matrice des flux, du plus grave au moins grave. Chacun relie au moins deux faits et cite les identifiants des objets.
@lignes 8

@retiens
L'inventaire applicatif décrit chaque application par au moins [[dix]] attributs, dont quatre de sécurité : les [[besoins de sécurité]] (cotation D, I, C, T), l'[[exposition à Internet]] (accessible depuis Internet ou non, et par qui), l'[[hébergement]] (lieu et exploitant) et l'[[état du support]] (maintenance de l'éditeur et des composants). Chaque valeur est prise dans une [[liste fermée]]. La matrice des flux décrit chaque flux par sept champs : source, cible, données, format, fréquence, le [[mode]] (automatique ou manuel) et la [[protection du canal]] (chiffrement ou non). Une valeur absente des sources s'écrit « [[non documentée]] » ou devient une hypothèse numérotée.

@corrige 1
Cinq échanges. RoutePro vers ERP finance, lettres de voiture livrées : automatique (copie par EXP_LV, intégration par IMP_LV). ERP finance vers la banque, fichiers de virement : manuel (export puis dépôt à la main). Paie vers ERP finance, écritures de paie : manuel (courriel puis import). KDriver vers Kestrel Track, synchronisation toutes les 2 minutes : automatique ; c'est le flux FLX-03 déjà inscrit à la matrice. ERP finance vers STO-01 NAS de sauvegarde : copie automatique, qui relève de l'inventaire de l'infrastructure plutôt que de la matrice des flux applicatifs. Le relevé des tâches (annexe 3), un outil, confirme l'échange RoutePro vers ERP décrit en entretien : c'est un recoupement entre deux sources de nature différente, plus solide qu'un témoignage seul (chapitre 4, « Les entretiens : préparer, conduire, recouper »).

@corrige 2
| Champ | FLX-07 : APP-01 RoutePro vers APP-07 ERP finance | FLX-08 : APP-07 ERP finance vers PP-15 Banque | FLX-09 : APP-08 Paie vers APP-07 ERP finance |
| --- | --- | --- | --- |
| Données | Lettres de voiture livrées la veille (éléments de facturation clients) | Ordres de virement fournisseurs (coordonnées bancaires, montants) | Écritures de paie (données salariales) |
| Format | Fichier déposé dans un répertoire d'échange (tâches EXP_LV et IMP_LV) | Fichier exporté, déposé sur le site de la banque | Fichier envoyé par courriel, puis importé |
| Fréquence | Chaque nuit (1 h 30 et 2 h) | Deux fois par semaine | Mensuelle |
| Mode | Automatique | Manuel | Manuel |
| Protection du canal | Aucun chiffrement (partage interne non chiffré) | Non documentée | Non documentée (courriel standard) |

Pour FLX-08, le site d'une banque est très probablement protégé par TLS, mais aucune source ne le dit : on écrit « non documentée » ou l'on pose une hypothèse numérotée à la suite du registre. Les données sont qualifiées avec leur sensibilité, pas « données » (chapitre 4, « La matrice des flux »).

@corrige 3
| Application | Hébergement | Exposition à Internet | État du support |
| --- | --- | --- | --- |
| APP-04 KDriver | Poste ou terminal (terminaux durcis des chauffeurs) | Exposée aux partenaires (sous-traitants du dernier kilomètre ; échanges par le réseau mobile avec APP-03 Kestrel Track) | Non documenté (application maintenue par la DSI, mais version d'Android des terminaux non suivie) |
| APP-07 ERP finance | Salle interne (SAL-01 Salle serveur du siège) | Non exposée | Maintenu par l'éditeur |
| APP-12 Site web | Cloud d'un hébergeur (PP-11 Hébergeur du site web, mutualisé) | Exposée au public | Non documenté (mises à jour des extensions inconnues) |

Pour KDriver, la valeur « maintenu par l'éditeur » appliquée à l'application seule (l'éditeur est ici la DSI) est acceptée si le composant Android non suivi est signalé en remarque : l'état du support porte sur l'application et sur ses composants (chapitre 4). Pour son exposition, « exposée aux utilisateurs internes » est aussi acceptée si l'élève signale en remarque l'usage par les sous-traitants.

@corrige 4
Cases renseignées : 12 + 12 + 11 + 9 + 8 + 7 + 6 + 4 = 69 sur 8 × 12 = 96, soit 71,9 % ; 27 cases manquent. Quatre attributs de sécurité (hébergement, exposition, état du support, besoins DICT) : 12 + 8 + 6 + 4 = 30 sur 4 × 12 = 48, soit 62,5 %, nettement moins que l'ensemble. Et l'hébergement, complet, masque le reste : exposition, état du support et besoins DICT ne sont renseignés que pour 18 cas sur 36, soit 50 %, et les besoins DICT pour 4 applications sur 12 (33,3 %). Conclusion : l'inventaire est le plus lacunaire là où le guide de l'ANSSI demande de mettre la priorité, sur les attributs de sécurité.

@corrige 5
La tâche SAUV_ERP montre qu'une sauvegarde nocturne de la base de l'ERP finance sur STO-01 est programmée : elle appuie H1 pour l'ERP finance seulement (une tâche programmée ne prouve ni qu'elle réussit chaque nuit, ni que la copie se restaure), et ne dit rien de RoutePro, dont aucune tâche de sauvegarde n'apparaît dans le relevé. Dans le registre, on garde le numéro H1, on note la source et la date du relevé et l'on précise que H1 reste une hypothèse, entière pour RoutePro. On ne renumérote jamais une hypothèse et on ne réutilise pas son numéro (chapitre 4, registre des hypothèses). Le constat ne dit rien de la durée de restauration, qui reste l'hypothèse H19.

@corrige 6
Oui. C'est un usage hors inventaire : un outil utilisé sans être connu ni validé par la DSI. L'inventorier ne revient pas à l'approuver ; cela rend le risque visible, et le D2 en exige au moins un. On l'inscrit à l'annexe A avec les mêmes attributs que les autres applications. Connus : type (service en ligne gratuit), utilisateurs (agents de Clermont-Ferrand), hébergement (SaaS du fournisseur), exposition (exposée au public), données (photos de colis, adresses des clients). Inconnus, à écrire « non documenté » : le nom exact du service, son pays d'hébergement, la durée de conservation des fichiers, les comptes utilisés. Le flux correspondant vers les clients se note aussi dans la matrice. Notion : chapitre 4, « L'inventaire applicatif et ses attributs ».

@corrige 7
Constats attendus, par exemple. Premier : les fichiers de paiement passent par deux flux manuels non protégés de façon documentée (FLX-08 vers PP-15 Banque, FLX-09 depuis APP-08 Paie par courriel) ; ce sont des points d'interception ou de modification, alors que la tentative de fraude au virement de septembre 2025 montre que le paiement est visé. Deuxième : APP-12 Site web, exposé au public, et APP-04 KDriver, utilisée par des partenaires, ont un état du support non documenté, comme la moitié de l'inventaire (6 applications sur 12 seulement renseignées). Troisième : FLX-07, flux automatique de facturation, transite par un partage interne non chiffré, sur un réseau supposé plat (H3). Un usage hors inventaire peut aussi être un constat. Barème indicatif sur 5 points : trois constats qui relient des faits (3), identifiants exacts (1), ordre justifié (1).

# FT 11 | Points uniques de défaillance et zones de confiance | 4

@situation
En mars 2026, la fibre qui relie l'agence de Clermont-Ferrand au siège a été coupée pendant une matinée. Romain Chevalier, responsable de l'infrastructure et RSSI à temps partiel, s'est rendu sur place. En alternance à ses côtés, vous préparez la mise à jour de la vue physique et de la vue de l'administration pour le site de Clermont-Ferrand, à partir de son rapport et de son relevé.

@capacites
Relever les effets d'une panne et leur cause
Calculer une durée d'arrêt, une disponibilité, une proportion
Tester un élément avec la définition du point unique de défaillance
Nommer des objets selon la règle de nommage
Délimiter des zones de confiance et repérer un franchissement
Hiérarchiser des constats de cartographie

@duree 75 minutes

@annexe 1 | Coupure de la liaison de Clermont-Ferrand : rapport d'incident | Rapport fictif de Romain Chevalier au comité de direction, mars 2026
Le 17 mars 2026, à 7 h 40, des travaux de voirie ont coupé la fibre de l'agence de Clermont-Ferrand. Le tunnel RES-02 VPN Clermont est tombé. L'agence n'avait plus aucun accès réseau : ni au siège, ni à Internet, auquel elle accède par le siège.

Les 14 scanners de l'agence, reliés au Wi-Fi des quais, ne joignaient plus StockFlow ; les postes ne pouvaient plus ouvrir RoutePro. Les camions de Kestrel, partis vers 6 h, ont livré normalement, car KDriver passe par le réseau mobile des terminaux. Les six tournées des sous-traitants, qui partent vers 8 h, ont été préparées sur papier. Les étiquettes n'ont pas pu être imprimées : la seule imprimante d'étiquettes est pilotée depuis StockFlow. La fibre a été rétablie à 13 h 40. Il a ensuite fallu ressaisir les réceptions de la matinée. Seul le responsable de l'agence dispose dans StockFlow des droits de validation des écarts de réception ; il était en congé, et deux réceptions sont restées bloquées jusqu'au lendemain.

Sur place, j'ai fait trois observations. Le routeur de l'opérateur et le commutateur de l'agence sont uniques, posés sur une étagère, sans onduleur. Le fichier « Litiges Clermont », enregistré sur le poste du responsable de l'agence, est copié chaque vendredi sur une clé USB rangée dans le tiroir du même bureau. Enfin, le mot de passe du Wi-Fi des quais est affiché dans le local des chauffeurs : les chauffeurs des sous-traitants du dernier kilomètre y connectent leurs téléphones personnels.

Bilan : sur environ 1 310 colis traités ce jour-là par l'agence, 330 sont partis l'après-midi au lieu du matin.

@annexe 2 | Relevé de l'infrastructure de SITE-03 Clermont-Ferrand | Relevé fictif de Romain Chevalier, mars 2026
| Élément | Nombre | Emplacement | Secours ou remarque |
| --- | --- | --- | --- |
| RES-02 VPN Clermont (fibre, 100 Mbit/s) | 1 | Liaison vers le siège | Aucun ; porte aussi l'accès à Internet |
| Routeur de l'opérateur (non numéroté) | 1 | Étagère du local technique | Aucun ; pas d'onduleur |
| Commutateur de l'agence (non numéroté) | 1 | Même étagère | Aucun ; pas d'onduleur |
| Bornes Wi-Fi des quais (RES-03) | 2 | Quai | Chacune couvre presque tout le quai |
| TRM-01 Scanners des quais | 14 | Quai | 2 scanners de réserve |
| TRM-05 Postes de Clermont-Ferrand | 12 | Bureaux | Aucun poste de réserve |
| Imprimante d'étiquettes (non numérotée) | 1 | Bureau du responsable de l'agence | Aucune autre imprimante d'étiquettes |
| Clé USB de copie du fichier des litiges (non numérotée) | 1 | Tiroir du bureau du responsable de l'agence | Copie hebdomadaire |

@annexe 3 | Coupures de RES-02 VPN Clermont depuis 2025 | Relevé fictif de l'outil de tickets, durée en heures, mars 2026
@graphique barres heures
Février 2025 : 2,5
Juin 2025 : 4
Novembre 2025 : 7,5
Mars 2026 : 6

@annexe 4 | Chemins d'accès depuis le quai de Clermont-Ferrand, tous par RES-02 VPN Clermont | Schéma de travail fictif de la DSI, mars 2026
@schema
Téléphones des sous-traitants -> [[ZC-04 Wi-Fi des quais]] -> [[ZC-05 Réseau interne du siège]]
TRM-01 Scanners des quais -> [[Sortie Internet du siège]] -> APP-02 StockFlow

@question 1 | Identifier | Annexe 1
Pour chaque activité, dites si elle s'est arrêtée ou a continué pendant la coupure, et quel élément l'explique.
@tableau
| Activité | Arrêtée ou poursuivie ? | Élément en cause |
| --- | --- | --- |
| Réceptionner les palettes avec les scanners | | |
| Imprimer les étiquettes | | |
| Consulter RoutePro depuis l'agence | | |
| Livrer avec les camions déjà partis | | |
| Valider les écarts de réception après la coupure | | |

@question 2 | Calculer | Annexes 1 et 3, fiche Kestrel
Calculez les indicateurs suivants. La disponibilité se calcule sur une année de 8 760 heures. Le besoin de continuité exprimé pour StockFlow est de 4 heures d'arrêt toléré.
@tableau
| Indicateur | Calcul posé avec les valeurs des annexes | Résultat arrondi |
| --- | --- | --- |
| Durée de la coupure de mars 2026 | | |
| Part des colis de l'agence partis en retard ce jour-là | | |
| Durée cumulée des coupures en 2025 | | |
| Disponibilité de RES-02 en 2025 | | |
| Coupures ayant atteint ou dépassé 4 heures | | |

@question 3 | Mobiliser | Annexes 1 et 2, cours
Appliquez à chaque élément le test du cours : s'il disparaît, qu'est-ce qui s'arrête, et existe-t-il un autre chemin ?
@tableau
| Élément | Ce qui s'arrête s'il disparaît (activité, service) | Autre chemin ? | Point unique de défaillance ? |
| --- | --- | --- | --- |
| RES-02 VPN Clermont | | | |
| Routeur de l'opérateur | | | |
| Bornes Wi-Fi des quais | | | |
| TRM-01 Scanners des quais | | | |
| Imprimante d'étiquettes | | | |
| Responsable de l'agence (droits de validation) | | | |
| Clé USB de copie des litiges | | | |

@question 4 | Mobiliser | Annexe 2, cours
Quatre éléments ne sont pas numérotés. Proposez pour chacun un identifiant conforme à la règle de nommage de Kestrel, sachant que l'inventaire compte déjà RES-01 à RES-03, TRM-01 à TRM-06 et STO-01 à STO-02.
@lignes 3

@question 5 | Analyser | Annexes 1 et 4, cours
Complétez le schéma de l'annexe 4. Quel franchissement déjà numéroté dans la vue de l'administration de Kestrel les scanners empruntent-ils ?
@lignes 3

@question 6 | Analyser | Annexes 1 et 4, cours
Les téléphones personnels des chauffeurs des sous-traitants changent-ils la vue de l'administration ? Raisonnez en zones de confiance et en franchissements, et dites quelle hypothèse du registre ce fait rend plus grave.
@lignes 6

@question 7 | Argumenter | Toutes les annexes
Rédigez pour Romain Chevalier les trois constats à porter sur les vues de Clermont-Ferrand, du plus grave au moins grave, chacun avec la vue où il se montre et un fait chiffré ou sourcé.
@lignes 10

@retiens
Un [[point unique de défaillance]] est un élément dont la panne suffit à arrêter un service, faute de [[redondance]] ou de solution de repli ; ce peut être un équipement, un fournisseur ou une [[personne]]. Une sauvegarde rangée près de ce qu'elle protège n'en est pas un : c'est un défaut d'[[isolement]]. Une [[zone de confiance]] regroupe des ressources de même niveau de confiance ; un [[franchissement]] est un passage autorisé vers une zone de niveau différent, à la fois point de [[contrôle]] et chemin d'[[attaque]].

@corrige 1
| Activité | Arrêtée ou poursuivie ? | Élément en cause |
| --- | --- | --- |
| Réceptionner les palettes avec les scanners | Arrêtée (papier) | RES-02 : plus d'accès à APP-02 StockFlow, joint par la sortie Internet du siège |
| Imprimer les étiquettes | Arrêtée | Imprimante unique pilotée depuis APP-02 StockFlow |
| Consulter RoutePro depuis l'agence | Arrêtée | RES-02 : APP-01 RoutePro est dans SAL-01, au siège |
| Livrer avec les camions déjà partis | Poursuivie | APP-04 KDriver passe par le réseau mobile, pas par RES-02 |
| Valider les écarts de réception après la coupure | Bloquée jusqu'au lendemain | Le responsable de l'agence, seul titulaire des droits, absent |

@corrige 2
| Indicateur | Calcul | Résultat |
| --- | --- | --- |
| Durée de la coupure de mars 2026 | 13 h 40 − 7 h 40 | 6 heures |
| Part des colis de l'agence partis en retard ce jour-là | 330 / 1 310 × 100 | 25,2 % |
| Durée cumulée des coupures en 2025 | 2,5 + 4 + 7,5 | 14 heures |
| Disponibilité de RES-02 en 2025 | (8 760 − 14) / 8 760 × 100 | 99,84 % |
| Coupures ayant atteint ou dépassé 4 heures | Juin 2025, novembre 2025, mars 2026 | 3 sur 4 |

Commentaire attendu : une disponibilité de 99,84 % paraît élevée, mais les coupures tombent en heures d'activité et durent en moyenne (2,5 + 4 + 7,5 + 6) / 4 = 5 heures ; trois sur quatre atteignent ou dépassent l'arrêt toléré pour StockFlow à l'agence. Un taux annuel cache la durée de chaque arrêt, qui compte pour les métiers (chapitre 8).

@corrige 3
| Élément | Ce qui s'arrête s'il disparaît | Autre chemin ? | Point unique de défaillance ? |
| --- | --- | --- | --- |
| RES-02 VPN Clermont | Tout accès de l'agence au siège et à Internet : StockFlow, RoutePro | Non | Oui (déjà repéré dans la version 1.0) |
| Routeur de l'opérateur | Même effet que la perte de RES-02 | Non, et pas d'onduleur | Oui |
| Bornes Wi-Fi des quais | Rien si une seule tombe : l'autre couvre presque tout le quai | Oui, en mode dégradé | Non (redondance partielle, à signaler) |
| TRM-01 Scanners des quais | Rien pour un scanner : 2 scanners de réserve | Oui | Non |
| Imprimante d'étiquettes | L'impression des étiquettes, donc les départs étiquetés | Non | Oui |
| Responsable de l'agence (droits de validation) | La validation des écarts de réception | Non, constaté lors de l'incident | Oui (point unique humain) |
| Clé USB de copie des litiges | Rien : sa perte n'arrête aucun service | Sans objet | Non : défaut d'isolement de la copie, dans le même bureau que l'original |

Le commutateur, absent du tableau, est lui aussi un point unique de défaillance. Notion : chapitre 4, « Ce que l'on cherche sur les vues » (définition et distinction avec le défaut d'isolement).

@corrige 4
Selon la règle (préfixe de type, numéro à deux chiffres, nom usuel) et en prenant les numéros libres suivants : « RES-04 Routeur de Clermont-Ferrand », « RES-05 Commutateur de Clermont-Ferrand » (liens et réseaux), « TRM-07 Imprimante d'étiquettes de Clermont-Ferrand » (lots de postes et terminaux), « STO-03 Clé USB des litiges de Clermont-Ferrand » (stockage et sauvegardes). Un classement du routeur et du commutateur sous un autre préfixe est accepté s'il est défini dans le modèle ; un numéro déjà attribué ne l'est pas.

@corrige 5
Boîtes à compléter : « ZC-04 Wi-Fi des quais » et « ZC-05 Réseau interne du siège » sur la première ligne ; « Sortie Internet du siège » sur la seconde. Les scanners empruntent FR-03, le franchissement de ZC-04 Wi-Fi des quais vers ZC-05 Réseau interne du siège, avant de rejoindre APP-02 StockFlow par la sortie Internet du siège. Le chemin de Clermont-Ferrand passe en plus par RES-02 : le constat de la version 1.0 sur FR-03 vaut donc aussi pour l'agence.

@corrige 6
Oui. La zone ZC-04 Wi-Fi des quais était pensée pour des terminaux de Kestrel, les scanners. Elle accueille désormais des téléphones personnels non gérés, appartenant à des tiers : leur niveau de confiance est celui d'appareils inconnus, proche de celui d'Internet. Il faut donc soit abaisser le niveau de confiance de ZC-04, soit représenter ces téléphones dans une zone à part et noter un nouveau franchissement vers ZC-04, à numéroter à la suite (FR-07). Dans les deux cas, ces appareils peuvent ensuite emprunter FR-03 vers ZC-05 Réseau interne du siège, où se trouvent APP-01 RoutePro et APP-07 ERP finance. Le fait rend plus grave l'hypothèse H3 (réseau interne plat) : sans segmentation, un téléphone compromis sur le quai de Clermont-Ferrand atteindrait le cœur du SI. Notion : chapitre 4, définition de la zone de confiance et du franchissement.

@corrige 7
Constats attendus. Premier, sur la vue de l'administration : des téléphones personnels de sous-traitants accèdent à ZC-04 Wi-Fi des quais, dont le mot de passe est affiché, puis, par FR-03 et RES-02, au réseau interne du siège supposé plat (H3) ; c'est un chemin d'attaque vers APP-01 RoutePro. Deuxième, sur la vue physique : l'agence dépend d'une chaîne de points uniques, RES-02, le routeur et le commutateur sans onduleur ; la coupure de mars a duré 6 heures et retardé 25,2 % des colis du jour, et trois coupures sur quatre ont atteint ou dépassé 4 heures. Troisième : deux points uniques locaux, l'imprimante d'étiquettes et le responsable de l'agence, seul à valider les écarts, auxquels s'ajoute le défaut d'isolement de la copie des litiges. L'ordre inverse des deux premiers est accepté s'il est justifié, par exemple par la fréquence constatée des coupures. Les constats ne proposent pas de solution. Barème indicatif sur 5 points : trois constats exacts (3), vue désignée pour chacun (1), faits chiffrés ou sourcés et ordre justifié (1).
