class Cultivos():
    identificador = '' #Identificador alfanumerico UNICO del cultivo.
    posible_suelo = [] #Lista de los suelos en los que es posible plantar el cultivo.
    area_minima = 0 #Area minima necesaria para plantar el cultivo.
    can_transformar = False #Indica la propiedad del cultivo para modificar el tipo de terreno.
    nuevo_suelo = '' #En el caso de que modifique el tipo de suelo; el tipo al que cambia el suelo.
    duracion_cultivo = 1 #Cantidad de días necesario para que se pueda cosechar lo cultivado.
    
    def __init__(self,identificador, posible_suelo, area_minima, can_transformar, nuevo_suelo, duracion_cultivo): #Se trata del construtor de la clase
        self.identificador = identificador
        self.posible_suelo = posible_suelo
        self.area_minima = area_minima
        self.can_transformar = can_transformar
        self.nuevo_suelo = nuevo_suelo
        self.duracion_cultivo = duracion_cultivo
    
    def _str__(self): #Impresión que se mostrará a imprimir la clase
        return "El cultivo con el ID {0} tiene un area de {2} hecatreas, se puede cultivar en parcelas de los tipos {1}. Su duración es de {3} días.".format(self.identificador, self.posible_suelo, self.area_minima, self.duracion_cultivo)
        
    def dias_transcurridos(self, factor_decremento = 1): #Método mediante el cual restaremos la cantidad de días deseada a los cultivos. Por defecto, el decremento de días será 1.
        self.duracion_cultivo -= factor_decremento
