%% Part 1 Answer
%% Document Information:
% * Author: Bardia Mojra 
% * Date: 11/25/2021 
% * Title: HW 07 - System 1
% * Term: Fall 2021
% * Class: EE 5323 - Nonlinear Systems 
% * Dr. Lewis

function xdot = q01_sys(t,x)
  u = -x(1)*x(2)^2;
  xdot = [  x(2)*sin(x(1)); 
            x(1)*x(2)^2]; 
end
