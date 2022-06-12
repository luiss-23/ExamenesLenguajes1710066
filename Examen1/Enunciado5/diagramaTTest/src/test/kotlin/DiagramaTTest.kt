import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class DiagramaTTest {
    private val dt = DiagramaT("LOCAL")

    @Test
    fun testDiagramaT() {
        var expectedOutput: String = "Se definió el programa 'fibonacci', ejecutable en 'LOCAL'"
        assertEquals(expectedOutput, dt.definir(mutableListOf("DEFINIR", "PROGRAMA", "fibonacci", "LOCAL")))

        expectedOutput = "Si, es posible ejecutar el programa 'fibonacci'"
        assertEquals(expectedOutput, dt.ejecutar("fibonacci"))

        expectedOutput = "Se definió el programa 'factorial', ejecutable en 'Java'"
        assertEquals(expectedOutput, dt.definir(mutableListOf("DEFINIR", "PROGRAMA", "factorial", "Java")))

        expectedOutput = "No es posible ejecutar el programa 'factorial'"
        assertEquals(expectedOutput, dt.buscarTraductor("Java","factorial"))

        expectedOutput = "Se definió un intérprete para 'Java', escrito en 'C'"
        assertEquals(expectedOutput, dt.definir(mutableListOf("DEFINIR", "INTERPRETE", "C", "Java")))

        expectedOutput = "Se definió un traductor de 'Java' hacia 'C', escrito en 'C'"
        assertEquals(expectedOutput, dt.definir(mutableListOf("DEFINIR", "TRADUCTOR", "C", "Java", "C")))

        expectedOutput = "Se definió un intérprete para 'C', escrito en 'LOCAL'"
        assertEquals(expectedOutput, dt.definir(mutableListOf("DEFINIR", "INTERPRETE", "LOCAL", "C")))

        expectedOutput = "Si, es posible ejecutar el programa 'factorial'"
        assertEquals(expectedOutput, dt.buscarTraductor("Java","factorial"))

        expectedOutput = "El programa 'WandaMaximoff' no está definido."
        assertEquals(expectedOutput, dt.ejecutar("WandaMaximoff"))


    }
}