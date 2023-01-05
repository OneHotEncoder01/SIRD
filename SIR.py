import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# SIR model differential equations
def dS_dt(S, I, N, beta, epsilon, mu):
    return mu*N - beta*S*I/N - mu*S + epsilon*I

def dI_dt(S, I, N, beta, gamma, epsilon, mu):
    return beta*S*I/N - (mu + gamma + epsilon)*I

def dR_dt(I, gamma):
    return gamma*I

def dD_dt(I, omega):
    return omega*I

def SIRD_modell(y, time, N, beta, gamma, omega, epsilon, mu):
    S, I, R, D = y
    return [dS_dt(S, I, N, beta, epsilon, mu), 
            dI_dt(S, I, N, beta, gamma, epsilon, mu), 
            dR_dt(I, gamma), 
            dD_dt(I, omega)]

# Initial values
S0 = 0.99 # Susceptible
I0 = 0.01 # Infected
R0 = 0.0 # Recovered
D0 = 0.0 # mortality
N = S0 + I0 + R0 + D0 # Total population
beta = 0.22 # rate of spread "Basic Reproductive Number" Estimated Corona = 2.2 
gamma = 0.07 # rate of recovery
omega = 0.1 - gamma # mortality rate of the disease
epsilon = 0.01 # individuals that can spread the disease but do not show symptoms yet
mu = 0.01 # rate of population grow (birth)


# Time grid
time = np.linspace(0,100,100000)

# Solve the ODEs
solution = scipy.integrate.odeint(SIRD_modell, [S0, I0, R0, D0], time, args=(N, beta, gamma, omega, epsilon, mu))
solution = np.array(solution)


plt.style.use('dark_background')

# Set up the plot
fig, ax = plt.subplots(figsize=[24,16])
plt.subplots_adjust(left=0.25, bottom=0.25)
l, = plt.plot(time, solution[:, 0], label = "Susceptible(t)")
i, = plt.plot(time, solution[:, 1], label = "Infected(t)")
r, = plt.plot(time, solution[:, 2], label = "Recovered(t)")
d, = plt.plot(time, solution[:, 3], label = "mortality(t)")
plt.legend()

# Set up the sliders
axcolor = 'lightgoldenrodyellow'
ax_beta = plt.axes([0.25, 0.14, 0.65, 0.03], facecolor=axcolor)
ax_gamma = plt.axes([0.25, 0.18, 0.65, 0.03], facecolor=axcolor)
ax_mu = plt.axes([0.25, 0.22, 0.65, 0.03], facecolor=axcolor)

s_beta = Slider(ax_beta, 'rate of spread', 0.001, 0.5, valinit=beta)
s_gamma = Slider(ax_gamma, 'rate of recovery', 0.001, 0.5, valinit=gamma)
s_mu = Slider(ax_mu, 'population grow', 0.001, 0.5, valinit=mu)


# Update the plot when the sliders are changed
def update(val):
    beta = s_beta.val
    gamma = s_gamma.val
    mu = s_mu.val
    solution = scipy.integrate.odeint(SIRD_modell, [S0, I0, R0, D0], time, args=(N, beta, gamma, omega, epsilon, mu))
    l.set_ydata(solution[:, 0])
    i.set_ydata(solution[:, 1])
    r.set_ydata(solution[:, 2])
    d.set_ydata(solution[:, 3])
    

    fig.canvas.draw_idle()

s_beta.on_changed(update)
s_gamma.on_changed(update)
s_mu.on_changed(update)

plt.show()
