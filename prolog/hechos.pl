% ============================================================
%  HECHOS - Base de conocimiento
%  app-gimnasio-multilenguaje / prolog / hechos.pl
% ============================================================

% --- Niveles de actividad ---
nivel_actividad(sedentario).
nivel_actividad(ligero).
nivel_actividad(moderado).
nivel_actividad(activo).
nivel_actividad(muy_activo).

% --- Objetivos fitness ---
objetivo(perder_peso).
objetivo(ganar_musculo).
objetivo(mantenimiento).

% --- Grupos musculares ---
grupo_muscular(pecho).
grupo_muscular(espalda).
grupo_muscular(piernas).
grupo_muscular(hombros).
grupo_muscular(brazos).
grupo_muscular(core).

% --- Ejercicios: ejercicio(Nombre, GrupoMuscular, CaloriasMinuto) ---
ejercicio(sentadilla,      piernas,  8).
ejercicio(peso_muerto,     espalda,  9).
ejercicio(press_banca,     pecho,    7).
ejercicio(dominadas,       espalda,  8).
ejercicio(press_militar,   hombros,  6).
ejercicio(curl_bicep,      brazos,   5).
ejercicio(tricep_polea,    brazos,   5).
ejercicio(plancha,         core,     4).
ejercicio(burpees,         core,    12).
ejercicio(correr,          piernas, 11).
ejercicio(bicicleta,       piernas,  9).
ejercicio(saltar_cuerda,   core,    13).

% --- Alimentos: alimento(Nombre, Calorias, Proteinas, Carbs, Grasas) ---
alimento(pollo_a_la_plancha, 165, 31, 0,  3.6).
alimento(arroz_integral,     216, 5,  45, 1.8).
alimento(brocoli,             55, 4,  11, 0.6).
alimento(avena,              303, 13, 51, 5.0).
alimento(huevo_entero,        78, 6,  1,  5.0).
alimento(salmon,             208, 20, 0,  13.0).
alimento(batata,              86, 2,  20, 0.1).
alimento(manzana,             52, 0,  14, 0.2).
alimento(almendras,          579, 21, 22, 50.0).
alimento(yogur_griego,       100, 10, 4,  0.7).
alimento(pechuga_pavo,       135, 30, 0,  1.0).
alimento(lentejas,           116, 9,  20, 0.4).
alimento(platano,             89, 1,  23, 0.3).
alimento(espinaca,            23, 3,  4,  0.4).
