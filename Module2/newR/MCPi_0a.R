# MonteCarlo Pi 
# MCPi_0.R
# M. Saum 8/31/2017
rm(list=ls())

set.seed(843)

NTrials <- c(10, 100, 1000, 10000, 100000, 1000000)
Ncases <- length(NTrials)
PiEst <- numeric(Ncases)

for( i in 1:Ncases) {
  x <- runif(NTrials[i])
  y <- runif(NTrials[i])
  Rcount <- sum(x^2 + y^2 <= 1)
  PiEst[i] <- 4*Rcount/NTrials[i]
}

sink("MCPi_0_R.txt")
print(cbind(NTrials,PiEst))
sink()

pdf("MCPi_0_R.pdf")
plot(NTrials,PiEst)
dev.off()
