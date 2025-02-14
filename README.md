# Código Limpio con Herencia, Principio Abierto/Cerrado y Strategy (Patrón de diseño comportamental)
### Realizado por: Luis Alfonso Díaz Vergel

## Descripción

El programa permite calcular el costo de envío para diferentes tipos de transporte y servicios. Se implementan tres tipos de envío:

- **Envío Terrestre**
- **Envío Aéreo**
- **Envío Marítimo**

Cada tipo de envío utiliza una fórmula específica para calcular la base del costo a partir de la distancia y el peso.

Además, se definen tres estrategias de cálculo de costo que permiten ofrecer distintos niveles de servicio:

- **Servicio Urgente:** Incrementa el costo base en un 50% y añade una tarifa fija.
- **Servicio Estándar:** Utiliza el costo base sin modificaciones.
- **Servicio Económico:** Aplica un descuento del 20% sobre el costo base.

El programa solicita al usuario los valores de distancia en kilómetros y peso en kilogramos, para luego mostrar los costos calculados para cada combinación de método de envío y estrategia.

## Tecnologías y Conceptos Utilizados

- **Python 3**
- **Librerías:**
  - `abc`: Para la implementación de clases abstractas y métodos abstractos.
- **Programación Orientada a Objetos (POO):** Uso de clases, herencia y métodos abstractos.
- **Principio Abierto/Cerrado:** Se pueden agregar nuevos métodos de envío sin modificar el código existente.
- **Patrón Strategy:** Permite cambiar dinámicamente la estrategia de cálculo del costo del envío.

