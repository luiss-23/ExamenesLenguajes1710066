KC=	kotlinc
KFLAG=	-cp

all:	\
	Grafo.class\
	Busqueda.class\
	ClienteKt.class

Grafo.class: Grafo.kt
	$(KC) $(KFLAG) . Grafo.kt

Busqueda.class: Busqueda.kt
	$(KC) $(KFLAG) . Busqueda.kt

ClienteKt.class: Cliente.kt
	$(KC) $(KFLAG) . Cliente.kt

clean:
	rm -rf *.class META-INF