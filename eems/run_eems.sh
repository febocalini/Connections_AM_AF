##### EEMS ######

##installation

#Download EEMS
git clone https://github.com/dipetkov/eems.git
#Download Eigen 3.3.9

tar xvzf /home/fernanda/Downloads/eigen-3.3.9.tar.gz

#copy to  /usr/local/include

sudo cp -r /home/fernanda/Documents/eems/eigen-3.3.9 /usr/local/include

cd /usr/local/include/eigen-3.3.9 
sudo cp -r Eigen/ .. ## copiar a pasta Eigen para include

#Download & install Boost 1_76

tar xvzf /home/fernanda/Downloads/boost_1_76_0.tar.gz
cd /home/fernanda/Documents/eems/boost_1_76_0
./bootstrap.sh #create the Boost build utilities
sudo ./b2 install --prefix=/usr/local/lib #build Boost libraries

#Update the variables EIGEN_INC, BOOST_INC, BOOST_LIB in the EEMS Makefile
#Link dependencies to program
cd /home/fernanda/Documents/eems/runeems_snps/src

make linux



#1. Transformar o vcf em diffs no R 

#2. Fazer o arquivo .coord - arquivo somente com as coordenadas separados por \t

#3. Para fazer o arquivo .outer eu fiz um poligono no Qgis de acordo com esse tutorial https://github.com/mtop/speciesgeocoder/wiki/Tutorial-for-creating-polygons-in-QGIS

# Fazer o arquivo com os parâmetros para rodar o programa, .in - fazer para 3 cadeias - 3 arquivos .in
cd /home/fernanda/Documents/eems/runeems_snps/src

#### Caryothraustes
#1
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/cary_eems/d400/cary_eems_chain1.in --seed 123

#2
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/cary_eems/d400/cary_eems_chain2.in --seed 145

#3
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/cary_eems/d400/cary_eems_chain3.in --seed 235


### Hemithraupis

#1
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/hemi_eems/d400/hemi_eems_chain1.in --seed 123

#2
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/hemi_eems/d400/hemi_eems_chain2.in --seed 145

#3
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/hemi_eems/d400/hemi_eems_chain3.in --seed 235


### Picumnus

#1
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/pic_eems/d400/pic_eems_chain1.in --seed 123

#2
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/pic_eems/d400/pic_eems_chain2.in --seed 145

#3
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/pic_eems/d400/pic_eems_chain3.in --seed 235


### Thalurania

#1
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/tha_eems/d400/tha_eems_chain1.in --seed 123

#2
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/tha_eems/d400/tha_eems_chain2.in --seed 145

#3
./runeems_snps --params /media/fernanda/BOCALINI_HD/eems_artigo2/eems_artigo2/tha_eems/d400/tha_eems_chain3.in --seed 235


