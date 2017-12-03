% MonteCarlo Pi
% MCPi_0.m
% M. Saum 8/31/2017
clear;

rand("seed",834);

NTrials = [10; 100; 1000; 10000; 100000; 1000000];
Ncases = numel(NTrials);
PiEst = zeros(Ncases,1);

for i =1:Ncases 
  Rcount = 0;
  for j = 1:NTrials(i) 
    x = rand(1);
    y = rand(1);
    if ( x^2 + y^2 <= 1) 
      Rcount = Rcount + 1;
    endif
  end
  PiEst(i) = 4*Rcount/NTrials(i);
end

dlmwrite("MCPi_0_m.txt",[NTrials,PiEst]);

hf = figure();
plot(NTrials',PiEst');
print(hf,"MCPi_0_m.pdf");
