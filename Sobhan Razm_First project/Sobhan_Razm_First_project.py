
a=1+1
print(a)

msg = "Hello world"
print(msg)


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

POP_SIZE = 500
MUT_RATE = 0.1
TARGET = 'sobhan razm'
GENES = ' abcdefghijklmnopqrstuvwxyz'


# In[2]:

# Initialize Population
def initialize_pop(TARGET):
    population = list()
    # tar_len is also called chromosome length
    # each chromosome in a population will be of length len(TARGET)
    tar_len = len(TARGET)

    for i in range(POP_SIZE):
        temp = list()
        for j in range(tar_len):
            temp.append(random.choice(GENES))
        population.append(temp)

    return population
# population = [[random.choice(GENES) for _ in range(tar_len)] for _ in range(POP_SIZE)]


# In[3]:


# now we will produce offspring using crossover
# 2 parents at random will be selected from the list selected_chromo
# crossover point will be also random
# produced child will be added to a list named offspring

def crossover(selected_chromo, CHROMO_LEN, population):
    offspring_cross = []
    for i in range(int(POP_SIZE)):
        parent1 = random.choice(selected_chromo)
        parent2 = random.choice(population[:int(POP_SIZE*50)]) # 50 is only to make sure that we are seen all chromozoms

        p1 = parent1[0] #  Because we have [[' ', 'j', 'z', 'v', 'g', 'p', 'm', 'z', 's'], 9]
        p2 = parent2[0] 
  
        crossover_point = random.randint(1, CHROMO_LEN-1)
        child =  p1[:crossover_point] + p2[crossover_point:]
        # child2 = p2[:crossover_point] + p1[crossover_point:]
        offspring_cross.extend([child]) #since we used extend, we used [] for child
    return offspring_cross

# crossover can be done anyway you like
# we selected the parents and crossover point at random
# then for child1, we set it to, parent1 from 0 to crossover point + parent2 from crossover to end
# if p1 = a,b,c,d,e and p2 = v,w,x,y,z and
# if crossover point = 3
# child1 = abcyz
# child2 = vwxde
# Add a picture
# offspring will contain both child1 and child2


# In[4]:


# now mutate the children
# means, change random genes from the chromosome to add diversity to the population

def mutate(offspring, MUT_RATE):
    mutated_offspring = []

    for arr in offspring:
        for i in range(len(arr)):
            if random.random() < MUT_RATE:
                arr[i] = random.choice(GENES)
        mutated_offspring.append(arr)
    return mutated_offspring

# the offspring we had after crossover now has some genes changed


# In[5]:


def selection(population, TARGET):
    # now we will sort chromo_pop accroding to the fitness
    sorted_chromo_pop = sorted(population, key= lambda x: x[1]) #ascending order
    # instead of lambda we could make a new function to extract the fitness of each chromosome
    # we will return the top 50% of our population since they will help us reach the goal
    return sorted_chromo_pop[:int(0.5*POP_SIZE)]


# In[6]:


# Design a fitness function
# this will be calculated for each chromosome in the population

def fitness_cal(TARGET, chromo_from_pop):
    difference = 0
    for tar_char, chromo_char in zip(TARGET, chromo_from_pop):
        if tar_char != chromo_char:
            difference+=1
    
    return [chromo_from_pop, difference]


# In[7]:


# Finally we will replace the less fit chromosomes in population with better chromosomes in the offspring

def replace(new_gen, population):
    for _ in range(len(population)):
        if population[_][1] > new_gen[_][1]:
          population[_][0] = new_gen[_][0]
          population[_][1] = new_gen[_][1]
    return population


# In[8]:


def main(POP_SIZE, MUT_RATE, TARGET, GENES):
    # 1) initialize population
    initial_population = initialize_pop(TARGET)
    found = False
    population = []
    generation = 1

    # 2) Calculating the fitness for the current population
    for _ in range(len(initial_population)):
        population.append(fitness_cal(TARGET, initial_population[_]))

    # now population has 2 things, [chromosome, fitness]
    # 3) now we loop until TARGET is found
    while not found:

      # 3.1) select best people from current population
      selected = selection(population, TARGET)

      # 3.2) mate parents to make new generation
      population = sorted(population, key= lambda x:x[1]) # we sort the initial_population 
      crossovered = crossover(selected, len(TARGET), population)
            
      # 3.3) mutating the children to diversify the new generation
      mutated = mutate(crossovered, MUT_RATE)

      new_gen = []
      for _ in mutated:
          new_gen.append(fitness_cal(TARGET, _))

      # 3.4) replacement of bad population with new generation
      # we sort here first to compare the least fit population with the most fit new_gen

      population = replace(new_gen, population)

      
      if (population[0][1] == 0): #first chromosom of each population, since it is sorted  
        print('Target found')
        print('String: ' + str(population[0][0]) + ' Generation: ' + str(generation) + ' Fitness: ' + str(population[0][1]))
        break
      print('String: ' + str(population[0][0]) + ' Generation: ' + str(generation) + ' Fitness: ' + str(population[0][1]))
      generation+=1

    


# In[9]:


main(POP_SIZE, MUT_RATE, TARGET, GENES)


# In[ ]:




