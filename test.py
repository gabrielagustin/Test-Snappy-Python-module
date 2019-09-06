"""
Created on: 2019-09-05 10:25:55
@Author: gag 
"""

import snappy

from snappy import ProductIO
from snappy import HashMap

import os, gc   
from snappy import GPF

GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
HashMap = snappy.jpy.get_type('java.util.HashMap')

### Now loop through all Sentinel-1 data sub folders that are located within a super folder 
### (of course, make sure, that the data is already unzipped):

path = "/media/gag/Datos/Imagenes_satelitales/Sentinel-1B-SantaFe/"
for folder in os.listdir(path):

      print(folder)


      # gc.enable()
      
      # output = path + folder + "\\"  
      # timestamp = folder.split("_")[4] 
      # date = timestamp[:8]

      # ### Then, read in the Sentinel-1 data product:

      # sentinel_1 = ProductIO.readProduct(output + "\\manifest.safe")    
      # print sentinel_1

      # ### If polarization bands are available, spolit up your code to process VH and VV intensity data separately. 
      # ### The first step is the calibration procedure by transforming the DN values to Sigma Naught respectively. 
      # ### You can specify the parameters to output the Image in Decibels as well.

      # pols = ['VH','VV'] 
      # for p in pols:  
      #       polarization = p    
      
      #       ### CALIBRATION
      
      #       parameters = HashMap() 
      #       parameters.put('outputSigmaBand', True) 
      #       parameters.put('sourceBands', 'Intensity_' + polarization) 
      #       parameters.put('selectedPolarisations', polarization) 
      #       parameters.put('outputImageScaleInDb', False)  

      #       calib = output + date + "_calibrate_" + polarization 
      #       target_0 = GPF.createProduct("Calibration", parameters, sentinel_1) 
      #       ProductIO.writeProduct(target_0, calib, 'BEAM-DIMAP')

      # ### Next, specify a subset AOI to reduce the data amount and processing time. The AOI specified by its outer 
      # ### polygon corners and is formatted through a Well Known Text (WKT).

      #       ### SUBSET

      #       calibration = ProductIO.readProduct(calib + ".dim")    
      #       WKTReader = snappy.jpy.get_type('com.vividsolutions.jts.io.WKTReader')

      #       wkt = "POLYGON((12.76221 53.70951, 12.72085 54.07433, 13.58674 54.07981, 
      #                   13.59605 53.70875, 12.76221 53.70951))"

      #       geom = WKTReader().read(wkt)

      #       parameters = HashMap()
      #       parameters.put('geoRegion', geom)
      #       parameters.put('outputImageScaleInDb', False)

      #       subset = output + date + "_subset_" + polarization
      #       target_1 = GPF.createProduct("Subset", parameters, calibration)
      #       ProductIO.writeProduct(target_1, subset, 'BEAM-DIMAP')


      # ### Apply a Range Doppler Terrain Correction to correct for layover and foreshortening effects,
      # ### by using the SRTM 3 arcsecond product (90m) that is downloaded automatically. You could also specify
      # ### an own DEM product with a higher spatial resolution from a local path:

      #       ### TERRAIN CORRECTION
      
      #       parameters = HashMap()     
      #       parameters.put('demResamplingMethod', 'NEAREST_NEIGHBOUR') 
      #       parameters.put('imgResamplingMethod', 'NEAREST_NEIGHBOUR') 
      #       parameters.put('demName', 'SRTM 3Sec') 
      #       parameters.put('pixelSpacingInMeter', 10.0) 
      #       parameters.put('sourceBands', 'Sigma0_' + polarization)
      
      #       terrain = output + date + "_corrected_" + polarization 
      #       target_2 = GPF.createProduct("Terrain-Correction", parameters, subset) 
      #       ProductIO.writeProduct(target_2, terrain, 'GeoTIFF')



