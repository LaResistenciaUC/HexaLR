L1=5;           % length of first link
L2=10;          % length of second link
r_limit=L1+L2;  % in radial direction
origin = zeros(1,3);

a_1_i = [L1 0 0];
a_2_i = [L2 0 0];
pose_i = a_1_i + a_2_i;
pose_f = [10 0 5];




pts_i = [origin; pose_i];
pts_f = [origin; pose_f];
plot3(pts_i(:,1), pts_i(:,2), pts_i(:,3)); l_i = 'Initial Point';
hold on; grid on;
plot3(pts_f(:,1), pts_f(:,2), pts_f(:,3)); l_f = 'Final Point';
legend(l_i,l_f);