# Campos Romero Adriana Jasiel 111-413
# A partir del codigo fuente del archivo bpa (Busqueda promero en anchura), modificar el mismo para encontrar la sulucion, pero utilizando 
# una lista_frontera ordenada de mayo a menor valor que cada nodo pueda tener en su campo costo, ese valor debe llenarselo de manera 
# aleatoria en el momento de creacion del nodo. Una vez implementado se debe describir que sucede y que capacidad de resolver rompecabezas 
# lineales de 4, 6, 7, 8, 9, 10, .... se puede resolver con el mismo. 

from random import *


class Node:
    def __init__(self, data, son=None):
        self.data = data
        self.sons = []
        self.father = None
        self.cost = {}
        self.set_son(son)

    #Se pueden pasar varios hijos
    def set_son(self, son):
        #self.son = son
        if (son is not None):
          self.sons.append(son)
          if self.sons is not None:
              for s in self.sons:
                  s.father = self

    def get_sons(self):
        return self.sons

    def get_father(self):
        return self.father

    def set_father(self, father):
        self.father = father

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost
    #obtencion de los datos
    def equal(self, node):
        if self.get_data() == node.get_data():
            return True
        else:
            return False

    def on_list(self, node_list):
        listed = False
        for n in node_list:
            if self.equal(n):
                listed = True
        return listed

    def __str__(self):
        return str(self.get_data()) #str representa los datos

# Una solucion heuristica es encontrar el nodo con el costo mas bajo, es por eso que las soluciones heuristicas son mas rapidas 
# La variable number es la cantidad de numeros que se van a ordenar (tamaño del estado inicial)
def search_heuristic_solution(init_node, solution, visited, number):
    visited.append(init_node.get_data())
    if init_node.get_data() == solution:
        return init_node
    else:
        # Expandir nodos sucesores (hijos)
        for i in range(number - 1):
            node_data = init_node.get_data().copy()
            temp = node_data[i]
            node_data[i] = node_data[i+1]
            node_data[i+1] = temp
            new_son = Node(node_data)
            init_node.set_son(new_son)
            new_son.set_father(init_node)

        for son_node in init_node.get_sons():
            if not son_node.get_data() in visited and improvement(init_node, son_node):
                # Llamada recursiva
                solutn = search_heuristic_solution(son_node, solution, visited, number)
                if solutn is not None:
                    return solutn
        return None

# la funcion improvement verifica si el nodo hijo es mejor o tiene un menor costo que el nodo padre
def improvement(father_node, son_node):
    father_quality = 0
    son_quality = 0
    father_data = father_node.get_data()
    son_data = son_node.get_data()
    father_cost = father_node.get_cost()
    son_cost = son_node.get_cost()

    for n in range(1, len(father_data)):
        if father_data[n] > father_data[n - 1]:
            father_quality = father_quality + 1
            father_cost[n] = randint(0,100) 
        if son_data[n] > son_data[n - 1]:
            son_quality = son_quality + 1
            son_cost[n] = randint(0,100)

    if son_quality >= father_quality:
        return True
    else:
        return False



if __name__ == "__main__":
  print('Introduzca el número de elementos: ')
  n = int(input())
  initial_state = list(range(n, 0, -1))
  solution_state = list(reversed(initial_state))

  visited_nodes = []
  initial_node = Node(initial_state)
  number = len(initial_state)
  solution_node = search_heuristic_solution(initial_node, solution_state, visited_nodes, number)

  result = []
  node = solution_node
  while node.get_father() is not None:
      result.append(node.get_data())
      node = node.get_father()
  result.append(initial_state)
  result.reverse()
  #print(result)
  total = 0
  for i in range(len(result)):
      
      total = total+i
      print(f'{i+1}: ',result[i])
print('Movimientos totales: ',len(result))