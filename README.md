# FinalProject_IP-Geo-Application_Devalopment

### Introduce

This is a project which aims to classify the **Geomorphology** in China and then visualize the **classification results in a map**. This project is based on the systems of classification on geomorphology in China. According to the height, the land is divided into five categories, which are respectively Hill, Small up and down mountain, Middle up and down mountain, Large up and down mountain and plain. After implementation of classification by using python, the results are needed to symbolize. We Combine the ArcGIS to form a thematic map. The map and the classification toolbox would be accessible for anyone who wants to use it if necessary.

### The data source

The original data of the classification zones are in raster file. We managed to get Digital Elevation Model (DEM) from the website which is free to get the available data (https://earthexplorer.usgs.gov/). The data of DEM is in raster format with WGS 84 coordinate coordinates and its resolution is 30m. The data were processed and geospatial analyzed so that it can be used for classification and mapping.

### Implementation

We mainly meet our needs through three functions:

+ *calRelief(demData, reliefSize)*: The terrain relief is calculated by DEM. This will classify Geomorphology.

+ *calRiver(demData)*: Use the Fill() function in the ArcGIS API to fill the DEM data to get flow direction and accumulation. The rivers and non-rivers are then binary-classified to obtain river elements.

+ *toPdf(aprxPath, pdfPath, mapExtent)*: This function is used to visualize Geomorphology classification results along with river features in a thematic map and then save it as a PDF file. Map templates are required to automatically create thematic maps through the program., so we designed the template in advance and passed it as a parameter to this function.

### Sample result

The result of this project is an ArcGIS tool, ***[FinalAss.tbx](https://github.com/MingleChou/FinalProject_IP-Geo-Application_Devalopment/blob/master/FinalAss.tbx)*** that can be used directly in ArcGIS Pro. The result we obtained using the test data is shown below:

![Sample result: Landform type](https://github.com/MingleChou/FinalProject_IP-Geo-Application_Devalopment/blob/master/ExampleResult.png "Landform Type")

### Contribution

The project was completed by Yiwen Liu, Jiemin Zhou and Jin Ma. Yiwen Liu is responsible for the completion of the literature research on the classification of Geomorphology and the realization of this part; Jiemin Zhou is responsible for part of the work of thematic map production, as well as program integration and improvement and project management on Github; Jin Ma is responsible for the river features extraction and thematic map production. All of us contributed in the program comments and documentation. The contribution of each of us accounts for 35%, 33%, and 32% of the total workload.
