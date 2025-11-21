Se implementa una clase base llamada FiguraGeometrica y clases hijas como Cuadrado y Rectangulo, que heredan y sobrescriben métodos clave. 
El programa principal permite crear objetos, validar datos, modificar atributos y calcular áreas y perímetros de forma polimórfica. 
También se demuestra el uso de excepciones para garantizar que los valores asignados sean válidos.
----FiguraGeometrica-----
Clase base abstracta que define los atributos ancho y alto con validación mediante setters. 
Incluye métodos area() y __str__() que son sobrescritos por las clases hijas.
-----Cuadrado---------
Hereda de FiguraGeometrica. Su constructor recibe un solo valor (lado) y lo asigna a ancho y alto usando los setters.
Sobrescribe los métodos area(), perimetro() y __str__().
-----Rectangulo---------
También hereda de FiguraGeometrica. Su constructor recibe ancho y alto por separado. Sobrescribe area(), perimetro() y __str__() para mostrar sus dimensiones.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/93ec6592-4039-4857-ae52-231b7646312a" />




