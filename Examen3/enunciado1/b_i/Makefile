KC=	kotlinc
KFLAG=	-cp

all:	\
	Secuencia.class\
	Pila.class\
	Cola.class\
	ClienteKt.class

Secuencia.class: Secuencia.kt
	$(KC) $(KFLAG) . Secuencia.kt

Pila.class: Pila.kt
	$(KC) $(KFLAG) . Pila.kt

Cola.class: Cola.kt
	$(KC) $(KFLAG) . Cola.kt

ClienteKt.class: Cliente.kt
	$(KC) $(KFLAG) . Cliente.kt

clean:
	rm -rf *.class META-INF