%% Part 2 Answer
%% Document Information:
% * Author: Bardia Mojra 
% * Date: 09/14/2021 
% * Title: HW 02 - Part 2 Answer
% * Term: Fall 2021
% * Class: EE 5323 - Nonlinear Systems 
% * Dr. Lewis

function xdot = part3(t,x)
    a=2; c=2; d=2; f=2;
    b=3; e=3;
    xdot = [a*x(1)-b*x(1)*x(2)-c*x(1)^2; d*x(2)-e*x(1)*x(2)-f*x(2)^2]; 
end
