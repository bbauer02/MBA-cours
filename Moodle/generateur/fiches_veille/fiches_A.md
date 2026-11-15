# FICHE 01 | La veille, c'est quoi ? | 1

@essentiel
La veille est une activité organisée et continue. Elle consiste à surveiller ce qui se passe autour d'une organisation, puis à transmettre ce qui compte à ceux qui décident.

Trois idées résument la définition. Organisée : il y a un besoin, des sources et une méthode. Continue : on ne la fait pas une fois pour toutes. Utile à la décision : c'est son but. Une veille qui ne sert aucune décision ne sert à rien.

@tableau Ne pas confondre
| Activité | Ce qu'elle regarde | Dans le temps |
| --- | --- | --- |
| Veille | L'extérieur de l'organisation | En continu |
| Audit | L'intérieur de l'organisation | Une fois, à un moment donné |
| Recherche documentaire | Une seule question | S'arrête quand on a la réponse |

@schema activites-temps Trois activités dans le temps

@rappel Medisecure, Kestrel et le dossier D1
Medisecure est un réseau fictif de 14 centres de santé : c'est le cas de l'année, sur lequel porte votre dossier D1, le dossier écrit qui évalue ce cours. Kestrel Logistique est un transporteur fictif de 300 salariés qui sert d'exemple dans le cours.

@rappel DSI
La direction des systèmes d'information : le service qui gère l'informatique d'une organisation (matériel, logiciels, réseaux, données, projets). Son responsable est le DSI, le directeur des systèmes d'information.

@rappel Système d'information (SI)
L'ensemble des moyens qui permettent de collecter, stocker, traiter et diffuser l'information d'une organisation : logiciels, données, matériel, mais aussi les personnes et les procédures.

@reflechir
Chez Medisecure, les développeurs ont découvert en 2024 que Node.js 14 (un logiciel qui fait tourner des applications web côté serveur) n'était plus maintenu depuis avril 2023, alors que l'information était publique. Qui aurait dû la repérer, et à qui aurait-il dû la transmettre ?

@qcm
Q: Quel est le but principal d'une veille ?
- Lire le plus d'articles possible sur son secteur
- Archiver toutes les actualités du secteur
+ Aider quelqu'un à prendre une décision
E: Une veille qui ne sert aucune décision est inutile, même si elle collecte beaucoup.

Q: Quelle activité examine l'intérieur de l'organisation ?
+ L'audit
- La veille
- La recherche documentaire
E: La veille regarde vers l'extérieur ; l'audit examine l'organisation elle-même.

Q: Que veut dire « continue » dans la définition de la veille ?
- Qu'on y consacre toute sa journée de travail
+ Qu'on ne la fait pas une fois pour toutes
- Qu'elle est faite par une seule personne
E: La veille suit son sujet dans le temps ; elle ne s'arrête pas après une première recherche.

# FICHE 02 | De l'information au renseignement | 1

@essentiel
Une information énonce un fait. Par exemple : « Node.js 14 n'est plus maintenu depuis le 30 avril 2023. » Elle peut être vraie ou fausse, mais elle ne dit pas quoi faire.

Un renseignement est une information triée, vérifiée, replacée dans son contexte et expliquée à une personne précise. Il répond à la question « et alors ? ». Le décideur n'a pas le temps de faire ce travail : c'est le rôle du veilleur.

@schema escalier Les trois ajouts du veilleur (exemple Kestrel Logistique)

@rappel Correctif de sécurité
Une mise à jour publiée par l'éditeur d'un logiciel pour corriger une faille. Quand un logiciel n'est plus maintenu, plus aucun correctif n'est publié : chaque nouvelle faille reste ouverte.

@rappel Version maintenue
Une version d'un logiciel que l'éditeur continue de corriger. Chaque version a une date de fin de support, après laquelle elle n'est plus maintenue.

@reflechir
Prenez une actualité informatique récente. Écrivez-la en une phrase, puis ajoutez le contexte, l'impact et une option de décision pour une organisation que vous connaissez.

@qcm
Q: Quelle phrase est un renseignement, et pas seulement une information ?
- Une nouvelle version de PostgreSQL vient de sortir, avec de nouvelles fonctions
- PostgreSQL est une base de données libre, utilisée par de nombreuses entreprises
+ Notre base de données passera hors support en juin : il faut prévoir la migration
E: Le renseignement relie le fait à l'organisation et propose une suite.

Q: Que se passe-t-il quand on transmet seulement des informations brutes au décideur ?
+ Le décideur doit faire lui-même le travail d'analyse
- Le décideur gagne du temps, car il a tout sous les yeux
- Rien de particulier, c'est la méthode recommandée
E: Une veille utile fait ce travail à la place du décideur.

Q: Quelle question le renseignement doit-il toujours traiter ?
- Qui a écrit l'article ?
- Combien d'articles parlent du sujet ?
+ Et alors, qu'est-ce que cela change pour nous ?
E: C'est la question « et alors ? » qui transforme une information en renseignement.

# FICHE 03 | Les familles de veille | 1

@essentiel
On classe les veilles selon ce qu'elles surveillent. Les frontières sont floues : une même information peut toucher plusieurs familles.

Ce cours se concentre sur la veille technologique et la veille réglementaire, car ce sont elles que votre diplôme évalue. Les autres familles les complètent.

@tableau Quatre familles
| Famille | Ce qu'elle surveille | Exemple chez Kestrel Logistique |
| --- | --- | --- |
| Technologique | Technologies, versions, fins de support, standards | La fin de support du framework de la plateforme de suivi |
| Réglementaire | Lois, règlements, doctrine des autorités, normes | Les règles de la CNIL sur la géolocalisation des salariés |
| Concurrentielle | Concurrents, offres, prix, partenariats | Un concurrent qui propose un créneau de livraison de 30 minutes |
| Sociétale et environnementale | Attentes des clients et des salariés, climat, énergie | Les zones à faibles émissions dans les métropoles |

@rappel RGPD et CNIL
Le RGPD est le règlement européen sur la protection des données personnelles. En France, c'est la CNIL qui contrôle son respect et peut sanctionner.

@rappel AI Act et NIS2
L'AI Act est le règlement européen sur l'intelligence artificielle. NIS2 est une directive européenne sur la cybersécurité. Les fiches 24 à 27 les détaillent.

@rappel Doctrine d'une autorité
La façon dont une autorité, comme la CNIL, interprète et applique un texte : ses recommandations et ses sanctions. À ne pas confondre avec « la doctrine » des juristes, qui désigne leurs analyses.

@rappel Framework
Une boîte à outils logicielle sur laquelle les développeurs construisent une application, par exemple Django ou Angular. Comme tout logiciel, il a des versions et des dates de fin de support.

@reflechir
L'AI Act devait rendre obligatoires, le 2 août 2026, les règles sur les systèmes d'IA à haut risque utilisés dans des domaines sensibles (emploi, éducation, accès aux services essentiels…), listés dans son annexe III. Une organisation a lu le texte en 2024 et ne l'a plus suivi depuis. Pourquoi risque-t-elle de se tromper aujourd'hui, et où vérifieriez-vous la date en vigueur ?

@qcm
Q: La fin de support d'un logiciel relève de quelle famille de veille ?
- Concurrentielle
+ Technologique
- Sociétale
E: Versions et fins de support sont des sujets de veille technologique.

Q: Une sanction de la CNIL relève de quelle famille ?
- Technologique
- Concurrentielle
+ Réglementaire
E: Les décisions des autorités font partie de la veille réglementaire.

Q: Quelles familles sont au cœur de ce cours ?
+ Technologique et réglementaire
- Concurrentielle et sociétale
- Toutes, à égalité
E: Ce sont elles que votre diplôme évalue.

# FICHE 04 | Le cycle de la veille | 1

@essentiel
La veille fonctionne comme un cycle en sept étapes. Chaque tour améliore le suivant : c'est la dernière étape, l'évaluation, qui permet d'ajuster le dispositif.

Le plan de votre dossier D1 suit ce cycle : besoin et ciblage (parties 1 et 2), collecte (partie 3), traitement et analyse (partie 4), capitalisation et diffusion (partie 5), recommandations (partie 6), évaluation (partie 7).

@schema cycle Les sept étapes et leur question

@rappel Capitaliser
Conserver une information dans un endroit partagé pour pouvoir la retrouver et la réutiliser, même après le départ de la personne qui l'a trouvée.

@astuce
Moyen mnémotechnique : on se demande quoi chercher et où (1-2), on récolte (3), on comprend (4), on partage (5), on garde (6), on vérifie que cela sert (7).

@reflechir
Quelle étape vous semble la plus souvent oubliée dans votre entreprise d'alternance ? Pourquoi ?

@qcm
Q: Quelle est la première étape du cycle ?
+ L'expression du besoin
- La collecte
- Le choix des outils
E: On commence toujours par savoir qui a besoin de quoi.

Q: Quelle étape fait du processus un cycle et pas une simple chaîne ?
- La diffusion
+ L'évaluation et l'ajustement
- La collecte
E: L'évaluation renvoie au début du cycle pour corriger le besoin, les sources ou les formats.

Q: Quelle étape répond à la question « qu'est-ce que cela change pour nous ? » ?
- Le ciblage
- La capitalisation
+ Le traitement et l'analyse
E: C'est l'étape qui transforme l'information en renseignement.

# FICHE 05 | Push, pull et méthode mixte | 1

@essentiel
En mode pull (« tirer »), le veilleur va chercher l'information lui-même : il consulte des sites, lance des recherches. En mode push (« pousser »), l'information arrive toute seule : alertes, flux RSS, newsletters.

Un bon dispositif est mixte. Mais dire « mixte » ne suffit pas : il faut préciser quelles sources sont suivies en push, lesquelles en pull, et pourquoi.

@tableau Comparer les deux modes
| | Pull | Push |
| --- | --- | --- |
| Principe | Je vais chercher | L'information vient à moi |
| Points forts | Recherche ciblée, sources sans flux | Régularité, rapidité, gain de temps |
| Points faibles | Prend du temps, risque d'oubli | Risque de surcharge, dépend du réglage |
| Exemple | Consulter chaque mois les décisions de la CNIL | Recevoir le flux RSS des avis du CERT-FR |

@schema push-pull Qui va vers qui ?

@rappel Flux RSS
Un fichier qu'un site publie pour annoncer ses nouveaux contenus. Un logiciel appelé agrégateur lit ces flux et rassemble les nouveautés de plusieurs sites au même endroit.

@rappel CERT-FR
Le centre gouvernemental français de veille, d'alerte et de réponse aux attaques informatiques. Il dépend de l'ANSSI, l'agence nationale de cybersécurité, et publie gratuitement des avis et des alertes de sécurité.

@reflechir
Une source publie quatre fois par an et n'a pas de flux RSS. Comment vous assureriez-vous de ne jamais manquer une de ses publications ?

@qcm
Q: Recevoir une alerte par courriel quand un mot-clé apparaît sur le web, c'est :
- Du pull
+ Du push
- Ni l'un ni l'autre
E: L'information arrive sans que vous alliez la chercher.

Q: Quel est le principal risque du push ?
+ Être noyé sous trop d'informations
- Oublier de consulter les sources
- Ne pas pouvoir suivre les sources institutionnelles
E: Mal réglé, le push envoie beaucoup trop de résultats.

Q: Dans le dossier, quand la réponse « mixte » est-elle acceptée ?
- Toujours, car tout dispositif sérieux mélange les deux modes
- Seulement si l'on utilise un outil payant pour le push
+ Quand on précise quelles sources relèvent de quel mode, et pourquoi
E: Le correcteur attend que chaque choix soit justifié par les besoins.

# FICHE 06 | Les rôles et les erreurs classiques | 1

@essentiel
Un dispositif de veille fait intervenir quatre rôles. Dans une petite structure, une seule personne peut les tenir tous, mais il est utile de les distinguer.

Attention au vocabulaire : un capteur est un outil qui détecte les nouveautés ; une personne qui signale une information est un correspondant.

Quatre erreurs classiques rendent une veille inutile : les connaître permet de les éviter.

@tableau Les quatre rôles
| Rôle | Ce qu'il fait |
| --- | --- |
| Veilleur ou animateur | Organise, configure les outils, collecte, trie, rédige, diffuse |
| Expert | Analyse et valide les informations de son domaine |
| Décideur | Exprime les besoins, décide, dit si la veille a servi |
| Correspondants | Font remonter des informations du terrain |

@tableau Les quatre erreurs
| Erreur | En clair |
| --- | --- |
| L'infobésité | Collecter trop, trier trop peu |
| La veille sans destinataire | Produire des documents que personne n'a demandés |
| L'absence de capitalisation | Rien n'est conservé, tout se perd |
| L'absence d'évaluation | On ne sait pas si la veille sert |

@rappel Infobésité
La surcharge d'informations : on reçoit tant de contenus qu'on ne voit plus ceux qui comptent.

@reflechir
Un correspondant signale une information mais ne reçoit jamais de réponse. Que risque-t-il de se passer au bout de quelques mois ?

@qcm
Q: Qui exprime les besoins et décide ?
- Le veilleur
- L'expert
+ Le décideur
E: Le décideur commande la veille et dit si elle a servi.

Q: S'abonner à cinquante newsletters sans avoir le temps de les lire, c'est :
+ De l'infobésité
- Une veille sans destinataire
- Une absence de capitalisation
E: Trop collecter et trop peu trier noie les informations importantes.

Q: Dans ce cours, que désigne le mot « capteur » ?
- Une personne qui signale une information
+ Un outil qui détecte les nouveautés
- Un expert qui valide l'information
E: Les personnes sont des correspondants ; les capteurs sont des outils.

# FICHE 07 | Partir des symptômes | 2

@essentiel
On ne commence pas une veille par les outils. On commence par ce qui ne va pas dans l'organisation : ce sont les symptômes.

Un symptôme est un fait observable, si possible chiffré et sourcé. De chaque symptôme, on déduit une décision à prendre, puis un besoin d'information.

@tableau Du symptôme au besoin (exemple Kestrel Logistique)
| Symptôme | Décision en jeu | Besoin d'information |
| --- | --- | --- |
| Plateforme de suivi en panne 11 heures en décembre | Moderniser la plateforme | Fins de support, failles connues, options d'hébergement |
| Un client exige une attestation de cybersécurité | Lancer un programme de conformité | Kestrel est-elle concernée par NIS2, la directive européenne sur la cybersécurité ? |

@astuce
La phrase magique : « Pour décider de X, telle personne a besoin de savoir Y, avant telle date. » Elle oblige à nommer un destinataire, une décision et une échéance.

@attention
« La sécurité est insuffisante » n'est pas un symptôme : c'est une opinion. « La plateforme a été indisponible 11 heures » en est un : c'est un fait.

@reflechir
Dans le dossier Medisecure, trouvez un symptôme chiffré. Écrivez le besoin d'information qui en découle avec la phrase magique.

@qcm
Q: Lequel est un symptôme exploitable ?
+ Deux composants de la plateforme ne sont plus maintenus
- Notre informatique est vieillissante
- Il faudrait passer au cloud
E: Un symptôme est un fait observable et vérifiable, pas une opinion ni une solution.

Q: Par quoi commence-t-on une veille ?
- Le choix d'un agrégateur
+ L'analyse des problèmes de l'organisation
- L'abonnement à des newsletters
E: Partir des outils donne une veille impressionnante mais inutile.

Q: Quels trois éléments la phrase « pour décider de X… » oblige-t-elle à nommer ?
- Un outil, une source, un budget
- Un axe, une priorité, une fréquence
+ Un destinataire, une décision, une échéance
E: Sans ces trois éléments, le besoin reste vague.

# FICHE 08 | Les parties prenantes | 2

@essentiel
Une partie prenante est une personne ou un groupe qui prend des décisions grâce à la veille, ou qui subit les conséquences de ces décisions.

Pour chacune, on note ce qu'elle doit décider, ce qu'elle a besoin de savoir, sous quelle forme et à quel rythme. Cette cartographie garantit que la veille aura des lecteurs, et elle prépare déjà la diffusion.

@tableau Exemple chez Kestrel Logistique
| Partie prenante | Ce qu'elle veut savoir | Sous quelle forme |
| --- | --- | --- |
| Directeur général | Obligations majeures, risques de sanction | Une note d'une page par mois |
| DSI | Fins de support, offres, coûts | Une synthèse toutes les deux semaines |
| Responsable de la plateforme | Versions, failles, dépendances | Une fiche technique chaque semaine |
| Chauffeurs | Ce qui change dans leur travail | Un message court au bon moment |

@rappel RSSI et DPO
Le RSSI est le responsable de la sécurité des systèmes d'information. Le DPO, ou délégué à la protection des données, veille au respect du RGPD dans l'organisation.

@rappel Tech lead
Le responsable technique d'une équipe de développement. Il prend les décisions techniques : versions, bibliothèques, architecture d'une application.

@attention
Pour le dossier D1, six parties prenantes minimum chez Medisecure : la direction générale, la DSI, le RSSI, le tech lead, le DPO et les soignants.

@reflechir
Parmi les acteurs cités dans le dossier Medisecure, lequel n'a jamais reçu d'information de veille ? Qu'aurait-il besoin de savoir ?

@qcm
Q: À quoi sert la cartographie des parties prenantes ?
- À choisir les outils de collecte et le budget de la veille
- À noter la fiabilité des sources avant de les retenir
+ À garantir que la veille a des lecteurs et à préparer la diffusion
E: Elle évite la veille sans destinataire et fixe déjà les formats attendus.

Q: Un directeur général veut plutôt :
- Une liste détaillée des versions et des failles de chaque logiciel
+ Une note courte avec les décisions à prendre
- Tous les articles collectés dans la semaine
E: Chaque lecteur a son format ; la direction veut de quoi décider.

Q: Combien de parties prenantes minimum le dossier D1 exige-t-il ?
+ Six
- Trois
- Dix
E: Direction générale, DSI, RSSI, tech lead, DPO et soignants.

# FICHE 09 | Cadrer avec le QQOQCCP | 2

@essentiel
Le QQOQCCP est une méthode de questionnement : Qui ? Quoi ? Où ? Quand ? Comment ? Combien ? Pourquoi ? Appliquée à la veille, elle permet de délimiter le périmètre et de repérer les oublis.

Le point clé : pour chaque question, on écrit aussi ce qu'on exclut. C'est ce qui empêche la veille de grossir sans fin.

@tableau Le QQOQCCP de la veille (extrait Kestrel)
| Question | Réponse | Ce qu'on exclut |
| --- | --- | --- |
| Qui ? | Le directeur général commande, un ingénieur de la DSI veille | La comptabilité, la paie |
| Quoi ? | La plateforme, l'IA, les données, la cybersécurité | Le droit du transport routier |
| Où ? | CNIL, ANSSI, CERT-FR, EUR-Lex (le site officiel du droit européen), éditeurs | Les marchés hors Europe |
| Quand ? | Lancement en janvier, productions chaque semaine et chaque mois, revue à six mois | — |
| Combien ? | Un jour par semaine, moins de 1 500 € par an | Aucun recrutement |
| Pourquoi ? | Sécuriser la plateforme, garder un grand client | — |

@rappel Périmètre
Ce que la veille couvre, et ce qu'elle ne couvre pas. Un périmètre trop large conduit à l'infobésité.

@astuce
On pense toujours au « quoi ». On oublie souvent le « combien » (le temps et le budget disponibles) et le « quand » (le rythme). Commencez par eux.

@reflechir
Pour Medisecure, que mettriez-vous dans la case « Combien ? » si vous deviez faire tourner la veille seul pendant trois semaines ?

@qcm
Q: Que signifie le deuxième C de QQOQCCP ?
- Comment
- Contrôle
+ Combien
E: Qui, Quoi, Où, Quand, Comment, Combien, Pourquoi.

Q: Pourquoi écrire une colonne d'exclusions ?
+ Pour empêcher le périmètre de grossir sans fin
- Pour remplir le tableau plus vite
- Parce que la CNIL l'exige
E: L'élargissement progressif du périmètre est la première cause d'infobésité.

Q: Quelle question précise le temps de travail et le budget disponibles ?
- Quand ?
+ Combien ?
- Comment ?
E: « Combien » fixe les moyens ; « quand » fixe le calendrier et le rythme.

# FICHE 10 | Axes, priorités et plan de veille | 2

@essentiel
Un axe de veille est un grand thème de surveillance, relié à un ou plusieurs besoins. Le dossier D1 en demande exactement cinq : quatre obligatoires et un libre.

Pour classer les axes, on peut utiliser une matrice importance × urgence. L'importance mesure l'ampleur de l'impact possible (coût, sanction, risque pour les personnes) ; l'urgence mesure la proximité de l'échéance (une fin de support dans six mois est plus urgente qu'une tendance à cinq ans). Tout le cadrage se rassemble ensuite dans un document court et daté : le plan de veille.

@schema matrice-importance-urgence La matrice importance × urgence

@rappel Les quatre axes obligatoires du dossier D1
Réglementation (santé, dispositifs médicaux, données, IA) ; technologies (architecture, données, IA) ; cybersécurité en santé ; numérique responsable. Le cinquième axe est libre, mais il doit répondre à un besoin de Medisecure que les quatre premiers ne couvrent pas déjà.

@rappel Plan de veille
Le document qui rassemble le cadrage en huit rubriques : contexte, parties prenantes, périmètre, axes et priorités, fréquence, ressources, indicateurs, révision. Il sert de contrat avec ceux qui ont demandé la veille. Les rubriques ressources et indicateurs sont les plus souvent oubliées.

@attention
Priorité faible ne veut pas dire axe abandonné. On le suit avec moins de sources et moins souvent.

@reflechir
Le plan Medisecure 2030 vise −30 % d'empreinte numérique par patient. Où placeriez-vous l'axe « numérique responsable » sur la matrice ?

@qcm
Q: Combien d'axes le dossier D1 demande-t-il ?
- Quatre, tous imposés
+ Cinq, dont un libre
- Autant qu'on veut, selon le temps disponible
E: Quatre axes obligatoires et un axe libre justifié.

Q: Un axe très important et très urgent est en :
- Priorité 2
- Priorité 4
+ Priorité 1
E: Il demande un suivi continu et des alertes immédiates.

Q: Quelles rubriques du plan de veille sont le plus souvent oubliées ?
+ Ressources et indicateurs
- Contexte et périmètre
- Axes et priorités
E: Sans ressources, le plan reste une intention ; sans indicateurs, on ne sait pas s'il sert.
