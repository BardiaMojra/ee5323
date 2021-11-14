%% Part 1 Answer
%% Document Information:
% @author Bardia Mojra
% @date 11/13/2021
% @title exam02 - q01 - lyapunov qnalysis 
% @term fall 2021
% @class ee5323 - nonlinear systems 
% @professor Dr. Frank Lewis

function xdot = q04_sys(t,x)
    xdot = [x(2) + x(1)*(x(1)^2-2); -x(1)]; 
end
