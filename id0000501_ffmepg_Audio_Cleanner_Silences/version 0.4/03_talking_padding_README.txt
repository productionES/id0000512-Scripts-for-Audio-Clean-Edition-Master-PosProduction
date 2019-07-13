para probarlo el siguiente comando:

python3 talking_padding.py -P ./in.wav -I ./silences_duration.txt
La prueba la he hecho con los archivos de prueba en el mismo directorio, si necesitas otros archivos que no esten en el mismo directorio sugiero que uses rutas absolutas.

con el parámetro -P le indicas el fichero .wav, esto antes no era necesario, pero ahora, para calcular el ultimo tramo lo he necesitado para poder extraer lo que dura la pista de audio.

Con el parámetro -I (i mayúscula) le indicas el silences_duration.txt como en el otro script de silences_padding.py

En este caso, lo que te va a sacar como salida es un fichero llamado "talking_duration_with_padding.txt" donde estará todo con el mismo formato que el silences_duration.txt pero invertido. Lo he probado aquí y me funciona.
