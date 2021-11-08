%% HW05 - Q03 - AS
% @author: Bardia Mojra
% @date: 10/28/2021
% @title HW05 - Q03 - Asymptotic Stability Simulation
% @class ee5323 - Nonlinear Systems
% @professor - Dr. Frank Lewis

clc
clear
close all
warning('off','all')
warning

% part a
t_intv= [0 20];
x_0= [0.1, 0]'; % initial conditions for x(t)
figure
[t,x]= ode23('q03_sys', t_intv, x_0);
plot(t,x)
hold on;
grid on;
title('First Integral of Motion - Time Plot','Interpreter','latex');
ylabel('$X(t)$','Interpreter','latex');
xlabel('t','Interpreter','latex');
legend('$x(t)$', '$\dot{x}(t)$','Interpreter','latex');

% part b
figure();
hold on;
grid on;
mesh = -10:2:10;
[x1,x2] = meshgrid(mesh,mesh);
dx1=[];
dx2=[];
N=length(x1);
for i=1:N
  for j=1:N
    dx = q03_sys(0, [x1(i,j);x2(i,j)]);
    dx1(i,j) = dx(1);
    dx2(i,j) = dx(2);
  end  
end
quiver(x1,x2,dx1,dx2);
ylabel('$x_2$','Interpreter','latex');
xlabel('$x_1$','Interpreter','latex');
legend('Flow Vector','Interpreter','latex');
title('Vector Field - Phase Plane','Interpreter','latex');
axis([-15 15 -15 15])

% part c
figure 
for i=mesh
  for j=mesh
    init=[i, j];
    [t, x] = ode23(@q03_sys, [0 10], init);
    plot(x(:,1),x(:,2))
    hold on;
  end
end
ylabel('$x_2$','Interpreter','latex');
xlabel('$x_1$','Interpreter','latex');
legend('Orbits','Interpreter','latex');
title('System Trajectories - Phase Plane','Interpreter','latex');
grid on;
axis([-50 50 -50 50])

%%
% 
% function xdot = q03_sys(t,x)
%   xdot = [x(1)*x(2)^2+x(1)*(x(1)^2+x(2)^2-3); -x(1)^2 *x(2)+x(2)*(x(1)^2+x(2)^2-3)]; 
% end

