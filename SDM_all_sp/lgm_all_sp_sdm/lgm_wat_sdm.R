#!/home/fernanda/miniconda3/envs/TEST2/bin/ Rscript

library(raster)

library(modleR)

library(rbioclim)

library(hier.part)

library(geodata)

###### Final ModleR watothraustes ######
setwd("/home/fernanda/lgm_all_sp_sdm_artigo2")

###### dados para watothraustes lgm ######

occu_wat <- read.csv("Thalurania_watertonii_occ.csv", header=T)

bio_lgm <-  getData('worldclim_past', var='bio', res=2.5,lon=-38.9, lat=-4.221, past="lgm", download=T)[[c(1,4,10,11,12,15,16,17)]]

### Poligono da Am. do Sul onde os modelos ser?o projetados ##

amsul_coords <- read.csv("am_sul_poly_final.csv",header=F)

amsul_poly <- sp::SpatialPolygons(list(sp::Polygons(list(sp::Polygon(amsul_coords)), ID=1)))

preds_lgm <- raster::crop(bio_lgm, amsul_poly)

preds_lgm <- raster::mask(preds_lgm, amsul_poly)

final_folder <- "/home/fernanda/lgm_all_sp_sdm_artigo2"


## plotando as vari?veis para confer?ncia ##
#plot(!is.na(preds_lgm[[1]]),
      #legend = FALSE,
      #col = c("white", "#00A08A"))
#points(lat ~ lon, data = occu_wat, pch = 19)

sdmdata_1sp <- setup_sdmdata(species_name = "lgm_wat",
                             occurrences = occu_wat,
                             predictors = preds_lgm,
                             models_dir = final_folder,
                             partition_type = "crossvalidation",
                             cv_partitions = 5,
                             cv_n = 2,
                             seed = 512,
                             buffer_type = "mean",
                             png_sdmdata = TRUE,
                             n_back = 10000,
                             geo_filt=FALSE,
                             geo_filt_dist=10,
                             env_filter=TRUE,
                             env_distance= "centroid",
                             min_env_dist=0.05,
                             clean_dupl = TRUE,
                             clean_uni = TRUE,
                             clean_nas = TRUE,
                             select_variables = TRUE,
                             sample_proportion = 0.5,
                             cutoff = 0.7)


### Fun??o do many #######

many <- do_many(species_name = "lgm_wat",
                predictors = preds_lgm,
                models_dir = final_folder,
                png_partitions = TRUE,
                write_bin_cut = FALSE,
                write_rda = TRUE,
                bioclim = TRUE,
                domain = FALSE,
                glm = TRUE,
                svmk = TRUE,
                svme = TRUE,
                maxent = TRUE,
                maxnet = TRUE,
                rf = TRUE,
                mahal = FALSE,
                brt = TRUE,
                equalize = TRUE)

### Partition joining ###

final_model(species_name = "lgm_wat",
            algorithms = NULL, #if null it will take all the algorithms in disk
            models_dir = final_folder,
            which_models = c("raw_mean",
                             "bin_mean",
                             "bin_consensus"),
            consensus_level = 0.5,
            uncertainty = TRUE,
            overwrite = TRUE)

### Função ensemble model

ens <- ensemble_model(species_name = "lgm_wat",
                      occurrences = occu_wat,
                      performance_metric = "pROC",
                      which_ensemble = c("average",
                                         "best",
                                         "frequency",
                                         "weighted_average",
                                         "median",
                                         "pca",
                                         "consensus"),
                      consensus_level = 0.5,
                      which_final = "raw_mean",
                      models_dir = final_folder,
                      write_map = TRUE,
                      overwrite = TRUE) 

save.image('lgm_wat_final_sdm_results.RData')


