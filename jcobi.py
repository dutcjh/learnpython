"""
%% jacobi 迭代法
% x0为初始迭代值，e0为最大允许误差，Nmax为最大迭代次数
"""
from numpy import *

def jacobi(A,b,x0=array([0,0,0]),e0=0.0001,Nmax = 100):
    n = b.size
    

