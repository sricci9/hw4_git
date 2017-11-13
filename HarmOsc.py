import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
plt.rc('figure', figsize=[5,5])

# Added changes for purpose of Assignment 4

def expEuler(x0, v0, h):
    '''Given initial conditions, runs the explicit Euler method and returns
    x values, v values, t values, and the h used.'''
    num = int(10 * np.pi / h)
    tVals = np.linspace(0, 10 * np.pi, num=num)
    xVals = np.zeros(num)
    vVals = np.zeros(num)
    xVals[0] = x0
    vVals[0] = v0
    for i in range(1,num):
        xVals[i] = xVals[i-1] + h * vVals[i-1]
        vVals[i] = vVals[i-1] - h * xVals[i-1]
    return h, xVals, vVals, tVals

def impEuler(x0, v0, h):
    '''Given initial conditions, runs the implicit Euler method and returns
    x values, v values, t values, and the h used.'''
    num = int(10 * np.pi / h)
    tVals = np.linspace(0, 10 * np.pi, num=num)
    xVals = np.zeros(num)
    vVals = np.zeros(num)
    xVals[0] = x0
    vVals[0] = v0
    for i in range(1,num):
        xVals[i] = (xVals[i-1] + h * vVals[i-1]) * 1/(1 + h**2)
        vVals[i] = (vVals[i-1] - h * xVals[i-1]) * 1/(1 + h**2)
    return h, xVals, vVals, tVals

def symEuler(x0, v0, h):
    '''Given initial conditions, runs the symplectic Euler method and
    returns x values, v values, t values, and the h used.'''
    num = int(10 * np.pi / h)
    tVals = np.linspace(0, 10 * np.pi, num=num)
    xVals = np.zeros(num)
    vVals = np.zeros(num)
    xVals[0] = x0
    vVals[0] = v0
    for i in range(1,num):
        xVals[i] = (xVals[i-1] + h * vVals[i-1])
        vVals[i] = (vVals[i-1] - h * xVals[i])
    return h, xVals, vVals, tVals

def eulerPlot(h, xVals, vVals, tVals, impExp):
    '''Plots the Euler plot for a given list of xVals,
    yVals, and tVals, and a given h value, and a string of
    either 'imp' or 'exp' that determines whether it's
    implicit or explicit Euler.'''
    plt.plot(tVals, xVals, color='red', label='x(t)')
    plt.plot(tVals, vVals, color='blue', label='v(t)')
    plt.legend()
    plt.xlabel('t')
    fileString = 'EulerOsc_x0_'+str(xVals[0])+'_v0_'+str(vVals[0])+\
    '_h_'+str(round(h,3))+'.png'
    assert impExp in ['imp', 'exp', 'sym']
    if impExp == 'imp': fileString = 'imp' + fileString
    plt.savefig(fileString)
    plt.clf()

def eulerError(impExp):
    '''Plots the error between the Euler solution ('imp' or 'exp') and
    the analytic solution to a simple harmonic oscillator with initial
    conditions x0 = 1 and v0 = 0.'''
    assert impExp in ['imp', 'exp']
    if impExp == 'exp': h, eeX, eeV, tVals = expEuler(1, 0, np.pi/1000)
    else: h, eeX, eeV, tVals = impEuler(1, 0, np.pi/1000)
    tVals2 = np.copy(tVals)
    analX = np.cos(tVals)
    analV = -np.sin(tVals)
    errX = analX - eeX
    errV = analV - eeV
    plt.plot(tVals, errX, color='red', label='x error')
    plt.plot(tVals, errV, color='blue', label='v error')
    plt.legend()
    plt.xlabel('t')
    fileString = 'ErrorOsc_x0_1.0_v0_0.0_h_'+str(round(h,3))+'.png'
    if impExp == 'imp': fileString = 'imp' + fileString
    plt.savefig(fileString)
    plt.clf()

def manyErrorPlots(h0):
    '''Shows the max value vs. h for the error plots
    of (1, 0.5, 0.25, 0.125, 0.0625) times h0'''
    hMults = np.array([1, 0.5, 0.25, 0.125, 0.0625])
    maxErr = np.zeros(5)
    for ind, mult in np.ndenumerate(hMults):
        Eu = expEuler(1, 0, mult * h0)
        eeX = Eu[1]
        tVals = Eu[3]
        analX = np.cos(tVals)
        errX = analX - eeX
        maxErr[ind] = np.amax(errX)
    plt.scatter(hMults, maxErr)
    plt.savefig('manyErrors.png')
    plt.clf()

def Energy(xVals, vVals, tVals, impExp):
    '''Plots the energy x**2 + v**2 over t.
    Requires whether it is 'imp', 'exp', or 'sym' to save the file'''
    energy = xVals ** 2 + vVals ** 2
    plt.plot(tVals, energy, color='blue', label='energy')
    assert impExp in ['imp', 'exp', 'sym']
    if impExp == 'imp': plt.savefig('impEnergy.png')
    elif impExp == 'sym': plt.savefig('symEnergy.png')
    else: plt.savefig('energy.png')
    plt.clf()
    tVals2 = np.copy(tVals)
    plt.plot(tVals, energy, color='blue', label='energy')
    plt.plot(tVals, np.cos(tVals2) - xVals + 1, color='red', label='x(t)')
    if impExp == 'imp': plt.savefig('impEnergyWithErr.png')
    elif impExp == 'sym': plt.savefig('symEnergyWithErr.png')
    else: plt.savefig('energyWithErr.png')
    plt.clf()

def phaseSpace(xVals, vVals, tVals, impExp):
    '''Plots the phase-space of the trajectory produced by a given set of
    x values and v values. Compares to an analytic solution for the given
    t values. Uses impExp to name a file ('imp', 'exp', or 'sym').'''
    tVals2 = np.copy(tVals)
    analX = np.cos(tVals)
    analV = -np.sin(tVals2)
    plt.plot(xVals, vVals, color='red', label=impExp + ' approx')
    plt.plot(analX, analV, color='blue', label='analytic')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('v')
    plt.xlim(-1.8, 1.8)
    plt.ylim(-1.8, 1.8)
    plt.savefig(impExp + 'PhaseSpace.png')
    plt.clf()

def allPhaseSpace(x0, v0, h):
    '''Creates a plot of phase space for all of the explicit, implicit,
    and symplectic approximations for a given set of initial conditions.'''
    h, expX, expV, tVals = expEuler(x0, v0, h)
    h, impX, impV, tVals = impEuler(x0, v0, h)
    h, symX, symV, tVals = symEuler(x0, v0, h)
    plt.plot(expX, expV, color='red', label='exp approx')
    plt.plot(impX, impV, color='blue', label='imp approx')
    plt.plot(symX, symV, color='green', label='sym approx')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('v')
    plt.xlim(-1.8, 1.8)
    plt.ylim(-1.8, 1.8)
    plt.savefig('allPhaseSpace.png')
    plt.clf()

def figGen():
    '''Generates the figures for the Latex document accompanying the code.
    Calling this function followed by compiling the Latex document will
    give the pdf report.'''
    expEuler1 = expEuler(1, 0, np.pi/1000)
    eulerPlot(expEuler1[0], expEuler1[1], expEuler1[2], expEuler1[3], 'exp')
    eulerError('exp')
    manyErrorPlots(np.pi/1000)
    Energy(expEuler1[1], expEuler1[2], expEuler1[3], 'exp')
    impEuler1 = impEuler(1, 0, np.pi/1000)
    eulerPlot(impEuler1[0], impEuler1[1], impEuler1[2], impEuler1[3], 'imp')
    eulerError('imp')
    Energy(impEuler1[1], impEuler1[2], impEuler1[3], 'imp')
    expEuler2 = expEuler(1, 0, np.pi/100)
    impEuler2 = impEuler(1, 0, np.pi/100)
    phaseSpace(expEuler2[1], expEuler2[2], expEuler2[3], 'exp')
    phaseSpace(impEuler2[1], impEuler2[2], impEuler2[3], 'imp')
    symEuler1 = symEuler(1, 0, np.pi/100)
    symEuler2 = symEuler(1, 0, np.pi/25)
    phaseSpace(symEuler2[1], symEuler2[2], symEuler2[3], 'sym')
    allPhaseSpace(1, 0, np.pi/100)
    Energy(symEuler1[1], symEuler1[2], symEuler1[3], 'sym')

# Execute figGen to get all of the figures
figGen()