######################################################################
# Verification of UAV track planning model based on DQN
#---------------------------------------------------------------
# author by younghow
# email: younghowkg@gmail.com
# --------------------------------------------------------------
#将训练好的DQN模型放入仿真模拟环境中进行测试，
#可以使用env类中的reset_test函数对测试环境进行设置，
#生成测试环境的UAV的起点与终点，并根据难度等级生成城市环境的建筑数目与风况。
#----------------------------------------------------------------
# Put the trained DQN model into the simulation environment for testing.
# You can use the reset_test function in the env class to set the test environment, 
# generate the starting point and end point of the UAV of the test environment, 
# and generate the number of buildings,the number of buildings and wind conditions
#  in the urban environment according to the difficulty level. 
##############################################################################
import numpy as np
import torch
import matplotlib
import matplotlib.pyplot as plt
import time
from env import *
import torch


if __name__ == '__main__':
    LEARNING_RATE = 0.00033  # 学习率
    num_episodes = 80000  # 训练周期长度
    space_dim = 42  # n_spaces   状态空间维度
    action_dim = 27  # n_actions   动作空间维度
    threshold = 200
    env = Env(space_dim, action_dim, LEARNING_RATE)
    check_point_Qlocal=torch.load('Qlocal.pth')
    check_point_Qtarget=torch.load('Qtarget.pth')
    env.q_target.load_state_dict(check_point_Qtarget['model'])
    env.q_local.load_state_dict(check_point_Qlocal['model'])
    env.optim.load_state_dict(check_point_Qlocal['optimizer'])
    epoch=check_point_Qlocal['epoch']
    #真实场景运行
    env.level= 8 #环境难度等级
    state = env.reset_test()  #环境重置1
    total_reward = 0
    env.render(1) #环境 设置
    n_done=0
    count=0
 
    n_test=1  #测试次数
    n_creash=0   #坠毁数目
    for i in range(n_test):
        while(1):
            if env.uavs[0].done:
                #无人机已结束任务，跳过
                break
            action = env.get_action(FloatTensor(np.array([state[0]])) , 0.01)   #根据Q值选取动作
            
            next_state, reward, uav_done, info= env.step(action.item(),0)  #根据选取的动作改变状态，获取收益

            total_reward += reward  #求总收益
            #交互显示
            print('ac',action)
            env.render()
            if uav_done:
                break
            if info==1:
                success_count=success_count+1

            state[0] = next_state  #状态变更
        print('env',env.uavs[0].step)
        # env.ax.scatter(env.target[0].x, env.target[0].y, env.target[0].z,c='red')
        plt.savefig("function3.jpg")
        plt.show()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for ob in env.bds:
        # 绘画出所有建筑
        x = ob.x
        y = ob.y
        z = 0
        dx = ob.l
        dy = ob.w
        dz = ob.h
        xx = np.linspace(x - dx, x + dx, 2)
        yy = np.linspace(y - dy, y + dy, 2)
        zz = np.linspace(z, z + dz, 2)

        xx2, yy2 = np.meshgrid(xx, yy)

        ax.plot_surface(xx2, yy2, np.full_like(xx2, z))
        ax.plot_surface(xx2, yy2, np.full_like(xx2, z + dz))

        yy2, zz2 = np.meshgrid(yy, zz)
        ax.plot_surface(np.full_like(yy2, x - dx), yy2, zz2)
        ax.plot_surface(np.full_like(yy2, x + dx), yy2, zz2)

        xx2, zz2 = np.meshgrid(xx, zz)
        ax.plot_surface(xx2, np.full_like(yy2, y - dy), zz2)
        ax.plot_surface(xx2, np.full_like(yy2, y + dy), zz2)
    plt.savefig("function2.jpg")



