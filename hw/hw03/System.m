%% HW03 - Q02 - System
% @author: Bardia Mojra
% @date: 09/28/2021
% @title HW03 - Q02 - System
% @class ee5323 - Nonlinear Systems
% @professor - Dr. Frank Lewis

function xdot = System(t,x)    
  xdot = [-x(1)*x(2)+x(2)^2 -x(2), x(1)^2 +x(2)*x(1) +x(1)];
end
