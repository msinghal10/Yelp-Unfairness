library(aod)
library(ggplot2)
library(readr)
# install.packages("dplyr")

library(dplyr)

# install.packages("quantreg")

library(quantreg)

mydata1 <- read.csv("/recommendation/Combined-Dataset-with-numberoffriends-reviews-andifreco.csv")

mylogit <- glm(Reco ~ Review, data=mydata1, family="binomial")
summary(mylogit)
exp(coef(mylogit))
nobs(mylogit)


# Coefficients:
#   Estimate Std. Error z value Pr(>|z|)    
# (Intercept) 0.4121643  0.0036524   112.8   <2e-16 ***
#   Review      0.0533987  0.0002556   208.9   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# (Dispersion parameter for binomial family taken to be 1)
# 
# Null deviance: 891168  on 886404  degrees of freedom
# Residual deviance: 719216  on 886403  degrees of freedom
# AIC: 719220
# 
# Number of Fisher Scoring iterations: 11
# 
# > exp(coef(mylogit))
# (Intercept)      Review 
# 1.510083    1.054850 
# > nobs(mylogit)
# [1] 886405


mylogit <- glm(Reco ~ Friend, data=mydata1, family="binomial")
summary(mylogit)
exp(coef(mylogit))
nobs(mylogit)


# Coefficients:
#   Estimate Std. Error z value Pr(>|z|)    
# (Intercept) 9.795e-01  3.015e-03   324.9   <2e-16 ***
#   Friend      7.862e-03  4.774e-05   164.7   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# (Dispersion parameter for binomial family taken to be 1)
# 
# Null deviance: 891168  on 886404  degrees of freedom
# Residual deviance: 827525  on 886403  degrees of freedom
# AIC: 827529
# 
# Number of Fisher Scoring iterations: 8
# 
# > exp(coef(mylogit))
# (Intercept)      Friend 
# 2.663138    1.007893 
# > nobs(mylogit)
# [1] 886405

mydata4 <- read.csv("/recommendation/Combined-Dataset-with-numberoffriends-reviews-andifreco.csv")

mydata4$qr_friend <- ntile(mydata4$Friend, 4)

mydata4$qr_review <- ntile(mydata4$Review, 4)


formula1= Reco ~ Friend 

mylogit7 <- glm(formula=formula1, subset(mydata4,qr_friend==1), family="binomial")
summary(mylogit7)
exp(coef(mylogit7))
nobs(mylogit7)

# Coefficients:
#   Estimate Std. Error z value Pr(>|z|)
# (Intercept)   -21.57      82.35  -0.262    0.793
# Friend         24.34      82.35   0.296    0.768
# 
# (Dispersion parameter for binomial family taken to be 1)
# 
# Null deviance: 299319  on 221601  degrees of freedom
# Residual deviance:  42742  on 221600  degrees of freedom
# AIC: 42746
# 
# Number of Fisher Scoring iterations: 20
# 
# > exp(coef(mylogit7))
# (Intercept)       Friend 
# 4.305023e-10 3.719566e+10 
# > nobs(mylogit7)
# [1] 221602



mylogit7 <- glm(formula=formula1, subset(mydata4,qr_friend==2), family="binomial")
summary(mylogit7)
exp(coef(mylogit7))
nobs(mylogit7)

# Coefficients:
#   Estimate Std. Error z value Pr(>|z|)    
# (Intercept)  4.153385   0.018559   223.8   <2e-16 ***
#   Friend      -0.372357   0.003618  -102.9   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# (Dispersion parameter for binomial family taken to be 1)
# 
# Null deviance: 88558  on 221600  degrees of freedom
# Residual deviance: 78465  on 221599  degrees of freedom
# AIC: 78469
# 
# Number of Fisher Scoring iterations: 6
# 
# > exp(coef(mylogit7))
# (Intercept)      Friend 
# 63.6491141   0.6891081 
# > nobs(mylogit7)
# [1] 221601








mylogit7 <- glm(formula=formula1, subset(mydata4,qr_friend==3), family="binomial")
summary(mylogit7)
exp(coef(mylogit7))
nobs(mylogit7)

# Coefficients:
#   Estimate Std. Error z value Pr(>|z|)    
# (Intercept) 1.9660923  0.0126900  154.93   <2e-16 ***
#   Friend      0.0028322  0.0002466   11.49   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# (Dispersion parameter for binomial family taken to be 1)
# 
# Null deviance: 153496  on 221600  degrees of freedom
# Residual deviance: 153363  on 221599  degrees of freedom
# AIC: 153367
# 
# Number of Fisher Scoring iterations: 4
# 
# > exp(coef(mylogit7))
# (Intercept)      Friend 
# 7.142710    1.002836 
# > nobs(mylogit7)
# [1] 221601









mylogit7 <- glm(formula=formula1, subset(mydata4,qr_friend==4), family="binomial")
summary(mylogit7)
exp(coef(mylogit7))
nobs(mylogit7)

# Coefficients:
#   Estimate Std. Error z value Pr(>|z|)    
# (Intercept) 2.387e+00  1.638e-02  145.77   <2e-16 ***
#   Friend      1.563e-03  4.846e-05   32.24   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# (Dispersion parameter for binomial family taken to be 1)
# 
# Null deviance: 90845  on 221600  degrees of freedom
# Residual deviance: 88911  on 221599  degrees of freedom
# AIC: 88915
# 
# Number of Fisher Scoring iterations: 7
# 
# > exp(coef(mylogit7))
# (Intercept)      Friend 
# 10.885331    1.001564 
# > nobs(mylogit7)
# [1] 221601





formula2= Reco ~ Review 

mylogit7 <- glm(formula=formula2, subset(mydata4,qr_review==1), family="binomial")
summary(mylogit7)
exp(coef(mylogit7))
nobs(mylogit7)

# Coefficients:
#   Estimate Std. Error z value Pr(>|z|)    
# (Intercept) -1.36135    0.01067  -127.6   <2e-16 ***
#   Review       0.64848    0.00562   115.4   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# (Dispersion parameter for binomial family taken to be 1)
# 
# Null deviance: 303926  on 221601  degrees of freedom
# Residual deviance: 289935  on 221600  degrees of freedom
# AIC: 289939
# 
# Number of Fisher Scoring iterations: 4
# 
# > exp(coef(mylogit7))
# (Intercept)      Review 
# 0.2563135   1.9126254 
# > nobs(mylogit7)
# [1] 221602


mylogit7 <- glm(formula=formula2, subset(mydata4,qr_review==2), family="binomial")
summary(mylogit7)
exp(coef(mylogit7))
nobs(mylogit7)

# 
# Coefficients:
#   Estimate Std. Error z value Pr(>|z|)    
# (Intercept) 0.345624   0.014938   23.14   <2e-16 ***
#   Review      0.152042   0.001978   76.86   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# (Dispersion parameter for binomial family taken to be 1)
# 
# Null deviance: 212807  on 221600  degrees of freedom
# Residual deviance: 206285  on 221599  degrees of freedom
# AIC: 206289
# 
# Number of Fisher Scoring iterations: 4
# 
# > exp(coef(mylogit7))
# (Intercept)      Review 
# 1.412872    1.164209 
# > nobs(mylogit7)
# [1] 221601



mylogit7 <- glm(formula=formula2, subset(mydata4,qr_review==3), family="binomial")
summary(mylogit7)
exp(coef(mylogit7))
nobs(mylogit7)

# Coefficients:
#   Estimate Std. Error z value Pr(>|z|)    
# (Intercept) 2.3990144  0.0249910   96.00   <2e-16 ***
#   Review      0.0197726  0.0007819   25.29   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# (Dispersion parameter for binomial family taken to be 1)
# 
# Null deviance: 84023  on 221600  degrees of freedom
# Residual deviance: 83333  on 221599  degrees of freedom
# AIC: 83337
# 
# Number of Fisher Scoring iterations: 6
# 
# > exp(coef(mylogit7))
# (Intercept)      Review 
# 11.012318    1.019969 
# > nobs(mylogit7)
# [1] 221601




mylogit7 <- glm(formula=formula2, subset(mydata4,qr_review==4), family="binomial")
summary(mylogit7)
exp(coef(mylogit7))
nobs(mylogit7)

# Call:
#   glm(formula = formula2, family = "binomial", data = subset(mydata4, 
#                                                              qr_review == 4))
# 
# Coefficients:
#   Estimate Std. Error z value Pr(>|z|)    
# (Intercept) 3.932e+00  2.782e-02  141.36   <2e-16 ***
#   Review      1.531e-03  9.718e-05   15.75   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# (Dispersion parameter for binomial family taken to be 1)
# 
# Null deviance: 30765  on 221600  degrees of freedom
# Residual deviance: 30343  on 221599  degrees of freedom
# AIC: 30347
# 
# Number of Fisher Scoring iterations: 8
# 
# > exp(coef(mylogit7))
# (Intercept)      Review 
# 51.027715    1.001532 
# > nobs(mylogit7)
# [1] 221601






