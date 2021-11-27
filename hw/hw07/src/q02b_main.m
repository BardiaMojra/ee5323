%% hw07 - q02b - lyapunov control design
% @author Bardia Mojra
% @date 11/25/2021
% @title hw07 - q02b - lyapunov control design
% @class ee5323 - Nonlinear Systems
% @professor Dr. Frank Lewis

clc
clear
close all
%warning('off','all')
%warning

syms f(x1,x2) x1 x2
f(x1,x2) = [x2*sin(x1)-x1;-x1*sin(x1)-x2];
x1_ICs = -20:2:20;
x2_ICs = -20:2:20;

J = jacobian(f(x1,x2),[x1;x2]); % instantiate symbolic jacobian 
F = solve(f==0,[x1,x2]); % solve jacobian symbolically 
eps = [double(F.x1),double(F.x2)]; % solve numerical solutions, eq. points (eps)
%eps(any(imag(eps),2),:) = []; % remove imaginary roots, they are not eps.
eps = unique(eps,'rows');
eps_x1 = eps(:,1);
eps_x2 = eps(:,2);
fprintf('Equilibrium Points:\n\t x1\t\tx2\n')
for i = 1:numel(eps_x1)
    fprintf('%6.4g %6.4g\n',eps_x1(i),eps_x2(i));
end

% create quiver plot
figure('color','white');
grid
mesh = -10:2:10;
[x1g,x2g] = meshgrid(mesh,mesh);
U = zeros(size(x1g)); % create directional components
V = U;
t = 0;

for i = 1:numel(x1g)-1
    xp = q02b_sys(t,[x1g(i);x2g(i)]);
    U(i) = xp(1);
    V(i) = xp(2);
end
qaxis = quiver(x1g,x2g,U,V);

grid on
grid minor
axis([-10 10 -10 10])

U = qaxis.UData;
V = qaxis.VData;
X = qaxis.XData;
Y = qaxis.YData;

headWidth = 4;
headLength = 8;
LineLength = 0.5;
tr = [0 20];

hold on
plot(nan,nan,'o','linewidth',1,'markeredgecolor','r','markerfacecolor','r')
legend('Trajectory of I.C.','location','northwest','AutoUpdate','off','Interpreter','latex')
for x1 = x1_ICs
    for x2 = x2_ICs
        out = ode23(@(t,x) q02b_sys(t,x),tr,[x1 x2]);
        plot(out.y(1,:),out.y(2,:))
    end
end

plot(eps_x1,eps_x2,'o','MarkerSize', 8,'linewidth',1,'markeredgecolor','r','markerfacecolor','r')
ylabel('$x_2$','Interpreter','latex');
xlabel('$x_1$','Interpreter','latex');
title('System Trajectories - Phase Plane','Interpreter','latex');




