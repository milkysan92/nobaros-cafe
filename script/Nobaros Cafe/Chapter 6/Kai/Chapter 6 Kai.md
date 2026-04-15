
```mermaid
graph TD

%% Define aliases
CH6[New customer Kai]
florist-kai[Florist Kai]
hanakotoba[Hanakotoba]
passion[Flower passion]
town-square[Town square Kai]
casual-outfit[Casual outfit]
swimsuit[Cute swimsuit]
nabe[Nabe Kai]
camellia-kai[Camellia Kai]
sakura-kai[Sakura Kai]
about-akina[About Akina]
rough-night[Rough night]
forehead-kiss[Forehead kiss]
hold-hands[Holding hands]
childhood-memory[Childhood Kai]
daybreak[Daybreak Kai]
convince-kai[Convince Kai]
comfort-kai[Comfort Kai]
mirror6[Sweven mirror 6]
thoughts[Night thoughts]
cuddle[Innocent cuddles]

%% Define node formatting for routes
classDef spirit-route fill:#d9d9d9,stroke:#999999,stroke-width:4px
classDef emi-route fill:#ffbcca,stroke:#f393a7,stroke-width:4px
classDef kai-route fill:#fad5af,stroke:#faac5f,stroke-width:4px

%% Establish node connections
CH6-->florist-kai--Ask about camellias VS sakura (+5)-->hanakotoba-->town-square
florist-kai--Ask about love for flowers (+0)-->passion-->town-square
town-square--Choose a tee and shorts (+10)-->casual-outfit-->nabe
town-square--Borrow a cute swimsuit (+0)-->swimsuit-->nabe
nabe--Choose the camellias (+15)-->camellia-kai-->about-akina
nabe--Choose the sakura blossoms (+5)-->sakura-kai-->about-akina
about-akina-->rough-night--Give him a forehead kiss (+15)-->forehead-kiss
forehead-kiss-->daybreak
rough-night--Lay the flower in his hands (+0)-->hold-hands
forehead-kiss & hold-hands--If not 'Remembering Kai'-->childhood-memory-->daybreak
hold-hands-->daybreak
daybreak--Convince Kai to confront mom (+15)-->convince-kai-->mirror6
daybreak--Reassure Kai's feelings (+0)-->comfort-kai-->mirror6
mirror6--165+ intimacy points-->thoughts
mirror6--Less than 165 intimacy points-->cuddle

%% Format the routes & link to script files accordingly
%%---------------------------------------------------------------------------
%% General storyline
class childhood-memory emi-route
class CH6,florist-kai,town-square,nabe,about-akina,rough-night,daybreak internal-link

%% Spiritguiding
class mirror6 spirit-route
class mirror6 internal-link

%% Kai decisions
class hanakotoba,passion,casual-outfit,swimsuit,camellia-kai,sakura-kai,forehead-kiss,hold-hands,convince-kai,comfort-kai,thoughts,cuddle kai-route
class hanakotoba,passion,casual-outfit,swimsuit,camellia-kai,sakura-kai,forehead-kiss,hold-hands,convince-kai,comfort-kai,thoughts,cuddle internal-link

```
