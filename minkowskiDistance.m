%x = [0,3 ;3,1; 5,1; 3,2; 2,4];
%x = [1,1 ;1,0; 0,2; 1.5,3.5; 3,5];
x = [0,2 ;2,0; 3,1; 5, 1];

%if x-axis only
%x = [16.9,0 ;38.5,0; 39.5,0; 80.8,0; 82,0; 34.6,0; 116.1,0];

% normal pt to pt dist, r = 2 , Z0 == Z2
D0 = pdist (x);
Z0 = squareform(D0);

% r = 1
D1 = pdist (x,'minkowski',1);
Z1 = squareform(D1);

% r = 2
D2 = pdist (x,'minkowski',2);
Z2 = squareform(D2);

% r = inf , close to the value, only need int part
% adjust the 100 if needed
D3 = pdist (x,'minkowski',100);
Z3 = squareform(D3);
