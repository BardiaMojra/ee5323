%% Lorenz Attractor Chaotic System
%% Document Information:
% * Author: Bardia Mojra 
% * Date: 09/07/2021 
% * Title: Lorenz
% * Term: Fall 2021
% * Class: EE 5323 Nonlinear Systems
% * Dr. Lewis

function xdot = Lorenz(t,x)
    sigma= 10; r=28; b=8/3;
    xdot = [-sigma*(x(1)-x(2)); r*x(1)-x(2)-x(1)*x(3); -b*x(3)+x(1)*x(2)]; 
end
