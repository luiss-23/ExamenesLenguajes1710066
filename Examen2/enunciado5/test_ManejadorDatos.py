""" 
    Programa que implementa los test para probar el codigo en 
    Simulador.py y encontrar la cobertura del codigo
"""

import Simulador as mbd
import DataTypes as dt
import io
import sys

manejadorDatos = mbd.Simulador()

def test_addAtomo() :
    compararDatosAtomico = {}
    compararDatosStruct = {}
    compararDatosUnion = {}

    compararDatosAtomico['Wanda'] = dt.Atomico('Wanda', 4, 4)
    compararDatosAtomico['Thor'] = dt.Atomico('Thor', 1, 2)
    manejadorDatos.addAtomo('Wanda', 4, 4)
    manejadorDatos.addAtomo('Thor', 1, 2)
    assert(manejadorDatos.atomos == compararDatosAtomico)

    # test_addStruct() :
    compararDatosStruct['Avengers'] = dt.Struct('Avengers', ['Wanda', 'Thor'])
    manejadorDatos.addStruct('Avengers', ['Wanda', 'Thor'])
    assert(manejadorDatos.structs == compararDatosStruct)

    # test_addUnion() :
    compararDatosUnion['Dioses'] = dt.Union('Dioses', ['Wanda', 'Thor'])
    manejadorDatos.addUnion('Dioses', ['Wanda', 'Thor'])
    assert(manejadorDatos.unions == compararDatosUnion)

    # test_mensajesDeError1() :
    msgError = io.StringIO()
    sys.stdout = msgError
    manejadorDatos.addStruct('Wanda', ['Wanda', 'Thor'])
    sys.stdout = sys.__stdout__

    msgErrorEsp = "Ya existe un atomo con nombre Wanda\n"
    assert(msgErrorEsp == msgError.getvalue())

    # test_mensajesDeError2() :
    msgError = io.StringIO()
    sys.stdout = msgError
    manejadorDatos.addAtomo('Wanda', 4, 4)
    sys.stdout = sys.__stdout__

    msgErrorEsp = "Ya existe un atomo con nombre Wanda\n"
    assert(msgErrorEsp == msgError.getvalue())

    # test_mensajesDeError3() :
    msgError = io.StringIO()
    sys.stdout = msgError
    manejadorDatos.addUnion('Thor', ['Wanda', 'Thor'])
    sys.stdout = sys.__stdout__

    msgErrorEsp = "Ya existe un atomo con nombre Thor\n"
    assert(msgErrorEsp == msgError.getvalue())

    # test_mensajesDeError4() :
    msgError = io.StringIO()
    sys.stdout = msgError
    manejadorDatos.addStruct('Avengers', ['Wanda', 'Thor'])
    sys.stdout = sys.__stdout__

    msgErrorEsp = "Ya existe un struct con nombre Avengers\n"
    assert(msgErrorEsp == msgError.getvalue())

    # test_mensajesDeError5() :
    msgError = io.StringIO()
    sys.stdout = msgError
    manejadorDatos.addAtomo('Avengers', 4, 4)
    sys.stdout = sys.__stdout__

    msgErrorEsp = "Ya existe un struct con nombre Avengers\n"
    assert(msgErrorEsp == msgError.getvalue())

    # test_mensajesDeError6() :
    msgError = io.StringIO()
    sys.stdout = msgError
    manejadorDatos.addUnion('Avengers', ['Wanda', 'Thor'])
    sys.stdout = sys.__stdout__

    msgErrorEsp = "Ya existe un struct con nombre Avengers\n"
    assert(msgErrorEsp == msgError.getvalue())

    # test_mensajesDeError7() :
    msgError = io.StringIO()
    sys.stdout = msgError
    manejadorDatos.addStruct('Dioses', ['Wanda', 'Thor'])
    sys.stdout = sys.__stdout__

    msgErrorEsp = "Ya existe una union con nombre Dioses\n"
    assert(msgErrorEsp == msgError.getvalue())

    # test_mensajesDeError8() :
    msgError = io.StringIO()
    sys.stdout = msgError
    manejadorDatos.addAtomo('Dioses', 4, 4)
    sys.stdout = sys.__stdout__

    msgErrorEsp = "Ya existe una union con nombre Dioses\n"
    assert(msgErrorEsp == msgError.getvalue())
    
    # test_mensajesDeError9() :
    msgError = io.StringIO()
    sys.stdout = msgError
    manejadorDatos.addUnion('Dioses', ['Wanda', 'Thor'])
    sys.stdout = sys.__stdout__
    
    msgErrorEsp = "Ya existe una union con nombre Dioses\n"
    assert(msgErrorEsp == msgError.getvalue())

    # test_mensajesDeError10() :
    msgError = io.StringIO()
    sys.stdout = msgError
    manejadorDatos.addStruct('YoungAvengers', ['int', 'Thor'])
    sys.stdout = sys.__stdout__

    msgErrorEsp = "El tipo int no ha sido definido.\n"
    assert(msgErrorEsp == msgError.getvalue())

    # test_mensajesDeError11() :
    msgError = io.StringIO()
    sys.stdout = msgError
    manejadorDatos.addUnion('YoungAvengers', ['Wanda', 'bishop'])
    sys.stdout = sys.__stdout__
    
    msgErrorEsp = "El tipo bishop no ha sido definido.\n"
    assert(msgErrorEsp == msgError.getvalue())

    # test_obtenerTipo():
    assert(manejadorDatos.obtenerTipo('Wanda') == dt.Atomico('Wanda', 4, 4))

    # test_obtenerTamanyoTipo():
    assert(manejadorDatos.obtenerTamanyoTipo(dt.Atomico('Thor', 1, 2)) == 1)
    assert(manejadorDatos.obtenerTamanyoTipo(dt.Struct('Avengers', ['Wanda', 'Thor'])) == 5)
    assert(manejadorDatos.obtenerTamanyoTipo(dt.Union('Dioses', ['Wanda', 'Thor'])) == 4)

    # test_alineacion():
    assert(manejadorDatos.alineacion(dt.Atomico('Thor', 1, 2)) == 2)
    assert(manejadorDatos.alineacion(dt.Struct('Avengers', ['Wanda', 'Thor'])) == 4)
    assert(manejadorDatos.alineacion(dt.Union('Dioses', ['Wanda', 'Thor'])) == 4)

    # test_datosSinEmpaquetar
    assert(manejadorDatos.tamanyoDesperdicioSinEmpaquetar(0, 0, dt.Atomico('Thor', 1, 2)) == (1, 0))
    assert(manejadorDatos.tamanyoDesperdicioReordenando(0, 0, dt.Atomico('Thor', 1, 2)) == (1, 0))
    assert(manejadorDatos.tamanyoDesperdicioSinEmpaquetar(0, 0, dt.Struct('Avengers', ['Wanda', 'Thor'])) == (5, 0))
    assert(manejadorDatos.tamanyoDesperdicioReordenando(0, 0, dt.Struct('Avengers', ['Wanda', 'Thor'])) == (5, 0))
    assert(manejadorDatos.tamanyoDesperdicioSinEmpaquetar(0, 0, dt.Union('Dioses', ['Wanda', 'Thor'])) == (4, 0))
    assert(manejadorDatos.tamanyoDesperdicioReordenando(0, 0, dt.Union('Dioses', ['Wanda', 'Thor'])) == (4, 0))
