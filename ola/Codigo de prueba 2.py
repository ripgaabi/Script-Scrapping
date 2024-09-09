import requests
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import filedialog, Tk, messagebox
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Función para verificar un correo en Intelx.io
def verificar_correo(correo):
    url = f"https://intelx.io/?s={correo}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        # Deshabilitar la verificación SSL con 'verify=False'
        response = requests.get(url, headers=headers, verify=False)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Busca el span con id="stats_line"
            stats_line = soup.find("span", id="stats_line")
            
            if stats_line and "Found" in stats_line.text:
                # Extrae el número de resultados encontrados
                results_text = stats_line.text.strip()
                print(f"Resultados encontrados: {results_text}")
                
                # Extrae números si se mencionan archivos encontrados
                if any(term in results_text for term in ["Text Files", "Database Files"]):
                    return True  # El correo ha sido comprometido o aparece en la base de datos
                else:
                    return False  # No se encontraron archivos relevantes
            else:
                return False
        else:
            return False
    except requests.exceptions.SSLError as e:
        print(f"Error SSL: {e}")
        return False
    except Exception as e:
        print(f"Error al verificar el correo {correo}: {e}")
        return False


# Cargar archivo CSV usando pandas
def leer_csv(ruta_archivo):
    try:
        df = pd.read_csv(ruta_archivo)
        
        if "Email" in df.columns:
            correos = df["Email"].dropna().tolist()
            return correos
        else:
            messagebox.showerror("Error", "No se encontró una columna llamada 'Email'.")
            return []
    except Exception as e:
        messagebox.showerror("Error", f"Error al leer el archivo: {e}")
        return []

# Función principal
def main():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter
    
    archivo_csv = filedialog.askopenfilename(title="Selecciona un archivo CSV", filetypes=(("CSV files", "*.csv"),))
    
    if archivo_csv:
        correos = leer_csv(archivo_csv)
        
        if not correos:
            print("No se encontraron correos en el archivo.")
            return
        
        print(f"Se encontraron {len(correos)} correos en el archivo.")
        
        for correo in correos:
            print(f"Verificando correo: {correo}...")
            if verificar_correo(correo):
                print(f"El correo {correo} ha sido comprometido o aparece en la base de datos.")
            else:
                print(f"El correo {correo} no ha sido comprometido.")
        
        print("Verificación completada.")
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()
