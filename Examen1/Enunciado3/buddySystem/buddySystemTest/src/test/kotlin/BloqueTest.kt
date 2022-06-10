import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class BloqueTest {
    private val bloqueTest: Bloque = Bloque(4, 10)

    @Test
    fun testDireccionInicial() {
        val expectedOutput: Int = 4
        assertEquals(expectedOutput, bloqueTest.direccionInicial())
    }

    @Test
    fun testDireccionFinal() {
        val expectedOutput: Int = 10
        assertEquals(expectedOutput, bloqueTest.direccionFinal())
    }

    @Test
    fun testDireccionInicialNot() {
        val expectedOutput: Int = 5
        assertNotEquals(expectedOutput, bloqueTest.direccionInicial())
    }

    @Test
    fun testDireccionFinalNot() {
        val expectedOutput: Int = 19
        assertNotEquals(expectedOutput, bloqueTest.direccionFinal())
    }
}