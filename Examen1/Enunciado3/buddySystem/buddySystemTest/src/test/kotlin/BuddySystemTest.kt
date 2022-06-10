import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class BuddySystemTest {
    private val buddyTest: BuddySystem = BuddySystem(70)

    @Test
    fun testBuddySystem() {
        val expectedOutput: String = "El bloque lenguajesEsIncreible ha sido reservado."
        assertEquals(expectedOutput, buddyTest.reservarEspacio("lenguajesEsIncreible", 5))

        val expectedOutput2: String = "lenguajesEsIncreible ya ha sido reservado."
        assertEquals(expectedOutput2, buddyTest.reservarEspacio("lenguajesEsIncreible", 5))

        val expectedOutput3: String = "mayThe4th ya ha sido reservado."
        assertNotEquals(expectedOutput3, buddyTest.reservarEspacio("mayThe4th", 10))

        val expectedOutput4: String = "El bloque con nombre lenguajesEsIncreible ha sido liberado."
        assertEquals(expectedOutput4, buddyTest.liberar("lenguajesEsIncreible"))

        val expectedOutput5: String = "No existe el bloque WandaMaximoff."
        assertEquals(expectedOutput5, buddyTest.liberar("WandaMaximoff"))
    }
}