resume_cours_cyber_reglementations.md



Introduction aux directives et réglementations en cybersécurité --- Fiche de cours
Objectif du cours : comprendre quelles règles s'appliquent à une
organisation, pourquoi elles existent, et comment transformer des
exigences réglementaires en mesures de cybersécurité concrètes.

1. L'idée centrale du cours
La cybersécurité n'est plus seulement un problème technique.

Une cyberattaque peut avoir des conséquences :

économiques : pertes financières, arrêt de production ;

organisationnelles : interruption des activités ;

juridiques : obligations et sanctions ;

sociétales : impact sur les citoyens et les services essentiels ;

réputationnelles : perte de confiance.

Exemple simple
Une attaque par ransomware contre une usine peut provoquer :

attaque → indisponibilité du SI → arrêt de production → retards →
pertes financières → perte de confiance

👉 La cybersécurité participe donc directement à la continuité de
l'activité.

2. Pourquoi réglementer la cybersécurité ?
2.1 La cybersécurité crée de la confiance
Un service numérique sécurisé doit notamment garantir le triptyque :

Principe Signification

Confidentialité seules les personnes autorisées
peuvent accéder aux informations

Intégrité les informations ne sont pas
modifiées de manière non autorisée

On retrouve ces trois notions dans de nombreux contextes :
entreprise/client, banque/client, hôpital/patient,
administration/citoyen, etc.

2.2 Pourquoi ne pas laisser chaque entreprise choisir son niveau de sécurité ?
Parce qu'une attaque peut dépasser l'organisation directement attaquée.

Exemples :

hôpital ;

banque ;

opérateur télécom ;

centrale énergétique ;

réseau d'eau ;

administration.

Une attaque contre ce type d'organisation peut affecter la population,
l'économie ou la continuité de services essentiels.

La réglementation sert donc notamment à imposer un niveau minimal de
sécurité lorsque les enjeux le justifient.

3. Pourquoi responsabiliser toute l'organisation ?
Une erreur fréquente consiste à penser :

« La cybersécurité est le problème du service informatique. »

Le cours présente une vision plus large :

La cybersécurité est une responsabilité de l'organisation.

Elle concerne notamment :

la direction ;

le RSSI ;

la DSI ;

les métiers ;

les utilisateurs ;

les fournisseurs ;

les sous-traitants.

À retenir
La responsabilité ne peut pas être entièrement transférée au service IT.

4. Obligation ≠ recommandation
Il faut faire attention au vocabulaire.

Recommandation
« Il est recommandé d'utiliser l'authentification multifacteur. »

Il s'agit d'une orientation ou d'une bonne pratique.

Obligation
« L'organisation doit mettre en œuvre certaines mesures prévues par le
cadre qui lui est applicable. »

Il s'agit d'une obligation lorsque le texte est juridiquement
contraignant et applicable à l'organisation.

👉 Toujours commencer par déterminer le texte applicable et son
périmètre.

5. Loi, règlement, directive, norme et référentiel
C'est une distinction fondamentale du cours.

5.1 Loi
Une loi est une règle adoptée par le Parlement dans les domaines
relevant de la loi.

Elle peut notamment concerner :

la sécurité ;

les données ;

les systèmes informatiques ;

les infractions numériques ;

les obligations des organisations.

5.2 Règlement européen
Un règlement européen est un acte juridique de l'Union européenne
directement applicable dans les États membres.

Exemple
RGPD --- Règlement (UE) 2016/679

5.3 Directive européenne
Une directive fixe des objectifs que les États membres doivent
atteindre.

Elle doit être transposée dans le droit national.

Exemple
NIS2 --- Directive (UE) 2022/2555

Elle traite notamment :

de la gestion des risques ;

de la sécurité des systèmes ;

des incidents ;

de la continuité ;

de la chaîne d'approvisionnement ;

de la gouvernance.

5.4 Norme
Une norme est un document élaboré selon un processus de normalisation.

⚠️ Une norme n'est pas automatiquement une loi.

Exemple :

ISO/IEC 27001

Une entreprise peut décider d'appliquer ISO 27001 sans que cela signifie
automatiquement que la loi lui impose cette norme.

Il faut toujours vérifier le contexte :

juridique ;

contractuel ;

sectoriel.

5.5 Référentiel
Un référentiel est un ensemble structuré de :

règles ;

pratiques ;

contrôles ;

recommandations ;

exigences.

Il sert de cadre de référence pour organiser ou évaluer la sécurité.

Exemple :

RGS --- Référentiel général de sécurité

⚠️ Un référentiel peut avoir une portée réglementaire lorsqu'un texte le
rend applicable, mais tous les référentiels ne sont pas automatiquement
des lois.

6. Les grands textes à connaître
Le cours présente plusieurs textes importants. Pour les distinguer,
pose-toi cette question :

Qu'est-ce que je cherche principalement à protéger ?

Texte Ce qu'il cible Exemple
principalement

RGPD Données personnelles données clients, RH,
étudiants

NIS2 Organisations/services énergie, eau, santé,
essentiels ou importants numérique

CRA Produits comportant des caméra, routeur, objet
éléments numériques connecté

DORA Résilience banques, assurances,
opérationnelle du fintechs
secteur financier

7. RGPD : protéger les données personnelles
7.1 Qu'est-ce que le RGPD ?
Le RGPD est le Règlement (UE) 2016/679 relatif à la protection
des données à caractère personnel.

C'est un règlement européen, donc il est directement applicable dans
les États membres.

7.2 Pourquoi est-il important en cybersécurité ?
Le RGPD n'est pas une réglementation « cyber » au sens strict.

Son objectif principal est de protéger les données personnelles.

Mais pour protéger ces données, il faut mettre en place des mesures de
sécurité adaptées au risque.

Exemples de données personnelles
nom ;

prénom ;

adresse ;

téléphone ;

e-mail ;

données RH ;

données financières ;

données de santé ;

informations scolaires.

7.3 Exemple : fuite de données
Une école possède une base contenant :

8 000 étudiants ;

noms ;

e-mails ;

notes ;

informations administratives.

Un pirate vole la base.

Il faut alors se demander :

Y a-t-il des données personnelles ? → Oui

Y a-t-il une violation de données ? → Oui

L'incident doit-il être analysé ? → Oui

Faut-il notifier la CNIL ? → Cela dépend notamment du risque.

Faut-il informer les personnes concernées ? → En cas de risque
élevé, selon les conditions applicables.

Le cours rappelle qu'une violation présentant un risque doit être
notifiée à la CNIL dans les meilleurs délais et, lorsque cela est
nécessaire, au plus tard dans les 72 heures après sa prise de
connaissance.

Mesures de protection possibles
chiffrement ;

contrôle des accès ;

restriction des copies ;

sensibilisation ;

sauvegardes sécurisées.

8. NIS2 : protéger la résilience des organisations importantes
8.1 Pourquoi NIS2 ?
Le RGPD se concentre principalement sur les données personnelles.

NIS2 répond à une autre problématique :

Comment maintenir la sécurité et la résilience des services et
organisations importants ?

Exemple :

Un hôpital peut perdre l'accès à son système informatique sans qu'aucune
donnée ne soit volée. L'impact peut pourtant être extrêmement grave.

8.2 NIS2 en bref
NIS2 = Directive (UE) 2022/2555

Elle remplace la première directive NIS de 2016 et élargit le cadre
européen.

Le cours met notamment en avant :

davantage de secteurs concernés ;

davantage d'organisations concernées ;

davantage de responsabilités pour la direction ;

gestion obligatoire des risques et des incidents.

Secteurs cités dans le cours
énergie ;

transport ;

santé ;

banques ;

infrastructures numériques ;

eau ;

administration publique ;

services numériques ;

certaines activités industrielles.

NIS2 distingue notamment :

les entités essentielles ;

les entités importantes.

⚠️ Il faut toujours vérifier les critères précis d'application.

9. CRA : sécuriser les produits numériques
9.1 Le problème
Que faire si le problème ne vient pas de l'organisation mais du
produit lui-même ?

Exemples :

caméra connectée ;

routeur ;

logiciel ;

appareil IoT ;

objet connecté ;

équipement industriel connecté.

C'est ici qu'intervient le Cyber Resilience Act (CRA).

9.2 CRA en bref
CRA = Règlement (UE) 2024/2847

Il établit des exigences horizontales de cybersécurité pour les produits
comportant des éléments numériques.

La cybersécurité doit être prise en compte tout au long du cycle de vie
:

conception → développement → production → mise sur le marché →
maintenance → gestion des vulnérabilités

Le cours mentionne notamment :

remontée des vulnérabilités ;

correction des vulnérabilités ;

mises à jour de sécurité pendant une période définie.

Idée importante
Le fabricant et les autres opérateurs économiques concernés ont une
responsabilité en matière de cybersécurité du produit.

10. DORA : résilience du secteur financier
DORA = Digital Operational Resilience Act

Le cours le rattache au secteur financier :

banques ;

assurances ;

fintechs ;

etc.

Objectif
Assurer la continuité des services, y compris en cas de
cyberattaque.

Le cours mentionne notamment :

scénarios de crise ;

tests de résilience ;

journalisation et traçabilité ;

contrôle des prestataires externes ;

audits de sécurité documentés.

Le cours indique une applicabilité à partir de janvier 2025.

11. LPM : infrastructures critiques
La LPM --- Loi de Programmation Militaire est présentée dans le
cours comme visant la protection des infrastructures critiques
nationales.

Le cours cite notamment :

OIV : Opérateur d'Importance Vitale ;

OSE : Opérateur de Services Essentiels.

Exigences citées :

audits de cybersécurité réguliers ;

systèmes durcis ;

plans d'alerte et de réponse.

Le cours souligne également que des entreprises non directement visées
peuvent être concernées lorsqu'elles interviennent dans la chaîne de
valeur.

12. Extraterritorialité
12.1 Définition
L'extraterritorialité correspond à la capacité d'une réglementation ou
d'un État à avoir des effets sur des données ou activités au-delà de
ses frontières territoriales.

Exemple : RGPD
Le RGPD ne concerne pas uniquement les entreprises physiquement
installées dans l'UE.

Il peut également s'appliquer à une organisation située hors UE
lorsqu'elle :

propose des biens ou services à des personnes se trouvant dans l'UE
;

ou, dans certaines situations, surveille leur comportement.

Exemple : CLOUD Act
Le cours présente le CLOUD Act américain comme une autre difficulté.

Sous certaines conditions et procédures légales, les autorités
américaines peuvent obtenir des données détenues par des fournisseurs
soumis à la juridiction américaine, même si les données sont stockées
sur des serveurs situés à l'étranger.

Idée clé
L'endroit où les données sont physiquement stockées n'est pas toujours
le seul critère.

Il faut également regarder les liens juridiques avec les fournisseurs.

13. ANSSI : rôle en France
ANSSI = Agence nationale de la sécurité des systèmes d'information

Le cours la présente comme l'autorité nationale française de référence
en matière de cybersécurité.

Ses missions comprennent notamment :

expertise ;

réglementation ;

accompagnement ;

prévention ;

réponse aux incidents ;

protection des systèmes sensibles ;

certification/qualification dans certains cadres ;

coordination nationale.

14. Pourquoi utiliser des normes ?
Une organisation peut acheter :

un antivirus ;

un pare-feu ;

une solution de sauvegarde.

Mais cela ne garantit pas que la sécurité est réellement maîtrisée.

Une norme permet d'avoir une approche globale et structurée.

Elle aide notamment à :

structurer la sécurité ;

identifier les risques ;

définir les responsabilités ;

mettre en place des mesures ;

contrôler leur efficacité ;

améliorer continuellement la sécurité.

15. ISO/IEC 27001 : le SMSI
15.1 Objectif
ISO/IEC 27001 concerne le Système de Management de la Sécurité de
l'Information (SMSI).

En anglais :

ISMS --- Information Security Management System

L'idée fondamentale :

Organiser la sécurité de l'information comme un système de management.

15.2 Le SMSI
Le SMSI permet notamment de :

définir les objectifs de sécurité ;

identifier les risques ;

choisir des mesures ;

définir les responsabilités ;

contrôler les résultats ;

améliorer continuellement la sécurité.

Vision simple
Identifier → Protéger → Surveiller → Contrôler → Améliorer

16. ISO 27001 vs ISO 27002
C'est une distinction à connaître.

ISO 27001 ISO 27002

Définit les exigences du SMSI Fournit des recommandations et
bonnes pratiques

Cadre de management Aide à choisir les mesures de
sécurité

Utilisée notamment pour la Sert notamment de guide de mise en
certification œuvre

Exemples de mesures abordées par ISO 27002
gestion des accès ;

gestion des incidents ;

sécurité des fournisseurs ;

sécurité des ressources humaines ;

cryptographie ;

sécurité physique ;

sécurité des systèmes.

17. L'approche par les risques
L'une des idées les plus importantes du cours :

On ne peut pas protéger toutes les informations de la même manière.

Il faut d'abord comprendre les risques.

Méthode
Identifier les actifs.

Identifier les menaces.

Identifier les vulnérabilités.

Évaluer les impacts.

Déterminer le niveau de risque.

Choisir les mesures de sécurité.

Exemple
Actif : base de données clients

Menace : vol de données

Vulnérabilité : serveur mal sécurisé

Impacts : - perte de confidentialité ; - sanctions ; - atteinte à
l'image.

Risque : important

Mesures : - contrôle des accès ; - chiffrement ; - sauvegardes ; -
surveillance ; - tests de sécurité.

18. Les familles de mesures de sécurité
Le cours distingue quatre grandes catégories dans ISO 27002.

Mesures organisationnelles
Exemples :

politiques de sécurité ;

responsabilités ;

gestion des fournisseurs ;

gestion des incidents ;

continuité d'activité.

Mesures liées aux personnes
Exemples :

sensibilisation ;

formation ;

gestion des responsabilités ;

gestion des départs ;

changements de poste.

Mesures physiques
Exemples :

contrôle d'accès aux bâtiments ;

protection des salles serveurs ;

vidéosurveillance ;

protection contre les incendies.

Mesures technologiques
Exemples :

authentification ;

contrôle des accès ;

chiffrement ;

sauvegarde ;

journalisation ;

protection contre les logiciels malveillants.

19. Conformité : comment démontrer qu'on respecte les exigences ?
La conformité ne consiste pas simplement à dire :

« Nous sommes sécurisés. »

Il faut pouvoir apporter des preuves.

Exemples :

politique de sécurité ;

registre RGPD ;

inventaire des actifs ;

journaux ;

rapports d'audit ;

preuves de sensibilisation.

Logique d'audit
Vérifier → auditer → collecter les preuves → identifier les écarts →
corriger

20. Hardening : réduire la surface d'attaque
Le hardening, ou durcissement, désigne les bonnes pratiques
techniques visant à réduire la surface d'attaque.

Exemples :

désactiver les services inutiles ;

fermer les ports non nécessaires ;

gérer finement les droits ;

appliquer des GPO ;

maintenir les systèmes à jour ;

chiffrer les disques et les flux ;

activer les journaux d'audit.

Le hardening contribue également à démontrer la mise en œuvre de mesures
de sécurité adaptées.

21. Gestion des incidents --- ISO/IEC 27035
ISO/IEC 27035 est une série de normes consacrée à la gestion des
incidents de sécurité de l'information.

Elle fournit une démarche permettant de :

se préparer ;

détecter ;

signaler ;

évaluer ;

répondre ;

tirer les enseignements des incidents.

Le cours présente notamment :

27035-1:2023 : principes et processus ;

27035-2:2023 : planification et préparation ;

27035-3:2020 : opérations de réponse ;

27035-4:2024 : coordination.

Cycle simple d'incident
Détection → Analyse → Confinement → Correction → Restauration → Retour
d'expérience

22. ISO 22301 : continuité d'activité
ISO 22301 concerne le Système de Management de la Continuité
d'Activité (SMCA / BCMS).

Objectif :

permettre à l'organisation de continuer à fonctionner ou de reprendre
rapidement après une crise ou une interruption majeure.

Elle aide à :

identifier les activités critiques ;

analyser les impacts ;

préparer les plans de continuité et de reprise ;

tester les dispositifs ;

réduire les temps d'arrêt.

Trois notions à connaître
BIA --- Business Impact Analysis
Analyse des impacts métier permettant notamment de déterminer :

activités critiques ;

durée maximale d'interruption acceptable ;

ressources nécessaires à la reprise.

PCA --- Plan de Continuité d'Activité
Permet de maintenir les services essentiels pendant la crise.

PRA --- Plan de Reprise d'Activité
Permet de revenir à un fonctionnement normal après l'incident.

À retenir
PCA = continuer pendant la crise

PRA = revenir après la crise

23. IEC 62443 : systèmes industriels
La famille IEC 62443 concerne la cybersécurité des systèmes
industriels (ICS/OT).

Elle s'applique notamment aux :

usines ;

stations de traitement d'eau ;

réseaux électriques ;

infrastructures critiques.

Elle définit des exigences pour :

exploitants ;

intégrateurs ;

fabricants.

Concepts importants
Zones et conduits
Le réseau industriel est segmenté en zones de sécurité.

Security Levels --- SL
Niveaux de sécurité allant de SL1 à SL4 selon les capacités des
attaquants.

Défense en profondeur
On multiplie les barrières :

pare-feu ;

cloisonnement ;

supervision ;

contrôle d'accès.

Exemple d'architecture
Réseau entreprise → DMZ industrielle → SCADA → PLC

24. ISO 31000 : management des risques
ISO 31000 fournit un cadre général de gestion des risques.

Elle n'est pas spécifique à la cybersécurité.

Processus présenté :

Identification ;

Analyse ;

Évaluation ;

Traitement ;

Surveillance.

Le cours indique que l'approche EBIOS RM est fortement compatible
avec les principes d'ISO 31000.

25. ISO 21434 : cybersécurité automobile
ISO 21434 concerne la cybersécurité des véhicules routiers.

Elle vise notamment :

calculateurs embarqués ;

réseaux CAN ;

logiciels automobiles ;

mises à jour OTA.

Elle cherche notamment à protéger contre :

le piratage d'un véhicule connecté ;

la compromission des mises à jour ;

la prise de contrôle à distance.

26. NIST Cybersecurity Framework 2.0
Le NIST CSF 2.0 est un cadre de référence permettant de gérer et
réduire les risques de cybersécurité dans différents types
d'organisations.

Il repose sur 6 fonctions.

Les 6 fonctions à mémoriser
1. GOVERN --- Gouverner
Définir :

stratégie cyber ;

responsabilités ;

gestion des risques.

2. IDENTIFY --- Identifier
inventorier les actifs ;

identifier les risques.

3. PROTECT --- Protéger
contrôle d'accès ;

formation ;

protection des données.

4. DETECT --- Détecter
supervision ;

détection d'anomalies.

5. RESPOND --- Répondre
gestion des incidents ;

communication de crise.

6. RECOVER --- Rétablir
reprise des activités ;

retour à la normale.

Mémo
G → I → P → D → R → R

Govern → Identify → Protect → Detect → Respond → Recover

27. EBIOS Risk Manager
EBIOS Risk Manager est une méthode de l'ANSSI pour analyser et
traiter les risques numériques.

Elle aide à choisir des mesures adaptées aux menaces réelles.

Les 5 ateliers
Atelier 1 --- Cadrage et socle de sécurité
Définir le périmètre étudié.

Atelier 2 --- Sources de risque
Identifier les attaquants potentiels.

Atelier 3 --- Scénarios stratégiques
Analyser les grandes menaces.

Atelier 4 --- Scénarios opérationnels
Étudier les chemins d'attaque de manière détaillée.

Atelier 5 --- Traitement du risque
Choisir les mesures de sécurité.

Particularité
EBIOS RM prend en compte :

les menaces cyber ;

le contexte métier ;

l'écosystème de l'organisation.

28. Common Criteria --- ISO/IEC 15408
Common Criteria permet d'évaluer et de certifier le niveau de
sécurité d'un produit informatique.

Exemples de produits :

pare-feu ;

cartes à puce ;

systèmes d'exploitation ;

équipements réseau ;

composants de sécurité.

Les niveaux EAL vont de :

EAL1 → EAL7

avec EAL7 comme niveau maximal présenté dans le cours.

Le cours indique une utilisation notamment dans les marchés
gouvernementaux et de défense.

29. Cartographie rapide : quel texte pour quel problème ?
C'est probablement la partie la plus utile pour raisonner sur un cas
pratique.

Situation Cadre principal présenté dans le
cours

Données personnelles RGPD

Service essentiel / organisation NIS2
importante

Produit connecté vendu sur le CRA
marché

Banque / assurance / finance DORA

Infrastructure critique LPM

Management de la sécurité de ISO 27001
l'information

Bonnes pratiques de sécurité ISO 27002

Gestion des incidents ISO 27035

Continuité d'activité ISO 22301

Systèmes industriels / OT IEC 62443

Management général des risques ISO 31000

Automobile ISO 21434

Framework cyber général NIST CSF 2.0

Analyse des risques cyber en France EBIOS RM

⚠️ Attention : plusieurs cadres peuvent s'appliquer simultanément.

30. La méthode à utiliser en examen
Lorsqu'on te donne une entreprise ou un système, ne commence pas
directement par citer une réglementation.

Utilise cette méthode :

Étape 1 --- Identifier ce qu'on protège
Exemples :

données personnelles ;

système industriel ;

produit connecté ;

service bancaire ;

infrastructure critique.

Étape 2 --- Identifier l'activité
Exemples :

santé ;

énergie ;

eau ;

finance ;

commerce ;

industrie ;

services numériques.

Étape 3 --- Identifier les risques
Exemples :

ransomware ;

phishing ;

fuite de données ;

vol d'ordinateur ;

mauvaise configuration cloud ;

accès non autorisé ;

vulnérabilité logicielle.

Étape 4 --- Chercher le cadre applicable
Exemple :

données personnelles → RGPD ;

service essentiel → NIS2 ;

produit connecté → CRA ;

finance → DORA.

Étape 5 --- Déterminer les mesures
Exemples :

MFA ;

chiffrement ;

sauvegardes ;

contrôle des accès ;

mises à jour ;

segmentation ;

supervision ;

sensibilisation.

Étape 6 --- Prévoir les preuves
Exemples :

politiques ;

journaux ;

rapports d'audit ;

inventaires ;

preuves de formation ;

procédures.

Schéma global à mémoriser
Texte réglementaire

↓

Champ d'application

↓

Obligations

↓

Exigences de sécurité

↓

Risques

↓

Mesures de sécurité

↓

Contrôle / conformité

31. Cas pratique : EasyShop
Le cours propose une PME fictive appelée EasyShop.

Elle possède notamment :

site web ;

application mobile ;

base clients ;

base fournisseurs ;

système de paiement ;

messagerie ;

serveurs cloud ;

ordinateurs portables ;

Wi-Fi ;

VPN.

Elle traite notamment :

noms/prénoms ;

adresses ;

e-mails ;

téléphones ;

historique des commandes ;

comptes clients ;

données des salariés.

Risques identifiés
Risque Conséquence

Fuite de données clients Violation du RGPD + perte de confiance
Piratage du site Indisponibilité ou vol d'informations
Phishing Compromission de comptes
Vol d'un portable Divulgation de données
Accès VPN non autorisé Intrusion
Mauvaise configuration cloud Exposition des données

Mesures proposées dans le cours
MFA ;

chiffrement ;

sauvegardes ;

sensibilisation au phishing ;

gestion des accès ;

mises à jour de sécurité.

Conformité
Pour démontrer la conformité, on peut conserver :

politiques de sécurité ;

registre RGPD ;

inventaire des actifs ;

journaux ;

rapports d'audit ;

preuves de sensibilisation.

32. Sanctions mentionnées dans le cours
Le cours donne les exemples suivants :

Texte Exemple d'impact

RGPD jusqu'à 20 M€ ou 4 % du CA mondial
NIS2 sanctions administratives
DORA contrôles du régulateur
CRA retrait de produits non conformes

33. Les points à absolument connaître
Si tu dois réviser rapidement, retiens au minimum ceci :

1. Cybersécurité ≠ uniquement informatique
Elle concerne aussi :

économie + droit + organisation + société + gouvernance

2. Une obligation dépend du champ d'application
Toutes les organisations n'ont pas les mêmes obligations.

3. Les textes ne sont pas interchangeables
RGPD → données personnelles

NIS2 → organisations/services importants

CRA → produits numériques

DORA → finance

LPM → infrastructures critiques

4. Une norme n'est pas automatiquement une loi
ISO 27001 ≠ obligation légale automatique

5. ISO 27001 et ISO 27002 sont différentes
27001 → exigences du SMSI

27002 → recommandations/mesures

6. PCA et PRA
PCA → continuer pendant la crise

PRA → reprendre après la crise

7. NIST CSF 2.0
Govern → Identify → Protect → Detect → Respond → Recover

8. EBIOS RM
Cadrage → Sources de risque → Scénarios stratégiques → Scénarios
opérationnels → Traitement

9. Conformité = preuves
Une organisation doit pouvoir démontrer que les mesures existent et
fonctionnent.

34. Mini-quiz de révision
Questions
Quelle est la différence fondamentale entre un règlement et une
directive européenne ?

Le RGPD protège principalement quoi ?

NIS2 cherche principalement à renforcer quoi ?

Quel texte concerne les produits comportant des éléments numériques
?

Quel texte concerne particulièrement le secteur financier ?

Une norme ISO est-elle automatiquement une loi ?

Quelle différence entre ISO 27001 et ISO 27002 ?

Que signifie MFA ?

Quelle différence entre PCA et PRA ?

À quoi sert l'ISO 27035 ?

À quoi sert l'IEC 62443 ?

Quelles sont les 6 fonctions du NIST CSF 2.0 ?

Combien d'ateliers sont présentés pour EBIOS RM ?

Quel est le rôle général de l'ANSSI ?

Pourquoi faut-il toujours vérifier le champ d'application d'un texte
?

Réponses
Règlement : directement applicable dans les États membres.
Directive : objectifs à atteindre et transposition dans le droit
national.

Les données à caractère personnel.

La cybersécurité et la résilience des organisations/services
importants.

CRA.

DORA.

Non.

27001 définit les exigences du SMSI ; 27002 fournit des
recommandations et bonnes pratiques de sécurité.

Multi-Factor Authentication / authentification multifacteur.

PCA : maintenir les activités pendant la crise ; PRA :
revenir à un fonctionnement normal après l'incident.

À structurer la gestion des incidents de sécurité de
l'information.

À traiter la cybersécurité des systèmes industriels ICS/OT.

Govern, Identify, Protect, Detect, Respond, Recover.

5 ateliers.

Expertise, réglementation, accompagnement, prévention, réponse aux
incidents, protection des systèmes sensibles,
certification/qualification dans certains cadres et coordination
nationale.

Parce que toutes les organisations n'ont pas les mêmes
obligations et qu'un texte n'est contraignant que dans son
périmètre d'application.

35. Résumé en une page
La réglementation cybersécurité définit des obligations dans
certains périmètres. Les normes et référentiels aident à organiser
concrètement la sécurité.

Les 5 réflexes
Qu'est-ce que je protège ?

Quels sont les risques ?

Quel texte s'applique ?

Quelles mesures dois-je mettre en place ?

Comment puis-je prouver que je suis conforme ?

Les associations essentielles
DONNÉES PERSONNELLES
        ↓
      RGPD

SERVICES / ORGANISATIONS IMPORTANTES
        ↓
      NIS2

PRODUITS NUMÉRIQUES
        ↓
      CRA

SECTEUR FINANCIER
        ↓
      DORA

INFRASTRUCTURES CRITIQUES
        ↓
      LPM
Et pour la mise en œuvre :

ISO 27001  → Management de la sécurité
ISO 27002  → Mesures / bonnes pratiques
ISO 27035  → Gestion des incidents
ISO 22301  → Continuité d'activité
IEC 62443  → Systèmes industriels
ISO 31000  → Gestion des risques
ISO 21434  → Automobile
NIST CSF   → Cadre de gestion cyber
EBIOS RM   → Analyse des risques cyber
ISO 15408  → Évaluation de produits
La phrase à retenir
Le professionnel cybersécurité transforme les exigences
réglementaires en mesures de sécurité adaptées aux risques, puis doit
être capable d'en démontrer la mise en œuvre.


