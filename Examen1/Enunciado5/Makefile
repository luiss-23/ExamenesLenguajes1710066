KC=	kotlinc
KFLAG=	-cp

all:	\
	DiagramaT.class\
	DiagramaTClienteKt.class

DiagramaT.class: DiagramaT.kt
	$(KC) $(KFLAG) . DiagramaT.kt

DiagramaTClienteKt.class: DiagramaTCliente.kt
	$(KC) $(KFLAG) . DiagramaTCliente.kt

clean:
	rm -rf *.class META-INF