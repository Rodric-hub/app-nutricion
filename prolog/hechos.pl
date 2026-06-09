% Hechos de alimentos con sus propiedades nutricionales
% alimento(nombre, calorias_por_100g, proteina, carbohidrato, grasa, categoria)

% Carnes y proteínas
alimento(pollo_pechuga, 165, 31, 0, 3.6, proteina).
alimento(res_magra, 250, 26, 0, 15, proteina).
alimento(salmon, 206, 25, 0, 13, proteina).
alimento(huevo, 155, 13, 1.1, 11, proteina).
alimento(atun_enlatado, 144, 29.9, 0, 0.9, proteina).

% Carbohidratos
alimento(arroz_blanco, 130, 2.7, 28, 0.3, carbohidrato).
alimento(papa_cocida, 77, 1.7, 17, 0.1, carbohidrato).
alimento(pan_integral, 265, 8.7, 49, 3.3, carbohidrato).
alimento(pasta_cocida, 131, 4.4, 25, 1.1, carbohidrato).
alimento(avena, 389, 16.9, 66.3, 6.9, carbohidrato).

% Grasas saludables
alimento(aguacate, 160, 2, 9, 15, grasa).
alimento(aceite_oliva, 884, 0, 0, 100, grasa).
alimento(nueces, 654, 15, 14, 65, grasa).
alimento(almendras, 579, 21, 22, 50, grasa).
alimento(cacahuete, 567, 26, 16, 49, grasa).

% Verduras
alimento(brocoli, 34, 2.8, 7, 0.4, verdura).
alimento(espinaca, 23, 2.9, 3.6, 0.4, verdura).
alimento(zanahoria, 41, 0.9, 10, 0.2, verdura).
alimento(tomate, 18, 0.9, 3.9, 0.2, verdura).
alimento(lechuga, 15, 1.2, 2.9, 0.2, verdura).

% Frutas
alimento(manzana, 52, 0.3, 14, 0.2, fruta).
alimento(platano, 89, 1.1, 23, 0.3, fruta).
alimento(naranja, 47, 0.9, 12, 0.1, fruta).
alimento(fresa, 32, 0.7, 8, 0.3, fruta).
alimento(arandano, 57, 0.7, 14, 0.3, fruta).

% Lácteos
alimento(leche_descremada, 35, 3.4, 5, 0.1, lacteo).
alimento(yogur_natural, 61, 3.5, 5, 0.4, lacteo).
alimento(queso_blanco, 98, 12, 1.3, 4.5, lacteo).
alimento(queso_cheddar, 403, 23, 1.3, 33, lacteo).

% Objetivo nutricional
objetivo(ganancia_muscular, proteina_alta, cardio_bajo).
objetivo(perdida_peso, proteina_media, cardio_alto).
objetivo(mantenimiento, proteina_media, cardio_moderado).

% Niveles de actividad
actividad(sedentario, 1.2).
actividad(ligero, 1.375).
actividad(moderado, 1.55).
actividad(intenso, 1.725).
actividad(muy_intenso, 1.9).