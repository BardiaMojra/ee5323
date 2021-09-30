%% Voltera Predator-Prey System
%% Document Information:
% * Author: Bardia Mojra 
% * Date: 09/07/2021 
% * Title: Voltera
% * Term: Fall 2021
% * Class: EE 5323 Nonlinear Systems
% * Dr. Lewis

function xdot = Voltera(t,x)    
  xdot = [-x(1)+x(1)*x(2); x(2)-x(1)*x(2)];
end
