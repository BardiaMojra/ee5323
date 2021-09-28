%% Duffing's Equation Answer
%% Document Information:
% * Author: Bardia Mojra 
% * Date: 09/14/2021 
% * Title: HW 02 - Duffing's Equation Answer
% * Term: Fall 2021
% * Class: EE 5323 - Nonlinear Systems 
% * Dr. Lewis

function xdot = duffinga(t,x)
    alpha = -1;
    xdot = [x(2); -alpha*x(1) - x(1)^3]; 
end
