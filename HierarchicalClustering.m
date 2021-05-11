% Manhattan distance and single linkage
% linkage method: "single" ~ min || "average" || "complete" ~ max

% x,y approache single
%x = [1,1; 1,0; 0,2; 1.5,3.5; 3,5]
%y = pdist(x,"cityblock");
%z = linkage(y,"single");
%dendrogram(z);

%if only distance matrix is given
%read type from up to down, left to right
%y = [0.12,0.51,0.84,0.28,0.34,0.25,0.16,0.77,0.61,0.14,0.70,0.93,0.45,0.20,0.67]

% x only approache single
x = [2,4,7,8,12,14];
y = pdist(x',"cityblock");
Z0 = squareform(y);
z = linkage(y,"complete");
dendrogram(z);

% x only approache average
%x = [16.9, 38.5, 39.5, 80.8, 82, 34.6, 116.1]
%y = pdist(x',"cityblock");
%Z0 = squareform(y);
%z = linkage(y,"average");
%dendrogram(z);
