



Résumé pédagogique --- Cours SCADA
1. Objectif du cours
Le cours présente les systèmes SCADA (Supervisory Control And Data
Acquisition), c'est-à-dire des systèmes de supervision, de contrôle
et d'acquisition de données en temps réel utilisés dans l'industrie et
les infrastructures techniques.

L'idée centrale à retenir :

Un SCADA permet de surveiller un processus physique, de récupérer
ses données et de le contrôler à distance.

Le cours aborde : - la définition d'un système SCADA ; - ses principaux
composants ; - son architecture générale ; - la stratégie de contrôle
; - les moyens de communication ; - les logiciels SCADA ; - les domaines
d'application.

2. Qu'est-ce qu'un système SCADA ?
SCADA signifie Supervisory Control And Data Acquisition.

C'est un système de télégestion à grande échelle capable de : - traiter
en temps réel un grand nombre de mesures ; - surveiller des
installations techniques ; - envoyer des commandes à distance ; -
centraliser les informations provenant du terrain.

Un système SCADA regroupe notamment : - du matériel ; - des contrôleurs
; - des réseaux de communication ; - une base de données ; - des
logiciels de gestion des entrées/sorties ; - une IHM/HMI (Interface
Homme-Machine).

À retenir
SCADA = mesurer + surveiller + contrôler + communiquer + historiser.

3. Les principaux composants d'un SCADA
3.1 IHM / HMI
L'Interface Homme-Machine (HMI) permet à l'opérateur humain de : -
visualiser les données du processus ; - surveiller son état ; -
effectuer des actions de contrôle.

Exemple
Un opérateur peut voir sur son écran : - une température ; - une
pression ; - l'état d'une machine ; - une alarme ; - une valeur de
production.

L'IHM constitue donc le lien entre l'opérateur et le processus
industriel.

3.2 RTU --- Remote Terminal Unit
Les RTU sont des unités terminales distantes.

Elles servent notamment à : - raccorder les capteurs au système ; -
récupérer les signaux ; - convertir les signaux en données numériques
; - transmettre ces données au système de supervision.

Schéma simplifié
Capteurs → RTU → Réseau → Système SCADA
3.3 PLC / API --- Automate Programmable
Le PLC (Programmable Logic Controller), appelé API en
français, est un ordinateur industriel utilisé pour contrôler des
processus.

Il peut : - recevoir des informations des capteurs ; - exécuter une
logique de commande ; - piloter des équipements ; - communiquer avec le
système SCADA.

Le cours souligne que les PLC sont souvent utilisés comme équipements de
terrain parce qu'ils sont : - économiques ; - polyvalents ; - souples
; - configurables.

Différence simplifiée
Élément Rôle principal

RTU Acquisition et transmission depuis un site distant
PLC/API Contrôle logique d'un processus
SCADA Supervision et contrôle global
HMI Interface avec l'opérateur

3.4 Serveur de contrôle
Le serveur de contrôle héberge le logiciel de contrôle-commande, par
exemple : - un DCS (Distributed Control System) ; - un PLC.

Il communique avec les dispositifs de contrôle de niveau inférieur et
accède aux modules de commande sur le réseau ICS (Industrial Control
System).

3.5 Serveur SCADA / MTU
Le serveur SCADA, ou MTU (Master Terminal Unit), agit comme le
maître du système SCADA.

Les RTU et les PLC situés sur les sites distants jouent généralement le
rôle d'équipements subordonnés.

Vision simple
             SERVEUR SCADA / MTU
                     │
          ───────────┼───────────
          │          │          │
         RTU        PLC        RTU
          │          │          │
       Capteurs   Machines   Capteurs
3.6 IED --- Intelligent Electronic Device
Un IED est un appareil électronique « intelligent ».

Il peut intégrer : - l'acquisition de données ; - la communication avec
d'autres équipements ; - du contrôle local ; - du traitement local ; -
de la mémoire.

Un IED peut donc regrouper plusieurs fonctions dans un seul appareil.

3.7 Historique des données
L'historique des données est une base de données centralisée
permettant d'enregistrer les informations du processus.

Ces données peuvent être utilisées pour : - analyser le fonctionnement
; - réaliser des analyses statistiques ; - suivre les processus ; -
aider à la planification.

Exemple
Capteur
   ↓
RTU / PLC
   ↓
SCADA
   ↓
Historique des données
   ↓
Analyse / statistiques / planification
3.8 Serveur d'entrée/sortie (I/O Server)
Le serveur d'E/S (Input/Output Server) est responsable notamment de
: - collecter les informations ; - mettre temporairement les données en
mémoire ; - donner accès aux informations provenant des PLC, RTU et
autres composants.

Il peut être installé : - sur le serveur de contrôle ; - ou sur une
machine distincte.

4. Architecture générale d'un SCADA
L'architecture relie généralement trois grandes parties :

1. Terrain
On trouve : - capteurs ; - actionneurs ; - PLC ; - RTU ; - IED.

2. Communication
Les réseaux permettent de transporter les données entre le terrain et la
supervision.

3. Supervision
On trouve : - serveur SCADA/MTU ; - serveurs de contrôle ; - bases de
données ; - IHM ; - postes opérateurs.

Schéma mental
┌─────────────────────────────┐
│       SUPERVISION            │
│ SCADA / MTU / HMI / Bases   │
└──────────────┬──────────────┘
               │
          Réseau / Com
               │
┌──────────────┴──────────────┐
│          TERRAIN             │
│ PLC / RTU / IED / Capteurs  │
└──────────────┬──────────────┘
               │
        Processus physique
5. Stratégie de contrôle
La centrale de contrôle / salle de contrôle-commande est conçue
notamment pour :

contrôler l'acquisition des données ;

équilibrer la production et la demande ;

surveiller les flux ;

observer les limites du système ;

coordonner la maintenance ;

coordonner les réponses d'urgence.

En résumé
La salle de contrôle permet de transformer les informations remontées du
terrain en surveillance et actions de commande.

6. Communication dans les systèmes SCADA
La communication est indispensable car les équipements de terrain
doivent échanger des informations avec le système de supervision.

Le cours présente notamment trois types de liaisons traditionnelles :

liaisons radio ;

liaisons filaires ;

liaisons par modem / Internet.

Les protocoles SCADA sont conçus pour être relativement compacts.

Certains fonctionnent selon un principe où la station maître interroge
les RTU afin d'obtenir les informations.

Schéma
SCADA / MTU
     │
     │ interrogation / communication
     ↓
    RTU
     │
     ↓
Capteurs / équipements
7. Protocoles SCADA cités dans le cours
Le cours cite notamment :

Modbus RTU

RP570

Profibus

Ces protocoles sont historiquement liés aux systèmes industriels et
certains disposent aujourd'hui d'extensions utilisant TCP/IP.

À retenir pour l'examen
Ne pas confondre :

SCADA → système global de supervision ;

protocole → moyen utilisé pour faire communiquer les équipements
;

réseau → infrastructure permettant le transport des
communications.

8. Que permet le système de contrôle-commande ?
D'après le cours, il permet notamment de :

fournir un état du réseau ;

permettre la commande à distance ;

optimiser les performances du système ;

réaliser des opérations d'urgence ;

répartir les équipes de réparation ;

coordonner les interventions avec d'autres services.

9. Logiciels SCADA
Un logiciel SCADA reçoit les données de fonctionnement d'un système afin
de permettre sa supervision et son contrôle.

Il permet notamment : - de collecter les données provenant des capteurs
; - de traiter les informations ; - d'afficher les données ; - de
fournir des interfaces graphiques ; - d'interagir avec les équipements
industriels via les réseaux et protocoles adaptés.

10. Exemples de logiciels SCADA
10.1 SIMATIC WinCC
SIMATIC WinCC est un logiciel SCADA et une interface homme-machine
développé par Siemens.

Il est utilisé pour : - la surveillance des processus industriels ; - la
surveillance des infrastructures.

Le cours indique notamment qu'il : - fonctionne sur Windows ; - peut
être utilisé avec Siemens PCS7 et Teleperm ; - utilise Microsoft SQL
Server pour gérer les connexions ; - est accompagné de VBScript et
d'applications d'interface en langage C.

10.2 InTouch Wonderware
Le cours présente InTouch Wonderware comme : - relativement facile à
prendre en main ; - doté d'un système de script flexible ; - adapté aux
grands systèmes lorsque les scripts sont correctement conçus ; - équipé
d'un client OPC permettant la connexion à de nombreux automates.

Le cours indique également qu'il occupe une part importante du marché
des logiciels SCADA.

10.3 Vijeo Designer
Vijeo Designer, de Schneider, est présenté comme un logiciel
relativement facile à prendre en main.

Il existe en plusieurs versions permettant de programmer : - des HMI
Magelis ; - des terminaux graphiques.

Le cours indique qu'il succède à Vijeo Citect.

10.4 Iconics
Le cours présente Iconics comme plus difficile à prendre en main,
notamment pour les scripts.

Ses caractéristiques citées sont : - nombreuses fonctions ; -
possibilité de réaliser rapidement de petites applications ; -
intégration du standard OPC ; - limitation du nombre de variables en
fonction de la licence.

10.5 Studio 5000 View Designer
Développé par Rockwell, il permet de programmer les panneaux de
supervision de la gamme PanelView 5000.

10.6 PCVue
PCVue, d'Arc Informatique, est présenté comme : - relativement
facile à prendre en main ; - disposant d'un client OPC ; - utilisé dans
les domaines de la GTB/GTC.

10.7 Movicon
Movicon, de Progea, est présenté comme facile à prendre en main.

Le cours mentionne notamment une limitation du nombre de variables dans
la version d'évaluation.

11. Domaines d'application du SCADA
Les systèmes SCADA sont utilisés dans de nombreux secteurs.

11.1 Grandes installations industrielles automatisées
Exemples cités dans le cours :

métallurgie ;

laminoirs à froid et à chaud ;

production pétrolière ;

distillation ;

production et stockage agroalimentaire ;

lait ;

céréales ;

production manufacturière ;

automobile ;

biens de consommation.

11.2 Installations réparties géographiquement
Les SCADA peuvent superviser des installations réparties sur plusieurs
sites.

Exemples :

alimentation en eau potable ;

traitement des eaux usées ;

gestion des flux hydrauliques ;

canaux ;

rivières ;

barrages ;

tunnels ;

ventilation ;

sécurité.

11.3 Gestion technique des bâtiments
Les SCADA sont également utilisés pour la GTB/GTC.

Exemples :

chauffage ;

éclairage ;

économies d'énergie ;

alarmes incendie ;

contrôle d'accès ;

alarmes intrusion.

12. Exemple concret pour comprendre
Imaginons une installation de traitement de l'eau.

             OPÉRATEUR
                 │
                 ▼
              HMI/SCADA
                 │
          Serveur SCADA
                 │
              Réseau
                 │
          ┌──────┴──────┐
          ▼             ▼
         PLC           RTU
          │             │
       Capteurs      Capteurs
          │             │
          └──────┬──────┘
                 ▼
       Installation d'eau
Fonctionnement
Les capteurs mesurent les paramètres du processus.

Les mesures arrivent vers un PLC ou une RTU.

Les données sont transmises par le réseau.

Le SCADA collecte et affiche les informations.

L'opérateur consulte les données sur l'HMI.

L'opérateur peut envoyer une commande.

Le PLC/RTU applique la commande au processus.

13. SCADA : les éléments à bien distinguer
Élément Fonction

Capteur Mesure une grandeur physique
Actionneur Agit sur le processus
RTU Acquiert et transmet les données d'un site distant
PLC/API Exécute une logique de contrôle industriel
IED Acquiert, communique et peut effectuer du contrôle local
Réseau Transporte les données
Protocole Définit les règles de communication
Serveur SCADA/MTU Supervise et coordonne le système
HMI/IHM Permet à l'opérateur de visualiser et contrôler
Historique Stocke les données du processus
I/O Server Collecte et met à disposition les données d'E/S

14. Les mots-clés à mémoriser
SCADA
Supervisory Control And Data Acquisition

→ Supervision + contrôle + acquisition de données.

HMI / IHM
→ Interface entre l'humain et la machine.

RTU
→ Équipement de terrain utilisé notamment pour acquérir et transmettre
les données.

PLC / API
→ Automate industriel qui exécute des fonctions de contrôle.

MTU
→ Maître du système SCADA, généralement associé au serveur SCADA.

IED
→ Équipement électronique intelligent capable d'acquisition,
communication et traitement/contrôle local.

Historien
→ Stockage des informations du processus dans une base de données.

15. Schéma global à mémoriser
                  OPÉRATEUR
                      │
                      ▼
                 ┌─────────┐
                 │   HMI   │
                 └────┬────┘
                      │
                      ▼
              ┌──────────────┐
              │ SCADA / MTU  │
              └──────┬───────┘
                     │
               Réseau / Protocoles
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        PLC         RTU        IED
          │          │          │
          └──────────┼──────────┘
                     ▼
              CAPTEURS / ACTIONNEURS
                     │
                     ▼
             PROCESSUS PHYSIQUE
16. Méthode pour retenir le fonctionnement
Retenir cette chaîne :

Mesurer → transmettre → superviser → décider → commander →
enregistrer

1. Mesurer
Les capteurs observent le processus.

2. Transmettre
Les RTU/PLC/IED transmettent les informations.

3. Superviser
Le SCADA reçoit et affiche les informations.

4. Décider
L'opérateur analyse la situation.

5. Commander
Une commande est envoyée vers le terrain.

6. Enregistrer
Les données peuvent être conservées dans l'historique.

17. Questions possibles d'examen
Question 1 --- Que signifie SCADA ?
Réponse : Supervisory Control And Data Acquisition.

Question 2 --- Quel est le rôle principal d'un SCADA ?
Réponse : Superviser et contrôler à distance un processus tout en
acquérant et traitant ses données en temps réel.

Question 3 --- Quel est le rôle d'une HMI ?
Réponse : Présenter les données du processus à l'opérateur et lui
permettre de surveiller et contrôler le processus.

Question 4 --- Quelle est la différence entre RTU et PLC ?
Réponse : - une RTU est principalement utilisée pour
l'acquisition et la transmission des données, notamment dans des sites
distants ; - un PLC/API est un automate industriel destiné à
exécuter des fonctions de contrôle.

Question 5 --- Quel est le rôle du serveur SCADA / MTU ?
Réponse : Il agit comme le maître du système SCADA et supervise les
équipements de terrain.

Question 6 --- Citer trois moyens de communication utilisés par les SCADA.
Réponse : - radio ; - liaison filaire ; - modem/Internet.

Question 7 --- Citer trois protocoles SCADA mentionnés dans le cours.
Réponse : - Modbus RTU ; - RP570 ; - Profibus.

Question 8 --- Donner des exemples de logiciels SCADA.
Réponse : - SIMATIC WinCC ; - InTouch Wonderware ; - Vijeo Designer
; - Iconics ; - Studio 5000 View Designer ; - PCVue ; - Movicon.

Question 9 --- Donner trois domaines d'application du SCADA.
Réponse : - industrie ; - gestion de l'eau ; - gestion technique des
bâtiments.

18. Mini-quiz de révision
Q1. SCADA signifie :
A. Secure Control And Data Application
B. Supervisory Control And Data Acquisition
C. System Control And Digital Automation

Réponse : B

Q2. Quel équipement permet à l'opérateur de visualiser le processus ?
A. RTU
B. HMI
C. PLC

Réponse : B

Q3. Quel équipement est un automate industriel ?
A. PLC
B. HMI
C. Historien

Réponse : A

Q4. Quel composant stocke les données historiques du processus ?
A. Historique des données
B. RTU
C. HMI

Réponse : A

Q5. Lequel est un protocole cité dans le cours ?
A. HTML
B. Modbus RTU
C. JPEG

Réponse : B

Q6. Les SCADA peuvent-ils être utilisés dans la gestion de l'eau ?
A. Oui
B. Non

Réponse : A

19. Résumé en une page
SCADA = système de supervision et de contrôle industriel
Fonction
Un SCADA permet de :

Acquérir → communiquer → superviser → contrôler → historiser

Composants
Capteurs → mesurent ;

RTU → acquièrent/transmettent ;

PLC/API → contrôlent ;

IED → acquièrent/communiquent/traitent localement ;

Réseau → transporte les informations ;

SCADA/MTU → supervise ;

HMI → interface opérateur ;

Historien → stocke les données.

Communication
Moyens : - radio ; - filaire ; - modem/Internet.

Protocoles cités : - Modbus RTU ; - RP570 ; - Profibus.

Logiciels cités
WinCC ;

InTouch Wonderware ;

Vijeo Designer ;

Iconics ;

Studio 5000 View Designer ;

PCVue ;

Movicon.

Applications
industrie ;

pétrole ;

métallurgie ;

agroalimentaire ;

automobile ;

eau potable ;

eaux usées ;

barrages ;

tunnels ;

bâtiments ;

chauffage ;

éclairage ;

sécurité.

20. À retenir absolument
Si tu dois retenir seulement 5 choses :

SCADA = supervision + contrôle + acquisition de données.

HMI = interface entre l'opérateur et le système.

RTU/PLC/IED = équipements proches du terrain.

Le réseau et les protocoles permettent les communications.

Le SCADA est utilisé pour superviser et contrôler des
installations industrielles ou techniques, parfois réparties sur
plusieurs sites.

Formule finale
PROCESSUS
   ↓
Capteurs
   ↓
RTU / PLC / IED
   ↓
Réseau + protocoles
   ↓
SCADA / MTU
   ↓
HMI
   ↓
OPÉRATEUR
   ↓
Commande
   ↓
RTU / PLC
   ↓
PROCESSUS
Le cours conclut qu'un système SCADA permet de superviser et de prendre
en main à distance un système industriel complet, notamment en
représentant son fonctionnement physique en temps réel sur des postes de
contrôle ou des panels industriels.