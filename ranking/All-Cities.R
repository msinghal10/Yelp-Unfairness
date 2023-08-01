##################################################### All Cities Combined ####################################################

library(aod)
library(ggplot2)
library(readr)
library(sandwich)
library(car)

mydata <- read_csv("/ranking/Cities-CSV/All_Cities-Combined.csv",col_types = cols(Restaurant=col_character(),Latitude=col_double(),Longitude=col_double(),Address=col_character(),PlaceID=col_character(),URL=col_character(),AverageExposure=col_double(),Stars=col_double(),ZIP=col_integer(),Count=col_integer(),White=col_integer(),ofWhite=col_double(),DWN=col_integer(),WN=col_integer(),Black=col_integer(),ofBlack=col_double(),BN=col_integer(),AmericanIndaian=col_integer(),ofAI=col_double(),AIN=col_integer(),Asian=col_integer(),ofAisan=col_double(),AN=col_integer(),NativeHawiian=col_integer(),ofNativeHawiian=col_double(),NHN=col_integer(),Edu=col_integer(),ofEDU=col_double(),HED=col_integer(),Unemployment=col_double(),HUne=col_integer(),Wealth=col_integer(),HWe=col_integer(),Attraction=col_integer(),Hotspot=col_integer()))

mylogit <- lm(AverageExposure ~ Hotspot+Stars, data=mydata)
summary(mylogit)


# Residuals:
#      Min       1Q   Median       3Q      Max 
# -0.14134 -0.05733  0.00316  0.03399  0.88884 

# Coefficients:
#             Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 0.066739   0.015330   4.353 1.39e-05 ***
# Hotspot     0.027183   0.003353   8.108 7.56e-16 ***
# Stars       0.010331   0.003642   2.837  0.00459 ** 
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# Residual standard error: 0.08882 on 2865 degrees of freedom
# Multiple R-squared:  0.02523,	Adjusted R-squared:  0.02455 
# F-statistic: 37.08 on 2 and 2865 DF,  p-value: < 2.2e-16
# 



mylogit <- miceadds::glm.cluster(Hotspot ~ WN + BN + AIN+ AN+HED + HUne + HWe, data=mydata,cluster=mydata$ZIP,family="binomial")
summary(mylogit)


# Estimate Std. Error     z value  Pr(>|z|)
# (Intercept) -0.43561469  0.3803621 -1.14526301 0.2521002
# WN          -0.03992180  0.2958256 -0.13495047 0.8926510
# BN           0.18359850  0.3010354  0.60989014 0.5419346
# AIN         -0.30961199  0.2441437 -1.26815497 0.2047426
# AN           0.02540780  0.2599718  0.09773292 0.9221444
# HED          0.33930382  0.3018038  1.12425289 0.2609058
# HUne        -0.04807908  0.3195129 -0.15047619 0.8803889
# HWe         -0.06300641  0.2994297 -0.21042135 0.8333388



##################################################### Anchorage ####################################################

mydata <- read_csv("/ranking/Cities-CSV/Anchronage.csv",col_types = cols(Restaurant=col_character(),Latitude=col_double(),Longitude=col_double(),Address=col_character(),PlaceID=col_character(),URL=col_character(),AverageExposure=col_double(),Stars=col_double(),ZIP=col_integer(),Count=col_integer(),White=col_integer(),ofWhite=col_double(),WN=col_integer(),Black=col_integer(),ofBlack=col_double(),BN=col_integer(),AmericanIndaian=col_integer(),ofAI=col_double(),AIN=col_integer(),Asian=col_integer(),ofAisan=col_double(),AN=col_integer(),NativeHawiian=col_integer(),ofNativeHawiian=col_double(),NHN=col_integer(),Edu=col_integer(),ofEDU=col_double(),HED=col_integer(),Unemployment=col_double(),HUne=col_integer(),Wealth=col_integer(),HWe=col_integer(),Attraction=col_integer(),Hotspot=col_integer()))

mydata$DWN <- ifelse(mydata$ofWhite>50, 1, 0)

mylogit <- lm(AverageExposure ~ Hotspot, data=mydata)
summary(mylogit)


# Residuals:
#   Min       1Q   Median       3Q      Max 
# -0.13282 -0.05809  0.00270  0.03341  0.89022 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 0.109776   0.002195   50.02  < 2e-16 ***
#   Hotspot     0.027258   0.003357    8.12 6.82e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.08893 on 2866 degrees of freedom
# Multiple R-squared:  0.02249,	Adjusted R-squared:  0.02215 
# F-statistic: 65.94 on 1 and 2866 DF,  p-value: 6.823e-16
# 


mylogit <- miceadds::glm.cluster(Hotspot ~ WN + BN + AIN+ AN+HED + HUne + HWe , data=mydata,cluster=mydata$ZIP,family='binomial')
summary(mylogit)
# 
# Estimate Std. Error     z value     Pr(>|z|)
# (Intercept)  0.4570946  0.1159669   3.9415974 8.094076e-05
# WN          -0.6589588  0.2232855  -2.9511933 3.165488e-03
# BN           0.5122709  0.1404363   3.6477101 2.645880e-04
# AIN          0.9726246  0.1555360   6.2533720 4.016838e-10
# AN          -0.5140278  0.1142109  -4.5006882 6.773380e-06
# HED          0.8302070  0.2662557   3.1180821 1.820321e-03
# HUne        -1.7203157  0.1704053 -10.0954338 5.787460e-24
# HWe          0.1701797  0.3205626   0.5308781 5.955032e-01

##################################################### Chicago ####################################################

mydata <- read_csv("/ranking/Cities-CSV/Chicago.csv",col_types = cols(Name_x=col_character(),URL=col_character(),ZIP=col_integer(),Count=col_integer(),AverageExposure=col_double(),Stars=col_double(),Latitude=col_double(),Longitude=col_double(),Address=col_character(),PlaceID=col_character(),White=col_integer(),ofWhite=col_double(),WN=col_integer(),Black=col_integer(),ofBlack=col_double(),BN=col_integer(),AmericanIndaian=col_integer(),ofAI=col_double(),AIN=col_integer(),Asian=col_integer(),ofAisan=col_double(),AN=col_integer(),NativeHawiian=col_integer(),ofNativeHawiian=col_double(),NHN=col_integer(),Edu=col_integer(),ofEDU=col_double(),HED=col_integer(),Unemployment=col_double(),HUne=col_integer(),Wealth=col_integer(),HWe=col_integer(),Attraction=col_integer(),Hotspot=col_integer()))
mydata$DWN <- ifelse(mydata$ofWhite>50, 1, 0)

mylogit <- lm(AverageExposure ~ Hotspot, data=mydata)
summary(mylogit)

# Residuals:
#   Min       1Q   Median       3Q      Max 
# -0.13343 -0.06106 -0.00080  0.03957  0.62712 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 0.100280   0.006290  15.942  < 2e-16 ***
#   Hotspot     0.037514   0.009784   3.834 0.000151 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.08739 on 327 degrees of freedom
# Multiple R-squared:  0.04303,	Adjusted R-squared:  0.0401 
# F-statistic:  14.7 on 1 and 327 DF,  p-value: 0.000151

mylogit <- miceadds::glm.cluster(Hotspot ~ WN + BN + AIN+ AN+HED + HUne + HWe , data=mydata,cluster=mydata$ZIP,family="binomial")
summary(mylogit)

# Estimate Std. Error     z value     Pr(>|z|)
# (Intercept) -13.9804185  1.0895762 -12.8310603 1.098505e-37
# WN          -16.4854382  1.7723381  -9.3015200 1.384521e-20
# BN          -16.2875220  1.3829372 -11.7774849 5.099194e-32
# AIN          -0.1425133  0.6290010  -0.2265709 8.207574e-01
# AN           -0.4571590  0.6008995  -0.7607910 4.467819e-01
# HED          14.9570236  1.1572260  12.9248945 3.257432e-38
# HUne         -0.6000764  0.7247272  -0.8280032 4.076687e-01
# HWe          15.7064526  1.8376588   8.5469909 1.263392e-17

##################################################### Corpus Christi ####################################################

mydata <- read_csv("/ranking/Cities-CSV/Corpus-Christi.csv",col_types = cols(Restaurant=col_character(),Latitude=col_double(),Longitude=col_double(),Address_x=col_character(),PlaceID=col_character(),URL=col_character(),ZIP=col_integer(),AverageExposure=col_double(),Stars=col_double(),Count=col_integer(),White_x=col_integer(),ofWhite=col_double(),WN=col_integer(),Black=col_integer(),ofBlack=col_double(),BN=col_integer(),AmericanIndaian=col_integer(),ofAI=col_double(),AIN=col_integer(),Asian=col_integer(),ofAisan=col_double(),AN=col_integer(),NativeHawiian=col_integer(),ofNativeHawiian=col_double(),NHN=col_integer(),Edu=col_integer(),ofEDU=col_double(),HED=col_integer(),Unemployment=col_double(),HUne=col_integer(),Wealth=col_integer(),HWe=col_integer(),OBJECTID=col_integer(),Attraction=col_integer(),Hotspot=col_integer()))

mydata$DWN <- ifelse(mydata$ofWhite>50, 1, 0)

mylogit <- lm(AverageExposure ~ Hotspot, data=mydata)
summary(mylogit)

# Residuals:
#   Min       1Q   Median       3Q      Max 
# -0.14390 -0.03477 -0.00542  0.02193  0.57896 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 0.129373   0.006002  21.556   <2e-16 ***
#   Hotspot     0.027302   0.012070   2.262   0.0245 *  
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.08572 on 269 degrees of freedom
# Multiple R-squared:  0.01866,	Adjusted R-squared:  0.01502 
# F-statistic: 5.116 on 1 and 269 DF,  p-value: 0.0245

mylogit <- miceadds::glm.cluster(Hotspot ~ WN + BN + AIN+ AN+HED + HUne + HWe , data=mydata,cluster=mydata$ZIP,family="binomial")
summary(mylogit)

# Estimate Std. Error     z value     Pr(>|z|)
# (Intercept)  -1.4157738  0.9200410  -1.5388159 1.238492e-01
# WN            0.8543047  1.1510435   0.7422002 4.579661e-01
# BN            0.7302514  0.9553966   0.7643437 4.446624e-01
# AIN         -15.0374595  1.4201249 -10.5888288 3.357665e-26
# AN          -13.8899068  1.4128398  -9.8311975 8.263028e-23
# HED          13.6685960  1.4637672   9.3379574 9.821043e-21
# HUne         -0.2417243  1.0056313  -0.2403708 8.100428e-01
# HWe          -0.5041046  0.9661373  -0.5217733 6.018282e-01


##################################################### Los Angeles ####################################################
mydata <- read_csv("/ranking/Cities-CSV/LA.csv",col_types = cols(Restaurant=col_character(),Latitude=col_double(),Longitude=col_double(),Address=col_character(),PlaceID=col_character(),URL=col_character(),ZIP=col_integer(),AverageExposure=col_double(),Stars=col_double(),Count=col_integer(),White=col_integer(),ofWhite=col_double(),WN=col_integer(),Black=col_integer(),ofBlack=col_double(),BN=col_integer(),AmericanIndaian=col_integer(),ofAI=col_double(),AIN=col_integer(),Asian=col_integer(),ofAisan=col_double(),AN=col_integer(),NativeHawiian=col_integer(),ofNativeHawiian=col_double(),NHN=col_integer(),Edu=col_integer(),ofEDU=col_double(),HED=col_integer(),Unemployment=col_double(),HUne=col_integer(),Wealth=col_integer(),HWe=col_integer(),Attraction=col_integer(),Hotspot=col_integer()))

mydata$DWN <- ifelse(mydata$ofWhite>50, 1, 0)

mylogit1 <- lm(AverageExposure ~ Hotspot, data=mydata)
summary(mylogit1)

# Residuals:
#   Min       1Q   Median       3Q      Max 
# -0.12213 -0.05361 -0.00406  0.03656  0.73830 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 0.098483   0.005483  17.960  < 2e-16 ***
#   Hotspot     0.027894   0.010661   2.616  0.00928 ** 
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.08722 on 342 degrees of freedom
# Multiple R-squared:  0.01962,	Adjusted R-squared:  0.01676 
# F-statistic: 6.845 on 1 and 342 DF,  p-value: 0.009282



mylogit <- miceadds::glm.cluster(Hotspot ~ WN + BN + AIN+ AN+HED + HUne + HWe , data=mydata,cluster=mydata$ZIP,family="binomial")
summary(mylogit)

# Estimate Std. Error      z value      Pr(>|z|)
# (Intercept) -16.51408590  1.5419727 -10.70971345  9.164504e-27
# WN           -0.38780272  0.8518166  -0.45526550  6.489182e-01
# BN            0.08876408  0.9397232   0.09445769  9.247456e-01
# AIN           1.18176158  0.8950724   1.32029713  1.867358e-01
# AN            0.50543195  0.6119788   0.82589778  4.088621e-01
# HED          16.62757455  0.7698114  21.59954256 1.814028e-103
# HUne         -2.08719486  0.7770723  -2.68597254  7.231903e-03
# HWe           0.68036238  1.1130853   0.61124009  5.410406e-01



##################################################### New Orleans ####################################################

mydata <- read_csv("/ranking/Cities-CSV/NOLA.csv",col_types = cols(Restaurant=col_character(),Latitude=col_double(),Longitude=col_double(),Address=col_character(),PlaceID=col_character(),URL=col_character(),ZIP=col_integer(),AverageExposure=col_double(),Stars=col_double(),Count=col_integer(),White=col_integer(),ofWhite=col_double(),WN=col_integer(),Black=col_integer(),ofBlack=col_double(),BN=col_integer(),AmericanIndaian=col_integer(),ofAI=col_double(),AIN=col_integer(),Asian=col_integer(),ofAisan=col_double(),AN=col_integer(),NativeHawiian=col_integer(),ofNativeHawiian=col_double(),NHN=col_integer(),Edu=col_integer(),ofEDU=col_double(),HED=col_integer(),Unemployment=col_double(),HUne=col_integer(),Wealth=col_integer(),HWe=col_integer(),Attraction=col_integer(),Hotspot=col_integer()))

mydata$DWN <- ifelse(mydata$ofWhite>50, 1, 0)

mylogit <- lm(AverageExposure ~ Hotspot, data=mydata)
summary(mylogit)

# Residuals:
#   Min       1Q   Median       3Q      Max 
# -0.15199 -0.03631 -0.00074  0.02504  0.81482 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 0.116588   0.007929  14.703  < 2e-16 ***
#   Hotspot     0.039625   0.010541   3.759 0.000208 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.08758 on 279 degrees of freedom
# Multiple R-squared:  0.0482,	Adjusted R-squared:  0.04479 
# F-statistic: 14.13 on 1 and 279 DF,  p-value: 0.0002078


mylogit <- miceadds::glm.cluster(Hotspot ~ WN + BN + AIN+ AN+HED + HUne + HWe , data=mydata,cluster=mydata$ZIP,family="binomial")
summary(mylogit)

# (Intercept) -14.3990568  1.7537557 -8.2104121 2.204305e-16
# WN            7.2615343  1.4185352  5.1190371 3.070996e-07
# BN            8.3791206  1.2968664  6.4610517 1.039778e-10
# AIN          -4.2177082  0.7063431 -5.9711891 2.355305e-09
# AN            0.7546058  0.7742949  0.9745715 3.297728e-01
# HED           4.0671027  0.4368769  9.3094941 1.284427e-20
# HUne          3.2960914  0.7554267  4.3632178 1.281633e-05
# HWe           1.2170896  0.8253045  1.4747159 1.402889e-01

##################################################### New York City ####################################################

mydata <- read_csv("/ranking/Cities-CSV/NYC.csv",col_types = cols(Restaurant=col_character(),Latitude=col_double(),Longitude=col_double(),Address=col_character(),PlaceID=col_character(),URL=col_character(),ZIP=col_integer(),AverageExposure=col_double(),Stars=col_double(),Count=col_integer(),White=col_integer(),ofWhite=col_double(),WN=col_integer(),Black=col_integer(),ofBlack=col_double(),BN=col_integer(),AmericanIndaian=col_integer(),ofAI=col_double(),AIN=col_integer(),Asian=col_integer(),ofAisan=col_double(),AN=col_integer(),NativeHawiian=col_integer(),ofNativeHawiian=col_double(),NHN=col_integer(),Edu=col_integer(),ofEDU=col_double(),HED=col_integer(),Unemployment=col_double(),HUne=col_integer(),Wealth=col_integer(),HWe=col_integer(),Attraction=col_integer(),Hotspot=col_integer()))

mydata$DWN <- ifelse(mydata$ofWhite>50, 1, 0)


mylogit <- lm(AverageExposure ~ Hotspot, data=mydata)
summary(mylogit)

# Residuals:
#   Min       1Q   Median       3Q      Max 
# -0.13334 -0.06080  0.00547  0.03582  0.89278 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 0.107220   0.006732   15.93  < 2e-16 ***
#   Hotspot     0.031182   0.009836    3.17  0.00166 ** 
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.09156 on 346 degrees of freedom
# Multiple R-squared:  0.02823,	Adjusted R-squared:  0.02542 
# F-statistic: 10.05 on 1 and 346 DF,  p-value: 0.001659


mylogit <- miceadds::glm.cluster(Hotspot ~ WN + BN + AIN+ AN+HED + HUne + HWe, data=mydata,cluster=mydata$ZIP,family="binomial")
summary(mylogit)


# Estimate Std. Error    z value   Pr(>|z|)
# (Intercept) -1.136603  1.2431816 -0.9142693 0.36057536
# WN          -2.077696  0.8794576 -2.3624747 0.01815338
# BN          -2.046894  0.9312886 -2.1979158 0.02795511
# AIN          0.597519  0.6521386  0.9162454 0.35953819
# AN           1.218427  0.5663662  2.1513051 0.03145213
# HUne         0.186691  0.5851900  0.3190262 0.74970664
# HWe          2.197434  0.9355883  2.3487185 0.01883814

##################################################### San Francisco  ####################################################

mydata <- read_csv("/ranking/Cities-CSV/SAFO.csv",col_types = cols(Name_x=col_character(),URL=col_character(),ZIP=col_integer(),AverageExposure=col_double(),Stars=col_double(),Count=col_integer(),Latitude=col_double(),Longitude=col_double(),Address=col_character(),PlaceID=col_character(),White=col_integer(),ofWhite=col_double(),WN=col_integer(),Black=col_integer(),ofBlack=col_double(),BN=col_integer(),AmericanIndaian=col_integer(),ofAI=col_double(),AIN=col_integer(),Asian=col_integer(),ofAisan=col_double(),AN=col_integer(),NativeHawiian=col_integer(),ofNativeHawiian=col_double(),NHN=col_integer(),Edu=col_integer(),ofEDU=col_double(),HED=col_integer(),Unemployment=col_double(),HUne=col_integer(),Wealth=col_integer(),HWe=col_integer(),Attractions=col_integer(),Hotspot=col_integer()))

mydata$DWN <- ifelse(mydata$ofWhite>50, 1, 0)

mylogit <- lm(AverageExposure ~ Hotspot, data=mydata)
summary(mylogit)

# Residuals:
#   Min       1Q   Median       3Q      Max 
# -0.11544 -0.06803 -0.00434  0.04119  0.54678 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 0.098211   0.006565  14.960   <2e-16 ***
#   Hotspot     0.021452   0.009219   2.327   0.0205 *  
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.08659 on 351 degrees of freedom
# Multiple R-squared:  0.01519,	Adjusted R-squared:  0.01239 
# F-statistic: 5.415 on 1 and 351 DF,  p-value: 0.02053

mylogit <- miceadds::glm.cluster(Hotspot ~ WN + BN + AIN+ AN+HED + HUne + HWe, data=mydata,cluster=mydata$ZIP,family="binomial")
summary(mylogit)

# Estimate Std. Error     z value     Pr(>|z|)
# (Intercept) -13.39500238  1.7138063 -7.81593740 5.455549e-15
# WN           -1.45794574  0.9990998 -1.45925940 1.444937e-01
# BN            0.02787245  0.6135083  0.04543125 9.637636e-01
# AIN          -0.78656612  0.7642527 -1.02919634 3.033874e-01
# AN           -1.81249004  1.4959502 -1.21159783 2.256664e-01
# HED          13.21478191  1.2650382 10.44615269 1.525903e-25
# HUne          0.82687966  0.9189942  0.89976587 3.682449e-01
# HWe           1.49149545  0.7589137  1.96530300 4.937918e-02


##################################################### San Jose  ####################################################

mydata <- read_csv("/ranking/Cities-CSV/SanJose.csv",col_types = cols(Restaurant=col_character(),Latitude=col_double(),Longitude=col_double(),Address=col_character(),PlaceID=col_character(),URL=col_character(),Stars=col_double(),ZIP=col_integer(),AverageExposure=col_double(),Count=col_integer(),White=col_integer(),ofWhite=col_double(),WN=col_integer(),Black=col_integer(),ofBlack=col_double(),BN=col_integer(),AmericanIndaian=col_integer(),ofAI=col_double(),AIN=col_integer(),Asian=col_integer(),ofAisan=col_double(),AN=col_integer(),NativeHawiian=col_integer(),ofNativeHawiian=col_double(),NHN=col_integer(),Edu=col_integer(),ofEDU=col_double(),HED=col_integer(),Unemployment=col_double(),HUne=col_integer(),Wealth=col_integer(),HWe=col_integer(),Attractions=col_integer(),Hotspot=col_integer()))
mydata$DWN <- ifelse(mydata$ofWhite>50, 1, 0)

mylogit1 <- lm(AverageExposure ~ Hotspot, data=mydata)
summary(mylogit1)

# Residuals:
#   Min       1Q   Median       3Q      Max 
# -0.12559 -0.06003  0.00376  0.03847  0.82456 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 0.102472   0.006321  16.210  < 2e-16 ***
#   Hotspot     0.027329   0.009833   2.779  0.00575 ** 
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.09006 on 344 degrees of freedom
# Multiple R-squared:  0.02196,	Adjusted R-squared:  0.01912 
# F-statistic: 7.725 on 1 and 344 DF,  p-value: 0.005746

mylogit <- miceadds::glm.cluster(Hotspot ~ WN + BN + AIN+ AN+HED + HUne + HWe , data=mydata,cluster=mydata$ZIP,family="binomial")
summary(mylogit)

# Estimate Std. Error    z value  Pr(>|z|)
# (Intercept)  0.1271308  1.0651283  0.1193573 0.9049923
# WN           1.0682072  0.8157184  1.3095294 0.1903551
# BN           0.4425505  0.5833269  0.7586664 0.4480521
# AIN         -0.1268693  0.6897029 -0.1839478 0.8540544
# AN           0.2652148  0.8387552  0.3162005 0.7518503
# HED         -1.1565928  1.2057554 -0.9592267 0.3374446
# HUne        -0.2241859  0.6696966 -0.3347574 0.7378081
# HWe         -0.3891490  0.5286457 -0.7361245 0.4616549

##################################################### Seattle  ####################################################

mydata <- read_csv("/ranking/Cities-CSV/Seattle.csv",col_types = cols(Restaurant=col_character(),Latitude=col_double(),Longitude=col_double(),Address_x=col_character(),PlaceID=col_character(),URL=col_character(),Stars=col_double(),ZIP=col_integer(),AverageExposure=col_double(),Count=col_integer(),White=col_integer(),ofWhite=col_double(),WN=col_integer(),Black=col_integer(),ofBlack=col_double(),BN=col_integer(),AmericanIndaian=col_integer(),ofAI=col_double(),AIN=col_integer(),Asian=col_integer(),ofAisan=col_double(),AN=col_integer(),NativeHawiian=col_integer(),ofNativeHawiian=col_double(),NHN=col_integer(),Edu=col_integer(),ofEDU=col_double(),HED=col_integer(),Unemployment=col_double(),HUne=col_integer(),Wealth=col_integer(),HWe=col_integer(),Attractions=col_integer(),Hotspot=col_integer()))

mydata$DWN <- ifelse(mydata$ofWhite>50, 1, 0)

mylogit <- lm(AverageExposure ~ Hotspot, data=mydata)
summary(mylogit)

# Call:
#   lm(formula = AverageExposure ~ Hotspot, data = mydata)
# 
# Residuals:
#   Min       1Q   Median       3Q      Max 
# -0.13639 -0.05078  0.00434  0.02866  0.81019 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 0.117565   0.007638  15.393   <2e-16 ***
#   Hotspot     0.023038   0.010260   2.245   0.0255 *  
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 0.08907 on 303 degrees of freedom
# Multiple R-squared:  0.01637,	Adjusted R-squared:  0.01312 
# F-statistic: 5.042 on 1 and 303 DF,  p-value: 0.02547

mylogit <- miceadds::glm.cluster(Hotspot ~ WN + BN + AIN+ AN+HED + HUne + HWe , data=mydata,cluster=mydata$ZIP,family="binomial")
summary(mylogit)

# Estimate Std. Error     z value     Pr(>|z|)
# (Intercept)  3.87170745  4.3516176  0.88971683 0.3736179559
# WN          -3.14546327  1.8720341 -1.68023827 0.0929109668
# BN          -0.12299578  1.4806922 -0.08306641 0.9337987365
# AIN         -2.62922910  1.0924987 -2.40661984 0.0161009205
# AN          -0.70987275  1.6126985 -0.44017698 0.6598089338
# HED         -0.44189183  1.7054233 -0.25910976 0.7955505533
# HUne         0.05915168  1.3799103  0.04286632 0.9658080936
# HWe         -2.06656499  0.5709227 -3.61969320 0.0002949525