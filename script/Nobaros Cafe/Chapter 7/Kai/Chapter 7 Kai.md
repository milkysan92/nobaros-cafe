```mermaid
graph TD

%% Define aliases
CH7[Morning recollection]
together[Here for you]
silent-comfort[Silent comfort]
outing[Special date]
jeweller[Jeweller workshop]
bracelet[Bracelet charm]
amulet[Lucky amulet]
ring[Childhood ring]
sunset-reflection[Sunset reflection]
about-sister[About sister]
sibling-bond[Sibling bond]
childhood[Their childhood]
personal-burden[Personal burden]
his-will[His will]
sudden-recollection[Sudden recollection]
before-nobaros[Before Nobaros]
back-to-kai[Back to Kai]
cherishing-you[Cherishing you]
relief[Relief]
future-dreams[Future dreams]
coming-home[Coming home]
solivagant[The solivagant]

%% Define node formatting for routes
classDef spirit-route fill:#d9d9d9,stroke:#999999,stroke-width:4px
classDef emi-route fill:#ffbcca,stroke:#f393a7,stroke-width:4px
classDef kai-route fill:#fad5af,stroke:#faac5f,stroke-width:4px

%% Establish node connections
CH7--'Let's figure it out together' (+10)-->together
CH7--Silently give him a hug (+5)-->silent-comfort
together & silent-comfort-->outing-->jeweller
jeweller--Recreate childhood ring (+15)-->ring
jeweller--Craft a good luck amulet (+10)-->amulet
jeweller--Make a new bracelet charm (+0)-->bracelet
ring & amulet & bracelet-->sunset-reflection
sunset-reflection--Ask what Kai's sister is like (+10)-->about-sister
sunset-reflection--Ask about Kai's relationship with his sister (+5)-->sibling-bond
about-sister & sibling-bond-->childhood
childhood--'You were just protecting her' (+0)-->personal-burden-->sudden-recollection
childhood--'You're just her brother, not a parent (+15)'-->his-will-->sudden-recollection
sudden-recollection-->before-nobaros-->back-to-kai
back-to-kai--'I'm here to stay' (+15)-->cherishing-you
back-to-kai--'It was just a nosebleed (+0)'-->relief
cherishing-you & relief--->future-dreams
future-dreams--175+ intimacy points; Good ending-->coming-home
future-dreams--Less than 175 intimacy points; Bad ending-->solivagant

%% Format the routes & link to script files accordingly
%%---------------------------------------------------------------------------
%% General storyline
class before-nobaros emi-route
class CH7,outing,jeweller,sunset-reflection,childhood,sudden-recollection,back-to-kai,future-dreams internal-link

%% Kai decisions
class together,silent-comfort,bracelet,amulet,ring,about-sister,sibling-bond,personal-burden,his-will,cherishing-you,relief,coming-home,solivagant kai-route
class together,silent-comfort,bracelet,amulet,ring,about-sister,sibling-bond,personal-burden,his-will,cherishing-you,relief,coming-home,solivagant internal-link
