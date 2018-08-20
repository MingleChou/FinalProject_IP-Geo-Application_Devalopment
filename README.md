# FinalProject_IP-Geo-Application_Devalopment

### Introduce

This is a project which aims to classify the **Geomorphology** in China and then visualize the **classification results in a map**. This project is based on the systems of classification on geomorphology in China. According to the height, the land is divided into five categories, which are respectively Hill, Small up and down mountain, Middle up and down mountain, Large up and down mountain and plain. After implementation of classification by using python, the results are needed to symbolize. We Combine the ArcGIS to form a thematic map. The map and the classification toolbox would be accessible for anyone who wants to use it if necessary.

### The data source

The original data of the classification zones are in raster file. We managed to get Digital Elevation Model (DEM) from the website which is free to get the available data (https://earthexplorer.usgs.gov/). The data of DEM is in raster format with WGS 84 coordinate coordinates and its resolution is 30m. The data were processed and geospatial analyzed so that it can be used for classification and mapping.

### Implementation

We mainly meet our needs through three functions:

+ *calRelief(demData, reliefSize)*: The terrain relief is calculated by DEM. This will classify Geomorphology.

+ *calRiver(demData)*: 
