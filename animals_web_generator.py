import requests


def load_data_from_api():
    """Lädt Tierdaten über die API."""
    animal_name = input("Enter a name of an animal: ").strip()
    api_key = "sl5K/ZnEUXPhl1zixQPn3w==atvhb8vzsjU72bw8"
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": api_key}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json(), animal_name
    else:
        print(f"Fehler beim Abrufen der API-Daten: {response.status_code}")
        return [], animal_name



def serialize_animal(animal_obj):
  """Serialisiert ein einzelnes Tierobjekt zu HTML mit strukturierter Liste."""
  name = animal_obj.get("name", "")
  characteristics = animal_obj.get("characteristics", {})
  taxonomy = animal_obj.get("taxonomy", {})
  diet = characteristics.get("diet")
  locations = animal_obj.get("locations", [])
  location = ", ".join(locations) if locations else None
  type_ = characteristics.get("type")
  lifespan = characteristics.get("lifespan")
  color = characteristics.get("color")
  top_speed = characteristics.get("top_speed")
  scientific_name = taxonomy.get("scientific_name")

  html = f'<li class="cards__item">'
  html += f'<div class="card__title">{name}</div>'
  html += '<div class="card__text"><ul class="card__list">'

  if diet:
    html += f'<li class="card__detail"><strong>Diet:</strong> {diet}</li>'
  if location:
    html += f'<li class="card__detail"><strong>Location:</strong> {location}</li>'
  if type_:
    html += f'<li class="card__detail"><strong>Type:</strong> {type_}</li>'
  if lifespan:
    html += f'<li class="card__detail"><strong>Lifespan:</strong> {lifespan}</li>'
  if color:
    html += f'<li class="card__detail"><strong>Color:</strong> {color}</li>'
  if top_speed:
    html += f'<li class="card__detail"><strong>Top Speed:</strong> {top_speed}</li>'
  if scientific_name:
    html += f'<li class="card__detail"><strong>Scientific Name:</strong> {scientific_name}</li>'

  html += '</ul></div></li>\n'
  return html


def generate_animal_cards(data):
    """Erzeugt HTML für alle Tierkarten."""
    return ''.join(serialize_animal(animal) for animal in data)


def create_html(data, template_path, output_path, animal_name):
    """Erstellt die finale HTML-Datei mit Tierkarten oder einer Fehlermeldung."""
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    if data:
        cards_html = generate_animal_cards(data)
    else:
        cards_html = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", cards_html)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)


if __name__ == "__main__":
    data, animal_name = load_data_from_api()
    create_html(data, "animals_template.html", "animals.html", animal_name)
