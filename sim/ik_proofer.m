L1=30;L2=92;L3=169;err=0;
tStart = tic;
parfor x_ = -200:200
    for y_ = -200:200
        for z_ = -200:200
            try
                ik(x_,y_,z_,L1,L2,L3);
            catch
                err=err+1;
%                 disp(['r is equal to ',num2str(x_),',',num2str(y_),',',num2str(z_),' .'])
            end
        end
    end
    tElapsed = toc(tStart);
end
err
disp(['porcentage of error is',num2str((err_/(400^3))*100),' %'])