%% Part 1 Answer
%% Document Information:
% * Author: Bardia Mojra 
% * Date: 10/28/2021 
% * Title: HW 05 - Part 4 System
% * Term: Fall 2021
% * Class: EE 5323 - Nonlinear Systems 
% * Dr. Lewis

function xdot = q04_sys(t,x)
    xdot = [x(2) + x(1)*(x(1)^2-2); -x(1)]; 
end
