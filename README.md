# SIRD
Pandemic simulator

SIRD simulation with adjustable values


epsilon : individuals that can spread the disease but do not show symptoms yet

### ***Susceptible***
 (rate of population grow * Total Population ) - (rate of spread * Susceptible * Infected / Total Population - rate of population grow * Susceptible + epsilon * Infected


### ***Infected***
rate of spread * Susceptible * Infected / Total Population - (rate of population grow + rate of recovery + epsilon) * Infected


### ***Susceptible***
rate of recovery * Infected


### ***Susceptible***
mortality rate of the disease * Infected
