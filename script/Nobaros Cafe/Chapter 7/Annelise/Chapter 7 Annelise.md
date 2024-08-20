
```mermaid
graph TD

%% Define aliases
CH7[The artist circle]
comraderie[Comraderie]
careful-warning[Careful warning]
budding-novelist[Budding novelist]
sensational-life[Sensational life]
idyllic-fantasy[Idyllic fantasy]
friendly-opinion[Friendly opinion]
inspiring-journey[Inspiring journey]
happy-ending[Happy ending]
familiar-taste[Familiar taste]
dreaming-of-annelise[Final dream Annelise]
comforting-shoulder[Comforting shoulder]
last-stretch[The last stretch]
roommate-advice[Roommate advice]
artist-advice[Artist advice]
her-masterpiece[Her masterpiece]
first-look-yuugen[First look Yuugen]
first-look-artist[First look artist]
her-happy-ending[Her happy ending]
her-life-journey[Her life journey]
mirror7[Sweven mirror Annelise]
hiraeth[Hiraeth]
kalopsia[Kalopsia]

%% Define node formatting for routes
classDef spirit-route fill:#d9d9d9,stroke:#999999,stroke-width:4px
classDef emi-route fill:#ffbcca,stroke:#f393a7,stroke-width:4px
classDef annelise-route fill:#fff2cc,stroke:#efcd7b,stroke-width:4px

%% Establish node connections
CH7--Encourage Annelise to write-->comraderie
CH7--Warn Annelise of the commitment required-->careful-warning
comraderie & careful-warning-->budding-novelist
budding-novelist--If 'Confession Annelise' in CH6-->sensational-life
budding-novelist-->idyllic-fantasy
sensational-life & idyllic-fantasy-->friendly-opinion
friendly-opinion--The hero's journey is the most satisfying-->inspiring-journey
friendly-opinion--The happy ending is the most satisfying-->happy-ending
inspiring-journey & happy-ending-->familiar-taste-->dreaming-of-annelise-->comforting-shoulder-->last-stretch
last-stretch--Ask Yuugen roommates for advice-->roommate-advice
last-stretch--Ask artist circle for advice-->artist-advice
roommate-advice & artist-advice-->her-masterpiece
her-masterpiece--??+ intimacy points-->first-look-yuugen
her-masterpiece--Less than ?? intimacy points-->first-look-artist
first-look-yuugen--Good ending-->her-life-journey-->mirror7-->hiraeth
first-look-artist--Bad ending-->her-happy-ending-->kalopsia

%% Format the routes & link to script files accordingly
%%---------------------------------------------------------------------------
%% General storyline
class CH7,budding-novelist,friendly-opinion,familiar-taste,dreaming-of-annelise,comforting-shoulder,last-stretch,her-masterpiece internal-link
class dreaming-of-annelise emi-route

%% Spiritguiding
class mirror7 spirit-route
class mirror7 internal-link

%% Annelise decisions
class comraderie,careful-warning,sensational-life,idyllic-fantasy,inspiring-journey,happy-ending,roommate-advice,artist-advice,first-look-yuugen,first-look-artist,her-happy-ending,her-life-journey,hiraeth,kalopsia annelise-route
class comraderie,careful-warning,sensational-life,idyllic-fantasy,inspiring-journey,happy-ending,roommate-advice,artist-advice,first-look-yuugen,first-look-artist,her-happy-ending,her-life-journey,hiraeth,kalopsia internal-link

```
