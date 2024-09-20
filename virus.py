import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
population_size = 1000  # Tamaño de la población
initial_infected = 1  # Número inicial de personas infectadas
infection_rate = 0.1  # Probabilidad de que una persona infectada contagie a una sana
recovery_time = 14  # Tiempo (en días) hasta que una persona infectada se recupere
days = 100  # Duración de la simulación en días

# Inicializar el estado de la población
# 0: Sana, 1: Infectada, 2: Recuperada
population = np.zeros(population_size)
population[:initial_infected] = 1  # Infectar a las primeras personas

# Variables para almacenar la evolución de la epidemia
healthy_count = []
infected_count = []
recovered_count = []

# Simulación día a día
for day in range(days):
    new_infected = 0
    new_recovered = 0
    
    # Iterar sobre cada persona
    for i in range(population_size):
        if population[i] == 1:  # Si la persona está infectada
            # Infectar a las personas sanas (probabilidad de infección)
            for j in range(population_size):
                if population[j] == 0 and np.random.rand() < infection_rate:
                    population[j] = 1
                    new_infected += 1
            # Recuperar a la persona si ha pasado el tiempo de recuperación
            if np.random.rand() < 1/recovery_time:
                population[i] = 2
                new_recovered += 1
    
    # Contar el número de personas en cada estado
    healthy_count.append(np.sum(population == 0))
    infected_count.append(np.sum(population == 1))
    recovered_count.append(np.sum(population == 2))

# Graficar la evolución de la epidemia
plt.figure(figsize=(10, 6))
plt.plot(healthy_count, label='Sanos', color='green')
plt.plot(infected_count, label='Infectados', color='red')
plt.plot(recovered_count, label='Recuperados', color='blue')
plt.xlabel('Días')
plt.ylabel('Número de personas')
plt.title('Simulación de la propagación de un virus')
plt.legend()
plt.grid(True)
plt.show()
