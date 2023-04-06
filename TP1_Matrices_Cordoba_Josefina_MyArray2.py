# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:15:09 2023

@author: Win10
"""

class myarray2:
    def __init__(self, elems: list, r: int, c: int, by_row: bool):
        """
        Inicializa una nueva instancia de la clase myarray2.
        - elems (list): la lista de listas que representa a la matriz;
        - r (int): el número de filas de la matriz;
        - c (int): el número de columnas de la matriz;
        - by_row (bool): dependiendo de si es True o False, define si la matriz se almacena por filas o
        por columnas.
        """
        self.elems  = elems
        self.r      = r
        self.c      = c
        self.by_row = by_row
        
    def get_pos(self, j, k):
        """
        Obtiene la posición de una coordenada en la matriz. Hay que tener en cuenta que estas coordenadas
        son de la manera en las que las lee Python: es decir, comienzan a partir del 0 y no del 1.
        - j (int): índice de la fila en la que está el elemento;
        - k (int): índice de la columna en la que está el elemento.
        Devuelve la posición del elemento o "None" si el usuario ingresó una coordenada que no corresponde
        a la matriz en cuestión.
        """
        if j >= self.r or k >= self.c:
            pos = None
        elif self.by_row == True:
            pos = j * self.c + k
        else:
            pos = k * self.r + j
        print(pos)
        return pos
    
    def get_coords(self, m):
        """
        Obtiene las coordenadas de un elemento de la matriz a partir del índice de este elemento.
        - m (int): índice (posición) del elemento;
        - j (int): índice de la fila;
        - k (int): índice de la columna.
        Devuelve una tupla con los índices de la fila y la columna en el que está el elemento.
        Observación: la primera fila está en el índice 0.
        """
        if self.by_row == True:
            j = m // self.c
            k = m % self.c 
            salida = (j, k)
        else:
            j = m // self.r
            k = m % self.r 
            salida = (j, k)
        print(salida)
        return salida
    
    def switch(self):
        """
        Invierte cómo se almacena u organiza la matriz. Si by_row era True, ahora la matriz se reorganiza
        como si este parámetro fuera False.
        - elems2 (list): nueva matriz con las filas cómo columnas o viceversa.
        Devuelve la nueva matriz.
        """
        elems2 = []
        elems = zip(*self.elems)
        # zip() --> la uso para trasponer las listas dentro de self.elems. Lo que hace '*' es desempaquetar
        # las sublistas como argumentos separados para la función zip(), que contiene tuplas donde cada tupla
        # tiene los elementos correspondientes a las listas originales.           
        
        for tuple in elems:
            new_elems = list(tuple)
            elems2.append(new_elems)
            # Por cada tupla que hay, esta se convierte a una lista, y se agrega a la nueva lista 'elems2',
            # que justamente va a ser la nueva matriz luego de que se aplique la función switch()
        print(elems2)
        return elems2
        
    
    def get_row(self, j):
        """
        Obtiene la fila de una matriz.
        - j (int): el índice de la fila que se quiere obtener
        Devuelve la fila en el índice j o "None" si el índice ingresado no coincide con uno de la matriz.
        Observación: la primera fila está en el índice 0.
        """
        if self.by_row == True:
            if j >= self.r:
                salida = [None] * self.c
            else:
                salida = self.elems[j]
        else:
            row = []
            for i in self.elems:
                row.append(i[j])
                salida = row
                
        print(salida)
        return salida
    
    def get_col(self, k):
        """
        Obtiene la columna de una matriz.
        - k (int): el índice de la columna que se quiere obtener
        Devuelve la fila en el índice k o "None" si el índice ingresado no coincide con uno de la matriz
        """
        if self.by_row == False:
            if k >= self.c:
                salida = [None] * self.r
            else:
                salida = self.elems[k]
        else:
            col = []
            for i in self.elems:
                col.append(i[k])
                salida = col
        print(salida)
        return salida
    
    def get_elem(self, j, k):
        """
        Obtiene un elemento de la matriz, particularmente en la coordenada (j, k).
        - j (int): índice de la fila en la que está el elemento.
        - k (int): índice de la columna en la que está el elemento.
        Devuelve el elemento desseado o "None" si se ingresó una coordenada que no se encuentra en la
        matriz.
        Observación: la primera fila está en el índice 0.
        """
        if j >= self.r or k >= self.c:
            elem = None
        elif self.by_row == True:
            row  = self.get_row(j)
            elem = row[k]
        else:
            col  = self.get_col(k)
            elem = col[j]
        print(elem)
        return elem
    
    def del_row(self, j):
        """
        Elimina una fila de la matriz. 
        - j: el índice de la fila que se desea eliminar
        Devuelve la matriz ingresada sin la fila en el índice "j" o "None" si no existe una fila en 
        ese índice. 
        """
        elems2 = []
        if j > self.r:
            elems2 = None
        elif self.by_row == True:
            row = self.get_row(j)
            for i in self.elems:
                if i != row:
                    elems2.append(i)                    
        else:
            row = self.get_row(j)
            for i in self.elems:
                if i != row:
                    elems2.append(i)
                    elems2 = self.switch()
                    elems2.remove(elems2[j])
        print(elems2)
        return elems2
    
    def del_col(self, k):
        """
        Elimina una fila de la matriz. 
        - k: el índice de la columna que se desea eliminar
        Devuelve la matriz ingresada sin la fila en el índice "k" o "None" si no existe una columna en 
        ese índice.
        """
        elems2 = []
        if k >= self.c:
            elems2 = None
        elif self.by_row == True:
            elems2 = self.switch()
            elems2.remove(elems2[k])
        else:
            col = self.get_col(k)
            for i in self.elems:
                if i != col:
                    elems2.append(i)
        print(elems2)
        return elems2
    
    def swap_rows(self, j, k):
        """
        Intercambia dos filas de una matriz.
        - j: índice de la primera fila que se desea intercambiar
        - k: índice de la segunda fila que se desea intercambiar
        Devuelve la matriz con las filas en dichos índices intercambiadas de lugar.
        """
        if j >= self.r or k >= self.r:
            elems = None
        elif self.by_row == True:
            self.elems[j], self.elems[k] = self.elems[k], self.elems[j]
            elems = self.elems
        else:
            self.elems = self.switch()
            self.elems[j], self.elems[k] = self.elems[k], self.elems[j]
            elems = self.elems
        print(elems)
        return elems
    
    def swap_cols(self, l, m):
        """
        Intercambia dos columnas de una matriz.
        - l: índice de la primera columna que se desea intercambiar
        - m: índice de la segunda columna que se desea intercambiar
        Devuelve la matriz con las columnas en dichos índices intercambiadas de lugar.
        """
        if l >= self.c or m >= self.c:
            elems = None
        elif self.by_row == True:
            for i in self.elems:
                for j in i:
                    i[l], i[m] = i[m], i[l]
                    elems = self.elems
        else:

            self.elems     = self.switch()
            elems          = self.elems
            for i in range(len(elems)):
                elems[i][l], elems[i][m] = elems[i][m], elems[i][l]
                                    
        print(elems)
        return elems
    
    def scale_row(self, j, x):
        """
        Escala los valores de la fila en el índice "j" por el escalar "x" dado.
        - j: índice de la fila que se desea escalar
        - x: valor escalar por el cual se van a multiplicar los elementos de la fila
        Devuelve la matriz modificada con la fila en el índice "j" escalada.
        """
        if self.by_row == True:
            row     = self.get_row(j)
            new_row = []
            for i in row:
                new_row.append(i * x)
            self.elems[j] = new_row
            
        else:
            self.elems = self.switch()
            row     = self.get_row(j)
            new_row = []
            for i in row:
                new_row.append(i * x)
            self.elems[j] = new_row        
        print(self.elems)
        return self.elems
    
    def scale_col(self, k, y):
        """
        Escala los valores de la columna en el índice "k" por el escalar "y" dado.
        - k: índice de la columna que se desea escalar
        - y: valor escalar por el cual se van a multiplicar los elementos de la columna
        Devuelve la matriz modificada con la columna en el índice "k" escalada.
        """
        if self.by_row == True:
            col     = self.get_col(k)
            new_col = []
            for i in col:
                new_col.append(i * y)
            for i in range(self.r):
                self.elems[i][k] = new_col[i]
        else:
            self.elems = self.switch()
            col     = self.get_row(k)
            new_col = []
            for i in col:
                new_col.append(i * y)
            for i in range(self.c):
                self.elems[i][k] = new_col[i]
            
        print(self.elems)
        return self.elems
    
    def transpose(self):
        """
        Transpone la matriz dada.
        Devuelve la matriz transpuesta.
        """
        if self.by_row == True:
            self.elems = self.switch()
        else:
            self.elems = self.switch()
            self.elems = self.switch()
        print(self.elems)
        return self.elems
    
    def flip_rows(self):
        """
        Intercambia la primera fila de la matriz con la última fila de la matriz.
        Devuelve una matriz con la primera y la última fila intercambiadas.
        """
        if self.by_row == True:
            self.swap_rows(0, self.r-1)
        else:
            self.swap_rows(0, self.c-1)
        print (self.elems)
        return self.elems
    
    def flip_cols(self):
        """
        Intercambia la primera columna de la matriz con la última columna de la matriz.
        Devuelve una matriz con la primera y la última columna intercambiadas.
        """
        if self.by_row == True:
            self.swap_cols(0, self.c-1)
        else:
            self.swap_cols(0, self.r-1)
        print(self.elems)
        
    # def sub_matriz(self, i, j):
        
    
    # def det(self):
    
    def __add__(self, B):
        if isinstance(B, type(self)):
            suma = []
            matriz1 = self.elems
            matriz3 = B.elems
            for i in range(len(self.elems)):
                row = []
                for j in range(len(self.elems[0])):
                    row.append(matriz1[i][j] + matriz3[i][j])
                suma.append(row)   
                
        elif isinstance(B, int):
            suma = []
            for i in range(len(self.elems)):
                row = []
                for j in range(len(self.elems[0])):
                    row.append(self.elems[i][j] + B)
                suma.append(row)
        # print(suma)
        return suma
    
    # def __radd__(self, B):
    #     if isinstance(B, type(self)):
            

    
    def __sub__(self, B):
        if isinstance(B, type(self)):
            resta = []
            matriz1 = self.elems
            matriz3 = B.elems
            for i in range(len(self.elems)):
                row = []
                for j in range(len(self.elems[0])):
                    row.append(matriz1[i][j] - matriz3[i][j])
                resta.append(row)                 
        elif isinstance(B, int):
            resta = []
            for i in range(len(self.elems)):
                row = []
                for j in range(len(self.elems[0])):
                    row.append(self.elems[i][j] - B)
                resta.append(row)
        print(resta)
        return resta
        

    # def __rsub__(self, B):
        
    
    def __mul__(self, B):
        # if isinstance(B, type(self)):
        if type(B) == int:
              mult = []
              for i in range(len(self.elems)):
                  row = []
                  for j in range(len(self.elems[0])):
                      row.append(self.elems[i][j] * B)
                  mult.append(row)
        elif (isinstance(B, type(self))):
            if self.c != B.r:
                print("No se pueden multiplicar las matrices dadas.")
                mult = None
            else:
                mult = []
                for i in range(self.r):
                    row = []
                    for j in range(B.c):
                        suma = 0
                        for k in range(self.c):
                            suma = suma + self.elems[i][k] * B.elems[k][j]
                        row.append(suma)
                    mult.append(row)
        print(mult)    
        return mult
                    
    
    # def __pow__(self, n):
        
matriz2 = myarray2([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3, True)
B       = myarray2([[1, 2, 73], [24, 5, 6], [7, 28, 9]], 3, 3, True)
# B = 5


# print(result)
# position      = matriz2.get_pos(0,2)
# coords        = matriz2.get_coords(3)
# cambio        = matriz2.switch()
# fila          = matriz2.get_row(0)
# col           = matriz2.get_col(2)
# elemento      = matriz2.get_elem(1,2)
# eliminar_r    = matriz2.del_row(1)
# eliminar_c    = matriz2.del_col(0)
# intercambio_r = matriz2.swap_rows(0,2)
# intercambio_c = matriz2.swap_cols(0,1)
# multiplicar_r = matriz2.scale_row(2,5)
# multiplicar_c = matriz2.scale_col(1,5)
# transponer    = matriz2.transpose()
# flip_r        = matriz2.flip_rows()
# flip_c        = matriz2.flip_cols()
# det           = matriz2.det()
# resultado1    = 2 + matriz2
# resultado2    = B + matriz2
# print(resultado1.elems) 
# print(resultado2.elems)
# resta         = B - matriz2
# print(resta.elems)
# result = matriz2 * B           
# result = B * matriz2
# print(result.elems)
# res = B - matriz2
# print(res)