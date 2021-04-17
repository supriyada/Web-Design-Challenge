# Web-Design-Challenge

## Overview: 
> We are using HTML and Bootstrap CSS to create a dashboard showing off the analysis on weather data.<br>
------------
## Pre-requisites:

> - Excel sheet containing the weather data for the cities. `cities.csv`.
> - Visulaizations on comparisons between latitude & other factors: max temperature, cloudiness, wind speed, humidity.
-------------
## Webiste overview:
> The pages included :
  > - `index.html` 
  > - `comparison.html`
  > - `data.html`
  > - `max_temprature.html`
  > - `cloudiness.html`
  > - `wind_speed.html`
  > - `humidity.html`
  > 
### Detailed description:
> The index.html page has the description of the website with the side bar. The sidebar has all the visualizations that are linked to the corresponding pages.<br>
> The comparison.html page has all four plots in the same screen to visually compare all the plots. They are linked to the corresponding visualization pages as well.<br>
> The data.html page displays the data used in plotting the weather informations.<br>
> Visualiztion pages has the description of the plot and the results drawn from the plots.<br>
> All the html pages are designed to be responsive pages.<br>
> At 576px page size, the changes can be noticed explicitely.<br>
> From any page, clicking on the text `Latitude` in the top left takes to the main page that is.,`index.html`<br>

### Retreiving data:
> The data.html page receives the data from the `cities.csv` file. <br>
> The .csv is converted into pandas dataframe and later into html page using to_html() and bootstrap classes.<br>
> This output is then embedded in the data.html page.<br>
