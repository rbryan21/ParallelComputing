% MonteCarlo Pi
% MCPi_0.m
% M. Saum 8/31/2017
clear;

rand("seed",843);

NTrials = [10; 100; 1000; 10000; 100000; 1000000];
Ncases = numel(NTrials);
PiEst = zeros(Ncases,1);

for i =1:Ncases 
  x = rand(NTrials(i), 1);
  y = rand(NTrials(i), 1);
  Rcount = sum(x.^2 + y.^2 <= 1); 
  PiEst(i) = 4*Rcount/NTrials(i);
end

dlmwrite("MCPi_0_m.txt",[NTrials,PiEst]);

hf = figure();
plot(NTrials',PiEst');
print(hf,"MCPi_0_m.pdf");
