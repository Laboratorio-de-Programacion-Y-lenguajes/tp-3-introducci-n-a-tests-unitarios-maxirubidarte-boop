"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0

@pytest.mark.parametrize("lista, esperado", [
    ([5], 5.0),        # Un solo elemento
    ([-2, -4, -6], -4.0),  # Negativos
    ([1.5, 2.5, 3.5], 2.5),  # Decimales
])
def test_mean_parametrizado(lista, esperado):
    assert mean(lista) == esperado

def test_mean_lista_vacia():
    with pytest.raises(ValueError):
        mean([])

# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
#   - Lista con números negativos
#   - Lista con números decimales (float)
#   - Lista vacía → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])
