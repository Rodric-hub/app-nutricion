% ============================================================
%  RECOMENDACIONES - Motor de sugerencias inteligentes
%  app-gimnasio-multilenguaje / prolog / recomendaciones.pl
% ============================================================

:- use_module(library(lists)).
:- consult('hechos.pl').
:- consult('reglas.pl').

% --- Recomendar lista de ejercicios para un objetivo ---
% Uso: recomendar_ejercicios(perder_peso, Lista)
recomendar_ejercicios(Objetivo, Lista) :-
    findall(E, ejercicio_apto(E, Objetivo), Lista).

% --- Recomendar lista de alimentos para un objetivo ---
% Uso: recomendar_alimentos(ganar_musculo, Lista)
recomendar_alimentos(Objetivo, Lista) :-
    findall(A, alimento_apto(A, Objetivo), Lista).

% --- Recomendación completa para un usuario ---
% Uso: recomendacion_usuario(ana, 65, 165, perder_peso, Ejercicios, Alimentos)
recomendacion_usuario(_, Peso, Altura, Objetivo, Ejercicios, Alimentos) :-
    calcular_imc(Peso, Altura, IMC),
    clasificar_imc(IMC, ClasIMC),
    format("IMC calculado: ~2f (~w)~n", [IMC, ClasIMC]),
    recomendar_ejercicios(Objetivo, Ejercicios),
    recomendar_alimentos(Objetivo, Alimentos).

% --- Plan semanal básico ---
% Uso: plan_semanal(perder_peso, Plan)
plan_semanal(perder_peso, [
    lunes-[sentadilla, burpees, correr],
    martes-descanso,
    miercoles-[saltar_cuerda, plancha, bicicleta],
    jueves-descanso,
    viernes-[correr, burpees, sentadilla],
    sabado-[bicicleta, plancha],
    domingo-descanso
]).

plan_semanal(ganar_musculo, [
    lunes-[press_banca, dominadas, curl_bicep],
    martes-[sentadilla, peso_muerto, press_militar],
    miercoles-descanso,
    jueves-[press_banca, tricep_polea, curl_bicep],
    viernes-[sentadilla, dominadas, peso_muerto],
    sabado-[plancha, press_militar],
    domingo-descanso
]).

plan_semanal(mantenimiento, [
    lunes-[correr, plancha],
    martes-[sentadilla, press_banca],
    miercoles-descanso,
    jueves-[bicicleta, dominadas],
    viernes-[correr, plancha],
    sabado-descanso,
    domingo-descanso
]).

% --- Punto de entrada para llamadas externas desde Python ---
% Uso desde CLI: swipl -g "main" recomendaciones.pl
main :-
    write('=== Motor de Recomendaciones Prolog ==='), nl,
    recomendar_ejercicios(perder_peso, Ej),
    format("Ejercicios para perder peso: ~w~n", [Ej]),
    recomendar_alimentos(ganar_musculo, Al),
    format("Alimentos para ganar músculo: ~w~n", [Al]),
    halt.
