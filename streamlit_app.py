import streamlit as st
import re
import csv

def search_emails(text):
    # Expresión regular para buscar correos electrónicos de Guatemala
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    # Buscar coincidencias en el texto
    matches = re.findall(pattern, text)

    # Filtrar correos electrónicos de Guatemala
    guatemala_emails = [email for email in matches if email.endswith(".gt")]

    return guatemala_emails

def save_to_csv(emails):
    # Nombre del archivo CSV
    filename = "guatemala_emails.csv"

    # Escribir los correos electrónicos en el archivo CSV
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Correo Electrónico"])
        writer.writerows([[email] for email in emails])

    return filename

def main():
    st.title("Búsqueda de Correos Electrónicos de Guatemala")

    # Ingresar el texto para buscar correos electrónicos
    text = st.text_area("Ingrese el texto")

    if st.button("Buscar"):
        # Buscar correos electrónicos de Guatemala
        guatemala_emails = search_emails(text)

        # Guardar los correos electrónicos en un archivo CSV
        filename = save_to_csv(guatemala_emails)

        # Mostrar el enlace para descargar el archivo CSV
        st.markdown(f"Descargar [aquí]({filename})")

if __name__ == "__main__":
    main()
