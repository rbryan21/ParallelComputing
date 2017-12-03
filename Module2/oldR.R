# MonteCarlo Pi 
# MCPi_0.R
# M. Saum 8/31/2017
rm(list=ls())

set.seed(834)

NTrials <- c(10,100,1000,10000,100000,1000000)
Ncases <- length(NTrials)
PiEst <- numeric(Ncases)

for( i in 1:Ncases) {
  Rcount <- 0
  for (j in 1:NTrials[i]) {
    x <- runif(1)
    y <- runif(1)
    if( x^2 + y^2 <= 1) {
      Rcount <- Rcount + 1
    }
  }
  PiEst[i] <- 4*Rcount/NTrials[i]
}

sink("MCPi_0_R.txt")
print(cbind(NTrials,PiEst))
sink()

pdf("MCPi_0_R.pdf")
plot(NTrials,PiEst)
dev.off()
