##### EEMS ######

##installation

#Download EEMS
git clone https://github.com/dipetkov/eems.git
#Download Eigen 3.3.9

tar xvzf /Volumes/BOCALINI_HD/eems_artigo2/eems_artigo2/eigen-3.3.9.tar.gz

#copy to  /usr/local/include

cp -r /Volumes/BOCALINI_HD/eems_artigo2/eems_artigo2/eigen-3.3.9/Eigen /usr/local/include

cd eigen-3.3.9 
 ## copiar a pasta Eigen para include

#Download & install Boost 1_76

tar xvzf /Volumes/BOCALINI_HD/eems_artigo2/eems_artigo2/boost_1_76_0.tar.gz
cd /Volumes/BOCALINI_HD/eems_artigo2/eems_artigo2/boost_1_76_0
./bootstrap.sh #create the Boost build utilities
sudo ./b2 install --prefix=/usr/local/lib #build Boost libraries

#Update the variables EIGEN_INC, BOOST_INC, BOOST_LIB in the EEMS Makefile
#/usr/local/include/eigen-3.3.9/Eigen
BOOST_LIB = /usr/local/lib
BOOST_INC = /usr/local/include
#Link dependencies to program
cd /Users/imac/eems/runeems_snps/src

make linux

make darwin #no Mac

#Install the Homebrew package manager.
#Install boost with 
brew install boost
#Install eigen3 with 
brew install eigen

#1. Transformar o vcf em diffs no R 

#2. Fazer o arquivo .coord - arquivo somente com as coordenadas separados por \t

#3. Para fazer o arquivo .outer eu fiz um poligono no Qgis de acordo com esse tutorial https://github.com/mtop/speciesgeocoder/wiki/Tutorial-for-creating-polygons-in-QGIS

#### esses passos já estão na pasta

# Fazer o arquivo com os parâmetros para rodar o programa, .in - fazer para 3 cadeias - 3 arquivos .in
##ir para a pasta com o arquivos executável
cd /Users/imac/eems/runeems_snps/src

#Cary
#1
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/cary_eems/d400/cary_eems_chain1.in --seed 123

#2
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/cary_eems/d400/cary_eems_chain2.in --seed 345

#3
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/cary_eems/d400/cary_eems_chain3.in --seed 567


#Hemithraupis
#1
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/hemi_eems/d400/hemi_eems_chain1.in --seed 123

#2
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/hemi_eems/d400/hemi_eems_chain2.in --seed 345

#3
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/hemi_eems/d400/hemi_eems_chain3.in --seed 567


### editar os caminhos para o arquivo .in que sempre fica na pasta d400 - Também editar os caminhos que estão nos arquivos .in
### Picumnus

#1
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/pic_eems/d400/pic_eems_chain1.in --seed 123

#2
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/pic_eems/d400/pic_eems_chain2.in --seed 345

#3
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/pic_eems/d400/pic_eems_chain3.in --seed 567

### Thalurania

#1
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/tha_eems/d400/tha_eems_chain1.in --seed 123

#2
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/tha_eems/d400/tha_eems_chain2.in --seed 345

#3
./runeems_snps --params /Users/imac/Desktop/eems_artigo2/tha_eems/d400/tha_eems_chain3.in --seed 567



