x = [3,7,10,17,18,20];
y = pdist(x',"cityblock");
z = linkage(y,"single");
dendrogram(z);
