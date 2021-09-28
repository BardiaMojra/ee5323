%% Van der Pol oscillator:
% * Author: Bardia Mojra 
% * Date: 09/07/2021 
% * Title: Van der Pol - Part B
% * Class: EE 5323 - Nonlinear Systems
% * Professor: Dr. Frank Lewis
% * Fall 2021

function xdot = VanDerPolB(t,x)
    alpha= 0.95;
    xdot = [x(2); -alpha*((x(1)^2)-1)*x(2) - x(1)]; 
end
