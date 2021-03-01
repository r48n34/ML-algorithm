% Manhattan distance and single linkage

% x,y approache single
%x = [1,1; 1,0; 0,2; 1.5,3.5; 3,5]
%y = pdist(x,"cityblock");
%z = linkage(y,"single");
%dendrogram(z);

% x only approache single
%x = [3,7,10,17,18,20];
%y = pdist(x',"cityblock");
%z = linkage(y,"single");
%dendrogram(z);

% x only approache average
x = [16.9, 38.5, 39.5, 80.8, 82, 34.6, 116.1]
y = pdist(x',"cityblock");
Z0 = squareform(y);
z = linkage(y,"average");
dendrogram(z);
