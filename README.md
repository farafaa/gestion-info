# 🗂️ Sistema de Gestión de Usuarios

Sistema CRUD en consola con persistencia en JSON, desarrollado en Python como proyecto de transferencia de manejo de archivos y estructuras de datos.

**Autor:** Rafael David Gaviria

---

## 📋 Descripción

Permite registrar, consultar, actualizar y eliminar usuarios de una organización. Los datos se guardan automáticamente en `data/records.json`. Incluye generación de usuarios de prueba con **Faker**, menú con colores usando **colorama** y pruebas unitarias con **pytest**.

## 🗃️ Estructura del proyecto

```
gestion-info/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── records.json          # Base de datos local (JSON)
├── src/
│   ├── main.py               # Punto de entrada
│   ├── menu.py               # Interfaz de consola con colorama
│   ├── service.py            # Lógica CRUD
│   ├── file.py               # Persistencia JSON
│   ├── validate.py           # Validaciones y helpers
│   └── integration.py        # Integración con Faker
└── test/
    └── tests.py              # Pruebas unitarias con pytest
```

## ⚙️ Requisitos

- Python 3.10 o superior
- pip

## 🚀 Cómo correr el programa

### 1. Clona el repositorio

```bash
git clone https://github.com/farafaa/gestion-info.git
cd gestion-info
```

### 2. Crea un entorno virtual (recomendado)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta el programa

```bash
cd src
python main.py
```

## 🧩 Funcionalidades

| Opción | Descripción |
|--------|-------------|
| `[1]` Crear usuario | Ingresa nombre, email, edad y rol |
| `[2]` Listar usuarios | Muestra todos los usuarios en tabla |
| `[3]` Buscar usuario | Busca por nombre, email o rol |
| `[4]` Actualizar usuario | Edita campos por ID |
| `[5]` Eliminar usuario | Elimina por ID con confirmación |
| `[6]` Generar con Faker | Crea N usuarios de prueba automáticamente |
| `[0]` Salir | Termina el programa |

## 🧪 Cómo ejecutar las pruebas

Desde la raíz del proyecto:

```bash
pytest test/ -v
```

Resultado esperado:

```
test/tests.py::test_usuario_valido        PASSED
test/tests.py::test_nombre_vacio          PASSED
test/tests.py::test_email_invalido        PASSED
test/tests.py::test_edad_fuera_de_rango   PASSED
test/tests.py::test_rol_invalido          PASSED
test/tests.py::test_lambda_email_valido   PASSED
test/tests.py::test_lambda_email_invalido PASSED
test/tests.py::test_lambda_is_not_empty   PASSED
```

## 🏷️ Tags de módulos

| Tag | Descripción |
|-----|-------------|
| `m0-setup` | Estructura base del proyecto |
| `m3-crud` | CRUD completo con list comprehensions y lambdas |
| `m4-menu` | Menú interactivo con colorama y validación de entradas |
| `m5-integracion` | Faker con *args/**kwargs y requirements actualizado |
| `m6-final` | Pruebas con pytest, refactor y buenas prácticas |

## 📦 Librerías externas

- [`faker`](https://faker.readthedocs.io/) — Generación de datos falsos realistas en español
- [`colorama`](https://pypi.org/project/colorama/) — Colores en la consola de Windows/Linux
- [`pytest`](https://pytest.org/) — Pruebas unitarias