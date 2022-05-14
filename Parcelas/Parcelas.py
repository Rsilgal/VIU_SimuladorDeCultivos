class Parcelas():
    identificador = ""  # Este valor será alfanumerico y no se puede repetir
    tipo_suelo = '' # El suelo de una parcela será de uno de estos 5: A,B,C,D o E
    area_parcela = 0 # El area de la parcela, en hectareas
    
    def __init__(self, identificador, tipo_suelo, area_parcela): #Creamos el constructor de la clase. En él se definiran los atributos del objeto
        self.identificador = identificador
        self.tipo_suelo = tipo_suelo
        self.area_parcela = area_parcela
    
    def __str__(self): #Es el mensaje por defecto si imprimios la clase.
        return "La parcela cuyo ID es {0} tiene una area de {2} hectareas y un suelo del tipo {1}".format(self.identificador, self.tipo_suelo, self.area_parcela)
        
    def transformacion_suelo(self, nuevo_tipo): #Este método intercambia el tipo de suelo de la parcela por el indicado.
        self.tipo_suelo = nuevo_tipo