%x = [6,-3,-2,7 ; -4,5,6,-3]; %[all x, all y]

x = [-1,-1,0,2,0 ; -2,0,0,1,1];
%(a) The covariance matrix;
%Each row mean
M = mean(x,2);
disp('µ = ')
disp(M)

%After sub
xNew = x - M;
disp('X - µ = ')
disp(xNew)
xTran = xNew';

n = length(x) - 1;

%covariance matrix
xCov = (1/n) * xNew * xTran;

disp('1/n * X * Xt = ');
disp(1/n)
disp('*')
disp(xNew)
disp('*')
disp(xTran)
disp('=')
disp(xCov);
disp('----------------')
%(b) Eigen values;
%https://matrixcalc.org/en/vectors.html#eigenvectors%28%7B%7B1%2e5,1%7D,%7B1,1%2e5%7D%7D%29
%input xCov matrix
%[a b]
%[c d]

%det [ val - x , val     ] => find two x
%    [  val    , val - x ] x1,x2 = [e1,e2]

[V,D] = eig(xCov);

%eigen values 
D = diag(D);
disp('det = ');
disp(D)

disp('λ1,λ2');
disp('----------------')

%(c) Eigen vectors; V = d1(up) value , D = d2(down) value

%eigen vectors
maxE = V(:,find(D == max(D)));

disp('eigen vectors = ');
disp(maxE)

%(d) Apply PCA;
final = maxE' * x;
disp('Apply PCA = ');
disp(maxE');
disp('*')
disp(x)
disp('=')
disp(final)
