## Road to Reduction

### Problem Statement:

The spectrum of how to replace fossil-fuel based energy producers is quite broad. Even between 'green activists' there is a large disagreement about where to invest in. Some say only a dozen of nuclear power plants will have a substantial impact on emission reduction, others swear by giant windmills. It's difficult for policy makers not to drown in the many trade-offs and numbers that appear on our road to reduction.

### Solution:

This vizualisation attempts to give a clear view of what the impact of the chosen policy will be on emmission reduction. The user can design it's own 'Road to Reduction' by chosing when and how much you invest in which source of energy (wind-, solar- and nuclear power). 

### Data Sources:

#### Heat map:
Wind hours: http://projects.knmi.nl/klimatologie/daggegevens/selectie.cgi (vink FHVEC aan)
Sun hours: http://projects.knmi.nl/klimatologie/daggegevens/selectie.cgi (vink SQ aan)

#### Line graph:
Calculate what how much energy "one unit" of wind, solar or nuclear power produces:
https://www.clo.nl/indicatoren/nl0019-inzet-energiedragers-en-bruto-elektriciteitsproductie

Amount of emissions fossil-fuel based power plants:
https://www.cbs.nl/nl-nl/nieuws/2018/19/uitstoot-broeikasgassen-in-2017-licht-afgenomen
https://themasites.pbl.nl/balansvandeleefomgeving/jaargang-2018/themas/energie-klimaat-lucht/emissies-broeikasgassen

External components:
d3-legend
d3-tip

#### Similar example: 

#### Hardest parts:

-Turn given 'Road to reduction' table into a dataset to generate a heat and line graph with it;
-Create heat table (new data visualisation for me);
-Generate circle and heat graph when a point on the line graph is clicked.

