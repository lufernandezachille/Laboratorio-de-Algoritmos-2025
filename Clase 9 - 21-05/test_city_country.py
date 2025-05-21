from city_functions import obtener_ubicacion
def test_city_country(ciudad, pais):
	ciudad_pais_formateado = obtener_ubicacion(
   'auschwitz', 'polonia')
    assert ciudad_pais_formateado == 'Auschwitz, Polonia'

def test_city_country_population(ciudad, pais, poblacion):
	ciudad_pais_formateado = obtener_ubicacion(
   'auschwitz', 'polonia', '1000000')
    assert ciudad_pais_formateado == 'Auschwitz, Polonia, 1000000'
