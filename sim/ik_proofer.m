L1=30;L2=92;L3=169;
for x_ = -50:50
    for y_ = -50:50
        for z_ = -50:50
            try
                ik(x_,y_,z_,L1,L2,L3);
            catch
                disp(['r is equal to ',num2str(x_),',',num2str(y_),',',num2str(z_),' .'])
            end
        end
    end
end