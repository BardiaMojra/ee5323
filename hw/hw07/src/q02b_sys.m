%% Part 2 Answer
%% Document Information:
% * Author: Bardia Mojra 
% * Date: 11/25/2021 
% * Title: HW 07 - System 2b
% * Term: Fall 2021
% * Class: EE 5323 - Nonlinear Systems 
% * Dr. Lewis

function xdot = q02b_sys(t,x)
  u1 = -x(1)^2 * x(2)^8;
  u2 = 0; 
  xdot = [x(1)*x(2)^2 + u1; (x(1)^3)*(x(2)^7) + u2]; 
end
