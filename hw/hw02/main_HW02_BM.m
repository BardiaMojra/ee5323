%% HW 02 - Nonlinear Systems Simulation 
%% Document Information:
% * Author: Bardia Mojra 
% * Date: 09/14/2021 
% * Title: HW 02 - Nonlinear Systems Simulation 
% * Term: Fall 2021
% * Class: EE 5323 - Nonlinear Systems 
% * Dr. Lewis

%% Duffing's Equation 
% Duffing’s equation is interesting in that it exhibits bifurcation, or 
% dependence of stability properties and number of equilibrium points on 
% a parameter. The undamped Duffing equation is
% 
% $$ \ddot{x} + \alpha x + x^3 = 0 $$
% 
% # Find the equilibrium points. Show that for \alpha \greater 0 there is
% only one e.p. .
% # Simulate the Duffing oscillator and make time plot and phase plane plot. 
% # Simulate the following cases,
%
% * $$ \alpha = -1 $$ .
% * $$ \alpha = -0.1 $$ .
% * $$ \alpha = 1 $$ .
% 
% For each case, take ICs spaced in a uniform mesh in a suitable box to 
% show the behavior. Pick the box size. Make one phase plane plot for each 
% case showing all trajectories for that case.
%
%% Duffing's Equation Answer
% Define state variable equations: 
% 
% $$ \dot{x}_{1} = {x}_{2} $$
%
% $$ \dot{x}_{2} = - \alpha {x}_{1} {x}_{1}^{3} $$ 
%
% To find the equalibrium we set $\dot{x}_{1}=0$ and plug it the state variable
% equations.
% 
% $$ x_{2}=0 $$ .
%
% $$ - \alpha {x}_{1} - {x}_{1}^{3}=0  \Rightarrow  $$
%
% $$ \dot{x}_{2} = - \alpha {x}_{1} {x}_{1}^{3} ~~\Rightarrow ~~-x_{1}(\alpha + x_{1}^{2}) = 0 ~~\Rightarrow ~~x_{1}=0, ~~x_{1}^{2} = - \alpha . $$
%
% Equilibrium points must be real. If $\alpha$ is greater than or equal to zero, there is only one equalibrium point at (0,0). If $\alpha$ is smaller than zero, two e.p. at,
%
% $$(\sqrt{- \alpha}, 0)$$ and
% $$(-\sqrt{- \alpha}, 0)$$
%
% 

clc
close all
warning('off','all')
warning

x0_set = -2:.2:2;
t_intv= [0 10];
x_0= [4.5, 9.7]'; % initial conditions for x(t)

% part a, alpha = -1;
figure 
[t,x]= ode23('duffinga', t_intv, x_0);
plot(t,x)
hold on;
grid on;
title("Duffing's Equation, Alpha -1");  
ylabel('x');
xlabel('t (sec)');
legend('x1', 'x2');

t_intv= [0 10];
figure 
for i=x0_set
  for j=x0_set
    x0 = [i; j];
    [t,x]= ode45('duffinga', t_intv, x0);
    plot(x(:,1),x(:,2))
    hold on;
  end
end
title("Duffing's Equation - Phase Plane, Alpha -1");  
ylabel('x_2');
xlabel('x_1');
axis([-3 3 -4 4]);
grid on;
%%
% 
%   function xdot = duffinga(t,x)
%     alpha = -1;
%     xdot = [x(2); -alpha*x(1) - x(1)^3]; 
%   end
% 
close all
% part b, alpha = -0.1
figure 
[t,x]= ode23('duffingb', t_intv, x_0);
plot(t,x)
hold on;
grid on;
title("Duffing's Equation, Alpha -0.1");  
ylabel('x');
xlabel('t (sec)');
legend('x1', 'x2');

t_intv= [0 10];
figure 
for i=x0_set
  for j=x0_set
    x0 = [i; j];
    [t,x]= ode45('duffingb', t_intv, x0);
    plot(x(:,1),x(:,2))
    hold on;
  end
end
title("Duffing's Equation - Phase Plane, Alpha -0.1");  
ylabel('x_2');
xlabel('x_1');
axis([-3 3 -4 4]);
grid on;
%%
% 
%   function xdot = duffingb(t,x)
%     alpha = -0.1;
%     xdot = [x(2); -alpha*x(1) - x(1)^3]; 
%   end
% 
close all
% part c, alpha = 1
figure 
[t,x]= ode23('duffingc', t_intv, x_0);
plot(t,x)
hold on;
grid on;
title("Duffing's Equation, Alpha 1");  
ylabel('x');
xlabel('t (sec)');
legend('x1', 'x2');

t_intv= [0 10];
figure 
for i=x0_set
  for j=x0_set
    x0 = [i; j];
    [t,x]= ode45('duffingc', t_intv, x0);
    plot(x(:,1),x(:,2))
    hold on;
  end
end
title("Duffing's Equation - Phase Plane, Alpha 1");  
ylabel('x_2');
xlabel('x_1');
axis([-3 3 -4 4]);
grid on;

%%
% 
%   function xdot = duffingc(t,x)
%     alpha = 1;
%     xdot = [x(2); -alpha*x(1) - x(1)^3]; 
%   end
% 


%% Part 2-A
% Define state variable equations: 
% 
%

clc
close all 
tspan = [0 5];
for k=-10:0.5:10
  for j=-10:0.5:10
    x0 = [k;j];
    [t,x] = ode23('part2', tspan, x0);
    plot(x(:,1),x(:,2))
    hold on
  end
end
title("Part 2-A - Phase Plane");  
ylabel('x_2');
xlabel('x_1');
axis([-15 15 -15 15]);
grid on;
%%
% 
%   function xdot = part2(t,x)
%     xdot = [x(2)*(1+x(1)-x(2)^2); x(1)*(1+x(2)-x(1)^2)]; 
%   end
% 

%% Part 2-B
% Define state variable equations: 
% 
%

clc
close all 
tspan = [0 5];
for k=-3:0.5:3
  for j=-3:0.5:3
    x0 = [k;j];
    [t,x] = ode23('part2', tspan, x0);
    plot(x(:,1),x(:,2))
    hold on
  end
end
title("Part 2-B - Phase Plane");  
ylabel('x_2');
xlabel('x_1');
axis([-5 5 -5 5]);
grid on;
%%
% 
%   function xdot = part2(t,x)
%     xdot = [x(2)*(1+x(1)-x(2)^2); x(1)*(1+x(2)-x(1)^2)]; 
%   end
% 

%% Part 3
% Define state variable equations: 
% 
%

clc
close all 
tspan = [0 5];
for k=-2:0.5:2
  for j=-2:0.5:2
    x0 = [k;j];
    [t,x] = ode23('part3', tspan, x0);
    plot(x(:,1),x(:,2))
    hold on
  end
end
title("Part 3 - Phase Plane");  
ylabel('x_2');
xlabel('x_1');
axis([-5 5 -5 5]);
grid on;
%%
% 
%   function xdot = part3(t,x)
%     a=2; c=2; d=2; f=2;
%     b=3; e=3;
%     xdot = [a*x(1)-b*x(1)*x(2)-c*x(1)^2; d*x(2)-e*x(1)*x(2)-f*x(2)^2]; 
%   end
% 

