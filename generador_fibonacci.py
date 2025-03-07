# Excepción personalizada para manejar errores de entrada
class ErrorEntradaInvalida(Exception):
    pass


class Fibonacci:
    def __init__(self):
        self.limite = None  

    def obtener_limite(self):
        while True:
            try:
               
                entrada = input("Ingresa un número límite para la serie Fibonacci: ")
                
                
                if not entrada.isdigit():
                    raise ErrorEntradaInvalida("Error: Debes ingresar un número entero positivo.")
                
                
                self.limite = int(entrada)
                if self.limite <= 0:
                    raise ErrorEntradaInvalida("Error: El número debe ser mayor que 0.")
                
                break 
            except ErrorEntradaInvalida as e:
                print(e)  
            except Exception as e:
                print(f"Error inesperado: {e}")  

    def generar_fibonacci(self):
       
        serie = []
        a, b = 0, 1
        
       
        while a <= self.limite:
            serie.append(a)
            a, b = b, a + b
        
        return serie

    def ejecutar(self):
        try:
           
            self.obtener_limite()
            
          
            serie_fibonacci = self.generar_fibonacci()
            print(f"\nSerie Fibonacci hasta {self.limite}: {serie_fibonacci}")
        
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        finally:
            print("Fin del programa.")



if __name__ == "__main__":
    programa = Fibonacci()
    programa.ejecutar()