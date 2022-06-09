;;; En el siguiente programa se implementará la potenciación modulada

(defun power (x y)
    "Función power que busca la potencia de x elevado a y.
    Recibe como parámetros a x e y que deben ser de tipo entero."
    (assert (and (typep x 'integer) (typep y 'integer)) (x y) "x o y no son enteros.")
    (if (= y 0) 
        1
        (* x (power x (- y 1)))
    )
)

(defun potenciacion-modulada (a b c)
    "Función que devuelve la potencia modulada de 3 enteros no-negativos y c >= 2"
    ;;; En primer lugar se verifica que los datos de entrada sean correctos. En caso de que haya
    ;;; algún error en los datos se lanza un mensaje indicando que valor esta erróneo.
    (assert (>= a 0) (a) "a = ~d no cumple la precondición" a)
    (assert (>= b 0) (b) "b = ~d no cumple la precondición" b)
    (assert (>= c 2) (c) "c = ~d no cumple la precondición" c)

    ;;; Se realiza el cálculo para encotnrar la potencia modulada.
    (if (= b 0)
        1
        (return-from potenciacion-modulada (* (mod a c) (mod (power a (- b 1)) c)))
    )
)

;;; main()
(format t "Ingrese el valor de a: ")
(defvar valA (read))
(format t "Ingrese el valor de b: ")
(defvar valB (read))
(format t "Ingrese el valor de c: ")
(defvar valC (read))
(format t "~d ^ ~d mod ~d = ~d" valA valB valC (potenciacion-modulada valA valB valC))