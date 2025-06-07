# Proyecto Final Módulo 1:

## Descripción general:
Este notebook trata sobre un análisis realizado en función a la adicción de redes sociales por parte de los estudiantes. Este conjunto de datos contiene registros anónimos de los comportamientos de los estudiantes social‐media y resultados de vida relacionados. Abarca varios países y niveles académicos, centrándose en dimensiones clave como la intensidad de uso, las preferencias de plataforma y la dinámica de las relaciones. Cada fila representa la respuesta a la encuesta de un estudiante y ofrece una instantánea transversal adecuada para análisis estadístico y aplicaciones de aprendizaje automático.

## Alcance y cobertura:
- Población: Los estudiantes de 16–25 años se matricularon en programas de escuela secundaria, pregrado o posgrado.
- Geografía: Cobertura multi‐país (e.g., Bangladesh, India, EE. UU., Reino Unido, Canadá, Australia, Alemania, Brasil, Japón, Corea del Sur).
- Plazo: Datos recopilados a través de una encuesta en línea única administrada en el primer trimestre de 2025.
- Volumen: Tamaños de muestra configurables (e.g., 100, 500, 1000 registros) según las necesidades de investigación.

## Metodología y recopilación de datos:
Se ha realizado un cuestionario con preguntas adaptadas de escalas validadas sobre adicción a las redes sociales. Estos participantes han sido reclutados a través de listas de correo universitarias y plataformas de redes sociales, garantizando la diversidad a nivel académico y nacional.

## Controles de calidad de datos:

- Validación: Campos obligatorios y comprobaciones de alcance (e.g., horas de uso entre 0–24).
- De‐duplicación: Eliminación de entradas duplicadas mediante comprobaciones únicas de ID_estudiante.
- Anonimización: No se recopiló información de identificación personal.
## Variables clave Tabla

A continuación se describen las variables que contiene el archivo **StudentsSocialMediaAddiction_Bruto.csv**.

| Variable                            | Tipo       | Descripción                                                                 |
|-------------------------------------|------------|------------------------------------------------------------------------------|
| ID_estudiante                       | Entero     | Identificador único del encuestado                                          |
| Edad                                | Entero     | Edad en años                                                                |
| Género                              | Categórico | “Male” o “Female”                                                           |
| Nivel_académico                     | Categórico | Escuela Secundaria / Pregrado / Grado                                      |
| País                                | Categórico | País de residencia                                                          |
| Promedio_Horas_de_uso_diario       | Flotador   | Promedio de horas diarias en las redes sociales                            |
| Plataforma_más_usada                | Categórico | Instagram, Facebook, TikTok, etc.                                          |
| Afecta_el_desempeño_académico      | Categórico | Auto‐impacto informado en los académicos (Yes/No)                          |
| Dormir_horas_por_noche             | Flotador   | Horas medias de sueño nocturno                                             |
| Puntuación_de_salud_mental         | Entero     | Salud mental auto‐rata (1 = pobre a 10 = excelente)                        |
| Relación_Estado                     | Categórico | Soltero / En Relación / Complicado                                         |
| Conflictos_Sobre_Social_Media      | Entero     | Número de conflictos de relaciones debido a las redes sociales             |
| Puntuación_adicta                  | Entero     | Puntuación de adicción a redes sociales (1 = bajo a 10 = alto)            |


