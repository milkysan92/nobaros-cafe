
```mermaid
graph TD

%% Define aliases
CH4[Sweets contest]
spectate-match[Spectate the match]
sweets-akira[Etude in E Minor]
sweets-ingram[La Campanella]
spectate-finish[Another song]
judge-sweets[Coordinate the match]
sweets-annelise[Strawberry shortcake]
sweets-kai[Sachertorte]
customer4[New customer 4]
mirror4[Sweven mirror 4]
meet-him[Meet at cafe]
stay-home[Stay at home]
kings-game[The King game]
tiebreaker[Tiebreaker]
king-kai[Kissing Kai]
king-akira[Kissing Akira]
king-ingram[Kissing Ingram]
king-annelise[Her courage]
shohei-dreams[Dreaming of Shohei]

%% Define node formatting for routes
classDef spirit-route fill:#d9d9d9,stroke:#999999,stroke-width:4px
classDef emi-route fill:#ffbcca,stroke:#f393a7,stroke-width:4px
classDef ingram-route fill:#9fe7ff,stroke:#78bff1,stroke-width:4px
classDef kai-route fill:#fad5af,stroke:#faac5f,stroke-width:4px
classDef akira-route fill:#c7f5c5,stroke:#86c083,stroke-width:4px
classDef annelise-route fill:#fff2cc,stroke:#efcd7b,stroke-width:4px

%% Establish node connections
CH4--Don't get involved-->spectate-match
spectate-match--Ask Akira to play Chopin-->sweets-akira
spectate-match--Ask Akira to play Liszt-->sweets-ingram
sweets-akira & sweets-ingram-->spectate-finish
CH4--Bring sweets for Annelise & Kaio-->judge-sweets
judge-sweets--Bring a strawberry dessert-->sweets-annelise
judge-sweets--Bring a chocolate dessert-->sweets-kai
sweets-annelise & sweets-kai & spectate-finish-->customer4-->mirror4
mirror4--Go meet Shin at cafe-->meet-him
mirror4--Stay at home-->stay-home
meet-him & stay-home-->kings-game-->tiebreaker
tiebreaker--Sit at the right-->king-annelise
tiebreaker--Sit at the left-->king-ingram
tiebreaker--Sit where you are-->king-akira
tiebreaker--Sit across the table-->king-kai
king-annelise & king-ingram & king-akira & king-kai-->shohei-dreams

%% Format the routes & link to script files accordingly
%%---------------------------------------------------------------------------
%% General storyline
class shohei-dreams emi-route
class CH4,spectate-match,spectate-finish,judge-sweets,customer4,kings-game,shohei-dreams,tiebreaker internal-link

%% Spiritguiding
class mirror4,meet-him,stay-home spirit-route
class mirror4,meet-him,stay-home internal-link

%% Ingram route
class sweets-ingram,king-ingram ingram-route
class sweets-ingram,king-ingram internal-link

%% Kai route
class sweets-kai,king-kai kai-route
class sweets-kai,king-kai internal-link

%% Annelise route
class sweets-annelise,king-annelise annelise-route
class sweets-annelise,king-annelise internal-link

%% Akira route
class sweets-akira,king-akira akira-route
class sweets-akira,king-akira internal-link

```
