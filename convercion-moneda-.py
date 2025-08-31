# Paso 1 : Definir el valor actual de los pesos a convertir (USD,EURO, MXN)


# Paso 2 : Solicitar al usuario el tipo de conversion (Euro a Mex o Dolar Mex)


# Paso 3 : Solicitar al usuario el monto a convertir


# Paso 4 : Realizar la conversion utilizando el tipo de cambio correspondiente




from unittest import result


tipo_cambio_eur_a_mxn = 21.77
tipo_cambio_usd_a_mxn = 18.66

tipo_conversion = (input("Por favor ingrese el tipo de moneda para conversion (EUR/USD): "))
monto_a_convertir = float(input("Ingrese el monto a conversion: "))

if tipo_conversion.upper() == "EUR":
    result = monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conversion de EUR a MXN es:", result)
elif tipo_conversion.upper() == "USD":
    result = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversion de USD a MXN es:", result)
else:
    print("Tipo de conversion no valido")

