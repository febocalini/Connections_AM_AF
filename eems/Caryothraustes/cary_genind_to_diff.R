### genind to diff -cary

library(adegenet)
library(ape)
library(hierfstat)
library(pegas)
library(dplyr)
library(tidyr)
library(tibble)
library(vcfR)
#install.packages("stringr")
library(stringr)
### Transformando vcf em genind

my_vcf_teste <- read.vcfR("cary_final_incomp_1SNP.vcf")
#3820 snps
genind_cary <- vcfR2genind(my_vcf_teste)
class(genind_cary)
nInd(genind_cary)
#15
ind_names <- indNames(genind_cary)
write.csv(ind_names, file="ind_names_cary.csv")
#removendo simulans e poli

genind_cary <- genind_cary[indNames(genind_cary) != "Car_pol_LSUMZ_B18093", drop=T,]

genind_cary <- genind_cary[indNames(genind_cary) != "Car_sim_LSUMZ_B1413", drop=T,]
genind_cary <- genind_cary[indNames(genind_cary) != "Car_sim_LSUMZ_B1414", drop=T,]


#genotype matrix
Geno2 <- genind_cary@tab
dim(Geno2)
## Keep SNPs that are observed to be bi-allelic.
multi.loci <- names(which(genind_cary@loc.n.all != 2))

## Explanation: 
## Suppose we want to remove locus, `L100` with alleles, `L100.00`, `L100.01`, `L100.02`, 
## then detect columns whose names matches the regular expression `^L100\\.\\d+$`
multi.cols <- which(grepl(paste0("^", multi.loci, "\\.\\d+$", collapse = "|"), colnames(Geno2)))
if (length(multi.cols)) Geno2 <- Geno2[, - multi.cols]
dim(Geno2)

##Let's convert the matrix to 0-1 labeling. I arbitrarily choose one allele to be the "derived" allele and, for each individual, 
#count how many copies of the derived allele it carries. 
#This is very easy if the tab matrix is of type "codom".

stopifnot(identical(genind_cary@type, 'codom'))

#Since the labeling does not matter for computing differences, I pick the second allele to label as the "derived" allele. 
#That is, I pick all loci whose name ends with .01.
#Geno3 <- Geno2[, str_detect(colnames(Geno2), "\\.01$")] ### essa linha acaba com tudo, n�o rodar

###bed to diffs function ###
bed2diffs_v2 <- function(Geno) {
  nIndiv <- nrow(Geno)
  nSites <- ncol(Geno)
  Miss <- is.na(Geno)
  ## Impute NAs with the column means (= twice the allele frequencies)
  Mean <- matrix(colMeans(Geno, na.rm = TRUE), ## a row of means
                 nrow = nIndiv, ncol = nSites, byrow = TRUE) ## a matrix with nIndiv identical rows of means
  Mean[Miss == 0] <- 0 ## Set the means that correspond to observed genotypes to 0
  Geno[Miss == 1] <- 0 ## Set the missing genotypes to 0 (used to be NA) 
  Geno <- Geno + Mean
  ## Compute similarities
  Sim <- Geno %*% t(Geno) / nSites
  SelfSim <- diag(Sim) ## self-similarities
  vector1s <- rep(1, nIndiv) ## vector of 1s
  ## This chunk generates a `diffs` matrix
  Diffs <- SelfSim %*% t(vector1s) + vector1s %*% t(SelfSim) - 2 * Sim
  Diffs
}

### vers�o 1
bed2diffs_v1 <- function(Geno) {
  nIndiv <- nrow(Geno)
  nSites <- ncol(Geno)
  Diffs <- matrix(0, nIndiv, nIndiv)
  
  for (i in seq(nIndiv - 1)) {
    for (j in seq(i + 1, nIndiv)) {
      x <- Geno[i, ]
      y <- Geno[j, ]
      Diffs[i, j] <- mean((x - y)^2, na.rm = TRUE)
      Diffs[j, i] <- Diffs[i, j]
    }
  }
  Diffs
}

### Let's compute both versions of the dissimilarity matrix and inspect the eigenvalues
Diffs_v1 <- bed2diffs_v1(Geno2)
Diffs_v2 <- bed2diffs_v2(Geno2)
Diffs_v1 <- round(Diffs_v1, digits = 6)
Diffs_v2 <- round(Diffs_v2, digits = 6)


## Check that the dissimilarity matrix has one positive eigenvalue and nIndiv-1 negative eigenvalues, as required by a full-rank Euclidean distance matrix.
sort(round(eigen(Diffs_v1)$values, digits = 2))

sort(round(eigen(Diffs_v2)$values, digits = 2))

#The condition does not hold for version 1, so let's save version 2 and use it as input to runeems.
#version1
write.table(Diffs_v1, "cary_eems.diffs", 
            col.names = FALSE, row.names = FALSE, quote = FALSE)
#version2
write.table(Diffs_v2, "cary_eems2.diffs", 
            col.names = FALSE, row.names = FALSE, quote = FALSE)
