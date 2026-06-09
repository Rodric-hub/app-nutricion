% Reglas para generar planes alimenticios basados en calorías

:- dynamic(plan_generado/4).

% Calcular necesidad calórica basal (Harris-Benedict)
calcular_bmr_hombre(Edad, Peso, Altura, BMR) :-
    BMR is 88.362 + (13.397 * Peso) + (4.799 * Altura) - (5.677 * Edad).

calcular_bmr_mujer(Edad, Peso, Altura, BMR) :-
    BMR is 447.593 + (9.247 * Peso) + (3.098 * Altura) - (4.330 * Edad).

% Calcular necesidad calórica diaria (TMR)
calcular_tmr(Genero, Edad, Peso, Altura, Actividad, TMR) :-
    (Genero = hombre -> calcular_bmr_hombre(Edad, Peso, Altura, BMR) ; 
     calcular_bmr_mujer(Edad, Peso, Altura, BMR)),
    actividad(Actividad, Factor),
    TMR is BMR * Factor.

% Determinar distribución de macronutrientes según objetivo
distribucion_macro(ganancia_muscular, 1.0, 0.5, 0.35) :- !.
distribucion_macro(perdida_peso, 0.8, 0.6, 0.3) :- !.
distribucion_macro(mantenimiento, 0.9, 0.5, 0.35) :- !.
distribucion_macro(_, 0.9, 0.5, 0.35).

% Calcular requerimientos de macronutrientes
calcular_macros(Objetivo, CaloriasTotal, CaloriasProte, CaloriasCarbos, CaloriasGrasas) :-
    distribucion_macro(Objetivo, PropProte, PropCarbos, PropGrasas),
    CaloriasProte is CaloriasTotal * PropProte,
    CaloriasCarbos is CaloriasTotal * PropCarbos,
    CaloriasGrasas is CaloriasTotal * PropGrasas.

% Seleccionar alimentos por categoría
alimentos_por_categoria(Categoria, Alimentos) :-
    findall(Nombre, alimento(Nombre, _, _, _, _, Categoria), Alimentos).

% Desayuno: carbohidratos + proteína (30% de calorías)
generar_desayuno(CaloriasTotal, Objetivo, Desayuno) :-
    DesayunoCaloricas is CaloriasTotal * 0.30,
    alimentos_por_categoria(carbohidrato, Carbos),
    alimentos_por_categoria(proteina, Proteinas),
    alimentos_por_categoria(fruta, Frutas),
    member(Carbo, Carbos),
    member(Proteina, Proteinas),
    member(Fruta, Frutas),
    Desayuno = desayuno(Carbo, Proteina, Fruta, DesayunoCaloricas).

% Almuerzo: proteína + vegetales + carbohidratos (35% de calorías)
generar_almuerzo(CaloriasTotal, Objetivo, Almuerzo) :-
    AlmuerzoCaloricas is CaloriasTotal * 0.35,
    alimentos_por_categoria(proteina, Proteinas),
    alimentos_por_categoria(verdura, Verduras),
    alimentos_por_categoria(carbohidrato, Carbos),
    member(Proteina, Proteinas),
    member(Verdura, Verduras),
    member(Carbo, Carbos),
    Almuerzo = almuerzo(Proteina, Verdura, Carbo, AlmuerzoCaloricas).

% Merienda: proteína o fruta (10% de calorías)
generar_merienda(CaloriasTotal, Objetivo, Merienda) :-
    MeriendaCaloricas is CaloriasTotal * 0.10,
    (alimentos_por_categoria(proteina, Alimentos) ; 
     alimentos_por_categoria(fruta, Alimentos) ;
     alimentos_por_categoria(grasa, Alimentos)),
    member(Alimento, Alimentos),
    Merienda = merienda(Alimento, MeriendaCaloricas).

% Cena: proteína + vegetales (25% de calorías)
generar_cena(CaloriasTotal, Objetivo, Cena) :-
    CenaCaloricas is CaloriasTotal * 0.25,
    alimentos_por_categoria(proteina, Proteinas),
    alimentos_por_categoria(verdura, Verduras),
    member(Proteina, Proteinas),
    member(Verdura, Verduras),
    Cena = cena(Proteina, Verdura, CenaCaloricas).

% Generar plan alimenticio completo
generar_plan(Genero, Edad, Peso, Altura, Actividad, Objetivo, Plan) :-
    calcular_tmr(Genero, Edad, Peso, Altura, Actividad, CaloriasTotal),
    calcular_macros(Objetivo, CaloriasTotal, _, _, _),
    generar_desayuno(CaloriasTotal, Objetivo, Desayuno),
    generar_almuerzo(CaloriasTotal, Objetivo, Almuerzo),
    generar_merienda(CaloriasTotal, Objetivo, Merienda),
    generar_cena(CaloriasTotal, Objetivo, Cena),
    Plan = plan(CaloriasTotal, Desayuno, Almuerzo, Merienda, Cena).

% Validar plan (verificar que sea balanceado)
validar_plan(plan(Calorias, _, _, _, _)) :-
    Calorias > 0,
    Calorias < 10000.

% Guardar plan generado
guardar_plan(Usuario, Fecha, Objetivo, Plan) :-
    assert(plan_generado(Usuario, Fecha, Objetivo, Plan)).

% Recuperar plan generado
obtener_plan(Usuario, Fecha, Objetivo, Plan) :-
    plan_generado(Usuario, Fecha, Objetivo, Plan).

% Recomendación de objetivo según objetivo
recomendar_objetivo(perdida_peso, Recomendacion) :-
    Recomendacion = 'Aumentar cardio, reducir carbohidratos simples, alta proteína'.

recomendar_objetivo(ganancia_muscular, Recomendacion) :-
    Recomendacion = 'Superavit calórico, alta proteína, entrenamiento con pesas'.

recomendar_objetivo(mantenimiento, Recomendacion) :-
    Recomendacion = 'Caloría balanceada, proteína moderada, ejercicio regular'.