"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8

@pytest.mark.parametrize("a, b, esperado", [
    (5, 0, 1),        # Cualquier número elevado a 0 es 1
    (3, 1, 3),        # Cualquier número elevado a 1 es el mismo número
    (-2, 4, 16),      # Base negativa con exponente par da resultado positivo
    (9, 0.5, 3),      # Exponente decimal (raíz cuadrada)
])
def test_pow_parametrizado(a, b, esperado):
    assert pow_(a, b) == esperado

# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
