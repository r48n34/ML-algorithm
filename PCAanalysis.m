x = [-1,-1,0,2,0 ; -2,0,0,1,1];

%(a) The covariance matrix;
%Each row mean
M = mean(x,2);

%After sub
xNew = x - M;
xTran = xNew';

n = length(x) - 1;

%covariance matrix
xCov = (1/n) * xNew * xTran;

%(b) Eigen values;
%https://matrixcalc.org/en/vectors.html#eigenvectors%28%7B%7B1%2e5,1%7D,%7B1,1%2e5%7D%7D%29
%input xCov matrix

%det [ val - x , val     ] => find two x
%    [  val    , val - x ] x1,x2 = [e1,e2]

[V,D] = eig(xCov);
%eigen values
D = diag(D);

%(c) Eigen vectors;

%eigen vectors
maxE = V(:,find(D == max(D)));


%(d) Apply PCA;
final = maxE' * x;