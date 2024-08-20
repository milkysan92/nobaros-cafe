
```mermaid
graph TD

%% Define aliases
CH6[Her reality]
customer6[New customer Annelise]
florist-annelise[Florist Annelise]
fellow-artist[Fellow artist]
artistic-ideal[Artistic ideal]
town-square[Town square Annelise]
ikebana-girls[Ikebana girls]
arrange-camellia[Arrange camellia]
arrange-sakura[Arrange sakura]
arrange-annelise[Arrange Annelise]
nabe-dinner[Nabe Annelise]
dessert-annelise[Dessert Annelise]
dessert-akina[Dessert Akina]
rooftop-story[Rooftop story]
sudden-recollect[Sudden recollection Annelise]
kai-lore[Kai lore Annelise]
akina-lore[Akina lore Annelise]
mirror6[Sweven mirror 6]
confession-annelise[Confession Annelise]

%% Define node formatting for routes
classDef spirit-route fill:#d9d9d9,stroke:#999999,stroke-width:4px
classDef emi-route fill:#ffbcca,stroke:#f393a7,stroke-width:4px
classDef annelise-route fill:#fff2cc,stroke:#efcd7b,stroke-width:4px

%% Establish node connections
CH6-->customer6-->florist-annelise
florist-annelise--'How did you become an ikebana artist?'-->fellow-artist
florist-annelise--'What inspires you as an ikebana artist?'-->artistic-ideal
fellow-artist & artistic-ideal-->town-square-->ikebana-girls
ikebana-girls--Choose the camellias-->arrange-camellia
ikebana-girls--Choose the sakura blossoms-->arrange-sakura
ikebana-girls--Let Annelise pick first-->arrange-annelise
arrange-camellia & arrange-sakura & arrange-annelise-->nabe-dinner
nabe-dinner--??+ intimacy points-->dessert-annelise
nabe-dinner--less than ?? intimacy points-->dessert-akina
dessert-annelise & dessert-akina-->rooftop-story-->sudden-recollect
sudden-recollect--If 'Dessert Annelise'-->kai-lore
sudden-recollect--If 'Dessert Akina'-->akina-lore
kai-lore & akina-lore-->mirror6
mirror6--??+ intimacy points-->confession-annelise

%% Format the routes & link to script files accordingly
%%---------------------------------------------------------------------------
%% General storyline
class CH6,customer6,florist-annelise,town-square,ikebana-girls,nabe-dinner,rooftop-story,sudden-recollect internal-link

%% Spiritguiding
class mirror6 spirit-route
class mirror6 internal-link

%% Annelise decisions
class fellow-artist,artistic-ideal,arrange-camellia,arrange-sakura,arrange-annelise,dessert-annelise,dessert-akina,kai-lore,akina-lore,confession-annelise annelise-route
class fellow-artist,artistic-ideal,arrange-camellia,arrange-sakura,arrange-annelise,dessert-annelise,dessert-akina,kai-lore,akina-lore,confession-annelise internal-link

```
