# Registre du fil rouge et des faits réels autorisés (livret Veille technologique BTS SIO 2)

Toute fiche respecte ce registre. On peut AJOUTER des faits fictifs (un graphique, un courriel, un échange avec le tuteur) s'ils ne contredisent rien ; on les signale dans son rapport. On ne cite AUCUN fait réel (date, version, chiffre, événement) absent de la liste « Faits réels autorisés » sans l'avoir signalé : en cas de doute, on rend le fait fictif (produit, entreprise ou chiffre inventé, signalé comme tel par la source « Source fictive »).

## Les personnages (fictifs)

| Code | Personnage | Situation |
| --- | --- | --- |
| P1 | Inès Morel, 20 ans | BTS SIO 2, option SISR. Alternante au service informatique de la Communauté de communes du Val-Morin (collectivité fictive, 9 communes, 140 agents, siège à Morin-sur-Loue, ville fictive). Projet professionnel : devenir administratrice systèmes et réseaux, puis poursuivre en licence professionnelle en alternance. Sujet de veille : « La virtualisation open source, alternative à VMware : Proxmox VE dans une petite collectivité ». |
| P2 | Marc Lefèvre | Responsable du service informatique du Val-Morin, tuteur d'Inès. Service de 3 personnes : Marc, Sonia Dubreuil (technicienne) et Inès. |
| P3 | Parc du Val-Morin | 165 postes sous Windows 11 (migration depuis Windows 10 terminée en septembre 2025), 3 serveurs physiques sous VMware vSphere 7 qui hébergent 14 machines virtuelles, un annuaire Active Directory sous Windows Server 2019, un pare-feu pfSense, des sauvegardes sur un NAS. Le renouvellement du contrat VMware est la préoccupation de Marc : le devis reçu au printemps 2026 est 3,4 fois plus élevé que le précédent (fait fictif). |
| P4 | Yanis Benali, 21 ans | BTS SIO 2, option SLAM. Alternant chez Pixel Brut, agence web lyonnaise fictive de 14 salariés (sites vitrines, boutiques en ligne, applications métier sur mesure). Projet professionnel : développeur full stack, puis bachelor ou licence en alternance. Sujet de veille : « Les assistants de code à base d'IA dans une petite agence web : gains, risques et bonnes pratiques ». |
| P5 | Claire Fabre | Lead développeuse de Pixel Brut, tutrice de Yanis. Pile technique de l'agence : PHP 8.3 et Symfony pour les applications, WordPress pour les sites vitrines, React pour les interfaces riches, MySQL, hébergement chez un hébergeur français. Gérant de l'agence : Bastien Roche. |
| P6 | Léo Martin | Camarade de classe, option SISR, passionné de cybersécurité. Il sert de contre-exemple bienveillant : sujet trop large (« la cybersécurité »), sources non vérifiées, veille sans méthode. Il progresse au fil des fiches. |
| P7 | Mme Haddad | Enseignante d'informatique de la classe, qui encadre la semaine de veille. |

Les deux sujets fil rouge servent de modèles, pas de sujets imposés : chaque étudiant choisit le sien.

## Faits réels autorisés (vérifiés, utilisables tels quels)

| Domaine | Fait |
| --- | --- |
| Référentiel | Le référentiel du BTS SIO regroupe dans le bloc 1, au sein de « Organiser son développement professionnel », les compétences « Mettre en place son environnement d'apprentissage personnel », « Mettre en œuvre des outils et stratégies de veille informationnelle », « Gérer son identité professionnelle » et « Développer son projet professionnel ». Ne pas citer de numéro d'épreuve. |
| Norme | La norme expérimentale AFNOR XP X50-053 (1998) porte sur les prestations de veille et décrit la veille comme une activité continue et en grande partie itérative de surveillance de l'environnement. Ne pas la citer mot pour mot entre guillemets. |
| Fins de support | Windows 10 : fin du support le 14 octobre 2025. PHP 8.1 : fin du support de sécurité le 31 décembre 2025 ; PHP 8.2 : fin du support de sécurité le 31 décembre 2026. Node.js 18 : fin de vie le 30 avril 2025. Python 3.9 : fin de vie en octobre 2025. |
| VMware | Broadcom a finalisé le rachat de VMware en novembre 2023, puis a mis fin à la vente de licences perpétuelles au profit d'abonnements ; de nombreuses organisations ont alors étudié des alternatives (Proxmox VE, Hyper-V, Nutanix, XCP-ng). |
| Proxmox VE | Plateforme de virtualisation open source (licence AGPLv3) éditée par la société autrichienne Proxmox Server Solutions, fondée sur Debian, qui combine KVM (machines virtuelles) et LXC (conteneurs) ; support commercial par abonnement facultatif. Ne pas citer de numéro de version. |
| Incidents | Log4Shell : vulnérabilité CVE-2021-44228 de la bibliothèque Java Log4j, rendue publique en décembre 2021, score CVSS de 10. Porte dérobée de xz Utils : CVE-2024-3094, découverte fin mars 2024 par l'ingénieur Andres Freund, qui avait remarqué une lenteur anormale de SSH. Panne CrowdStrike du 19 juillet 2024 : une mise à jour défectueuse du logiciel Falcon a bloqué environ 8,5 millions d'ordinateurs Windows selon Microsoft. Left-pad, mars 2016 : le retrait d'un paquet npm de 11 lignes a cassé la construction de milliers de projets. |
| Versions | Gestion sémantique de version (semver.org) : MAJEUR.MINEUR.CORRECTIF. LTS = Long Term Support. |
| Vulnérabilités | CVE = identifiant public d'une vulnérabilité (programme géré par MITRE). CVSS = score de gravité de 0 à 10 (version 4.0 publiée en novembre 2023, la 3.1 reste très utilisée). Le CERT-FR (rattaché à l'ANSSI) publie des alertes et des avis de sécurité ; ne pas citer son adresse web. Le site endoflife.date, communautaire, recense les dates de fin de support de centaines de produits. |
| Analyse | Cycle de la hype de Gartner, cinq phases : déclenchement de l'innovation, pic des attentes exagérées, creux de la désillusion, pente de l'éclaircissement, plateau de productivité. Technology Radar de Thoughtworks : quatre anneaux (Adopt, Trial, Assess, Hold) et quatre quadrants (techniques, plateformes, outils, langages et frameworks), publié deux fois par an. |
| Recherche | Opérateurs Google : guillemets (expression exacte), signe moins (exclusion), OR, site:, filetype:, intitle:, before: et after:. |
| Flux | Formats RSS et Atom. Flux des versions d'un dépôt GitHub : adresse du dépôt suivie de /releases.atom. Lecteurs : Feedly, Inoreader, NetNewsWire, Thunderbird. Google Alertes envoie des alertes par courriel ou par flux RSS. |
| Sources | Enquête annuelle Stack Overflow Developer Survey. Documentation officielle, notes de version (release notes), dépôts GitHub et GitLab, forums officiels, CERT-FR, presse informatique (Le Monde Informatique, LeMagIT, 01net, Developpez.com, ZDNet), Grafikart (tutoriels vidéo francophones). Pour les chiffres d'audience ou de part de marché, utiliser des données fictives. |
| IA générative | Les modèles de langage peuvent produire des affirmations fausses présentées avec assurance (« hallucinations »), y compris des références ou des liens inventés. Un résultat d'IA se vérifie sur une source primaire. Ne pas citer de nom de modèle ni de version. On peut citer des types d'outils (assistants conversationnels, assistants de code intégrés à l'éditeur). |

## Valeurs de référence communes aux fiches (à ne pas contredire)

Le cycle de la veille du livret a six étapes : 1 Cadrer (définir le besoin), 2 Sourcer (identifier et évaluer les sources), 3 Collecter, 4 Traiter et analyser, 5 Diffuser et partager, 6 Exploiter et faire évoluer (bilan, ajustement). Il boucle.

Grille de fiabilité d'une source sur 10 (fiche 07) : cinq critères notés de 0 à 2, Auteur (qui publie, compétence), Origine (primaire ou reprise), Date (datée, à jour), Preuves (références, liens, données vérifiables), Neutralité (intérêt commercial ou non). Cotes : 9-10 A fiable ; 7-8 B plutôt fiable ; 5-6 C à recouper ; 0-4 D à écarter.

Les quatre types de veille du livret (fiche 02) : veille technologique, veille sécurité (vulnérabilités, menaces), veille concurrentielle et marché, veille juridique et réglementaire. La veille technologique de l'étudiant intègre toujours une part de veille sécurité sur sa technologie.

Le dossier de veille de l'étudiant (consignes) comprend : une présentation du projet professionnel et du sujet, une fiche de cadrage (QQOQCCP, 3 axes, mots-clés FR et EN), une cartographie de 10 sources minimum cotées avec la grille, un dispositif de collecte (un agrégateur RSS et au moins deux alertes), 6 fiches de veille minimum, une synthèse d'analyse (positionnement de la technologie sur le cycle de la hype ou sur un radar, et avis argumenté), une production partagée (page de portfolio ou lettre de veille) et un bilan réflexif. Volume indicatif 12 à 15 pages hors annexes. Pas de date de rendu.

La fiche de veille du livret (fiche 14) comporte : titre, date de l'information, source et cote, axe, résumé en 3 à 5 lignes avec ses propres mots, « Ce que ça change pour moi ou pour mon entreprise », niveau d'importance (1 à 3), mots-clés (tags), lien.

## Faits fictifs ajoutés par les fiches (à respecter)

Léo Martin est alternant dans un cabinet d'expertise comptable de 25 salariés, seul informaticien sur place, aidé par un prestataire extérieur ; une collaboratrice s'y est fait voler son mot de passe par un faux courriel. Il vise un métier de la cybersécurité et une licence professionnelle en alternance. Son sujet reformulé (fiche 04) : « L'authentification multifacteur dans un cabinet comptable de 25 salariés ».
Pixel Brut compte six développeurs ; Bastien Roche hésite à payer des abonnements à un assistant de code pour toute l'équipe ; Claire attend de Yanis une synthèse d'une page toutes les deux semaines.
Au Val-Morin, Sonia surveille la sécurité de pfSense, de l'annuaire et du NAS ; Marc limite la veille d'Inès à 2 heures par semaine ; les trois axes d'Inès sont « fonctions et maturité », « migration et coûts », « sécurité et exploitation » ; Inès prévoit une maquette de test sur un ancien serveur.
Les trois axes de Yanis : « Gains de productivité », « Risques et sécurité du code », « Bonnes pratiques en agence » ; son budget de veille est d'une heure et demie par semaine ; son agrégateur compte 18 flux et un quatrième dossier « Pile technique de l'agence ». Kodexa est un éditeur fictif d'assistant de code (étude interne : « jusqu'à 55 % plus rapide » sur une tâche, 40 développeurs). Sources fictives cotées en fiche 07 : comparatif TopLogiciels-Pro (1/10, D), vidéo TechTurbo « PROXMOX DÉTRUIT VMWARE ?! » (D), La Gazette numérique des territoires (8/10, B), documentation officielle de Proxmox VE (9/10, A).
Pixel Brut a testé l'assistant Kodexa pendant six semaines sur quatre postes (fiche 13 : 23 % de temps gagné sur le code répétitif, bogues de 14 à 17, 76 € par mois pour 4 postes). Le NAS du Val-Morin est un Stokéo sous StokéOS (fiche 11) ; règles de Marc : faille notée 9 ou plus corrigée sous 48 h, de 7 à 8,9 sous 7 jours.
