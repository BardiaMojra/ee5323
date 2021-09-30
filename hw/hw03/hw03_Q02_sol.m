%% HW03 - Q02 - System
% @author: Bardia Mojra
% @date: 09/28/2021
% @title HW03 - Q02 - System
% @class ee5323 - Nonlinear Systems
% @professor - Dr. Frank Lewis


clc
close all
warning('off','all')
warning

x0_set = -2:.5:2;
t_intv= [0 100];
x_0= [4.5, 9.7]'; % initial conditions for x(t)
figure
[t,x]= ode23('hw03_Q02_system', t_intv, x_0);
plot(t,x)
hold on;
grid on;
title('Q02 System - Time Plot');
xlabel('t (sec)');
legend('dx_1', 'dx_2');
t_intv= [0 10];
figure
for i=x0_set
for j=x0_set
x0 = [i; j];
[t,x]= ode45('hw03_Q02_system', t_intv, x0);
plot(x(:,1),x(:,2))
hold on;
end
end
title('System - Phase Plane');
ylabel('dx_2');
xlabel('dx_1');
axis([-5 5 -5 5]);
grid on;

%%
%

