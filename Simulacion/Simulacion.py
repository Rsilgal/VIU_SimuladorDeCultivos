from pyparsing import Or


class Simulacion():
    def asignar_cultivos(self,diccionario_parcelas, diccionario_cultivos,diccionario_asignaciones): #Realiza la asiganción de los cultivos a la parcela correspondiente
        self.diccionario_parcelas = diccionario_parcelas
        self.diccionario_cultivos = diccionario_cultivos
        self.diccionario_asignaciones = diccionario_asignaciones
        # Recorremos todas las parcelas que tenemos guardadas en el sistema
        for parcela in diccionario_parcelas:
            id_cultivo_aux = 'NA'
            dif_parcela_cultivo = 99999999
            # Comprobamos cada uno de los cultivos
            for cultivo in diccionario_cultivos:
                # Recisamos la existencia del identificador del cultivo en la lista de valores del diccionario de asignaciones.
                # Si no está asignado, continuamos.
                if (diccionario_cultivos[cultivo].identificador in list(diccionario_asignaciones.values())) or not (diccionario_parcelas[parcela].tipo_suelo in diccionario_cultivos[cultivo].posible_suelo) or not (diccionario_parcelas[parcela].areaParcela >= diccionario_cultivos[cultivo].area_minima):
                # Comprobamos si el cultivo se puede plantar en el tipo de suelo de la parcela.
                # Comprobación de si la parcela tiene espacio suficiente para albergar el cultivo.
                    continue
                # Si la diefrencia de tamaño entre parcela y cultivo es menor que las comprobaciones anteriores
                if((int(diccionario_parcelas[parcela].area_parcela) - int(diccionario_cultivos[cultivo].area_minima)) < dif_parcela_cultivo):
                    # Guardamos el identificador del cultivo que mejor se adapta a la parcela
                    id_cultivo_aux = diccionario_cultivos[cultivo].identificador
                    # Guardamos un registro de la diferencias de tamaños para comprobar si hay otro cultivo que se adapte mejor
                    dif_parcela_cultivo = int(diccionario_parcelas[parcela].area_parcela) - int(diccionario_cultivos[cultivo].area_minima)
                
            if (id_cultivo_aux != 'NA'):
                diccionario_asignaciones[diccionario_parcelas[parcela].identificador] = id_cultivo_aux
                print(diccionario_asignaciones[diccionario_parcelas[parcela].identificador])
        
        self.print_asignaciones(diccionario_asignaciones)
        

    def print_asignaciones(self, diccionario_asignaciones):
        for elemento in diccionario_asignaciones:
            print("Para la parcela " + elemento + " ha sido asinado el cultivo " + diccionario_asignaciones[elemento] + ".")

    def simular_duracion(self, tiempo_simulacion, diccionario_parcelas, diccionario_cultivos, diccionario_asignaciones, diccionario_registro): #Simulamos el paso del tiempo en cada uno de las parcelas
        self.diccionario_parcelas = diccionario_parcelas
        self.diccionario_cultivos = diccionario_cultivos
        self.diccionario_asignaciones = diccionario_asignaciones
        self.diccionario_registro = diccionario_registro    
        #Obtenemos la lista de claves del diccionario Asignaciones.
        dA = list(diccionario_asignaciones.keys()) # Entrega las claves de las parcelas
        
        # Creamos un bucle en el que iteraremos hasta consumir los días a simular
        for dia in range(0,tiempo_simulacion):
            # Añadimos un bucle en el que recorreremos las parcelas para restar los días a los cultivos
            for parcela in dA:
                try:
                    # Accedemos al cultivo desde el identificador de la parcela y restamos un día al cultivo
                    diccionario_cultivos[diccionario_asignaciones[parcela]].duracion_cultivo = int(diccionario_cultivos[diccionario_asignaciones[parcela]].duracion_cultivo) - 1
                    
                    if (int(diccionario_cultivos[diccionario_asignaciones[parcela]].duracion_cultivo) == 0):
                        # Si el cultivo con el que estamos trabajando transforma el suelo de la parcela
                        if (diccionario_cultivos[diccionario_asignaciones[parcela]].can_transformar):
                            # Cambiamos el tipo de suelo de la parcela
                            diccionario_parcelas[parcela].tipo_suelo = diccionario_cultivos[diccionario_asignaciones[parcela]].nuevo_suelo
                        # Añadimos el cultivo al registro de cultivos que han sido producidos
                        diccionario_registro[parcela] = diccionario_asignaciones[parcela]
                        # Eliminamos el cultivo producido del registro de control actual
                        del diccionario_cultivos[diccionario_asignaciones[parcela]]
                        # Borramos la asignación de la parcela con el cultivo producido
                        del diccionario_asignaciones[parcela]
                except KeyError:
                    pass

    def enviar_datos_simulacion(self, diccionario_cultivos, diccionario_asignaciones):
        self.diccionario_cultivos = diccionario_cultivos
        self.diccionario_asignaciones = diccionario_asignaciones
        #Obtenemos la lista de claves del diccionario Asignaciones.
        dA = list(diccionario_asignaciones.keys()) # Entrega las claves de las parcelas
        diccionario_retorno = {}

        # Añadimos un bucle en el que recorreremos las parcelas para restar los días a los cultivos
        for parcela in dA:
            diccionario_retorno[parcela] = diccionario_cultivos[diccionario_asignaciones[parcela]].duracion_cultivo
        return diccionario_retorno
