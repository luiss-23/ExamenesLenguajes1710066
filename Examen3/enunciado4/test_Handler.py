import Handler as h
import io
import sys

handler = h.Handler()

def test_handler():
    compararTiposAgregados = {}

    compararTiposAgregados["Avengers"] = h.Tipo("Avengers", None, ["nombre", "superpoder"])
    handler.class_("Avengers", None, ["nombre", "superpoder"])
    assert(handler.tiposCreados == compararTiposAgregados)

    compararTiposAgregados["Wanda Maximoff"] = h.Tipo("Wanda Maximoff", "Avengers", ["nombre", "superpoder", "peliculas"])
    handler.class_("Wanda Maximoff", "Avengers", ["nombre", "superpoder", "peliculas"])
    assert(handler.tiposCreados == compararTiposAgregados)

    msgError = io.StringIO()
    sys.stdout = msgError
    handler.class_("Wanda Maximoff", "Avengers", ["nombre", "superpoder", "peliculas"])
    sys.stdout = sys.__stdout__
    msgErrorEsp = "La clase Wanda Maximoff ya ha sido creada anteriormente.\n"
    assert(msgErrorEsp == msgError.getvalue())

    msgError = io.StringIO()
    sys.stdout = msgError
    handler.class_("Kate Bishop", "Young Avengers", ["nombre", "superpoder", "peliculas"])
    sys.stdout = sys.__stdout__
    msgErrorEsp = "La superclase Young Avengers no existe, no se puede heredar de una clase inexistente.\n"
    assert(msgErrorEsp == msgError.getvalue())

    msgDescribir = io.StringIO()
    sys.stdout = msgDescribir
    handler.describir("Avengers")
    sys.stdout = sys.__stdout__
    msgDescribirEsp = "nombre -> Avengers :: nombre\n"
    msgDescribirEsp += "superpoder -> Avengers :: superpoder\n"
    assert(msgDescribirEsp == msgDescribir.getvalue())

    msgDescribir = io.StringIO()
    sys.stdout = msgDescribir
    handler.describir("Wanda Maximoff")
    sys.stdout = sys.__stdout__
    msgDescribirEsp = "nombre -> Wanda Maximoff :: nombre\n"
    msgDescribirEsp += "superpoder -> Wanda Maximoff :: superpoder\n"
    msgDescribirEsp += "peliculas -> Wanda Maximoff :: peliculas\n"
    assert(msgDescribirEsp == msgDescribir.getvalue())

    msgError = io.StringIO()
    sys.stdout = msgError
    handler.describir("Kate Bishop")
    sys.stdout = sys.__stdout__
    msgErrorEsp = "La clase Kate Bishop que se quiere describir no está definida.\n"
    assert(msgErrorEsp == msgError.getvalue())








