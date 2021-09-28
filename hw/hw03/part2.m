%% Part 2 Answer
%% Document Information:
% * Author: Bardia Mojra 
% * Date: 09/14/2021 
% * Title: HW 02 - Part 2 Answer
% * Term: Fall 2021
% * Class: EE 5323 - Nonlinear Systems 
% * Dr. Lewis

function xdot = part2(t,x)
    xdot = [x(2)*(1+x(1)-x(2)^2); x(1)*(1+x(2)-x(1)^2)]; 
end
