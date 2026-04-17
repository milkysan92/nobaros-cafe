
```mermaid
graph TD

%% Define aliases
CH2[Cafe Intro]
meet-kai[Meeting Kai]
macarons-kai[Macarons]
strawberry-kai[Strawberry tart]
meet-annelise[Meeting Annelise]
shelve-annelise[Shelve books]
dust-annelise[Continue dusting]
meet-akira[Meeting Akira]
clean-akira[Cafe duties]
chat-akira[Afternoon chat]
report-ingram[Report to Ingram]
ingram-job[About Ingram]
meeting-others[Meeting others]
customer2[New customer 2]
mirror2[Sweven mirror 2]
waterfall[Waterfall]
maple[Maple grove]
celebrate-dinner[Welcome dinner]
bathtime[Bath time]
choose-drink[Something to drink]
night-ingram[Milk and honey]
night-annelise[Lull of lavender]
night-kai[Midnight snack]
night-akira[Twilight stroll]
school-dreams[Dreaming of school]
masterchef[Pastry training]
sweets-ingram[First aid]
sweets-kai[Swimming hole]
wipe-crumb[Wipe crumb]
gesture-crumb[Tell Kai about crumb]
sweets-akira[Rooftop garden]
sweets-kai[Swimming hole]
wipe-crumb[Wipe crumb]
tell-kai[Tell Kai]
sweets-annelise[Afternoon tea]
aged-tangerine[Aged tangerine]
blueberry-bergamot[Blueberry bergamot]
group-dinner[A meal together]

%% Define node formatting for routes
classDef spirit-route fill:#d9d9d9,stroke:#999999,stroke-width:4px
classDef emi-route fill:#ffbcca,stroke:#f393a7,stroke-width:4px
classDef ingram-route fill:#9fe7ff,stroke:#78bff1,stroke-width:4px
classDef kai-route fill:#fad5af,stroke:#faac5f,stroke-width:4px
classDef akira-route fill:#c7f5c5,stroke:#86c083,stroke-width:4px
classDef annelise-route fill:#fff2cc,stroke:#efcd7b,stroke-width:4px

%% Establish node connections
CH2--Sweep foyer (+5)-->meet-kai
meet-kai--Offer macarons (+5)-->macarons-kai-->report-ingram
meet-kai--Offer a strawberry tart (+0)-->strawberry-kai-->report-ingram
CH2--Dust library (+5)-->meet-annelise
meet-annelise--Put books away (+5)-->shelve-annelise-->report-ingram
meet-annelise--Leave Annelise alone (+0)-->dust-annelise-->report-ingram
CH2--Clean tables (+5)-->meet-akira
meet-akira--Stay and chat (+5)-->chat-akira-->report-ingram
meet-akira--Clear tables (+0)-->clean-akira-->report-ingram
report-ingram--Describe encounters (+0)-->meeting-others
report-ingram--Ask about Ingram (+10)-->ingram-job-->meeting-others
meeting-others-->customer2-->mirror2--Follow the trail-->waterfall
mirror2--Go to maple trees-->maple
maple & waterfall-->celebrate-dinner
celebrate-dinner-->bathtime
bathtime--Head straight to bed (+10)-->night-akira
bathtime--Head downstairs-->choose-drink
choose-drink--Milk (+10)-->night-ingram
choose-drink--Water (+10)-->night-kai
choose-drink--Tea (+10)-->night-annelise
night-ingram & night-kai & night-akira & night-annelise-->school-dreams
school-dreams-->masterchef
masterchef--Almond croissants (+10)-->sweets-ingram
masterchef--French macarons (+5)-->sweets-kai
sweets-kai--Wipe crumb for Kai (+5)-->wipe-crumb-->group-dinner
sweets-kai--Tell Kai about the crumb (+0)-->gesture-crumb-->group-dinner
masterchef--Fruit tarts (+10)-->sweets-akira
masterchef--Pound cake (+0)-->sweets-annelise
sweets-annelise--Tangerine tea (+10)-->aged-tangerine-->group-dinner
sweets-annelise--Blueberry tea (+10)-->blueberry-bergamot-->group-dinner
sweets-ingram & sweets-akira-->group-dinner

%% Format the routes & link to script files accordingly
%%---------------------------------------------------------------------------
%% General storyline
class school-dreams emi-route
class CH2,report-ingram,meeting-others,customer2,mirror2,pond,sakura,celebrate-dinner,bathtime,choose-drink,school-dreams,masterchef,group-dinner internal-link

%% Spiritguiding
class mirror2,waterfall,maple spirit-route
class mirror2,waterfall,maple internal-link

%% Ingram route
class ingram-job,night-ingram,sweets-ingram ingram-route
class ingram-job,night-ingram,sweets-ingram internal-link

%% Kai route
class meet-kai,macarons-kai,strawberry-kai,night-kai,sweets-kai,wipe-crumb,gesture-crumb kai-route
class meet-kai,macarons-kai,strawberry-kai,night-kai,sweets-kai,wipe-crumb,gesture-crumb internal-link

%% Annelise route
class meet-annelise,shelve-annelise,dust-annelise,night-annelise,sweets-annelise,aged-tangerine,blueberry-bergamot annelise-route
class meet-annelise,shelve-annelise,dust-annelise,night-annelise,sweets-annelise,aged-tangerine,blueberry-bergamot internal-link

%% Akira route
class meet-akira,clean-akira,chat-akira,night-akira,sweets-akira akira-route
class meet-akira,clean-akira,chat-akira,night-akira,sweets-akira internal-link

```



