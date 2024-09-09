# README: Análisis de Correos Maliciosos

## Descripción

Este proyecto tiene como objetivo analizar correos electrónicos para verificar si han sido comprometidos utilizando la información de la página HaveIBeenPwned (HIBP) sin necesidad de utilizar una clave API. Se desarrolló un código en Python que realiza una solicitud HTTP a la página de HIBP y lee el código fuente en busca de la clase `pwnTitle`, que indica si un correo electrónico ha sido comprometido. A través de este enfoque, logramos identificar la presencia de vulneraciones en los correos electrónicos de los usuarios.

## Funcionamiento del Código

El script ejecuta los siguientes pasos para verificar si un correo está comprometido:

1. **Lectura de correos electrónicos**: Se toma una lista de correos electrónicos, ya sea desde un archivo CSV o directamente desde una variable en el código.
2. **Solicitud a HaveIBeenPwned**: Se realiza una consulta HTTP a la página de HaveIBeenPwned (https://haveibeenpwned.com) por cada correo electrónico en la lista.
3. **Verificación en el código fuente**: Se busca la clase `pwnTitle` en el código HTML devuelto por la página. Si esta clase está presente, el correo ha sido comprometido.
4. **Salida de resultados**: El programa genera una lista de correos comprometidos, indicando cuáles han sido encontrados en bases de datos vulneradas.

### Uso del código:

1. **Instalación de dependencias**: 
   Antes de ejecutar el código, asegúrate de instalar las bibliotecas necesarias. Puedes hacerlo con el siguiente comando:
   ```bash
   pip install requests beautifulsoup4
   ```

2. **Ejecutar el script**:
   Simplemente ejecuta el script de Python proporcionando el archivo CSV que contiene la lista de correos electrónicos, o puedes modificar el script para analizar un correo en específico. 

   ```bash
   python analizar_correos.py
   ```

   El archivo CSV debe tener una estructura básica con una columna de correos electrónicos.

## Bibliotecas Utilizadas

El código hace uso de las siguientes bibliotecas de Python:

- **requests**: Se utiliza para hacer las solicitudes HTTP a la página de HaveIBeenPwned.
- **BeautifulSoup**: Esta biblioteca es utilizada para analizar el código HTML de la página y extraer información específica, como la clase `pwnTitle`.

## Aplicaciones donde fue probado

El código fue desarrollado y probado en **PyCharm** y **Visual Studio Code**. Ambas herramientas permiten una experiencia de desarrollo fluida, con características como depuración, resaltado de sintaxis y control de versiones. Se verificó su funcionamiento en sistemas operativos Windows y Linux.

## Problemas y Errores Significativos

Durante el desarrollo del proyecto, surgieron varios problemas importantes que se tuvieron que resolver:

1. **Bloqueos por parte de HaveIBeenPwned**: Dado que no se utilizó una API oficial, las solicitudes frecuentes a la página a veces resultaban en bloqueos temporales o en respuestas HTML modificadas, lo que afectaba la fiabilidad de los resultados. Como solución temporal, se introdujeron tiempos de espera (`time.sleep`) entre las solicitudes para reducir la posibilidad de ser bloqueado.

2. **Detección incorrecta de correos comprometidos**: Inicialmente, el código no distinguía adecuadamente entre las diferentes respuestas que ofrecía HaveIBeenPwned, lo que llevó a falsos positivos en la verificación de correos. Este problema fue resuelto ajustando la búsqueda de la clase `pwnTitle` de manera más precisa y asegurando que sólo se contaran los resultados válidos.

3. **Rendimiento en listas grandes**: Al trabajar con listas grandes de correos electrónicos, el tiempo de ejecución del script se incrementaba significativamente debido al tiempo de espera entre solicitudes y la necesidad de realizar muchas consultas HTTP. Se está trabajando en una posible optimización que divida la lista en bloques más pequeños para evitar el sobrecarga de solicitudes.

4. **Ausencia de API**: Debido a que se tomó la decisión de no utilizar una clave API de HIBP, hubo limitaciones en el número de solicitudes por segundo y en la precisión de las respuestas obtenidas.

## Codigos prueba utilizados para el proyecto
1. **Codigo principal**:
		En este codigo podemos observar lo que serian las bases del script, Este funciona de manera que realiza una solicitud a la URL de HaveIBeenPwned asociada al correo electrónico proporcionado. Utiliza un User-Agent personalizado para simular la solicitud como si fuera hecha desde un navegador web real. Si la página devuelve un código de estado 200 (éxito), se analiza el contenido HTML de la página en busca de la palabra clave "Pwned". Si se encuentra, el correo ha sido comprometido; de lo contrario, no lo ha sido. 
		Durante las solicitudes HTTP, un error recurrente que puede surgir está relacionado con SSL (Secure Socket Layer), que asegura la comunicación entre el cliente y el servidor. Por eso misma razon se deja el codigo sin uso para buscar sus soluciones en los siguientes codigos de prueba
2. **Codigo de prueba 1**: 
		El código actualizado permite realizar conexiones con HaveIBeenPwned deshabilitando la verificación SSL, lo que resuelve problemas previos de conexión. Sin embargo, el error principal es que, aunque se puede acceder a la página, el programa no logra determinar si un correo fue vulnerado. A pesar de realizar la solicitud correctamente, el código no extrae de manera efectiva la información que indica si el correo ha sido comprometido. Esto representa una limitación clave, ya que el objetivo principal de verificar si un correo ha sido vulnerado no se cumple.
3.**Codigo de prueba 2**:
		El tercer código intenta verificar correos electrónicos en la página Intelx.io en lugar de HaveIBeenPwned. En este enfoque, el programa busca en el código fuente de la página un elemento con el identificador stats_line para extraer información sobre archivos encontrados que podrían estar asociados con el correo. Sin embargo, a pesar de realizar las solicitudes correctamente y acceder al HTML de la página, sigue existiendo el mismo problema: el código no proporciona una respuesta efectiva sobre si el correo ha sido vulnerado.
		Aunque se intentó buscar clases y elementos específicos en el código fuente de la página (como el identificador stats_line), esto no resuelve el problema de identificación de correos comprometidos. Aún no se puede extraer la información relevante de manera fiable, por lo que el código sigue sin cumplir su objetivo principal.
		Se han explorado diferentes enfoques, pero la obtención de resultados precisos sigue siendo un desafío, ya que la página web no facilita la extracción directa de datos o no tiene un formato predecible que el código pueda interpretar adecuadamente.


## Conclusión

Este proyecto es un primer paso para realizar una verificación de correos electrónicos comprometidos sin la necesidad de una clave API. A lo largo del desarrollo, se resolvieron problemas importantes, como las advertencias SSL que afectaban el rendimiento del script, y se mejoró la estructura para leer archivos CSV y hacer solicitudes web. Sin embargo, **el código aún no está completamente funcional, ya que no logra leer ni identificar correctamente los correos comprometidos.** Este error persiste a pesar de los intentos de extraer información relevante del código fuente de las páginas consultadas. Identificar y corregir este problema será clave en futuras versiones para mejorar la precisión y utilidad del script.

---

En cada codigo proporcionado estaran los comentarios para entender mas a profundidad el codigo :p
