class InfoSistemas():

    def comparador_dicccionarios(self,diccionario_1,diccionario_2):
        '''
        Este metodo compara dos diccionarios y te devuelve los valores existentes en diccionario_2 que 
        no existen en diccionario_1.
        '''
        lista_diccionario_1 = list(diccionario_1.values())
        lista_diccionario_2 = list(diccionario_2.keys())
        diccionario_diferencias = {}
        
        for elemento in lista_diccionario_2:        # Recorremos cada uno de los elementos presentes en la lista_2 
            if elemento not in lista_diccionario_1: # En el caso de que el elemento, de la lista_2, no este presente en la lista_1 
                diccionario_diferencias[elemento] = diccionario_2.get(elemento) # Agregaremos este elemento al diccionario de las diferencias

        return diccionario_diferencias