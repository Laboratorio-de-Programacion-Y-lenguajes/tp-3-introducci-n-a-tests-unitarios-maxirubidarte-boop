"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3

@pytest.mark.parametrize("a, b, esperado", [
    (2, 5, -3),       # Restar un número mayor al primero (resultado negativo)
    (7, 0, 7),        # Restar cero
    (-3, -2, -1),     # Restar dos números negativos
    (5.5, 2.2, 3.3)   # Restar dos números decimales
])
def test_sub_parametrizado(a, b, esperado):
    assert sub(a, b) == esperado

    
# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
