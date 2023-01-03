k1 = 10; 
k2 = 5;

c1(1) = 4;
c2(1) = 2;
c3(1) = 0;

dt= 0.001;
i = 0;

for t = 1:400
    c1(t+1) = c1(t) + (k2*c3(t)-k1*c1(t)*c2(t))*dt;
    c2(t+1) = c2(t) + (k2*c3(t)-k1*c1(t)*c2(t))*dt;
    c3(t+1) = c3(t) + (2*k1*c1(t)*c2(t)-2*k2*c3(t))*dt;
    i(t+1) = t* dt;
end

subplot(2,2,1);
plot(c1);
title('Reactant 1');
subplot(2,2,2);
plot(i,c2);
title('Reactant 2');
subplot (2,2,3);
plot(i,c3);
title('Product');