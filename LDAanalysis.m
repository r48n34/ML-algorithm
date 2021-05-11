x1 = [3,2; 2,3; 4,4; 3,1; 3,5; 3,3 ];
x2 = [9,9; 10,9; 8,7; 8,10; 9,6; 7,9];

%plot
scatter (x1 (:,1), x1(:,2),'ro');hold on;
scatter (x2 (:,1), x2(:,2),'b*');

% b)
%Class mean 1
mu1 = mean(x1)';
disp('class mean of class 1 = ')
disp(mu1)
%Class mean 2
mu2 = mean(x2)';
disp('class mean of class 2 = ')
disp(mu2)

%Covariance matrix of class 1
s1 = cov(x1);
disp('Covariance matrix of class 1 = ')
disp(s1)

%Covariance matrix of class 2
s2 = cov(x2);
disp('Covariance matrix of class 2 = ')
disp(s2)

disp('-----------------------------')

% c)
% Withn-class scatter matrix
sw = (s1 + s2);
disp('Withn-class scatter matrix = ')
disp(sw)

% Between-class scatter matrix
sb = (mu1-mu2) * (mu1-mu2)';
disp('Between-class scatter matrix = ')
disp(sb)

% d)
% Computing the LDA projection
invSw = inv(sw);
invSW_by_SB = invSw * sb;

% get projection vector
[V,D] = eig(invSW_by_SB);

% the projection vector
W = V(:,1);
disp('hte require projection vector = ')
disp(W)
