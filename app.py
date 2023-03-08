from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

# Definim un rang mínim i màxim per a les entrades de potència i hores
MIN_POWER = 0.1
MAX_POWER = 5000
MIN_HOURS = 0.1
MAX_HOURS = 24

# Definim una llista d'opcions de moneda per a l'usuari
CURRENCY_OPTIONS = [
    {"code": "EUR", "symbol": "€"},
    {"code": "USD", "symbol": "$"},
    {"code": "GBP", "symbol": "£"},
]

# Definim la moneda predeterminada
DEFAULT_CURRENCY = "EUR"

# Definim la llista d'electrodomèstics, el cost de l'electricitat
# i la moneda actual
appliances = [
    {"name": "Frigorífic", "power": 200, "hours": 24},
    {"name": "Rentadora", "power": 1200, "hours": 1},
    {"name": "Televisor", "power": 100, "hours": 4},
]
electricity_cost = 0.20
currency = DEFAULT_CURRENCY


# Definim una funció de validació d'entrada per assegurar-nos que
# els valors introduïts són vàlids
def validate_input(name, power, hours):
    errors = []

    if not name:
        errors.append("El nom de l'electrodomèstic és obligatori.")
    if not power:
        errors.append("La potència de l'electrodomèstic és obligatòria.")
    elif float(power) < MIN_POWER or float(power) > MAX_POWER:
        errors.append(
            f"La potència de l'electrodomèstic ha de ser entre {MIN_POWER} \
            i {MAX_POWER} W."
        )
    if not hours:
        errors.append("Les hores d'ús de l'electrodomèstic són obligatòries.")
    elif float(hours) < MIN_HOURS or float(hours) > MAX_HOURS:
        errors.append(
            f"Les hores d'ús de l'electrodomèstic han de ser entre \
            {MIN_HOURS} i {MAX_HOURS} hores."
        )

    return errors


# Definim la ruta de l'aplicació per a la pàgina d'inici
@app.route("/")
def home():
    # Calculem el cost total de l'electricitat per a tots els electrodomèstics
    total_cost = sum(
        [
            appliance["power"] * appliance["hours"] * electricity_cost / 1000
            for appliance in appliances
        ]
    )

    # Mostrem la pàgina d'inici amb la llista d'electrodomèstics, el cost total
    # i altres valors necessaris
    return render_template(
        "index.html",
        appliances=appliances,
        total_cost=total_cost,
        electricity_cost=electricity_cost,
        currency=currency,
        currency_options=CURRENCY_OPTIONS,
    )


# Definim la ruta de l'aplicació per afegir un nou electrodomèstic
@app.route("/add", methods=["POST"])
def add():
    # Obtenemos los valores del formulario
    name = request.form["name"]
    power = request.form["power"]
    hours = request.form["hours"]

    # Validem l'entrada de l'usuari
    errors = validate_input(name, power, hours)

    if errors:
        # Si hay errors, els mostrem l'usuari i no afegim l'electrodomèstic
        return render_template(
            "index.html",
            appliances=appliances,
            errors=errors,
            electricity_cost=electricity_cost,
            currency=currency,
            currency_options=CURRENCY_OPTIONS,
        )

    # Convertim la potencia i les hores a números
    power = float(power)
    hours = float(hours)

    # Afegim l'electrodomèstic a la llista
    appliance = {"name": name, "power": power, "hours": hours}
    appliances.append(appliance)

    # Recalculem els costos totals per hora/dia
    total_cost = sum(
        [
            appliance["power"] * appliance["hours"] * electricity_cost / 1000
            for appliance in appliances
        ]
    )

    # Mostrem la pàgina d'inici amb els electrodomèstics actualitzats i
    # els costos recalculats
    return render_template(
        "index.html",
        appliances=appliances,
        total_cost=total_cost,
        electricity_cost=electricity_cost,
        currency=currency,
        currency_options=CURRENCY_OPTIONS,
    )


# Definim la ruta de l'aplicació per eliminar un electrodomèstic
@app.route("/remove", methods=["POST"])
def remove():
    # Obtenim el nom de l'electrodomèstic a eliminar del formulari
    name = request.form["name"]

    # Eliminem l'electrodomèstic de la llista
    for appliance in appliances:
        if appliance["name"] == name:
            appliances.remove(appliance)

    # Recalculem els costos totals per hora i per dia
    total_cost = sum(
        [
            appliance["power"] * appliance["hours"] * electricity_cost / 1000
            for appliance in appliances
        ]
    )

    # Mostrem la pàgina d'inici amb els electrodomèstics actualitzats i els
    # costos recalculats
    return render_template(
        "index.html",
        appliances=appliances,
        total_cost=total_cost,
        electricity_cost=electricity_cost,
        currency=currency,
        currency_options=CURRENCY_OPTIONS,
    )


# Definim la ruta de l'aplicació per reiniciar la llista d'electrodomèstics
@app.route("/reset", methods=["POST"])
def reset():
    # Buidem la llista d'electrodomèstics
    appliances.clear()

    # Recalculem els costos totals per hora i per dia (que haurien de ser 0)
    total_cost = 0

    # Mostrem la pàgina d'inici amb la llista buida i els costos a 0
    return render_template(
        "index.html",
        appliances=appliances,
        total_cost=total_cost,
        electricity_cost=electricity_cost,
        currency=currency,
        currency_options=CURRENCY_OPTIONS,
    )


# Executem l'aplicació
if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
