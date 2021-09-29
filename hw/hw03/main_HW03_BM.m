%% HW 03 - Nonlinear Systems Simulation 
%% Document Information
% * Author: Bardia Mojra 
% * Date: 09/28/2021 
% * Title: HW 03 - Nonlinear Systems Simulation 
% * Term: Fall 2021
% * Class: EE 5323 - Nonlinear Systems 
% * Dr. Lewis

%% Voltera Predator-Prey System
% Consider the Voltera predator-prey system
% 
% * $$ \dot{x}_1 = - x_1 + x_1 x_2 $$
% * $$ \dot{x}_2 = x_2 -  x_1 x_2 $$
% 
% # Find the equilibrium points and their nature.
%
%% Answer
% State variable is given as: 
% 
% $$ ~\dot{x}_1 = - x_1 + x_1 x_2 $$
% $$ ~\dot{x}_2 = x_2 -  x_1 x_2 $$
%
% The Voltera predator-prey system has limit cycles therefore the system is
% at equilibrium when the population of both predator and prey remain
% constant; thus, derivative should be zero.
% To find the equilibrium, I set $\dot{x}_{1}=0$ and $\dot{x}_{2}=0$. Solve
% the system for its roots. 
% 
% $$ ~\dot{x}_1 = 0 \Rightarrow 0 =  - x_1 + x_1 x_2 $$
% 
% $$ ~\dot{x}_2 = 0 \Rightarrow 0 = x_2 -  x_1 x_2 $$
% 
% $$~0 = x_1 (\beta x_2 - \alpha)~\Rightarrow~x_1 = 0 ; ~x_2 = \alpha/\beta $$
% 
% $$~0 = x_2 (\gamma - \sigma x_1)~\Rightarrow~x_1 = \gamma/\sigma ; ~x_2 = 0 $$
%
% There are two equilibrium points at $(x_1,~x_2)$, 
%
% # At zero, $~(0 ,~ 0),$ 
% # Any positive pair of integers $(\alpha/\beta,~\gamma/\sigma)$
%
% Equilibrium point nature of the zero is a stable center point that is a
% limit cycle. The other e.p. has saddle point nature because it is stable
% in one dimension (goes to zero) and unstable in the other (goes to
% infinity). 
% 

clc
close all
warning('off','all')
warning

x0_set = -2:.5:2;
t_intv= [0 100];
x_0= [4.5, 9.7]'; % initial conditions for x(t)
figure
[t,x]= ode23('Voltera', t_intv, x_0);
plot(t,x)
hold on;
grid on;
title('Voltera Predator-Prey System - Time Plot');
ylabel('x');
xlabel('t (sec)');
legend('Predator', 'Prey');
t_intv= [0 10];
figure
for i=x0_set
for j=x0_set
x0 = [i; j];
[t,x]= ode45('Voltera', t_intv, x0);
plot(x(:,1),x(:,2))
hold on;
end
end
title('Voltera Predator-Prey System - Phase Plane');
ylabel('x_2 - Predator');
xlabel('x_1 - Prey');
axis([-5 5 -5 5]);
grid on;

%%
% 
%   function xdot = Voltera(t,x)
%     xdot = [-x(1)+x(1)*x(2); x(2)-x(1)*x(2)];
%   end
% 

