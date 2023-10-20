### Hemi results eems deme 200 com 20M de itera??es ####
setwd("E:/eems_artigo2/results/eems_artigo2/hemi_eems/d200")
library(rEEMSplots)
Sys.setenv(R_GSCMD="C:/Program Files/gs/gs9.53.1/bin/gswin64c.exe")
# Use the provided example or supply the path to your own EEMS run.
hemidata_path <- getwd()

eems_results <- file.path(hemidata_path, c("output_run1","output_run2","output_run3") )
name_figures <- file.path(hemidata_path, "hemi_eems_d200pdf")
library("rgdal")
projection_none <- "+proj=longlat +datum=WGS84"
projection_mercator <- "+proj=merc +datum=WGS84"
library("rworldmap")
library("rworldxtra")
library("RColorBrewer")
##Add arbitrary graphical elements (points, lines, etc)
library("rgdal") ## Defines functions to transform spatial elements
library("rworldmap") ## Defines world map

projection_none <- "+proj=longlat +datum=WGS84"
projection_mercator <- "+proj=merc +datum=WGS84"
#### Add the map of America explicitly by passing the shape file # mapafinal RODAS ESSE PARA PDF
map_world <- getMap()
map_america <- map_world[which(map_world@data$continent == "South America"), ]
plot(map_america)
eems.plots(mcmcpath = eems_results,
           plotpath = paste0(name_figures, "-shapefile"),
           longlat = TRUE,
           out.png = FALSE,
           m.plot.xy = {plot(map_america, col = NA, add = TRUE)},
           q.plot.xy = {plot(map_america, col = NA, add = TRUE)})


############# D400 ####################

### hemi results eems deme 400 com 20M de itera??es ####
setwd("E:/eems_artigo2/results/eems_artigo2/hemi_eems/d400")

# Use the provided example or supply the path to your own EEMS run.
hemidata_path4 <- getwd()

eems_results4 <- file.path(hemidata_path4, c("output_run1","output_run2","output_run3") )
name_figures4 <- file.path(hemidata_path4, "hemi_eems_d400pdf")
projection_none <- "+proj=longlat +datum=WGS84"
projection_mercator <- "+proj=merc +datum=WGS84"

##Add arbitrary graphical elements (points, lines, etc)

projection_none <- "+proj=longlat +datum=WGS84"
projection_mercator <- "+proj=merc +datum=WGS84"
#### Add the map of America explicitly by passing the shape file # mapafinal RODAS ESSE PARA PDF
map_world <- getMap()
map_america <- map_world[which(map_world@data$continent == "South America"), ]
plot(map_america)
eems.plots(mcmcpath = eems_results4,
           plotpath = paste0(name_figures4, "-shapefile"),
           longlat = TRUE,
           out.png = FALSE,
           m.plot.xy = {plot(map_america, col = NA, add = TRUE)},
           q.plot.xy = {plot(map_america, col = NA, add = TRUE)})


############# D600 ####################

### hemi results eems deme 600 com 20M de itera??es ####
setwd("E:/eems_artigo2/results/eems_artigo2/hemi_eems/d600")

# Use the provided example or supply the path to your own EEMS run.
hemidata_path6 <- getwd()

eems_results6 <- file.path(hemidata_path6, c("output_run1","output_run2","output_run3") )
name_figures6 <- file.path(hemidata_path6, "hemi_eems_d600pdf")
projection_none <- "+proj=longlat +datum=WGS84"
projection_mercator <- "+proj=merc +datum=WGS84"

##Add arbitrary graphical elements (points, lines, etc)

projection_none <- "+proj=longlat +datum=WGS84"
projection_mercator <- "+proj=merc +datum=WGS84"
#### Add the map of America explicitly by passing the shape file # mapafinal RODAS ESSE PARA PDF
map_world <- getMap()
map_america <- map_world[which(map_world@data$continent == "South America"), ]
plot(map_america)
eems.plots(mcmcpath = eems_results6,
           plotpath = paste0(name_figures6, "-shapefile"),
           longlat = TRUE,
           out.png = FALSE,
           m.plot.xy = {plot(map_america, col = NA, add = TRUE)},
           q.plot.xy = {plot(map_america, col = NA, add = TRUE)})

###### script final para projeção com pontos ########


setwd("D:/eems_artigo2/results/eems_artigo2/hemi_eems/d400")
hemidata_path <- getwd()
eems_results <- file.path(hemidata_path, c("output_run1","output_run2","output_run3") )
name_figures <- file.path(hemidata_path, "hemi_eems_d400pointsfinal")
coordenadas <- read.table("hemi_eems.coord", header=FALSE, sep="\t", dec=".", colClasses="numeric")

projection_none <- "+proj=longlat +datum=WGS84"
projection_mercator <- "+proj=merc +datum=WGS84"
#### Add the map of America explicitly by passing the shape file # mapafinal RODAS ESSE PARA PDF
map_world <- getMap()
map_america <- map_world[which(map_world@data$continent == "South America"), ]
plot(map_america)
eems.plots(mcmcpath = eems_results,
           plotpath = paste0(name_figures, "-shapefile"),
           longlat = TRUE,
           out.png = FALSE,
           m.plot.xy = {plot(map_america, col = NA, add = TRUE)
             points(coordenadas, col = "deeppink4", pch = 19)},
           q.plot.xy = {plot(map_america, col = NA, add = TRUE) 
             points(coordenadas, col = "deeppink4", pch = 19)},
           res=300)

