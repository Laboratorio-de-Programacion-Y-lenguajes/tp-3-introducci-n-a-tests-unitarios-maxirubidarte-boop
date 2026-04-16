"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12

@pytest.mark.parametrize("a, b, esperado", [
    (5, 0, 0),        # Multiplicar por cero
    (-2, -3, 6),      # Multiplicar dos negativos
    (4, -2, -8),      # Multiplicar un positivo y un negativo
    (1, 7, 7),        # Multiplicar por 1 (elemento neutro)
    (1.5, 2.5, 3.75) # Multiplicar dos decimales
])
def test_mul_parametrizado(a, b, esperado):
    assert mul(a,b) == esperado
    
# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
