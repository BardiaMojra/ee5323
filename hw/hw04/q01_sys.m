%% Part 1 Answer
%% Document Information:
% * Author: Bardia Mojra 
% * Date: 10/14/2021 
% * Title: HW 04 - Part 1 System
% * Term: Fall 2021
% * Class: EE 5323 - Nonlinear Systems 
% * Dr. Lewis

function xdot = q01_sys(t,x)
    xdot = [x(2); -x(1)]; 
end
