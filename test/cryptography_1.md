# Chapitre 1 — Introduction à la Cryptographie

**Module :** Chiffrement et cryptographie
**Année :** 2024-2025

---

## 1. Motivation

- Les besoins en sécurité ne cessent de croître, l'informatique est omniprésente.
- Les échanges de données exigent des réseaux sécurisés.
- La sécurité doit être assurée à plusieurs niveaux (du plus large au plus fin) :
  **Réseau(x) → Machine (host) → Application → Données**

---

## 2. Définition de la cryptographie

> La cryptographie est un processus qui utilise des algorithmes mathématiques pour rendre des informations illisibles, les protégeant ainsi de tout accès non autorisé.

Exemple : transformer un texte brut en texte chiffré (« ciphertext ») via un algorithme = une série d'opérations mathématiques.

---

## 3. Objectifs de la sécurité et rôle de la cryptographie

L'objectif est de protéger les données dans **tous leurs états** : en transmission, stockées, en cours de traitement.

| Principe | Définition | Contribution de la cryptographie |
|---|---|---|
| **Confidentialité** | Seuls les utilisateurs autorisés accèdent à l'information | Chiffrement (AES, RSA, etc.) |
| **Intégrité** | L'information n'a pas été altérée | Fonctions de hachage (SHA-2, SHA-3) |
| **Authenticité** | L'identité de l'émetteur est vérifiée | Signature numérique, certificats |
| **Non-répudiation** | L'émetteur ne peut nier l'envoi d'un message | Signature électronique, journaux horodatés |
| **Disponibilité** | Accès aux données garanti en temps voulu | Indirectement via résilience (VPN, sécurisation des communications) |

> Note : la **signature numérique** est un procédé technique cryptographique, tandis que la **signature électronique** est un concept juridique plus global (qui peut inclure ou non une signature numérique).

**« Pas de cybersécurité sans cryptographie. Pas de confiance numérique sans sécurité. »**

### Exemples de domaines d'utilisation

| Domaine | Utilisation de la cryptographie |
|---|---|
| Banque/Finance | Chiffrement des transactions, signature numérique |
| Santé | Confidentialité des dossiers médicaux |
| E-commerce | Paiements sécurisés (3D Secure, SSL/TLS) |
| Cloud Computing | Chiffrement des données stockées |
| Justice/Contrats | Signature électronique, preuve numérique |
| Blockchain | Hachage, consensus, signature numérique |

---

## 4. Histoire et évolution de la cryptographie

### Origines antiques (avant le Ve siècle)
Objectif : masquer un message de l'ennemi ou d'un tiers.
- **Égypte ancienne** : écriture codée dans les hiéroglyphes (usages symboliques).
- **Scytale spartiate** : bande de cuir enroulée autour d'un bâton (transposition).
- **Chiffre d'Atbash** (Hébreux) : une lettre remplacée par son opposée dans l'alphabet.
- **Chiffre de César** (Rome) : décalage alphabétique fixe.

### Moyen Âge et Renaissance (Ve – XVe siècle)
- Chiffres **monoalphabétiques** (un seul alphabet de substitution pour tout le message) : César, substitution simple.
- **Limite** : vulnérables à l'**analyse fréquentielle**, méthode inventée par **Al-Kindi** (IXe siècle).
- **Chiffre de Vigenère** (XVIe siècle) : premier chiffrement **polyalphabétique**, utilise un mot-clé pour varier le décalage lettre par lettre — longtemps considéré comme incassable.

### XVIIIe siècle
- **Thomas Jefferson** propose la roue de chiffrement.

### De l'ère mécanique à l'informatique
- Machines à rotors : **Enigma** (Allemagne), **Purple/Code 97** (Japon) — utilisées massivement lors des deux guerres mondiales.
- WWII : les Alliés cassent Enigma grâce à **Alan Turing** et Bletchley Park.
- Les besoins en cryptanalyse stimulent la naissance de l'informatique.

### Cryptographie moderne (1970 – aujourd'hui)
- **Clé symétrique** : DES adopté en 1977 par le NIST (une seule clé pour chiffrer/déchiffrer).
- **Cryptographie asymétrique** :
  - 1976 : **Diffie-Hellman** — notion de clé publique / clé privée.
  - 1977 : **RSA** (Rivest, Shamir, Adleman) — premier algorithme à clé publique robuste.
- **Algorithmes modernes** : **AES** (2001, remplace DES) ; **SHA** (intégrité des données).

### Cryptographie contemporaine et avenir
- **Domaines actuels** : TLS/SSL, blockchain & crypto-monnaies, vote électronique, e-santé, cloud sécurisé.
- **Vers l'avenir** :
  - **Cryptographie post-quantique** : résister aux ordinateurs quantiques.
  - **Zero-Knowledge Proofs (ZKP)** : prouver une information sans la révéler.
  - **Cryptographie homomorphe** : calculer sur des données chiffrées sans les déchiffrer.

---

## 5. Protocole de chiffrement (schéma général)

```
Texte clair → [Algorithme cryptographique + Clé de chiffrement] → Texte chiffré (Cryptogramme)
Texte chiffré → [Algorithme cryptographique + Clé de déchiffrement] → Texte clair
```
Le texte chiffré peut aussi faire l'objet d'une **cryptanalyse**, visant à retrouver le texte clair et/ou la clé.

---

## 6. Vocabulaire de base

- **Cryptologie** : science mathématique du secret, composée de deux branches :
  - **Cryptographie** : conception des procédés de chiffrement.
  - **Cryptanalyse** : étude des textes chiffrés pour retrouver le message original en exploitant les failles.
- **Chiffrement** : transformation d'une donnée en forme illisible pour tout autre que l'expéditeur/destinataire (opération inverse = déchiffrement).
- **Texte chiffré (cryptogramme)** : résultat de l'application du chiffrement sur un texte clair.
- **Clé** : paramètre secret permettant le chiffrement et/ou le déchiffrement.

### Crypto-système
Un crypto-système est défini par :
- l'ensemble des clés possibles (**espace de clés**) ;
- les textes clairs et textes chiffrés associés à un algorithme donné.

Un algorithme de chiffrement comprend 3 parties :
1. **Génération des clés K**
2. **Fonction de chiffrement** (transforme M en texte chiffré)
3. **Fonction de déchiffrement** (retrouve M à partir de C)

### Notations
- M = texte clair, C = texte chiffré, K = clé (symétrique) ou (Ke, Kd) (asymétrique)
- E(x) = fonction de chiffrement, D(x) = fonction de déchiffrement
- Propriété de base : **M = D(E(M))**
- Cas symétrique : **M = D(C) si C = E(M)**

### Terminologie (Alice, Bob, Oscar)
- **Alice et Bob** : souhaitent se transmettre des informations.
- **Oscar** : opposant qui souhaite espionner Alice et Bob.
- **Objectif fondamental** : permettre à Alice et Bob de communiquer sur un canal peu sûr sans qu'Oscar comprenne l'échange.
- **Texte clair** : information qu'Alice souhaite transmettre à Bob.
- **Chiffrement** : M → C = E(M)
- **Déchiffrement** : D(C) = D(E(M)) = M (D et E sont injectives)

---

## 7. Propriétés théoriques des algorithmes de cryptographie

- **Confusion** : le texte chiffré ne doit révéler aucune régularité statistique du texte clair.
- **Diffusion** : une petite modification du texte clair doit entraîner une modification importante du texte chiffré.

### Relation fondamentale (en pratique)
```
E_Ke(M) = C
D_Kd(C) = M
```
avec Ke, Kd ∈ {espace des clés}. Deux catégories de systèmes cryptographiques :
1. **Systèmes à clé secrète (symétriques)** : Ke = Kd = K
2. **Systèmes à clé publique (asymétriques)** : Ke ≠ Kd

### Exemple : représentation mathématique de E et D
Pour analyser un système cryptographique, on représente les messages M et C par des valeurs numériques (ex. alphabet de n = 38 caractères, ou n = 256 en ASCII).

Exemple — **chiffrement par décalage** (arithmétique modulaire) :
```
E_K(M) = M + K  mod n
D_K(C) = C - K  mod n
```

---

## 8. Applications modernes de la cryptographie

### a) Communication sécurisée
- **Web (HTTPS)** : SSL/TLS — cryptographie asymétrique (RSA, ECC) + chiffrement symétrique (AES) après échange de clés.
- **Messagerie chiffrée** (Signal, WhatsApp, Telegram) : chiffrement de bout en bout.
  - Technologies : Protocole Signal, Double Ratchet, Curve25519, AES-GCM.
- **Paiements/e-commerce** : cartes à puce, 3D Secure, Apple Pay.

### b) Stockage et identité
- **Chiffrement de fichiers/disques** : BitLocker, VeraCrypt.
- **Cloud sécurisé** : données chiffrées au repos et en transit.
- **Certificats numériques (PKI)** : garantissent l'identité (HTTPS, VPN, S/MIME).
- **Authentification forte (MFA)** : mot de passe + SMS/biométrie (ex. Google Authenticator).

### c) Signature électronique, légal et santé
- **Signature numérique** : documents/contrats sans impression, conforme eIDAS.
- **Archivage électronique sécurisé** : horodatage + empreinte numérique.
- **Santé numérique** : téléconsultation, chiffrement des dossiers médicaux, conformité RGPD/HIPAA.

### d) Blockchain, cyberdéfense, IoT
- **Blockchain/crypto-monnaies** (Bitcoin, Ethereum, Monero) : hachage (SHA-256), signatures numériques, smart contracts.
- **Cyberdéfense** : cryptographie quantique (en développement), chiffrement militaire, protection contre l'espionnage.
- **IoT** : chiffrement intégré (caméras, montres, thermostats), authentification machine-à-machine.

---

## Glossaire des acronymes rencontrés

| Acronyme | Signification |
|---|---|
| NIST | National Institute of Standards and Technology |
| AES | Advanced Encryption Standard |
| DES | Data Encryption Standard |
| RSA | Rivest, Shamir, Adleman |
| PKI | Public Key Infrastructure |
| eIDAS | Electronic Identification, Authentication and Trust Services |
| RGPD | Règlement Général sur la Protection des Données |
| HIPAA | Health Insurance Portability and Accountability Act |
| ZKP | Zero-Knowledge Proofs |