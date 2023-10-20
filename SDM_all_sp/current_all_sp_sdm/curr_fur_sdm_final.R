#!/home/fernanda/miniconda3/envs/TEST2/bin/ Rscript

library(raster)

library(modleR)

library(rbioclim)

library(hier.part)

library(geodata)

###### Final ModleR T. furcata ######
setwd("/home/fernanda/curr_all_sp_sdm_artigo2")

###### dados para T. furcata presente ######

occu_fur <- read.csv("Thalurania_furcata_occ.csv", header=T)

bio_curr <- worldclim_global(var='bio', res=0.5, path="/home/fernanda/curr_all_sp_sdm_artigo2", download=F)[[c(1,4,10,11,12,15,16,17)]]
bio_curr_final <- raster::stack(bio_curr)

### Poligono da Am. do Sul onde os modelos serÃo projetados ##

am_sul_coords <- read.csv("am_sul_poly_final.csv",header=F)

am_sul_poly <- sp::SpatialPolygons(list(sp::Polygons(list(sp::Polygon(am_sul_coords)), ID=1)))

preds_curr <- raster::crop(bio_curr_final, am_sul_poly)

preds_curr <- raster::mask(preds_curr, am_sul_poly)

final_folder <- "/home/fernanda/curr_all_sp_sdm_artigo2"

## plotando as variáveis para conferência ##


#plot(!is.na(preds_curr[[1]]), legend = FALSE, col = c("white", "#00A08A"))
#points(lat ~ lon, data = occu_cary, pch = 19)

#####Rodando o ModleR
sdmdata_1sp <- setup_sdmdata(species_name = "curr_fur",
                             occurrences = occu_fur,
                             predictors = preds_curr,
                             models_dir = final_folder,
                             partition_type = "crossvalidation",
                             cv_partitions = 5,
                             cv_n = 2,
                             seed = 123,
                             buffer_type = "mean",
                             png_sdmdata = TRUE,
                             n_back = 10000,
                             geo_filt=FALSE,
                             geo_filt_dist=10,
                             min_env_dist=0.05,
                             clean_dupl = TRUE,
                             clean_uni = TRUE,
                             clean_nas = TRUE,
                             select_variables = TRUE,
                             sample_proportion = 0.5,
                             cutoff = 0.7)


### Função do many #######

many <- do_many(species_name = "curr_fur",
                predictors = preds_curr,
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
                brt = FALSE,
                equalize = TRUE)

### Partition joining ###

final_model(species_name = "curr_fur",
            algorithms = NULL, #if null it will take all the algorithms in disk
            models_dir = final_folder,
            which_models = c("raw_mean",
                             "bin_mean",
                             "bin_consensus"),
            consensus_level = 0.5,
            uncertainty = TRUE,
            overwrite = TRUE)

### FunÃ§Ã£o ensemble model

ens <- ensemble_model(species_name = "curr_fur",
                      occurrences = occu_fur,
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

save.image('curr_fur_final_sdm_results.RData')


