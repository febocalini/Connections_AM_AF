### cary results eems deme 200 com 20M de iterações ####

library(rEEMSplots)
Sys.setenv(R_GSCMD="C:/Program Files/gs/gs9.53.1/bin/gswin64c.exe")
# Use the provided example or supply the path to your own EEMS run.
carydata_path <- getwd()

eems_results <- file.path(carydata_path, c("output_run1","output_run2","output_run3") )
name_figures <- file.path(carydata_path, "cary_eems_d200pdf")
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

### cary results eems deme 400 com 20M de iterações ####
setwd("E:/eems_artigo2/results/eems_artigo2/cary_eems/d400")

# Use the provided example or supply the path to your own EEMS run.
carydata_path4 <- getwd()

eems_results4 <- file.path(carydata_path4, c("output_run1","output_run2","output_run3") )
name_figures4 <- file.path(carydata_path4, "cary_eems_d400pdf")
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

### cary results eems deme 400 com 20M de iterações ####
setwd("E:/eems_artigo2/results/eems_artigo2/cary_eems/d600")

# Use the provided example or supply the path to your own EEMS run.
carydata_path6 <- getwd()

eems_results6 <- file.path(carydata_path6, c("output_run1","output_run2","output_run3") )
name_figures6 <- file.path(carydata_path6, "cary_eems_d600pdf")
projection_none <- "+proj=longlat +datum=WGS84"
projection_mercator <- "+proj=merc +datum=WGS84"

##Add arbitrary graphical elements (points, lines, etc)

projection_none <- "+proj=longlat +datum=WGS84"
projection_mercator <- "+proj=merc +datum=WGS84"
#### Add the map of America explicitly by passing the shape file # mapafinal RODAS ESSE PARA PDF
map_world <- getMap()
map_america <- map_world[which(map_world@data$continent == "South America"), ]
plot(map_america)
plot_coord <- read.table("cary_eems.coord")
plot_coord <- as.matrix(plot_coord)
colors <- c("red", "blue", "orange")

points_coords <- sp::spTransform(SpatialPoints(plot_coord, CRS(projection_none)),
                                CRS(projection_mercator))
## `coords_merc` is a SpatialPoints structure
## but we only need the coordinates themselves
points_coords <- points_coords@coords
eems.plots(mcmcpath = eems_results6,
           plotpath = paste0(name_figures6, "-shapefile"),
           longlat = TRUE,
           out.png = TRUE,
           m.plot.xy = {plot(map_america, col = NA, add = TRUE);
                                text(points_coords, col = rainbow(16), pch = 19); },
           q.plot.xy = {plot(map_america, col = NA, add = TRUE);
                                text(points_coords, col = rainbow(16), pch = 19); })



m.plot.xy = { plot(map_africa, col = NA, add = TRUE);
  text(coords_merc, col = colors, pch = labels, font = 2); },
  q.plot.xy = { plot(map_africa, col = NA, add = TRUE);
  text(coords_merc, col = colors, pch = labels, font = 2); })

