function [q1, q2, q3] = ik(x, y, z, L1, L2, L3)
    q1 = atan2d(y, x);
    cosq_3 = (x^2 + y^2 + (z-L1)^2 - L2^2 - L3^2)/(2*L2*L3);
    q3 = atan2d(-sqrt(1 - cosq_3^2), cosq_3);
    q2 = atan2d(z - L1, sqrt(x^2 + y^2)) - atan2d(-L3*sqrt(1 - cosq_3^2), L2 + L3*cosq_3);
end