%% HW03 - Q02 - System
% @author: Bardia Mojra
% @date: 09/28/2021
% @title HW03 - Q02 - System
% @class ee5323 - Nonlinear Systems
% @professor - Dr. Frank Lewis

clc
close all
%warning('off','all')
%warning

x0_set = -2:.5:2;
t_intv= [0 100];
x_0= [4.5; 9.7]; % initial conditions for x(t)
%t = t_intv;

figure
[t, y] = ode23(@System, t_intv, x_0);
plot(t,y)
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
    [t,x]= ode45(@System, t_intv, x0);
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

