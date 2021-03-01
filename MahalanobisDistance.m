%Mahalanobis Distance
cor = [0.3, 0.2 ; 0.2, 0.3];

A = [0.5, 0.5];
B = [0, 1];
C = [1.5,1.5]

MahalAB = (A-B) * cor^(-1) * (A-B)' % MahalAB = ans^1/2
MahalAC = (A-C) * cor^(-1) * (A-C)' % MahalAC = ans^1/2
