%% HW04 - Q02 - Vector Fields, Flows, First Integrals
% @author: Bardia Mojra
% @date: 10/14/2021
% @title HW03 - Q01 - First Integral of Motion for Undamped Oscillator
% @class ee5323 - Nonlinear Systems
% @professor - Dr. Frank Lewis

clc
clear
close all
warning('off','all')
warning

% part b
t_intv= [0 20];
x_0= [0.1, 0]'; % initial conditions for x(t)
figure
[t,x]= ode23('q02_sys', t_intv, x_0);
plot(t,x)
hold on;
grid on;
title('First Integral of Motion for Undamped Oscillator - Time Plot','Interpreter','latex');
ylabel('$X(t)$','Interpreter','latex');
xlabel('t','Interpreter','latex');
legend('$x(t)$', '$\dot{x}(t)$','Interpreter','latex');

% part c
figure
hold on;
grid on;
[x1,x2] = meshgrid(-10:1:10,-10:1:10);
dx1=[];
dx2=[];
N=length(x1);
for i=1:N
  for j=1:N
    dx = q02_sys(0, [x1(i,j);x2(i,j)]);
    dx1(i,j) = dx(1);
    dx2(i,j) = dx(2);
  end
end
quiver(x1,x2,dx1,dx2);
ylabel('$x_2$','Interpreter','latex');
xlabel('$x_1$','Interpreter','latex');
legend('Flow Vector','Interpreter','latex');
title('Vector Field - Phase Plane','Interpreter','latex');

% part d
figure
hold on
for i=-10:1:10
  for j=-10:1:10
    init=[i j];
    [t, x] = ode23('q02_sys', [0 10], init);
    figure(3)
    plot(x(:,1),x(:,2))
    hold on;
  end
end
ylabel('$x_2$','Interpreter','latex');
xlabel('$x_1$','Interpreter','latex');
legend('Orbits','Interpreter','latex');
title('System Trajectories - Phase Plane','Interpreter','latex');
grid on;

% part e
figure
hold on
for i=-10:1:10
  for j=-10:1:10
    init=[i j];
    [t, x] = ode23('q02_sys', [0 10], init);
    N=length(x);
    figure(4)
    hold on;
    plot3(x(:,1), x(:,2), zeros(N,1))
    hold on;
    syms x1 x2
    fsurf(-0.5* x1^2 -0.5* x2^2)
    hold on;
  end
end


%%
%
% function xdot = q02_sys(t,x)
%   xdot = [x(2); x(1)];
% end
