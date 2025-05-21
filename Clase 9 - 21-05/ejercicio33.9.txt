from pathlib import Path
import json
numero = input("Cuál es tu número favorito?")
path = Path("numero_favorito.json")
contenido = json.dumps(numero)
path.write_text(contenido)
print(f"Tu número favorito es {numero}")
