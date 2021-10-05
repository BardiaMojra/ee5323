%% HW03 - Q01 - Voltera Predator-Prey System
% @author: Bardia Mojra
% @date: 09/28/2021
% @title HW03 - Q01 - Voltera Predator-Prey System
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

function xdot = Voltera(t,x)
  xdot = [-x(1)+x(1)*x(2); x(2)-x(1)*x(2)];
end

