3%% Part 2 Answer
%% Document Information:
% * Author: Bardia Mojra 
% * Date: 11/25/2021 
% * Title: HW 07 - System 3
% * Term: Fall 2021
% * Class: EE 5323 - Nonlinear Systems 
% * Dr. Lewis

function xdot = q03_sys(t,x)
  u = (1/cos(x(2)))*x(1)^4 * cos(x(2))^2 ;
  xdot = [sin(x(2)); x(1)^4* cos(x(2)) + u]; 
end
