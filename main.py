#-------------------------------------------------LIBRERÍAS Y PAQUETES EXTERNOS-------------------------------------------------#
from vosk import Model, KaldiRecognizer
import pyaudio
import serial
#-------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------VARIABLES GLOBALES-------------------------------------------------#
#ser = serial.Serial('COM3', 9600)

Luz1_ON = 1
Luz1_OFF = 2
Luz2_ON = 3
Luz2_OFF = 4
Luz3_ON = 5
Luz3_OFF = 6
Luz4_ON = 7
Luz4_OFF = 8
Calefaccion_ON = 9
Calefaccion_OFF = 10
Ventilador_ON = 11
Ventilador_OFF = 12
Alarma_ON = 13
Alarma_OFF = 14
Enchufe1_ON = 15
Enchufe1_OFF = 16
Enchufe2_ON = 17
Enchufe2_OFF = 18
Enchufe3_ON = 19
Enchufe3_OFF = 20
#---------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------LISTAS-------------------------------------------------#

hotword = (
   #"coto",
   #"voto",
   #"go to",
   #"goto",
   "gordo",
   "gozo",
   "contó",
   "to",
   "gota",
   "cuando",
   "botón"
)


Activar_luz1 = (
      "activar luz uno",
      "activar la luz uno",
      "activar los uno",
      "activar la los uno",
      "activa luz uno",
      "activa la luz uno",
      "activa los uno",
      "activa la los uno",
      "activa la aviso",
      "activar aviso",
      "activado solo",
      "activa la dos uno",
      "activar los no",
      "activo la los uno",
      "activará los uno",
      "activar los una",
      "activar la luz una",
      "activa la luz una"
)

Apagar_luz1 = (
      'apagar luz uno',
      'apagar la luz uno',
      'apagar los uno',
      'apagar la los uno',
      'apaga luz uno',
      'apaga la luz uno',
      'apaga los uno',
      'apaga la los uno',
      'apagar los una',
      'apaga los solo',
      'apagarlo los solo',
      'apagarlo seguro',
      'apagarlo los uno',
      'apaga la luz una',
      'apagarlo solo',
      "a pagar los uno"     
)

Activar_luz2 = (
      'activar luz dos',
      'activar la luz dos',
      'activar los dos',
      'activar la los dos',
      'activa luz dos',
      'activa la luz dos',
      'activa los dos',
      'activa la los dos',
      'activarla los dos',
      'activar los los dos',
      'activarlo los dos',
      'activaron los dos', 
      'activa los los dos',
      'activar los los dos',
      'activar a los dos',
      'activaron a los dos',
      'activar alumnos',
      'activarla alumnos',
      'activa la alumnos',
      'activar la alumnos',
      'activar la luz voz'    
)

Apagar_luz2 = (
      'apagar luz dos',
      'apagar la luz dos',
      'apagar la los dos',
      'apaga luz dos',
      'apaga la luz dos',
      'apaga los dos',
      'apaga la los dos',
      'apagar la luz voz',
      'apagar a los dos',
      'apagar la luz los',
      'apagarla en los dos',
      'apagarlo los dos',
      'apagarla los dos',
      "pagar los dos"   
)

Activar_luz3 = (
     "activar luz tres",
      "activar la luz tres",
      "activar los tres",
      "activar la los tres",
      "activa luz tres",
      "activa la luz tres",
      "activa los tres",
      "activa la los tres"
)

Apagar_luz3 = (
      'apagar luz tres',
      'apagar la luz tres',
      'apagar los tres',
      'apagar la los tres',
      'apaga luz tres',
      'apaga la luz tres',
      'apaga los tres',
      'apaga la los tres',
      'pagar ilustres',
      "pagar los tres"
)

Activar_luz4 = (
     "activar luz cuatro",
      "activar la luz cuatro",
      "activar los cuatro",
      "activar la los cuatro",
      "activa luz cuatro",
      "activa la luz cuatro",
      "activa los cuatro",
      "activa la los cuatro",
      "activa luz cuadro",
      "activar luz cuadro",
      "activa la luz cuadro",
      "activa la los cuadro",
      "activar la luz cuadro",
      "activar la los cuadro",
      "activar la cuadro",
      "activa la cuadro",
      "activarlo los cuatro",
      "activar un cuatro",
      "activa la cuatro",
      "activarlo en un cuadro",
      "activando el un cuadro",
      "activarla en un cuatro",
      "activarla en los cuatro"
)

Apagar_luz4 = (
      'apagar luz cuatro',
      'apagar la luz cuatro',
      'apagar los cuatro',
      'apagar la los cuatro',
      'apaga luz cuatro',
      'apaga la luz cuatro',
      'apaga los cuatro',
      'apaga la los cuatro',
      'apaga la luz cuadro',
      'apagar la luz cuadro',
      'apaga la los cuadro',
      'apagar la los cuadro',
      'pagar de los cuatro',
      'pagar el cuadro',
      'apagar cuatro',
      'apagar las cuatro',
      'apagar los cuatro',
      'apagar en cuadro',
      'apagar los cuadros',
      "pagar los cuatro"
)

Activar_calefaccion = (
     "activar calefacción",
     "activar la calefacción",
     "activa calefacción",
     "activa la calefacción"
)

Apagar_calefaccion = (
     "apagar calefacción",
     "apagar la calefacción",
     "apaga calefacción",
     "apaga la calefacción"
)

Activar_ventilador = (
     "activar ventilador",
     "activar el ventilador",
     "activa ventilador",
     "activa el ventilador"
)

Apagar_ventilador = (
     "apagar ventilador",
     "apagar el ventilador",
     "apaga ventilador",
     "apaga el ventilador"
)

Activar_alarma = (
     "activar la alarma",
     "activa la alarma",
     "activar alarma",
     "activa alarma"
)

Apagar_alarma = (
     "apagar la alarma",
     "apaga la alarma",
     "apagar alarma",
     "apaga alarma"
)

Activar_enchufe1 = (
      "activar enchufe uno",
      "activar el enchufe uno",
      "activa enchufe uno",
      "activa el enchufe uno",
      "activa el hecho fue uno",
      "activar el hecho fue uno",
      "activar el hecho fue una",
      "activa el hecho fue una"
      "activar enchufes uno",
      "activar enchufes una",
      "activar el enchufes uno",
      "activar en enchufes uno",
      "activar el fue uno",
      "activar el enchufado uno",
      "activa el enchufado uno",
      "activar el hecho que bueno",
      "activa el hecho que bueno",
      "activa el hecho fue bueno",
      "activar el hecho fue bueno",
      "activa el hecho que uno",
      "activa el hecho de uno",
      "activar en enchufado uno",
      "activar enchufes uno"
)

Apagar_enchufe1 = (
   "apagar enchufe uno",
   "pagar el enchufe uno",
   "apaga enchufe uno",
   "apaga el enchufe uno",
   "apagar el hecho fue uno",
   "apagar hecho fue uno",
   "apaga el hecho fue uno",
   "apagar el enchufado uno",
   "apagar el enchufado bueno",
   "apaga el enchufado uno",
   "apaga el enchufado bueno",
   "apagar el fuego uno",
   "apagar el fuego no",
   "apaga el hecho fue bueno",
   "apagar el en uno",
   "apagar el enchufes uno",
   "apagar el hecho que bueno",
   "apagar el en tu uno",
   "pagar el enchufe bueno",
   "pagar el hecho fue bueno"
)

Activar_enchufe2 = (
   "activar enchufe dos",
   "activar el enchufe dos",
   "activa enchufe dos",
   "activa el enchufe dos",
   "activar el enchufados",
   "activa el enchufados",
   "activar en enchufados",
   "activa en enchufados",
   "activa el enchufes dos",
   "activar el enchufes dos",
   "activar el en sus dedos",
   "activar el en dedos",
   "activa el en dedos",
   "activar el hecho pedazos",
   "activa el hecho pedazos",
   "activar en el dos",
   "activa en el dos",
   "activar el hecho fue dos",
   "activa el hecho fue dos",
   "activar el enchufe los",
   "activar el hecho de los",
   "activa el hecho de los",
   "activan enchufados",
   "activar el tus dedos",
   "activa enchufados",
   "activar el que dos",
   "activar el enchufes los",
   "activa el hecho dos"
)

Apagar_enchufe2 = (
   "apagar enchufe dos",
   "pagar el enchufe dos",
   "apaga el enchufe dos",
   "apaga enchufe dos",
   "apagar el enchufados",
   "apagar en enchufados",
   "apagar el hecho fue dos",
   "apaga el hecho fue dos",
   "apagar el hecho pedazos",
   "apagar el hecho dos",
   "apagar el enchufes dos",
   "apagar el hecho que dos",
   "apagar el en tus dedos",
   "apagar el enchufe el dos"
)

Activar_enchufe3 = (
   "activar enchufe tres",
   "activar el enchufe tres",
   "activa enchufe tres",
   "activa el enchufe tres",
   "activar el hecho fue tres",
   "activar el hecho que tres",
   "activar el hecho tres",
   "activar el equipo tres",
   "activan enchufe tres"
)

Apagar_enchufe3 = (
   "apagar enchufe tres",
   "pagar el enchufe tres",
   "apaga el enchufe tres",
   "apaga enchufe tres",
   "apagar en enchufe tres",
   "apagar el choque tres",
   "apagar el hecho que tres",
   "apagar el hecho fue tres",
   "apagar el enchufes tres",
   "apagar el hecho de tres"
)

#--------------------------------------------------------------------------------------------------------#

#-------------------------------------------------FUNCIONES-------------------------------------------------#
def serial_com(val):
  data = str(val).encode()
  #ser.write(data)

def luz1():
  #-------------------------------------ACTIVADO-------------------------------------#
  for i in Activar_luz1: 
    if i in result:
         print("ACTIVANDO LUZ UNO")
         serial_com(Luz1_ON)    
 #-------------------------------------APAGADO-------------------------------------#
  for i in Apagar_luz1:
      if i in result:
         print("APAGAR LUZ UNO")
         serial_com(Luz1_OFF)

def luz2():
  #-------------------------------------ACTIVADO-------------------------------------#
  for i in Activar_luz2:
      if i in result:
       print("ACTIVANDO LUZ DOS")
       serial_com(Luz2_ON)
#-------------------------------------APAGADO-------------------------------------#
  for i in Apagar_luz2:
      if i in result:
       print("APAGAR LUZ DOS")
       serial_com(Luz2_OFF)

def luz3():
  #-------------------------------------ACTIVADO-------------------------------------#
  for i in Activar_luz3:
      if i in result:
        print("ACTIVANDO LUZ TRES")
        serial_com(Luz3_ON)    
#-------------------------------------APAGADO-------------------------------------#
  for i in Apagar_luz3:
      if i in result:
         print("APAGAR LUZ TRES")
         serial_com(Luz3_OFF)
     
def luz4():
  #-------------------------------------ACTIVADO-------------------------------------#
  for i in Activar_luz4:
       if i in result:
        print("ACTIVANDO LUZ CUATRO")
        serial_com(Luz4_ON)  
#-------------------------------------APAGADO-------------------------------------#
  for i in Apagar_luz4:
      if i in result:
         print("APAGAR LUZ CUATRO")
         serial_com(Luz4_OFF)

def calefaccion():
  #-------------------------------------ACTIVADO-------------------------------------#
  for i in Activar_calefaccion:
      if i in result:
        print("ACTIVANDO CALEFACCION")
        serial_com(Calefaccion_ON) 
#-------------------------------------APAGADO-------------------------------------#
  for i in Apagar_calefaccion:
      if i in result:
       print("APAGANDO CALEFACCION")
       serial_com(Calefaccion_OFF)    

def ventilador():
  #-------------------------------------ACTIVADO-------------------------------------#
  for i in Activar_ventilador:
      if i in result:
        print("ACTIVANDO VENTILADOR")
        serial_com(Ventilador_ON)     
#-------------------------------------APAGADO-------------------------------------#
  for i in Apagar_ventilador:
      if i in result:
       print("APAGANDO VENTILADOR")
       serial_com(Ventilador_OFF)         

def alarma():
  #-------------------------------------ACTIVADO-------------------------------------#
  for i in Activar_alarma:
      if i in result:
        print("ACTIVANDO ALARMA")
        serial_com(Alarma_ON)     
#-------------------------------------APAGADO-------------------------------------#
  for i in Apagar_alarma:
      if i in result:
       print("APAGANDO ALARMA")
       serial_com(Alarma_OFF)       

def enchufe1():
  #-------------------------------------ACTIVADO-------------------------------------#
  for i in Activar_enchufe1:
      if i in result:
        print("ACTIVANDO ENCHUFE UNO")
        serial_com(Enchufe1_ON)     
  #-------------------------------------APAGADO-------------------------------------#
  for i in Apagar_enchufe1:
      if i in result:
       print("APAGANDO ENCHUFE UNO")
       serial_com(Enchufe1_OFF)              

def enchufe2():
  #-------------------------------------ACTIVADO-------------------------------------#
  for i in Activar_enchufe2:
      if i in result:
        print("ACTIVANDO ENCHUFE DOS")
        serial_com(Enchufe2_ON)     
 #-------------------------------------APAGADO-------------------------------------#
  for i in Apagar_enchufe2:
      if i in result:
       print("APAGANDO ENCHUFE DOS")
       serial_com(Enchufe2_OFF)      

def enchufe3():
  #-------------------------------------ACTIVADO-------------------------------------#
  for i in Activar_enchufe3:
      if i in result:
        print("ACTIVANDO ENCHUFE TRES")
        serial_com(Enchufe3_ON)     
  #-------------------------------------APAGADO-------------------------------------#
  for i in Apagar_enchufe3:
      if i in result:
       print("APAGANDO ENCHUFE TRES")
       serial_com(Enchufe3_OFF)      


#-----------------------------------------------------------------------------------------------------------#

#-------------------------------------------------CONTROL DE VOZ-------------------------------------------------#
model = Model(r"C:\Users\Usuario\Documents\Control_de_Voz(Beta)\es-lib")                                 #Modelo de Lenguaje
recognizer = KaldiRecognizer(model, 16000)                                                               #Variable con modelo de lenguaje y frecuencia
mic = pyaudio.PyAudio()                                                                                  #Microfono 
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)    #Parámetros de la transmisión 
stream.start_stream()                                                                                    #Inicio de la transmisión
print("Empezando reconocimiento de voz...")
#----------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------PROGRAMA PRINCIPAL-------------------------------------------------#
if __name__=="__main__":

   while True:
      data = stream.read(4096) #Variable de lectura de la transmisión

      if len(data)==0:
         break

      if recognizer.AcceptWaveform(data): #Procesa la onda de audio y la convierte en información
       result = recognizer.Result() #Resultado del reconocimiento de voz
       print(result)
       for i in hotword:
          if i in result:
            luz1()
            luz2()
            luz3()
            luz4()
            calefaccion()
            ventilador()
            alarma()
            enchufe1()
            enchufe2()
            enchufe3()    

