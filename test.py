import unittest
from heladeria import Heladeria, Base, Complemento, Copa, Malteada


class TestHeladeria(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba para preparar el entorno"""
        # Crear algunos ingredientes
        self.base_1 = Base(nombre="Vainilla", precio=2.0, calorias=150, inventario=10, es_vegetariano=True, sabor="Vainilla")
        self.base_2 = Base(nombre="Chocolate", precio=2.5, calorias=180, inventario=5, es_vegetariano=True, sabor="Chocolate")
        self.complemento_1 = Complemento(nombre="Chispas de chocolate", precio=1.0, calorias=100, inventario=15, es_vegetariano=True)
        self.complemento_2 = Complemento(nombre="Fruta", precio=1.5, calorias=50, inventario=10, es_vegetariano=True)

        # Crear algunos productos
        self.producto_1 = Copa(nombre="Copa de Vainilla", precio_publico=6.0, ingredientes=[self.base_1, self.complemento_1], tipo_vaso="Plástico")
        self.producto_2 = Malteada(nombre="Malteada de Chocolate", precio_publico=7.5, ingredientes=[self.base_2, self.complemento_2], volumen=500)

        # Inicializar la heladería y agregar productos
        self.heladeria = Heladeria()
        self.heladeria.agregar_producto(self.producto_1)
        self.heladeria.agregar_producto(self.producto_2)

    def test_sano(self):
        """Probar si un ingrediente es sano (es vegetariano)"""
        self.assertTrue(self.base_1.es_vegetariano)
        self.assertTrue(self.complemento_1.es_vegetariano)
        self.assertFalse(self.base_2.es_vegetariano)

    def test_abastecer_ingrediente(self):
        """Probar si un ingrediente se abastece correctamente"""
        inventario_inicial = self.base_1.inventario
        self.base_1.abastecer(5)
        self.assertEqual(self.base_1.inventario, inventario_inicial + 5)

    def test_renovar_inventario_complemento(self):
        """Probar que los complementos renuevan su inventario correctamente"""
        inventario_inicial = self.complemento_1.inventario
        self.complemento_1.renovar_inventario()
        self.assertEqual(self.complemento_1.inventario, 0)

    def test_calcular_calorias_copa(self):
        """Probar que se calculan las calorías de una copa correctamente"""
        calorias_totales = self.producto_1.calorias()
        self.assertEqual(calorias_totales, 150 + 100 * 0.95)

    def test_calcular_calorias_malteada(self):
        """Probar que se calculan las calorías de una malteada correctamente"""
        calorias_totales = self.producto_2.calorias()
        self.assertEqual(calorias_totales, 180 + 50 + 200)

    def test_calcular_costo_producto(self):
        """Probar que se calcula correctamente el costo de producción"""
        costo_copa = self.producto_1.costo_producto()
        costo_malteada = self.producto_2.costo_producto()
        self.assertEqual(costo_copa, 2.0 + 1.0)  # Sumar el costo de los ingredientes
        self.assertEqual(costo_malteada, 2.5 + 1.5 + 500)  # Costo adicional por malteada

    def test_calcular_rentabilidad_producto(self):
        """Probar que se calcula correctamente la rentabilidad del producto"""
        rentabilidad_copa = self.producto_1.rentabilidad_producto()
        rentabilidad_malteada = self.producto_2.rentabilidad_producto()
        self.assertEqual(rentabilidad_copa, 6.0 - (2.0 + 1.0))
        self.assertEqual(rentabilidad_malteada, 7.5 - (2.5 + 1.5 + 500))

    def test_producto_mas_rentable(self):
        """Probar que se encuentra el producto más rentable"""
        producto_rentable = self.heladeria.producto_mas_rentable()
        self.assertEqual(producto_rentable, self.producto_1)  # Copa debería ser más rentable

    def test_vender_producto_exitoso(self):
        """Probar que la venta de un producto sea exitosa"""
        mensaje = self.heladeria.vender("Copa de Vainilla")
        self.assertEqual(mensaje, "¡Vendido!")

    def test_vender_producto_fallido_ingrediente_faltante(self):
        """Probar que lanzar un error si falta un ingrediente"""
        self.complemento_1.inventario = 0  # Agotamos el inventario de este ingrediente
        with self.assertRaises(ValueError) as context:
            self.heladeria.vender("Copa de Vainilla")
        self.assertTrue("¡Oh no! Nos hemos quedado sin Chispas de chocolate" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
