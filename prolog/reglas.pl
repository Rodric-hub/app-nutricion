% ============================================================
%  REGLAS - Inferencia lógica
%  app-gimnasio-multilenguaje / prolog / reglas.pl
% ============================================================

:- use_module(library(lists)).

% --- Clasificación de IMC ---
clasificar_imc(IMC, bajo_peso)   :- IMC < 18.5.
clasificar_imc(IMC, normal)      :- IMC >= 18.5, IMC < 25.0.
clasificar_imc(IMC, sobrepeso)   :- IMC >= 25.0, IMC < 30.0.
clasificar_imc(IMC, obesidad)    :- IMC >= 30.0.

calcular_imc(Peso, Altura, IMC) :-
    AlturaM is Altura / 100,
    IMC is Peso / (AlturaM * AlturaM).

% --- Determinar nivel recomendado ---
nivel_recomendado(_, _, principiante) :-
    % Por defecto si no hay historial
    true.

% --- Un alimento es apto para un objetivo ---
alimento_apto(Alimento, perder_peso) :-
    alimento(Alimento, Calorias, _, _, _),
    Calorias < 200.

alimento_apto(Alimento, ganar_musculo) :-
    alimento(Alimento, _, Proteinas, _, _),
    Proteinas >= 10.

alimento_apto(Alimento, mantenimiento) :-
    alimento(Alimento, _, _, _, _).

% --- Un ejercicio es apto para un objetivo ---
ejercicio_apto(Ejercicio, perder_peso) :-
    ejercicio(Ejercicio, _, CalMin),
    CalMin >= 9.

ejercicio_apto(Ejercicio, ganar_musculo) :-
    ejercicio(Ejercicio, Grupo, _),
    member(Grupo, [pecho, espalda, piernas, hombros, brazos]).

ejercicio_apto(Ejercicio, mantenimiento) :-
    ejercicio(Ejercicio, _, _).

% --- Calcular calorías quemadas ---
calorias_quemadas(Ejercicio, Duracion, Calorias) :-
    ejercicio(Ejercicio, _, CalMin),
    Calorias is CalMin * Duracion.
