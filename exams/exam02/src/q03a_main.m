%% exam02 - q03 - lyapunov equation
% @author Bardia Mojra
% @date 11/13/2021
% @title  exam02 - lyapunov equation
% @class ee5323 - Nonlinear Systems
% @professor Dr. Frank Lewis

clc
clear
close all
%warning('off','all')
%warning



A = [0 1; 0 -6];

Q1 = [1 0; 0 1];
Q2 = [0 1; 1 0];
Q3 = [1 0; 0 0];
Q4 = [0 1; 0 0];
Q5 = [0 0; 1 0];
Q6 = [0 0; 0 1];

Q7 = [0 1; 1 1];
Q8 = [1 0; 1 1];
Q9 = [1 1; 0 1];
Q10 = [1 1; 1 0];

Q11 = [0 0; 1 1];
Q12 = [1 1; 0 0];
Q13 = [1 0; 0 1];
Q14 = [0 1; 1 0];

Q1
P = lyap(A,Q1)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

Q2
P = lyap(A,Q2)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

Q3
lyap(A,Q3)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

Q4
P = lyap(A,Q4)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

disp(Q5)
P = lyap(A,Q5)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

disp(Q6)
P = lyap(A,Q6)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

disp(Q7)
P = lyap(A,Q7)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

disp(Q8)
P = lyap(A,Q8)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

disp(Q9)
P = lyap(A,Q9)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

disp(Q10)
P = lyap(A,Q10)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

disp(Q11)
P = lyap(A,Q11)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

disp(Q12)
P = lyap(A,Q12)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

disp(Q13)
P = lyap(A,Q13)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)

disp(Q14)
P = lyap(A,Q14)
m11 = P(1,1)
m22 = P(1,1)*P(2,2) - P(1,2)*P(2,1)
