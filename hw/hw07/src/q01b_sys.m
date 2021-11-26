%% exam02 - q01b - lyapunov analysis 
%% Document Information:
% @author Bardia Mojra
% @date 11/13/2021
% @title exam02 - q01b - lyapunov analysis 
% @term fall 2021
% @class ee5323 - nonlinear systems 
% @professor Dr. Frank Lewis

function xdot = q01b_sys(t,x)
    xdot = [ x(2)*sin(x(1))-x(1);
            -x(1)*sin(x(1))]; 
end
